#!/usr/bin/env python3
"""백준 학습 기록 도구. Python 3.11+, 핵심 기능은 표준 라이브러리만 사용한다."""
import argparse
from datetime import date, datetime, timedelta
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
VERDICTS = ("AC", "WA", "TLE", "MLE", "RE", "CE")
TRACKS = {"concept": "개념", "practical": "실전", "challenge": "도전"}
REVIEW_SECTIONS = ("문제를 내 말로", "접근과 정당성", "경계 입력과 검증", "시간·공간 복잡도", "다음에 기억할 것", "블로그 판단")


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def cfg():
    return read(ROOT / "study-workflow/config.json")


def now():
    return datetime.now(ZoneInfo(cfg()["timezone"]))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def catalog():
    return read(ROOT / "study-workflow/curriculum.json")


def inside(base, relative):
    result = (base / relative).resolve()
    if not result.is_relative_to(base.resolve()):
        raise ValueError("허용 범위 밖의 경로: " + str(relative))
    return result


def problem(pid):
    matches = [p for p in catalog()["problems"] if p["id"] == pid]
    if len(matches) != 1:
        raise ValueError(f"후보 목록에서 {pid}번을 유일하게 찾을 수 없습니다.")
    p = matches[0]
    return p, inside(ROOT / "백준/개념별", f'{p["concept"]}/{pid}')


def opened(pid):
    p, folder = problem(pid)
    if not (folder / "meta.json").is_file():
        raise ValueError(f"먼저 start {pid}를 실행하세요.")
    return p, folder, read(folder / "meta.json")


def fingerprints(folder):
    files = [folder / "solution.py"] + sorted((folder / "tests").glob("*.in")) + sorted((folder / "tests").glob("*.out"))
    return {str(p.relative_to(folder)): sha(p) for p in files}


def local_ok(folder, m):
    run = m.get("local_test") or {}
    return bool(run.get("passed") and run.get("cases") and run.get("files") == fingerprints(folder))


def accepted(folder, m):
    last = (m.get("submissions") or [{}])[-1]
    return last.get("verdict") == "AC" and last.get("solution_sha256") == sha(folder / "solution.py")


def reviewed(folder, m):
    last = (m.get("reviews") or [{}])[-1]
    return (last.get("result") == "complete" and local_ok(folder, m) and accepted(folder, m)
            and last.get("files") == fingerprints(folder)
            and last.get("note_sha256") == sha(folder / "README.md"))


def status(folder, m):
    if reviewed(folder, m):
        return "정리 완료"
    if accepted(folder, m):
        return "AC 기록 · 검토 필요"
    if local_ok(folder, m):
        return "로컬 통과 · AC 미확인"
    return "풀이 중"


def template(name):
    return (ROOT / "study-workflow/templates" / name).read_text(encoding="utf-8")


def start(args):
    p, folder = problem(args.id)
    if folder.exists():
        raise ValueError("기존 문제 폴더가 있습니다. 덮어쓰지 않습니다: " + str(folder))
    folder.mkdir(parents=True)
    (folder / "tests").mkdir()
    difficulty = p.get("solved_ac_level") or "난이도 미확인"
    tiers = dict(Bronze="브론즈", Silver="실버", Gold="골드", Platinum="플래티넘", Diamond="다이아몬드", Ruby="루비")
    tier, _, rank = difficulty.partition(" ")
    ranks = ["I", "II", "III", "IV", "V"]
    if tier in tiers and rank in ranks:
        difficulty = f"{tiers[tier]} {ranks.index(rank) + 1}"
    header = template("solution.py").format(id=p["id"], title=p["title"], difficulty=difficulty)
    (folder / "solution.py").write_text(header, encoding="utf-8")
    note = f'# BOJ {p["id"]} · {p["title"]}\n\n[문제]({p["url"]})\n\n' + template("review.md")
    (folder / "README.md").write_text(note, encoding="utf-8")
    for case in p.get("cases", []):
        if not re.fullmatch(r"[a-z0-9_-]+", case["name"]):
            raise ValueError("테스트 이름은 영문 소문자·숫자·밑줄·하이픈만 허용합니다.")
        for ext, key in (("in", "input"), ("out", "output")):
            (folder / "tests" / f'{case["name"]}.{ext}').write_text(case[key], encoding="utf-8")
    write(folder / "meta.json", {"version": 1, "boj_id": p["id"], "title": p["title"],
          "concept": p["concept"], "tags": p.get("tags", []), "created_at": now().isoformat(),
          "submissions": [], "reviews": [], "local_test": None, "blog": "undecided"})
    (folder / "tests/README.md").write_text(
        "# 테스트 출처\n\n" + "\n".join(f'- `{c["name"]}`: {c["source"]}' for c in p.get("cases", []))
        + "\n\n추가 입력은 같은 이름의 .in/.out 쌍으로 저장한다. 기댓값을 별도로 계산하고 출처를 기록한다.\n"
        + "비교 방식은 각 줄 끝의 공백과 마지막 줄바꿈만 무시한다. 실수 오차·다중 정답 문제는 별도 검증기가 필요하다.\n",
        encoding="utf-8")
    index(args)
    print("시작:", folder.relative_to(ROOT))


