import os, re
folders = [
    "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website",
    "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/fr"
]
for folder in folders:
    prefix = "../" if folder.endswith("/fr") else ""
    for fname in os.listdir(folder):
        if not fname.endswith('.html'): continue
        path = os.path.join(folder, fname)
        try:
            with open(path,'r',encoding='utf-8') as f: content = f.read()
        except:
            with open(path,'r',encoding='latin-1') as f: content = f.read()
        original = content
        content = re.sub(r'<span class="[^"]*ph[^"]*" data-label="[^"]*[Dd]rinks[^"]*"></span>',
            f'<img src="{prefix}assets/beverage.jpg" alt="Drinks and Doogh">', content)
        content = re.sub(r'<span class="[^"]*ph[^"]*" data-label="[^"]*[Dd]oogh[^"]*"></span>',
            f'<img src="{prefix}assets/beverage.jpg" alt="Drinks and Doogh">', content)
        content = re.sub(r'<span class="[^"]*ph[^"]*" data-label="[^"]*[Bb]everage[^"]*"></span>',
            f'<img src="{prefix}assets/beverage.jpg" alt="Drinks and Doogh">', content)
        if content != original:
            with open(path,'w',encoding='utf-8') as f: f.write(content)
            print(f"Updated: {fname}")
        else:
            print(f"No change: {fname}")
print("Done!")
