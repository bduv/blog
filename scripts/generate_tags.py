from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

DOCS = ROOT / "docs"

TAGS_DIR = DOCS / "tags"

TAGS_DIR.mkdir(exist_ok=True)

articles = list(DOCS.rglob("*.md"))

tags_map = {}

for article in articles:

    try:
        content = article.read_text(
            encoding="utf-8"
        )

    except:
        continue

    match = re.search(
        r"tags:\s*((?:\n\s*-\s*.+)+)",
        content
    )

    if not match:
        continue

    tag_block = match.group(1)

    tags = re.findall(
        r"-\s*(.+)",
        tag_block
    )

    for tag in tags:

        tags_map.setdefault(tag, [])

        tags_map[tag].append(article)

for tag, files in tags_map.items():

    output = f"# {tag}\n\n"

    for file in files:

        rel = file.relative_to(DOCS)

        title = file.stem.replace(
            "-",
            " "
        ).title()

        output += (
            f"- [{title}]"
            f"(../{rel.as_posix()})\n"
        )

    (TAGS_DIR / f"{tag}.md").write_text(
        output,
        encoding="utf-8"
    )

print("Tags générés")