def normalize(data):
    return "\n".join(line.rstrip() for line in data.rstrip().splitlines())


def run_tests(args):
    _, folder, m = opened(args.id)
    ins = sorted((folder / "tests").glob("*.in"))
    outs = sorted((folder / "tests").glob("*.out"))
    if not ins or {x.stem for x in ins} != {x.stem for x in outs}:
        raise ValueError("1개 이상의 동일 이름 .in/.out 쌍이 필요합니다. 누락·고아 파일을 확인하세요.")
    before = fingerprints(folder)
    timeout = args.timeout if args.timeout is not None else cfg()["local_timeout_seconds"]
    if timeout <= 0:
        raise ValueError("timeout은 양수여야 합니다.")
    cases = []
    for inp in ins:
        # 출력은 임시 파일로 받아 잘못된 코드의 무한 출력이 메모리를 채우지 않게 한다.
        with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
            begin = now()
            try:
                result = subprocess.run([sys.executable, "-B", str(folder / "solution.py")],
                                        input=inp.read_bytes(), stdout=out, stderr=err, cwd=folder, timeout=timeout)
                out.seek(0); err.seek(0)
                actual = out.read(2_000_001)
                stderr = err.read(4_000).decode("utf-8", errors="replace")
                too_large = len(actual) > 2_000_000
                output = actual.decode("utf-8", errors="replace")
                expected = inp.with_suffix(".out").read_text(encoding="utf-8")
                ok = result.returncode == 0 and not too_large and normalize(output) == normalize(expected)
                reason = "PASS" if ok else ("출력 제한 초과" if too_large else f"FAIL(exit={result.returncode})")
            except subprocess.TimeoutExpired:
                ok, reason, stderr = False, "TIMEOUT(로컬)", ""
            cases.append({"name": inp.stem, "passed": ok, "result": reason,
                          "elapsed_seconds": round((now() - begin).total_seconds(), 4), "stderr": stderr})
            print(inp.stem, reason)
    unchanged = before == fingerprints(folder)
    m["local_test"] = {"checked_at": now().isoformat(), "python": sys.version.split()[0],
                       "timeout_seconds": timeout, "files": before, "cases": cases,
                       "passed": unchanged and all(c["passed"] for c in cases),
                       "note": "로컬 사례 검사이며 BOJ 채점·시간 제한 통과 증거가 아니다."}
    write(folder / "meta.json", m)
    index(args)
    if not m["local_test"]["passed"]:
        raise ValueError("로컬 테스트가 실패했거나 실행 중 코드·테스트가 바뀌었습니다.")


def record(args):
    _, folder, m = opened(args.id)
    if not args.evidence.strip():
        raise ValueError("판정 근거를 입력하세요.")
    if args.source == "page_verified" and not re.match(r"https://(?:www\.)?acmicpc\.net/", args.evidence):
        raise ValueError("직접 확인한 BOJ 페이지 URL이 필요합니다.")
    m["submissions"].append({"verdict": args.verdict, "source": args.source, "evidence": args.evidence,
                             "recorded_at": now().isoformat(), "solution_sha256": sha(folder / "solution.py")})
    write(folder / "meta.json", m)
    index(args)
    print("판정 기록:", args.verdict, args.source, "(URL 자체를 자동 검증한 것은 아닙니다.)")


def has_todo(text):
    return bool(re.search(r"\bTODO\b|\bTBD\b|작성 예정|내용을 입력", text, re.I))


