import re, os

folders = [
    "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website",
    "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/fr"
]

all_files = []
for folder in folders:
    for f in os.listdir(folder):
        if f.endswith('.html'):
            all_files.append(os.path.join(folder, f))

for path in all_files:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='latin-1') as f:
            content = f.read()
    original = content

    # Remove mi-fa spans entirely (Farsi menu item names)
    content = re.sub(r'<span class="mi-fa">.*?</span>', '', content)

    # Remove Bonjour · سلام · Welcome → Bonjour · Welcome
    content = re.sub(r'Bonjour\s*·\s*[\u0600-\u06FF]+\s*·\s*Welcome', 'Bonjour · Welcome', content)

    # Remove سلام · Bonjour · Welcome → Bonjour · Welcome
    content = re.sub(r'[\u0600-\u06FF\s·]+·\s*Bonjour\s*·\s*Welcome', 'Bonjour · Welcome', content)

    # Remove · فروشگاه شهران from copyright
    content = re.sub(r'\s*·\s*[\u0600-\u06FF\s]+شهران', '', content)

    # Remove Certified · حلال → Certified Halal
    content = re.sub(r'Certified\s*·\s*[\u0600-\u06FF]+', 'Certified Halal', content)

    # Remove Certifiée · حلال → Certifiée Halal
    content = re.sub(r'Certifi[eé]e\s*·\s*[\u0600-\u06FF]+', 'Certifi\u00e9e Halal', content)

    # Remove In-store kitchen · آشپزخانه → In-store kitchen
    content = re.sub(r'In-store kitchen\s*·\s*[\u0600-\u06FF]+', 'In-store kitchen', content)

    # Remove Cuisine sur place · آشپزخانه → Cuisine sur place
    content = re.sub(r'Cuisine sur place\s*·\s*[\u0600-\u06FF]+', 'Cuisine sur place', content)

    # Remove خوش آمدید kicker span entirely
    content = re.sub(r'<span class="kicker[^"]*">\s*[\u0600-\u06FF\s]+\s*</span>', '', content)

    # Remove Du gril — کباب → Du gril
    content = re.sub(r'Du gril\s*—\s*[\u0600-\u06FF]+', 'Du gril', content)

    # Remove From the Grill — کباب → From the Grill
    content = re.sub(r'From the Grill\s*—\s*[\u0600-\u06FF]+', 'From the Grill', content)

    # Remove Ragoûts & plats chauds — خورش → Ragoûts & plats chauds
    content = re.sub(r'(Rago\u00fbts[^<]*?)\s*—\s*[\u0600-\u06FF]+', r'\1', content)

    # Remove Stews & Warm Food — خورش
    content = re.sub(r'(Stews[^<]*?)\s*—\s*[\u0600-\u06FF]+', r'\1', content)

    # Remove any remaining Farsi/Arabic unicode characters
    content = re.sub(r'[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]+', '', content)

    # Clean up empty · · patterns left behind
    content = re.sub(r'\s*·\s*·', ' ·', content)
    content = re.sub(r'·\s*</span>', '</span>', content)
    content = re.sub(r'·\s*\n\s*</span>', '\n</span>', content)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned: {os.path.relpath(path)}")
    else:
        print(f"No change: {os.path.basename(path)}")

print("\nAll Farsi text removed!")
