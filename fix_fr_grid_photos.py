import os, re

BASE = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website"

# Fix frozen label in French pages - Surgelés is actually correct Quebec French
# but client prefers Congelés. Update text in fr pages.
fr_files = []
for fname in os.listdir(os.path.join(BASE, "fr")):
    if fname.endswith('.html'):
        fr_files.append(os.path.join(BASE, "fr", fname))

# Photo replacements for French category grid
# These are the exact placeholder labels visible in the screenshot
replacements = [
    # Halal butcher counter
    ('PHOTO : COMPTOIR BOUCHERIE HALAL',    'meat-counter.jpg',    'Comptoir boucherie Halal'),
    ('Photo : comptoir boucherie Halal',    'meat-counter.jpg',    'Comptoir boucherie Halal'),
    # Marinated meat
    ('PHOTO : PLATEAUX DE KABAB',          'marinated-meat.jpg',  'Viande marinée'),
    ('Photo : plateaux de kabab',          'marinated-meat.jpg',  'Viande marinée'),
    # Frozen
    ('PHOTO : RAYON',                      'frozen.jpg',          'Rayon surgelés'),
    ('Photo : rayon surgel',               'frozen.jpg',          'Rayon surgelés'),
    # Bread
    ('PHOTO : PAIN FRAIS ET LAVASH',       'bread.jpg',           'Pain frais et lavash'),
    ('Photo : pain frais',                 'bread.jpg',           'Pain frais et lavash'),
    # Sweets
    ('PHOTO : SUCRERIES PERSANES',         'sweets.jpg',          'Sucreries persanes'),
    ('Photo : sucreries',                  'sweets.jpg',          'Sucreries persanes'),
]

for path in fr_files:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='latin-1') as f:
            content = f.read()

    original = content

    for label_fragment, imgfile, alt in replacements:
        # Match span with img class
        content = re.sub(
            r'<span class="img ph" data-label="[^"]*' + re.escape(label_fragment) + r'[^"]*"></span>',
            f'<img src="../assets/{imgfile}" alt="{alt}">',
            content, flags=re.IGNORECASE
        )
        # Match plain ph class
        content = re.sub(
            r'<span class="ph" data-label="[^"]*' + re.escape(label_fragment) + r'[^"]*"></span>',
            f'<img src="../assets/{imgfile}" alt="{alt}">',
            content, flags=re.IGNORECASE
        )
        # Match ph with style
        content = re.sub(
            r'<span class="ph" data-label="[^"]*' + re.escape(label_fragment) + r'[^"]*" style="[^"]*"></span>',
            f'<img src="../assets/{imgfile}" alt="{alt}" style="width:100%;height:100%;object-fit:cover">',
            content, flags=re.IGNORECASE
        )

    # Fix "Surgelés" label text to "Congelés" throughout French pages
    content = content.replace('Surgelés', 'Congelés')
    content = content.replace('surgelés', 'congelés')
    content = content.replace('Surgel\u00e9s', 'Congel\u00e9s')
    content = content.replace('surgel\u00e9s', 'congel\u00e9s')
    content = content.replace('Surgelé', 'Congelé')
    content = content.replace('surgelé', 'congelé')

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {os.path.basename(path)}")
    else:
        print(f"No change: {os.path.basename(path)}")

print("\nDone!")
