from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

articles_dir = project_root / "docs" / "articles"
includes_dir = project_root / "docs" / "includes"

includes_dir.mkdir(parents=True, exist_ok=True)

articles = sorted(
    articles_dir.glob("*.md"),
    key=lambda x: x.stat().st_mtime,
    reverse=True
)

content = "# Derniers articles\n\n"

for article in articles[:5]:

    title = article.stem.replace("-", " ").title()

    content += f"- {title}\n"

with open(
    includes_dir / "latest_articles.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(content)

print("Derniers articles générés.")