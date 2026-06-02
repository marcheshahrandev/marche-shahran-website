import os

path = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/styles.css"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make nav links position relative
content = content.replace(
    '.nav-links a{font-family:var(--f-head);font-weight:500;font-size:.98rem;\n  padding:.55em .85em;border-radius:999px;color:var(--ink);transition:.18s}',
    '.nav-links a{font-family:var(--f-head);font-weight:500;font-size:.98rem;\n  padding:.55em .85em;border-radius:999px;color:var(--ink);transition:.18s;position:relative}'
)

# Fix active underline to use absolute positioning so it doesn't push text
content = content.replace(
    '.nav-links a.active::after{content:"";display:block;height:2px;background:var(--saffron);\n  margin:.25em .85em 0;border-radius:2px}',
    '.nav-links a.active::after{content:"";position:absolute;bottom:0;left:.85em;right:.85em;height:2px;background:var(--saffron);border-radius:2px}'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Nav jump fixed.")
