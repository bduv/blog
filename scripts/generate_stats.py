from pathlib import Path

ROOT = Path("../docs")

articles = len(list(ROOT.rglob("*.md")))

output = f"""
<div class="stats-grid">

<div class="stat-card">
<h2>{articles}</h2>
<p>Pages publiées</p>
</div>

<div class="stat-card">
<h2>∞</h2>
<p>Curiosité intellectuelle</p>
</div>

</div>
"""

(Path("../docs/includes")).mkdir(exist_ok=True)

with open("../docs/includes/stats.md", "w", encoding="utf-8") as f:
    f.write(output)

print("Statistiques générées.")