import os, re

BASE = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website"
FR = os.path.join(BASE, "fr")

# Map of regex patterns to (image file, alt text)
photo_map = [
    (r'[Kk]oobideh|[Kk]abab.*[Gg]rill|mangal',         'kabab-grill.png',      'Kabab grillé',                  True),
    (r'[Bb]oucher|[Bb]utcher|[Hh]alal.*comptoir|comptoir.*[Hh]alal', 'meat-counter.jpg', 'Comptoir boucherie Halal', False),
    (r'[Mm]arin',                                        'marinated-meat.jpg',   'Viande marinée',                False),
    (r'[Ss]urgel|[Cc]ongel|[Ff]rozen',                  'frozen.jpg',           'Rayon congelés',                False),
    (r'[Pp]ain|[Bb]read.*[Ll]avash|[Ll]avash',          'bread.jpg',            'Pain frais et lavash',          False),
    (r'[Ss]ucrerie|[Pp][aâ]tisserie|[Ss]weet|[Pp]astry','sweets.jpg',           'Sucreries persanes',            False),
    (r'[Bb]oisson|[Dd]oogh|[Bb]everage|[Dd]rink',       'beverage.jpg',         'Boissons et Doogh',             False),
]

for fname in os.listdir(FR):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(FR, fname)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='latin-1') as f:
            content = f.read()

    original = content

    for pattern, imgfile, alt, has_style in photo_map:
        img_tag = f'<img src="../assets/{imgfile}" alt="{alt}">'
        img_tag_style = f'<img src="../assets/{imgfile}" alt="{alt}" style="width:100%;height:100%;object-fit:cover">'

        # span with style attribute (hero backgrounds)
        content = re.sub(
            r'<span class="ph" data-label="[^"]*(?:' + pattern + r')[^"]*" style="[^"]*"></span>',
            img_tag_style, content, flags=re.IGNORECASE
        )
        # img ph class
        content = re.sub(
            r'<span class="img ph" data-label="[^"]*(?:' + pattern + r')[^"]*"></span>',
            img_tag, content, flags=re.IGNORECASE
        )
        # plain ph class
        content = re.sub(
            r'<span class="ph" data-label="[^"]*(?:' + pattern + r')[^"]*"></span>',
            img_tag, content, flags=re.IGNORECASE
        )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {fname}")
    else:
        print(f"No change: {fname}")

# Also fix ticks color on dark band in CSS
css_path = os.path.join(BASE, "styles.css")
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '.band .ticks li' not in css:
    css = css.replace(
        '.ticks li{display:flex;gap:.7rem;align-items:flex-start;color:var(--ink-soft)}',
        '.ticks li{display:flex;gap:.7rem;align-items:flex-start;color:var(--ink-soft)}\n.band .ticks li{color:rgba(255,255,255,.82)}'
    )
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS ticks color fixed!")

print("\nAll done!")
