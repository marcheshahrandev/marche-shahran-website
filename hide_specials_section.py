import os

BASE = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website"
folders = [BASE, os.path.join(BASE, "fr")]

for folder in folders:
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

        # Add hidden class to the specials teaser section on homepage (band-saffron)
        # This is the "This week's specials" / "Les spéciaux" section
        content = content.replace(
            '<section class="section band-saffron">',
            '<section class="section band-saffron specials-hidden">'
        )

        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {fname}")
        else:
            print(f"No change: {fname}")

# Add the hide rule to CSS
css_path = os.path.join(BASE, "styles.css")
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

hide_rule = "\n/* Weekly specials — hidden until activated */\n.specials-hidden { display: none; }\n"

if '.specials-hidden' not in css:
    css += hide_rule
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS hide rule added!")

print("\nDone! To re-enable, remove 'specials-hidden' class or change display:none to display:block in styles.css")
