"""임시 합성 문제로 상태 전이와 잘못된 완료 처리를 검사한다. 실제 BOJ 실적이 아니다."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "study-workflow/scripts/study.py"


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        work = self.root / "study-workflow"
        work.mkdir()
        shutil.copy(REPO / "study-workflow/config.json", work / "config.json")
        shutil.copytree(REPO / "study-workflow/templates", work / "templates")
        concept = {"id": "01_test", "name": "합성 테스트", "question": "상태 관리가 올바른가?"}
        problems = [{"id": pid, "title": f"Synthetic {pid}", "concept": "01_test", "track": track,
                     "reason": "도구 검증 전용", "url": f"https://acmicpc.net/problem/{pid}",
                     "cases": [{"name": "sample01", "input": "hello\n", "output": "hello\n", "source": "synthetic"}]}
                    for pid, track in [(1, "concept"), (2, "practical"), (3, "challenge")]]
        self.dump(work / "curriculum.json", {"concepts": [concept], "problems": problems})
        self.folder = self.root / "백준/개념별/01_test/1"

    def dump(self, path, obj):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")

    def run_cli(self, *args, ok=True):
        result = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), *args],
                                capture_output=True, text=True, timeout=20)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def meta(self):
        return json.loads((self.folder / "meta.json").read_text())

    def passing(self):
        self.run_cli("start", "1")
        (self.folder / "solution.py").write_text("import sys\nsys.stdout.write(sys.stdin.read())\n")
        self.run_cli("test", "1")

    def complete(self):
        self.passing()
        self.run_cli("record", "1", "--verdict", "AC", "--source", "user_report", "--evidence", "합성 테스트 전용")
        (self.folder / "README.md").write_text("# 합성 문제\n\n## 문제를 내 말로\n입력 문자열을 출력한다.\n\n## 접근과 정당성\n입력을 그대로 출력한다.\n\n## 경계 입력과 검증\n합성 문자열 검사.\n\n## 시간·공간 복잡도\n입력 길이 N에 대해 시간 O(N), 공간 O(N).\n\n## 다음에 기억할 것\n문자열 보존.\n\n## 블로그 판단\n도구 테스트 전용.\n")
        self.run_cli("review", "1", "--note", "합성 검토", "--blog", "candidate", "--blog-reason", "합성 글")

    def test_start_preserves_existing_files_and_empty_code_fails(self):
        self.run_cli("start", "1")
        original = (self.folder / "solution.py").read_text()
        self.run_cli("start", "1", ok=False)
        self.assertEqual((self.folder / "solution.py").read_text(), original)
        self.run_cli("test", "1", ok=False)
        self.assertFalse(self.meta()["local_test"]["passed"])
        self.assertEqual(self.meta()["submissions"], [])

    def test_missing_and_orphan_tests_fail(self):
        self.run_cli("start", "1")
        (self.folder / "tests/sample01.out").unlink()
        self.run_cli("test", "1", ok=False)
        (self.folder / "tests/sample01.in").unlink()
        self.run_cli("test", "1", ok=False)

    def test_local_pass_does_not_create_ac_or_allow_review(self):
        self.passing()
        self.assertEqual(self.meta()["submissions"], [])
        self.run_cli("review", "1", "--note", "test", "--blog", "skip", "--blog-reason", "test", ok=False)
        self.assertIn("로컬 통과 · AC 미확인", (self.root / "백준/README.md").read_text())

    def test_timeout_and_wrong_answer_are_failures(self):
        self.run_cli("start", "1")
        (self.folder / "solution.py").write_text("print('wrong')\n")
        self.run_cli("test", "1", ok=False)
        (self.folder / "solution.py").write_text("while True: pass\n")
        self.run_cli("test", "1", "--timeout", "0.05", ok=False)
        self.assertEqual(self.meta()["local_test"]["cases"][0]["result"], "TIMEOUT(로컬)")

    def test_ac_requires_evidence_and_complete_notes(self):
        self.passing()
        self.run_cli("record", "1", "--verdict", "AC", "--source", "user_report", "--evidence", " ", ok=False)
        self.run_cli("record", "1", "--verdict", "AC", "--source", "page_verified", "--evidence", "https://example.com", ok=False)
        self.run_cli("record", "1", "--verdict", "AC", "--source", "user_report", "--evidence", "합성")
        self.run_cli("review", "1", "--note", "test", "--blog", "skip", "--blog-reason", "test", ok=False)

    def test_modified_code_invalidates_test_ac_and_review(self):
        self.complete()
        self.run_cli("check")
        with (self.folder / "solution.py").open("a") as f:
            f.write("# changed\n")
        self.run_cli("check", ok=False)
        self.run_cli("test", "1")
        self.run_cli("review", "1", "--note", "test", "--blog", "skip", "--blog-reason", "test", ok=False)

    def test_modified_note_or_tests_invalidates_review(self):
        self.complete()
        before = (self.folder / "README.md").read_text()
        (self.folder / "README.md").write_text(before + "추가 설명\n")
        self.run_cli("check", ok=False)
        (self.folder / "README.md").write_text(before)
        (self.folder / "tests/sample01.in").write_text("changed\n")
        self.run_cli("check", ok=False)

    def test_import_excludes_solved_without_inventing_solutions(self):
        path = self.root / "solved.json"
        self.dump(path, [1, 2])
        self.run_cli("import-solved", str(path), "--observed-at", "2026-11-23", "--source", "synthetic")
        result = self.run_cli("next")
        self.assertNotIn("1 · Synthetic", result.stdout)
        self.assertNotIn("2 · Synthetic", result.stdout)
        self.assertIn("3 · Synthetic", result.stdout)
        self.assertFalse(self.folder.exists())

    def test_solved_ac_namespace_is_not_assumed_to_be_boj(self):
        path = self.root / "solved.json"
        self.dump(path, ["1", "100a"])
        self.run_cli("import-solved", str(path), "--namespace", "solved_ac", "--observed-at", "2026-11-23", "--source", "synthetic")
        self.assertIn("1 · Synthetic", self.run_cli("next").stdout)
        cat = self.root / "study-workflow/curriculum.json"
        data = json.loads(cat.read_text()); data["problems"][0]["solved_ac_id"] = "100a"; self.dump(cat, data)
        self.assertNotIn("1 · Synthetic", self.run_cli("next").stdout)

    def test_due_review_is_prioritized(self):
        self.complete()
        m = self.meta(); m["reviews"][-1]["next_review"] = "2020-01-01"; self.dump(self.folder / "meta.json", m)
        result = self.run_cli("next", "--limit", "1")
        self.assertIn("1 · Synthetic 1 [복습", result.stdout)

    def test_index_staleness_is_rejected(self):
        self.passing()
        (self.root / "백준/README.md").write_text("오래된 목록\n")
        self.run_cli("check", ok=False)
        self.run_cli("index")
        self.run_cli("check")

    def test_heading_only_note_is_not_complete(self):
        self.passing()
        self.run_cli("record", "1", "--verdict", "AC", "--source", "user_report", "--evidence", "합성")
        (self.folder / "README.md").write_text("# 제목만 있는 노트\n")
        self.run_cli("review", "1", "--note", "test", "--blog", "skip", "--blog-reason", "test", ok=False)

    def test_dashboard_keeps_local_pass_separate_from_online_ac(self):
        self.passing()
        snapshot = json.loads((self.root / "study-workflow/dashboard-data.json").read_text())
        p = snapshot["problems"][0]
        self.assertEqual(p["status"], "tested")
        self.assertIsNone(p["submission"])
        self.assertNotIn("solution_sha256", json.dumps(snapshot))
        self.assertNotIn("sys.stdout.write", json.dumps(snapshot))

    def test_dashboard_stale_profile_is_rejected(self):
        self.passing()
        config = self.root / "study-workflow/config.json"
        data = json.loads(config.read_text()); data["profile"]["rating"] += 1; self.dump(config, data)
        result = self.run_cli("check", ok=False)
        self.assertIn("대시보드", result.stderr)
        self.run_cli("index")
        self.run_cli("check")

    def test_blog_handoff_requires_ready_and_detects_changes(self):
        self.complete()
        self.run_cli("blog", "demo", "--ids", "1", "--title", "합성 입력 전달 예제")
        self.run_cli("blog", "demo", "--ids", "1", "--title", "보존", ok=False)
        self.run_cli("blog-ready", "demo", ok=False)
        folder = self.root / "blog-workflow/posts/demo"
        meta = json.loads((folder / "post.json").read_text())
        meta.update(reader_question="어떻게 입력을 보존하는가?", contribution="검사 예제")
        meta["review"] = {"technical": True, "visual": True, "notes": "합성 테스트에서만 사용"}
        self.dump(folder / "post.json", meta)
        (folder / "post.md").write_text("입력을 그대로 출력하면 문자열이 보존된다.\n\n```python\nprint('hello')\n```\n")
        (folder / "QA_REPORT.md").write_text("합성 검수. 이미지 없는 예제에서 인계 검사만 수행한다.\n")
        self.run_cli("handoff", "demo", ok=False)
        self.run_cli("blog-ready", "demo")
        result = self.run_cli("handoff", "demo")
        self.assertIn("````markdown", result.stdout)
        self.assertIn("print('hello')", result.stdout)
        (folder / "post.md").write_text("원고를 바꿨다.\n")
        self.run_cli("handoff", "demo", ok=False)

    def test_blog_missing_image_and_stale_source_fail(self):
        self.complete()
        self.run_cli("blog", "demo", "--ids", "1", "--title", "테스트")
        folder = self.root / "blog-workflow/posts/demo"
        meta = json.loads((folder / "post.json").read_text())
        meta.update(reader_question="검수 질문", contribution="검수 예제", images=[{"path": "img/missing.png", "purpose": "검증"}])
        meta["review"] = {"technical": True, "visual": True}
        self.dump(folder / "post.json", meta)
        (folder / "post.md").write_text("본문.\n<!-- 이미지 삽입: img/missing.png | 대체텍스트: 검증 | 캡션: 검증 -->\n")
        (folder / "QA_REPORT.md").write_text("합성 검수\n")
        self.run_cli("blog-ready", "demo", ok=False)
        meta["images"] = []; self.dump(folder / "post.json", meta)
        (folder / "post.md").write_text("본문.\n")
        (self.folder / "README.md").write_text("변경한 풀이 노트.\n")
        self.run_cli("blog-ready", "demo", ok=False)


if __name__ == "__main__":
    unittest.main()
