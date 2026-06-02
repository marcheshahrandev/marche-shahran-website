import os, re

files = [
    "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/products.html",
    "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/fr/produits.html",
]

for path in files:
    prefix = "../" if "/fr/" in path else ""
    try:
        with open(path,'r',encoding='utf-8') as f: content = f.read()
    except:
        with open(path,'r',encoding='latin-1') as f: content = f.read()
    original = content

    content = re.sub(r'<span class="[^"]*ph[^"]*" data-label="[^"]*[Ff]rozen[^"]*"></span>',
        f'<img src="{prefix}assets/frozen.jpg" alt="Frozen aisle">', content)
    content = re.sub(r'<span class="[^"]*ph[^"]*" data-label="[^"]*[Bb]read[^"]*"></span>',
        f'<img src="{prefix}assets/bread.jpg" alt="Fresh bread and lavash">', content)
    content = re.sub(r'<span class="[^"]*ph[^"]*" data-label="[^"]*[Ss]weet[^"]*"></span>',
        f'<img src="{prefix}assets/sweets.jpg" alt="Persian sweets and pastries">', content)

    if content != original:
        with open(path,'w',encoding='utf-8') as f: f.write(content)
        print(f"Updated: {os.path.basename(path)}")
    else:
        print(f"No change: {os.path.basename(path)}")

print("Done!")