def complete_note(body):
    if has_todo(body):
        return False
    sections = dict(re.findall(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", body, re.M | re.S))
    return all(sections.get(name, "").strip() for name in REVIEW_SECTIONS)


def review(args):
    _, folder, m = opened(args.id)
    if not local_ok(folder, m) or not accepted(folder, m):
        raise ValueError("현재 코드의 로컬 테스트 통과와 AC 근거를 먼저 기록하세요.")
    body = (folder / "README.md").read_text(encoding="utf-8")
    if args.result == "complete" and not complete_note(body):
        raise ValueError("풀이 README의 미완성 내용·빈 절을 먼저 채우세요.")
    if not args.note.strip() or not args.blog_reason.strip():
        raise ValueError("검토 내용과 블로그 판단 이유가 필요합니다.")
    count = sum(r["result"] == "complete" for r in m["reviews"])
    intervals = cfg()["review_days"]
    days = intervals[min(count, len(intervals) - 1)] if args.result == "complete" else 1
    m["reviews"].append({"reviewed_at": now().isoformat(), "result": args.result, "note": args.note,
                         "files": fingerprints(folder), "note_sha256": sha(folder / "README.md"),
                         "next_review": (now().date() + timedelta(days=days)).isoformat()})
    m["blog"], m["blog_reason"] = args.blog, args.blog_reason
    write(folder / "meta.json", m)
    index(args)
    print("검토 기록 완료. 다음 복습:", m["reviews"][-1]["next_review"])


def profile():
    p = ROOT / "study-workflow/state/profile.json"
    return read(p) if p.exists() else None


def previously_solved(p, prof=None):
    prof = prof or profile() or {}
    return (p["id"] in prof.get("solved_boj_ids", [])
            or (p.get("solved_ac_id") is not None
                and str(p["solved_ac_id"]) in prof.get("solved_ac_ids", []))
            or p.get("prior_solved", False))


def import_solved(args):
    data = read(Path(args.file))
    if not isinstance(data, list):
        raise ValueError("파일은 문제 번호의 JSON 배열이어야 합니다.")
    if args.namespace == "boj" and any(type(i) is not int or i <= 0 for i in data):
        raise ValueError("BOJ 번호는 양의 정수여야 합니다. 예: [1000, 1001]")
    if args.namespace == "solved_ac" and any(not isinstance(i, str) or not re.fullmatch(r"[0-9]+[a-z]*", i) for i in data):
        raise ValueError('solved.ac ID는 문자열이어야 합니다. 예: ["1000", "19759a"]')
    observed = date.fromisoformat(args.observed_at)
    if observed > now().date():
        raise ValueError("관측일은 미래일 수 없습니다.")
    key = "solved_boj_ids" if args.namespace == "boj" else "solved_ac_ids"
    current = profile() or {}
    current.update({"boj_handle": cfg()["boj_handle"],
          key: sorted(set(data)), "observed_at": args.observed_at, "source": args.source,
          "note": "추천 제외용 스냅샷. 저장소 풀이·AC·검토 완료로 자동 등록하지 않는다."})
    write(ROOT / "study-workflow/state/profile.json", current)
    print("기존 해결 목록 반영:", len(set(data)), "개. 저장소 기록은 변경하지 않았습니다.")


def next_problems(args):
    prof = profile()
    print("선정 기준: 개념 2 · 실전 2 · 도전 1 + 기한이 된 복습 우선")
    print("기존 해결 목록:", f'{prof["observed_at"]} 스냅샷' if prof else "미확인 — 추천 후보의 중복 여부 확인 필요")
    baseline = cfg().get("profile", {})
    print(f'티어 기준: {baseline.get("tier", "미확인")} ({cfg()["profile_checked_at"]} 관측). 도전 표시는 학습 단계입니다.')
    pool, urgent, planned = [], [], []
    for p in catalog()["problems"]:
        if args.concept and p["concept"] != args.concept:
            continue
        _, folder = problem(p["id"])
        if (folder / "meta.json").exists():
            m = read(folder / "meta.json")
            last = (m.get("reviews") or [{}])[-1]
            due = last.get("next_review")
            if due and due <= now().date().isoformat():
                urgent.append((p, f"복습 {due}"))
            elif accepted(folder, m):
                if not reviewed(folder, m):
                    urgent.append((p, "AC 풀이 정리"))
            else:
                urgent.append((p, "진행 중 이어서"))
        elif not previously_solved(p, prof):
            if p.get("planned_for"):
                planned.append((p, f'풀이 예정 {p["planned_for"]}'))
            else:
                pool.append(p)
    picked = (urgent + sorted(planned, key=lambda item: item[0]["planned_for"]))[:args.limit]
    cycle = cfg()["selection_cycle"]
    while pool and len(picked) < args.limit:
        track = cycle[len(picked) % len(cycle)]
        candidate = next((p for p in pool if p["track"] == track), pool[0])
        pool.remove(candidate)
        picked.append((candidate, TRACKS[candidate["track"]]))
    for p, why in picked:
        print(f'{p["id"]} · {p["title"]} [{why}] · {p["url"]}')
    if not picked:
        print("남은 후보가 없습니다. 현재 개념의 응용·실전·도전 후보를 공식 원문 확인 후 추가하세요.")


def index_text():
    data = catalog()
    lines = ["# 백준 학습 현황", "", "자동 생성: `python3 study-workflow/scripts/study.py index`", "",
             "[학습 절차](../study-workflow/PIPELINE.md) · [선정 근거](../study-workflow/SOURCES.md)", "",
             "현재 난이도·기존 해결 목록은 별도 확인한다. 후보는 미해결 문제라는 뜻이 아니다.", "",
             "| 개념 | 문제 | 목적 | 상태 | 다음 복습 |", "|---|---|---|---|---|"]
    for p in data["problems"]:
        _, folder = problem(p["id"])
        m = read(folder / "meta.json") if (folder / "meta.json").exists() else None
        state = status(folder, m) if m else ("기존 해결 · 코드 미정리" if p.get("prior_solved") else "후보")
        if not m and not p.get("prior_solved") and p.get("planned_for"):
            state = f'풀이 예정 {p["planned_for"]}'
        due = (m.get("reviews") or [{}])[-1].get("next_review", "—") if m else "—"
        label = f'{p["id"]} {p["title"]}'
        link = f'개념별/{p["concept"]}/{p["id"]}/README.md' if m else p["url"]
        lines.append(f'| {p["concept"]} | [{label}]({link}) | {TRACKS[p["track"]]} | {state} | {due} |')
    lines += ["", "## 개념 노트", ""]
    lines += [f'- [{c["name"]}](개념별/{c["id"]}/README.md) — {c["question"]}' for c in data["concepts"]]
    return "\n".join(lines) + "\n"


def index(args):
    (ROOT / "백준").mkdir(exist_ok=True)
    (ROOT / "백준/README.md").write_text(index_text(), encoding="utf-8")
    import dashboard_export
    dashboard_export.export(sys.modules[__name__])


def blog_path(slug):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("slug는 영문 소문자·숫자·하이픈으로 작성하세요.")
    return ROOT / "blog-workflow/posts" / slug


def make_blog(args):
    folder = blog_path(args.slug)
    if folder.exists():
        raise ValueError("이미 존재하는 글 패키지입니다. 기존 원고를 보존합니다.")
    sources, versions, notes = [], [], []
    for pid in dict.fromkeys(args.ids):
        p, prob_folder, m = opened(pid)
        if not reviewed(prob_folder, m):
            raise ValueError(f"{pid}번은 현재 코드의 정리 완료 상태가 필요합니다.")
        sources.append({"kind": "public", "url": p["url"], "supports": "문제 조건과 공식 예제"})
        versions.append({"boj_id": pid, "solution_sha256": sha(prob_folder / "solution.py"),
                         "note_sha256": sha(prob_folder / "README.md")})
        notes.append((pid, prob_folder))
    folder.mkdir(parents=True)
    (folder / "img").mkdir()
    (folder / "evidence").mkdir()
    experiments = []
    for pid, prob_folder in notes:
        tests_copy = folder / "evidence" / f"{pid}-tests"
        tests_copy.mkdir()
        for test in (prob_folder / "tests").iterdir():
            if test.is_file():
                (tests_copy / test.name).write_bytes(test.read_bytes())
        for name in ("README.md", "solution.py", "meta.json"):
            (folder / "evidence" / f"{pid}-{name}").write_bytes((prob_folder / name).read_bytes())
        result, script = f"evidence/{pid}-meta.json", f"evidence/{pid}-solution.py"
        experiments.append({"path": result, "sha256": sha(folder / result), "script": script,
                            "script_sha256": sha(folder / script), "supports": "로컬 테스트·판정·검토 기록. 실제 제출 근거는 기록의 source 참조."})
    for name in ("post.md", "visual-brief.md"):
        (folder / name).write_text(template(name), encoding="utf-8")
    (folder / "QA_REPORT.md").write_text("# 글·그림 검수\n\nTODO: 기술적 근거, 기존 글 대조 결과, 코드·본문 일치, 이미지별 원본·360px·390px 검수 결과를 기록한다.\n", encoding="utf-8")
    write(folder / "post.json", {"id": args.slug, "title": args.title, "category": "알고리즘",
          "tags": ["백준", "알고리즘", "Python"], "reader_question": "TODO", "contribution": "TODO",
          "intent": "new", "target_url": None, "sources": sources, "experiments": experiments,
          "images": [], "review": {"technical": False, "visual": False, "notes": ""},
          "source_versions": versions, "status": "draft", "publication": None})
    print("글 초안 패키지 생성:", folder.relative_to(ROOT), "— 본문·그림 제작과 실제 검수가 필요합니다.")


def blog_module():
    spec = importlib.util.spec_from_file_location("blog_tool", Path(__file__).with_name("blog.py"))
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ImportError as exc:
        raise ValueError("블로그 도구 설치: python3 -m pip install -r study-workflow/requirements-blog.txt") from exc
    return module


def validate_blog(folder):
    module = blog_module()
    report = module.check_post(folder)
    m = read(folder / "post.json")
    errors = list(report["errors"])
    if not m.get("source_versions"):
        errors.append("source_versions가 비어 있습니다.")
    for source in m.get("source_versions", []):
        _, prob_folder, pm = opened(source["boj_id"])
        if (not reviewed(prob_folder, pm) or source["solution_sha256"] != sha(prob_folder / "solution.py")
                or source["note_sha256"] != sha(prob_folder / "README.md")):
            errors.append(f'{source["boj_id"]}번 원본이 변경되었거나 검토가 필요합니다.')
    for field in ("reader_question", "contribution", "title"):
        if has_todo(m.get(field, "")):
            errors.append("미완성 메타데이터: " + field)
    for name in ("post.md", "QA_REPORT.md"):
        path = folder / name
        if not path.exists() or not path.read_text(encoding="utf-8").strip() or has_todo(path.read_text(encoding="utf-8")):
            errors.append("미완성 문서: " + name)
    if any(m.get("review", {}).get(key) is not True for key in ("technical", "visual")):
        errors.append("기술·시각 검수 기록이 필요합니다. 그림이 없으면 그 이유와 본문 미리보기 검수를 QA에 기록하세요.")
    if errors:
        raise ValueError("\n".join(errors))
    return module, m


def handoff_hash(folder, m):
    files = [folder / "post.md", folder / "QA_REPORT.md"]
    files += [inside(folder, image["path"]) for image in m["images"]]
    content = {str(p.relative_to(folder)): sha(p) for p in files}
    content["metadata"] = {k: v for k, v in m.items() if k not in {"status", "ready_at", "handoff_sha256", "publication"}}
    return hashlib.sha256(json.dumps(content, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def blog_ready(args):
    folder = blog_path(args.slug)
    _, m = validate_blog(folder)
    m["status"] = "ready_for_user_authoring"
    m["ready_at"] = now().isoformat()
    m["handoff_sha256"] = handoff_hash(folder, m)
    write(folder / "post.json", m)
    print("작성 인계 준비 완료. 티스토리 발행 상태와 별개입니다.")


def handoff(args):
    folder = blog_path(args.slug)
    _, m = validate_blog(folder)
    if m.get("status") != "ready_for_user_authoring" or m.get("handoff_sha256") != handoff_hash(folder, m):
        raise ValueError("현재 원고·그림으로 blog-ready를 먼저 실행하세요.")
    body = (folder / "post.md").read_text(encoding="utf-8")
    fence = "`" * max(4, max((len(x) + 1 for x in re.findall(r"`+", body)), default=4))
    text = f'제목: {m["title"]}\n카테고리: {m["category"]}\n태그: {", ".join(m["tags"])}\n\n{fence}markdown\n{body.rstrip()}\n{fence}\n'
    for img in m["images"]:
        text += f'\n![{img.get("purpose", "본문 삽입 이미지")}]({inside(folder, img["path"])})\n'
    # 로컬 절대 경로를 포함하므로 이 파일은 Git 제외 패키지 안에만 보관한다.
    (folder / "chat-handoff.md").write_text(text, encoding="utf-8")
    print(text)


def check(args):
    data = catalog()
    ids = [p["id"] for p in data["problems"]]
    if len(ids) != len(set(ids)):
        raise ValueError("중복 BOJ 번호가 있습니다.")
    concept_ids = {c["id"] for c in data["concepts"]}
    expected_paths = set()
    for p in data["problems"]:
        if type(p["id"]) is not int or p["id"] <= 0 or p["concept"] not in concept_ids or p["track"] not in TRACKS:
            raise ValueError("잘못된 후보 정보: " + str(p))
        _, folder = problem(p["id"])
        expected_paths.add(folder / "meta.json")
        if not (folder / "meta.json").exists():
            continue
        m = read(folder / "meta.json")
        if m["boj_id"] != p["id"] or m["concept"] != p["concept"]:
            raise ValueError("후보와 문제 메타데이터 불일치")
        for name in ("solution.py", "README.md", "tests/README.md"):
            if not (folder / name).is_file():
                raise ValueError("필수 파일 누락: " + str(folder / name))
        if (m.get("local_test") or {}).get("passed"):
            if not local_ok(folder, m):
                raise ValueError(f'{p["id"]}: 코드·테스트 수정 후 재실행 필요')
        if (m.get("reviews") or [{}])[-1].get("result") == "complete" and not reviewed(folder, m):
            raise ValueError(f'{p["id"]}: 현재 버전의 AC·테스트·풀이 검토 갱신 필요')
    actual_paths = set((ROOT / "백준/개념별").glob("*/*/meta.json"))
    if actual_paths - expected_paths:
        raise ValueError("후보 목록에 없는 문제 메타데이터가 있습니다.")
    index_path = ROOT / "백준/README.md"
    if not index_path.is_file() or index_path.read_text(encoding="utf-8") != index_text():
        raise ValueError("문제 인덱스가 최신 상태가 아닙니다. index를 실행하세요.")
    import dashboard_export
    dashboard_path = ROOT / "study-workflow/dashboard-data.json"
    if not dashboard_path.is_file() or read(dashboard_path) != dashboard_export.build(sys.modules[__name__]):
        raise ValueError("대시보드 데이터가 최신 상태가 아닙니다. index를 실행하세요.")
    print(f"기록 검사 통과: 후보 {len(ids)}개, 시작한 문제 {len(actual_paths)}개. 풀이 정답 판정은 별도입니다.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="별도 복사본/테스트 루트")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("next"); p.add_argument("--concept"); p.add_argument("--limit", type=int, default=5)
    p = sub.add_parser("start"); p.add_argument("id", type=int)
    p = sub.add_parser("test"); p.add_argument("id", type=int); p.add_argument("--timeout", type=float)
    p = sub.add_parser("record"); p.add_argument("id", type=int); p.add_argument("--verdict", choices=VERDICTS, required=True)
    p.add_argument("--source", choices=("user_report", "page_verified"), required=True); p.add_argument("--evidence", required=True)
    p = sub.add_parser("review"); p.add_argument("id", type=int)
    p.add_argument("--result", choices=("complete", "retry"), default="complete"); p.add_argument("--note", required=True)
    p.add_argument("--blog", choices=("skip", "candidate"), required=True); p.add_argument("--blog-reason", required=True)
    p = sub.add_parser("import-solved"); p.add_argument("file"); p.add_argument("--observed-at", required=True); p.add_argument("--source", required=True)
    p.add_argument("--namespace", choices=("boj", "solved_ac"), default="boj")
    for name in ("index", "check"):
        sub.add_parser(name)
    p = sub.add_parser("blog"); p.add_argument("slug"); p.add_argument("--ids", nargs="+", type=int, required=True); p.add_argument("--title", required=True)
    for name in ("blog-ready", "handoff"):
        p = sub.add_parser(name); p.add_argument("slug")
    args = parser.parse_args()
    global ROOT
    if args.root:
        ROOT = args.root.resolve()
    try:
        if args.command == "next" and args.limit <= 0:
            raise ValueError("limit은 양수여야 합니다.")
        {"next": next_problems, "start": start, "test": run_tests, "record": record, "review": review,
         "import-solved": import_solved, "index": index, "check": check, "blog": make_blog,
         "blog-ready": blog_ready, "handoff": handoff}[args.command](args)
        return 0
    except (ValueError, KeyError, OSError, TypeError) as exc:
        print("오류:", exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
