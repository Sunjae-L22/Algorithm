"""공개 저장소의 학습 기록만 웹 대시보드용 JSON으로 내보낸다."""
import json
from urllib.parse import quote


def build(study):
    config, curriculum = study.cfg(), study.catalog()
    repo = config["github"]["repository"]
    branch = config["github"]["branch"]
    github = f"https://github.com/{repo}/blob/{branch}/"
    concept_names = {c["id"]: c["name"] for c in curriculum["concepts"]}
    problems = []
    timestamps = [config["profile_checked_at"]]
    for p in curriculum["problems"]:
        _, folder = study.problem(p["id"])
        m = study.read(folder / "meta.json") if (folder / "meta.json").exists() else None
        prior = bool(p.get("prior_solved"))
        key, label = ("previous", "기존 해결") if prior else ("candidate", "후보")
        local = submission = review = None
        if m:
            key, label = "in_progress", "풀이 중"
            if study.reviewed(folder, m): key, label = "complete", "정리 완료"
            elif study.accepted(folder, m): key, label = "accepted", "AC · 정리 필요"
            elif study.local_ok(folder, m): key, label = "tested", "로컬 테스트 통과"
            run = m.get("local_test")
            if run:
                local = {"passed": study.local_ok(folder, m), "recorded_passed": bool(run.get("passed")),
                         "stale": run.get("files") != study.fingerprints(folder), "checked_at": run["checked_at"],
                         "cases": [{"name": c["name"], "passed": c["passed"]} for c in run["cases"]]}
                timestamps.append(run["checked_at"])
            if m.get("submissions"):
                last = m["submissions"][-1]
                submission = {"verdict": last["verdict"], "source": last["source"], "recorded_at": last["recorded_at"],
                              "current_code": last["solution_sha256"] == study.sha(folder / "solution.py")}
                timestamps.append(last["recorded_at"])
            if m.get("reviews"):
                last = m["reviews"][-1]
                review = {"result": last["result"], "next_review": last["next_review"],
                          "reviewed_at": last["reviewed_at"], "current": study.reviewed(folder, m)}
                timestamps.append(last["reviewed_at"])
            timestamps.append(m["created_at"])
        relative = str(folder.relative_to(study.ROOT))
        problems.append({"id": p["id"], "title": p["title"], "url": p["url"], "concept_id": p["concept"],
                         "concept": concept_names[p["concept"]], "track": p["track"], "status": key, "status_label": label,
                         "prior_solved": prior, "started_at": m["created_at"] if m else None,
                         "local_test": local, "submission": submission, "review": review,
                         "blog": m.get("blog", "undecided") if m else "undecided",
                         "github_note": github + quote(relative + "/README.md") if m else None,
                         "github_code": github + quote(relative + "/solution.py") if m else None})
    return {"version": 1, "repository": repo, "branch": branch, "updated_at": max(timestamps),
            "profile": {**config["profile"], "handle": config["solved_ac_handle"], "observed_at": config["profile_checked_at"]},
            "concepts": [{"id": c["id"], "name": c["name"], "question": c["question"],
                          "url": github + quote(f'백준/개념별/{c["id"]}/README.md')} for c in curriculum["concepts"]],
            "problems": problems}


def export(study):
    study.write(study.ROOT / "study-workflow/dashboard-data.json", build(study))


if __name__ == "__main__":
    import study
    export(study)
    print("대시보드 공개 데이터 갱신 완료")
