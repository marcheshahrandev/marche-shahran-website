import os, re

BASE = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website"

# Fix 1: Replace BOUCHER HALAL AU COMPTOIR placeholder in ALL pages (EN + FR)
all_folders = [BASE, os.path.join(BASE, "fr")]

for folder in all_folders:
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

        # All variations of the boucher/halal butcher placeholder
        patterns = [
            r'<span class="ph" data-label="[^"]*[Bb]oucher[^"]*"></span>',
            r'<span class="ph" data-label="[^"]*[Bb]utcher[^"]*"></span>',
            r'<span class="img ph" data-label="[^"]*[Bb]oucher[^"]*"></span>',
            r'<span class="img ph" data-label="[^"]*[Bb]utcher[^"]*"></span>',
        ]
        for p in patterns:
            content = re.sub(p,
                f'<img src="{prefix}assets/meat-counter.jpg" alt="Halal butcher counter">',
                content, flags=re.IGNORECASE)

        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Photo fixed: {fname}")

# Fix 2: Fix ticks text color on dark .band sections in styles.css
css_path = os.path.join(BASE, "styles.css")
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

original_css = css

# Make ticks readable on dark band background
old = '.ticks li{display:flex;gap:.7rem;align-items:flex-start;color:var(--ink-soft)}'
new = '.ticks li{display:flex;gap:.7rem;align-items:flex-start;color:var(--ink-soft)}\n.band .ticks li{color:rgba(255,255,255,.82)}'

css = css.replace(old, new)

if css != original_css:
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS ticks color fixed!")
else:
    print("CSS — no change (already fixed or pattern not found)")

print("\nDone!")
