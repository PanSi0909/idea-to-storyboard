#!/usr/bin/env python3
"""Validate the installable Skill, tutorial assets, and distribution archive."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "idea-to-storyboard"
ARCHIVE = ROOT / "dist" / "idea-to-storyboard.skill"
CHECKSUM = ROOT / "dist" / "idea-to-storyboard.skill.sha256"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_skill() -> None:
    required = [
        SKILL_DIR / "SKILL.md",
        SKILL_DIR / "agents" / "openai.yaml",
        SKILL_DIR / "references" / "input-routing.md",
        SKILL_DIR / "references" / "storyboard-schema.md",
    ]
    for path in required:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("SKILL.md frontmatter is not closed")
    frontmatter = parts[1]
    if not re.search(r"(?m)^name:\s*idea-to-storyboard\s*$", frontmatter):
        fail("SKILL.md name must be idea-to-storyboard")
    if not re.search(r"(?m)^description:\s*\S.+$", frontmatter):
        fail("SKILL.md needs a non-empty description")


def validate_svgs() -> None:
    for path in sorted((ROOT / "docs" / "images").glob("*.svg")):
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            fail(f"invalid SVG {path.relative_to(ROOT)}: {exc}")


def validate_archive() -> None:
    if not ARCHIVE.is_file() or not CHECKSUM.is_file():
        fail("distribution archive or checksum is missing")

    fields = CHECKSUM.read_text(encoding="utf-8").strip().split()
    if len(fields) != 2 or fields[1] != ARCHIVE.name:
        fail("checksum file must contain '<sha256>  idea-to-storyboard.skill'")
    actual_hash = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    if fields[0] != actual_hash:
        fail("distribution archive checksum does not match")

    expected_files = {
        f"idea-to-storyboard/{path.relative_to(SKILL_DIR).as_posix()}"
        for path in SKILL_DIR.rglob("*")
        if path.is_file()
    }
    with zipfile.ZipFile(ARCHIVE) as archive:
        actual_files = {name for name in archive.namelist() if not name.endswith("/")}
    if actual_files != expected_files:
        missing = sorted(expected_files - actual_files)
        extra = sorted(actual_files - expected_files)
        fail(f"archive contents differ from Skill source; missing={missing}, extra={extra}")
    if any(".git" in Path(name).parts for name in actual_files):
        fail("distribution archive contains .git data")


def validate_sensitive_data() -> None:
    allowed_public_urls = {
        "https://bytedance.larkoffice.com/wiki/YOE3wXEBriAPESkNcB4cSKxJn2c",
        "https://waytoagi.feishu.cn/wiki/QPe5w5g7UisbEkkow8XcDmOpn8e",
    }
    patterns = {
        "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
        "authorization bearer token": re.compile(
            r"authorization\s*:\s*bearer\s+[A-Za-z0-9._-]{16,}", re.IGNORECASE
        ),
        "Lark secret": re.compile(
            r"(?:tenant_access_token|user_access_token|app_secret)\s*[:=]\s*[\"']?[A-Za-z0-9._-]{8,}",
            re.IGNORECASE,
        ),
    }
    text_suffixes = {".md", ".txt", ".yaml", ".yml", ".json", ".svg"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in text_suffixes and path.name not in {"LICENSE"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "\ufffd" in text:
            fail(f"Unicode replacement character in {path.relative_to(ROOT)}")
        for raw_url in re.findall(r"https?://[^\s)\]>]+", text):
            url = raw_url.rstrip(".,;:!?，。；：！？")
            is_lark_document = any(
                host in url
                for host in ("feishu.cn/", "larksuite.com/", "larkoffice.com/")
            )
            if is_lark_document and url not in allowed_public_urls:
                fail(f"unapproved Feishu/Lark URL in {path.relative_to(ROOT)}")
        for label, pattern in patterns.items():
            if pattern.search(text):
                fail(f"possible {label} in {path.relative_to(ROOT)}")


def validate_markdown_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (path.parent / local_target).resolve().exists():
                fail(
                    f"broken local link in {path.relative_to(ROOT)}: {local_target}"
                )


def main() -> None:
    validate_skill()
    validate_svgs()
    validate_archive()
    validate_sensitive_data()
    validate_markdown_links()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
