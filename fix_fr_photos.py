import os, re

folder = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/fr"

photo_map = [
    (r'[Ss]urgel',                                'frozen.jpg',         'Rayon surgelés'),
    (r'[Pp]ain',                                  'bread.jpg',          'Pain frais et lavash'),
    (r'[Ss]ucrerie|[Pp]tisserie|astisserie',      'sweets.jpg',         'Sucreries persanes'),
    (r'[Bb]oisson|[Dd]oogh|[Bb]everage',         'beverage.jpg',       'Boissons et Doogh'),
    (r'[Kk]abab|mangal',                          'kabab-grill.png',    'Kabab grillé'),
    (r'[Bb]oucher|comptoir.*alal|alal.*comptoir', 'meat-counter.jpg',   'Comptoir boucherie Halal'),
    (r'[Mm]arin',                                 'marinated-meat.jpg', 'Viande marinée'),
]

for fname in os.listdir(folder):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(folder, fname)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(path, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            print(f"Skipping {fname}: {e}")
            continue

    original = content

    for pattern, imgfile, alt in photo_map:
        # with style attribute
        content = re.sub(
            r'<span class="[^"]*ph[^"]*" data-label="[^"]*' + pattern + r'[^"]*" style="[^"]*"></span>',
            f'<img src="../assets/{imgfile}" alt="{alt}" style="width:100%;height:100%;object-fit:cover">',
            content, flags=re.IGNORECASE
        )
        # img ph class
        content = re.sub(
            r'<span class="img ph" data-label="[^"]*' + pattern + r'[^"]*"></span>',
            f'<img src="../assets/{imgfile}" alt="{alt}">',
            content, flags=re.IGNORECASE
        )
        # plain ph class
        content = re.sub(
            r'<span class="ph" data-label="[^"]*' + pattern + r'[^"]*"></span>',
            f'<img src="../assets/{imgfile}" alt="{alt}">',
            content, flags=re.IGNORECASE
        )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {fname}")
    else:
        print(f"No change: {fname}")

print("\nDone!")
