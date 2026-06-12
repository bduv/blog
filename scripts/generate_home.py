from pathlib import Path

articles = sorted(
    Path("../docs/articles").glob("*.md"),
    key=lambda x: x.stat().st_mtime,
    reverse=True
)

content = "# Derniers articles\n\n"

for a in articles[:5]:
    content += f"- [{a.stem}](/blog/articles/{a.name})\n"

with open(
    "../docs/includes/latest_articles.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(content)