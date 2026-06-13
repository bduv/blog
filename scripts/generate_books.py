from pathlib import Path

ROOT = Path("docs/livres")

books = []

for file in ROOT.rglob("*.md"):

    if file.name == "index.md":
        continue

    books.append(file)

books.sort(
    key=lambda x: x.stat().st_mtime,
    reverse=True
)

content = "# Dernières lectures\n\n"

for book in books[:8]:

    title = book.stem.replace("-", " ").title()

    rel = str(book.relative_to("docs")).replace("\\", "/")
    content += f"- [{title}]({rel})\n"

Path("docs/includes").mkdir(exist_ok=True)

with open(
    "docs/includes/latest_books.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(content)

print("Dernières lectures générées")