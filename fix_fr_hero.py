path = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/fr/index.html"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the wrongly injected meat counter image from inside the hero-inner
content = content.replace(
    '<img src="../assets/meat-counter.jpg" alt="Halal butcher counter" style="width:100%;height:100%;object-fit:cover">',
    ''
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
