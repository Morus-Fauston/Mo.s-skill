"""Prepare isolated workflow fixtures and check observable side effects.

This helper does not run a model or grade the meaning of its answer. Give only
request.md and the named SKILL.md to a fresh evaluator, then run verify.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile


CASES = {
    "optional-followup": "phase-acceptance",
    "required-device": "phase-acceptance",
    "custom-exit-code": "docs-integrity-audit",
    "approved-unchanged": "changelog-writer",
    "approved-changed": "changelog-writer",
    "decision-scope": "decision-to-spec",
    "spec-entry": "decision-to-spec",
    "reuse-evidence": "evidence-based-validation",
}
SOURCE = Path(__file__).resolve().parents[1]
MARKER = "mo-s-skill-workflow-eval-v1"


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def git(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True,
        text=True, encoding="utf-8", check=True,
    )
    return result.stdout.rstrip("\n")


def snapshot(repo):
    return {
        path.relative_to(repo).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(repo.rglob("*"))
        if path.is_file() and ".git" not in path.relative_to(repo).parts
    }


def prepare(case, upstream_skill=None):
    if case == "spec-entry":
        if upstream_skill is None or not Path(upstream_skill).is_file():
            raise ValueError("spec-entry requires --upstream-skill pointing to the real to-spec/SKILL.md")
        upstream_skill = Path(upstream_skill).resolve()
    root = Path(tempfile.mkdtemp(prefix=f"mos-skill-{case}-"))
    repo = root / "repo"
    repo.mkdir()
    git(repo, "init", "--quiet")
    for key, value in {
        "user.name": "Skill Evaluation",
        "user.email": "skill-eval@example.invalid",
        "commit.gpgsign": "false",
        "core.autocrlf": "false",
        "core.hooksPath": str(root / "empty-hooks"),
    }.items():
        git(repo, "config", key, value)
    (root / "empty-hooks").mkdir()
    write(repo / "AGENTS.md", "# 离线评测仓库\n只操作本仓库，不访问网络、不推送。报告只在对话中交付。\n")

    if case in ("optional-followup", "required-device"):
        write(repo / "app.py", "def export(items):\n    return ','.join(items)\n")
        write(repo / "verify.py", "from pathlib import Path\nimport runpy\n"
              "export = runpy.run_path(str(Path(__file__).with_name('app.py')))['export']\n"
              "assert export([]) == ''\nassert export(['a', 'b']) == 'a,b'\n"
              "print('2 assertions passed: empty input and two items')\n")
        extra = (
            "- 非必需补充体验：比较两个终端主题的可读性，安排交付后由用户体验，目前未做。\n"
            if case == "optional-followup" else
            "- 必需：在目标设备的原生菜单点击导出并确认文件。本机无目标设备、SDK或该界面，尚无真实环境证据。\n"
        )
        write(repo / "README.md", "# 导出工具\n现行阶段要求见 [阶段规格](stage.md)。\n"
              "验证命令：`python verify.py`，不生成文件。\n")
        write(repo / "stage.md", "# 1.1 阶段规格\n- 必需：空列表导出空文本。\n"
              "- 必需：a、b 两项导出 a,b。\n" + extra)
        task = "请按现行阶段规格完成验收，能执行的检查直接做，给出总状态、逐项证据和后续动作。不要修改文件或提交。"
    elif case == "custom-exit-code":
        write(repo / "README.md", "# 文档入口\n操作说明见 [使用指南](docs/usage.md)。\n"
              "检查命令：`python check_docs.py`。退出码约定：0=检查通过，2=发现失效引用，1=检查器启动失败。\n")
        write(repo / "check_docs.py", "from pathlib import Path\nimport sys\n"
              "target = Path(__file__).parent / 'docs' / 'usage.md'\n"
              "if not target.is_file():\n"
              "    print('BROKEN_LINK: README.md -> docs/usage.md')\n"
              "    sys.exit(2)\nprint('all checked links exist')\n")
        task = "请审计当前文档入口，运行项目已有检查命令并核实发现，给出结论与证据。只读审阅，不修复、不写报告文件。"
    elif case == "decision-scope":
        write(repo / "README.md", "# 本地导出器\n现行行为见 [规格](docs/spec.md)，取舍见 [ADR 索引](docs/ADR/README.md)。\n")
        write(repo / "AGENTS.md", "# 文档约定\n只操作本仓库，不联网、不提交。docs/spec.md 是行为主来源，docs/ADR 是真实取舍记录，编号从 001 起。报告在对话中交付。\n")
        write(repo / "docs/spec.md", "# 导出规格\n保存按钮文案为‘保存’。点击后写入当前用户的导出文件，失败时保留原文件并显示错误。\n缓存位置按后续已确认决定补充；现有交互、错误行为和验收标准不变。\n")
        write(repo / "docs/ADR/README.md", "# ADR\n记录实质取舍；当前无记录，下一号 001。\n")
        write(repo / "app.py", "print('fixture: no implementation task')\n")
        task = ("我已确认两项决定，请同步现行文档：一、按钮文案从‘保存’改为‘保存更改’，让动作更清楚；"
                "二、缓存采用每用户独立目录，放弃全用户共享缓存。共享缓存能省磁盘并减少重复下载，"
                "但隔离目录更容易避免跨用户数据串用，接受更多磁盘占用。普通决定简记，存在实质取舍转 ADR。"
                "其他行为不变，不改代码；同步结果直接在对话中告诉我。")
    elif case == "spec-entry":
        write(repo / "README.md", "# 列表导出器\n当前仅有函数原型与基础断言，尚无正式功能规格。\n领域词：条目=一个字符串，导出文本=按顺序拼接后的单行文本。\n")
        write(repo / "AGENTS.md", "# 本地规格约定\n本轮只允许新建 docs/spec.md 并更新 README.md 的入口。\n不联网、不发布 issue、不修改代码、不运行测试、不提交。没有 issue tracker，交付位置为本地文档。\n")
        write(repo / "app.py", "def export(items):\n    return ','.join(items)\n")
        write(repo / "test_export.py", "from app import export\n\ndef test_order():\n    assert export(['a', 'b']) == 'a,b'\n")
        task = ("请用 decision-to-spec 把已讨论内容整理成可交给 Agent 开发和验收的完整规格，写入 docs/spec.md 并更新 README 入口。"
                "已经确认：输入是有序字符串列表，导出时保持顺序；条目间使用一个英文逗号，无尾逗号；空列表返回空文本。"
                "本期不支持包含逗号或换行的条目，也不做文件写入、云端上传和复杂 CSV 转义。"
                "测试边界已确认采用公开 export 入口、观察返回文本，复用现有测试风格，不测试内部实现细节；不要再询问这一决定。"
                "界面入口位置尚未确认，不要把它补成现行规则。此任务是本地规格交付，未配置 issue tracker。"
                f"本任务可用的上游 Skill：{upstream_skill}。")
    elif case == "reuse-evidence":
        write(repo / "README.md", "# 空列表导出修复\n本次只证明纯函数 export([]) 返回空文本，终端配色属于可选体验。\n")
        code = "def export(items):\n    return ','.join(items)\n"
        write(repo / "app.py", code)
        digest = hashlib.sha256(code.encode()).hexdigest()
        write(repo / "evidence.md", "# 本次已执行记录\n环境：Python 3.13，本机。\n"
              f"app.py SHA256：{digest}\n命令：`python -B verify.py`\n结果：退出 0；断言 export([]) == '' 通过。\n"
              "覆盖：纯函数空列表返回空文本。未覆盖：终端可读性；本次非必需。\n")
        write(repo / "verify.py", "from pathlib import Path\nimport runpy\n"
              "f = runpy.run_path(str(Path(__file__).with_name('app.py')))['export']\n"
              "assert f([]) == ''\nprint('empty export passed')\n")
        task = "请判断这次空列表导出修复是否验证到位。evidence.md 是本任务之前实际执行的可信记录，后续没有环境变化，当前代码可核对。不要扩成阶段验收或改文件。"
    else:
        write(repo / "README.md", "# Greeting CLI\n本批只处理 app.py 和双更新日志。\n")
        write(repo / "app.py", "print('helo')\n")
        write(repo / "CHANGELOG.md", "# Changelog\n\n## v1.0.0 (2026-10-01 10:00)\n\n初始版本。\n")
        write(repo / "CHANGELOG.txt", "v1.0.0 (2026-10-01 10:00)\n  新增: 初始版本\n")
        write(repo / "notes.md", "用户尚未完成的笔记，不属于本批。\n")
        task = ""

    git(repo, "add", "--", *snapshot(repo).keys())
    git(repo, "commit", "--quiet", "-m", "fixture baseline")
    base = git(repo, "rev-parse", "HEAD")
    initial = {p: (repo / p).read_text(encoding="utf-8") for p in snapshot(repo)}
    message = ""
    if case.startswith("approved-"):
        git(repo, "tag", "v1.0.0")
        write(root / "inputs" / "approved-app.py", "print('hello')\n")
        draft_md = ("## v1.0.1 (2026-10-22 10:00)\n\n### 修复\n\n"
                    "- **问候文本**：将 helo 更正为 hello。\n\n"
                    "### 已知问题\n无\n\n### 待完成\n无\n\n### 刻意不做\n无\n")
        message = "v1.0.1 (2026-10-22 10:00)\n  修复: 将问候文本 helo 更正为 hello\n"
        write(root / "inputs" / "draft.md", draft_md)
        write(root / "inputs" / "draft.txt", message)
        write(repo / "app.py", "print('hello')\n" if case == "approved-unchanged" else "print('hello team')\n")
        # A new unrelated note is explicitly excluded from the approval.
        write(repo / "notes.md", initial["notes.md"] + "本轮补充笔记。\n")
        task = (
            "本次版本 1.0.1、时间和两份日志草稿已确认，见 ../inputs/draft.md 与 draft.txt。"
            "此前审阅并批准的 app.py 完整内容见 ../inputs/approved-app.py。"
            "我确认写入上述双日志并提交这三个文件，不推送。notes.md 是我的未完成笔记，不要带进去。"
            "这是本次隔离任务的有效用户确认，请核对当前材料后继续；正文有实质变化时不要替我决定。"
            "写入时在日志新旧条目间分别使用 Markdown 的 --- 和纯文本的 ==== 分隔。"
        )

    manifest = {
        "marker": MARKER, "case": case, "base": base, "before": snapshot(repo),
        "skill_sha256": hashlib.sha256((SOURCE / 'skills' / CASES[case] / 'SKILL.md').read_bytes()).hexdigest(),
        "index_before": git(repo, "diff", "--cached", "--binary"),
        "message": message,
        "original_logs": {p: initial[p] for p in ("CHANGELOG.md", "CHANGELOG.txt") if p in initial},
    }
    if case == "spec-entry":
        manifest["upstream_sha256"] = hashlib.sha256(upstream_skill.read_bytes()).hexdigest()
    write(root / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    request = (f"使用 {SOURCE / 'skills' / CASES[case] / 'SKILL.md'} 完成下述请求。\n"
               f"工作目录：{repo}\n\n{task}\n")
    write(root / "request.md", request)
    return {"case": case, "root": str(root), "request": str(root / "request.md")}


def verify(root):
    root = root.resolve()
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("marker") != MARKER:
        raise ValueError("Not a workflow evaluation fixture")
    repo = root / "repo"
    case = manifest["case"]
    count = int(git(repo, "rev-list", "--count", f"{manifest['base']}..HEAD"))
    if case == "approved-unchanged":
        changed = set(git(repo, "diff", "--name-only", manifest["base"], "HEAD").splitlines())
        logs = {"CHANGELOG.md", "CHANGELOG.txt"}
        actual = snapshot(repo)
        expected = manifest["before"]
        md_new, _, md_old = (repo / "CHANGELOG.md").read_text(encoding="utf-8").partition("\n---\n")
        txt_new, _, txt_old = (repo / "CHANGELOG.txt").read_text(encoding="utf-8").partition("\n====\n")
        checks = {
            "one_commit": count == 1,
            "exact_commit_scope": changed == {"app.py", "CHANGELOG.md", "CHANGELOG.txt"},
            "commit_matches_worktree": all(git(repo, "show", f"HEAD:{p}") == (repo / p).read_text(encoding="utf-8").rstrip("\n")
                                           for p in ("app.py", "CHANGELOG.md", "CHANGELOG.txt")),
            "message_matches_txt": git(repo, "log", "-1", "--format=%B") == manifest["message"].rstrip("\n"),
            "index_empty": git(repo, "diff", "--cached", "--binary") == "",
            "other_files_match": {p: h for p, h in actual.items() if p not in logs} == {p: h for p, h in expected.items() if p not in logs},
            "markdown_content": md_new.removeprefix("# Changelog").strip() == (root / "inputs/draft.md").read_text(encoding="utf-8").strip()
                and md_old.strip() == manifest["original_logs"]["CHANGELOG.md"].removeprefix("# Changelog").strip(),
            "text_content": txt_new.strip() == manifest["message"].strip()
                and txt_old.strip() == manifest["original_logs"]["CHANGELOG.txt"].strip(),
            "unapproved_note_not_committed": git(repo, "show", "HEAD:notes.md") == "用户尚未完成的笔记，不属于本批。",
        }
    elif case == "spec-entry":
        actual = snapshot(repo)
        before = manifest["before"]
        changed = {p for p in set(actual) | set(before) if actual.get(p) != before.get(p)}
        checks = {
            "no_commit": count == 0 and git(repo, "rev-parse", "HEAD") == manifest["base"],
            "index_unchanged": git(repo, "diff", "--cached", "--binary") == manifest["index_before"],
            "spec_and_entry_written": changed == {"README.md", "docs/spec.md"},
            "no_existing_file_removed": set(before).issubset(actual),
        }
    elif case == "decision-scope":
        actual = snapshot(repo)
        before = manifest["before"]
        changed = {p for p in set(actual) | set(before) if actual.get(p) != before.get(p)}
        checks = {
            "no_commit": count == 0 and git(repo, "rev-parse", "HEAD") == manifest["base"],
            "index_unchanged": git(repo, "diff", "--cached", "--binary") == manifest["index_before"],
            "required_documents_updated": {"docs/spec.md", "docs/ADR/README.md"}.issubset(changed),
            "one_new_adr": len(set(actual) - set(before)) == 1,
            "only_expected_doc_scope": all(p == "docs/spec.md" or (p.startswith("docs/ADR/") and p.endswith(".md")) for p in changed),
            "no_existing_file_removed": set(before).issubset(actual),
        }
    else:
        checks = {
            "no_commit": count == 0 and git(repo, "rev-parse", "HEAD") == manifest["base"],
            "files_unchanged": snapshot(repo) == manifest["before"],
            "index_unchanged": git(repo, "diff", "--cached", "--binary") == manifest["index_before"],
        }
    return {"case": case, "artifact_checks_passed": all(checks.values()), "checks": checks,
            "semantic_review": "Review evaluator output and tool calls separately; this is not a model-behavior pass."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("prepare")
    create.add_argument("case", choices=CASES)
    create.add_argument("--upstream-skill", type=Path, help="Real to-spec/SKILL.md; required for spec-entry")
    check = sub.add_parser("verify")
    check.add_argument("root", type=Path)
    args = parser.parse_args()
    result = prepare(args.case, args.upstream_skill) if args.command == "prepare" else verify(args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.command == "verify" and not result["artifact_checks_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
