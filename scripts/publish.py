from datetime import datetime
from pathlib import Path

title = input('Titre : ')

slug = title.lower().replace(' ','-')

today = datetime.now().strftime('%Y-%m-%d')

content = f'''# {title}

Publié le {today}

Votre contenu ici...
'''

path = Path('../docs/articles') / f'{slug}.md'

with open(path,'w',encoding='utf-8') as f:
    f.write(content)

print('Article créé :', path)
