import os

folders = [
    "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website",
    "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/fr"
]

placeholders = [
    'data-label="Photo: Halal butcher counter"',
    'data-label="Photo: Halal butcher at the counter"',
    'data-label="Photo : comptoir boucherie Halal"',
    'data-label="Photo : boucher Halal au comptoir"',
]

for folder in folders:
    prefix = "../" if folder.endswith("/fr") else ""
    for fname in os.listdir(folder):
        if not fname.endswith('.html'):
            continue
        path = os.path.join(folder, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(path, 'r', encoding='latin-1') as f:
                content = f.read()
        original = content
        for label in placeholders:
            content = content.replace(
                f'<span class="img ph" {label}></span>',
                f'<img src="{prefix}assets/meat-counter.jpg" alt="Halal butcher counter">'
            )
            content = content.replace(
                f'<span class="ph" {label}></span>',
                f'<img src="{prefix}assets/meat-counter.jpg" alt="Halal butcher counter">'
            )
            content = content.replace(
                f'<span class="ph" {label} style="width:100%;height:100%"></span>',
                f'<img src="{prefix}assets/meat-counter.jpg" alt="Halal butcher counter" style="width:100%;height:100%;object-fit:cover">'
            )
        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {fname}")
        else:
            print(f"No change: {fname}")

print("\nDone!")
