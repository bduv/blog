from pathlib import Path
from datetime import datetime
import re
import unicodedata

title = input("Titre : ")

# Conversion en slug sans accents
slug = unicodedata.normalize("NFKD", title)
slug = slug.encode("ascii", "ignore").decode("ascii")
slug = slug.lower()
slug = re.sub(r"[^a-z0-9\s-]", "", slug)
slug = re.sub(r"[\s-]+", "-", slug).strip("-")

today = datetime.now().strftime("%Y-%m-%d")

content = f"""---
title: {title}
date: {today}
description:
---

# {title}

Votre contenu ici.
"""

# Racine du projet
project_root = Path(__file__).resolve().parent.parent

# Dossier des articles
articles_dir = project_root / "docs" / "articles"
articles_dir.mkdir(parents=True, exist_ok=True)

# Nom du fichier
file_path = articles_dir / f"{slug}.md"

# Écriture
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print()
print("Article créé avec succès :")
print(file_path)