from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

docs_dir = project_root / "docs"
includes_dir = docs_dir / "includes"

includes_dir.mkdir(parents=True, exist_ok=True)

pages = len(list(docs_dir.rglob("*.md")))

content = f"""
<div class="stats-grid">

<div class="stat-card">
<h2>{pages}</h2>
<p>Pages publiées</p>
</div>

<div class="stat-card">
<h2>∞</h2>
<p>Curiosité intellectuelle</p>
</div>

</div>
"""

with open(
    includes_dir / "stats.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(content)

print("Statistiques générées.")