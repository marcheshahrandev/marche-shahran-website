import os, re

BASE = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website"
FR = os.path.join(BASE, "fr")

all_folders = [BASE, FR]

for folder in all_folders:
    is_fr = folder.endswith("/fr")

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

        # ── PHONE ──
        content = content.replace('(514) 000-0000', '(514) 532-1485')

        # ── EMAIL ──
        content = content.replace('info@marcheshahran.ca', 'info@marcheshahran.com')
        content = content.replace('info@marcheshahran.com', 'info@marcheshahran.com')  # idempotent

        # ── INSTAGRAM link ──
        content = content.replace(
            '<a href="#" aria-label="Instagram">Instagram</a>',
            '<a href="https://www.instagram.com/marche_shahran/" target="_blank" rel="noopener" aria-label="Instagram">Instagram</a>'
        )
        content = content.replace(
            '<a href="#">Instagram</a>',
            '<a href="https://www.instagram.com/marche_shahran/" target="_blank" rel="noopener">Instagram</a>'
        )

        # ── HOURS in footer ──
        content = content.replace(
            'Open daily · 9am – 9pm',
            'Mon–Fri · 8am–8pm · Sat–Sun · 8am–7pm'
        )
        content = content.replace(
            'Ouvert quotidiennement · 9h – 21h',
            'Lun–Ven · 8h–20h · Sam–Dim · 8h–19h'
        )

        # ── TOPBAR hours ──
        content = content.replace(
            'Fresh produce daily · 9am–9pm',
            'Mon–Fri 8am–8pm · Sat–Sun 8am–7pm'
        )
        content = content.replace(
            'Produits frais quotidiens · 9h\u201321h',
            'Lun\u2013Ven 8h\u201320h · Sam\u2013Dim 8h\u201319h'
        )
        content = content.replace(
            'Produits frais quotidiens \u00b7 9h\u201321h',
            'Lun\u2013Ven 8h\u201320h \u00b7 Sam\u2013Dim 8h\u201319h'
        )

        # ── HOURS TABLE in contact pages ──
        if is_fr:
            old_hours_table = '''<table class="hours-table">
            <tr class="today"><td>Lundi</td><td>9:00 — 21:00</td></tr>
            <tr><td>Mardi</td><td>9:00 — 21:00</td></tr>
            <tr><td>Mercredi</td><td>9:00 — 21:00</td></tr>
            <tr><td>Jeudi</td><td>9:00 — 21:00</td></tr>
            <tr><td>Vendredi</td><td>9:00 — 21:00</td></tr>
            <tr><td>Samedi</td><td>9:00 — 21:00</td></tr>
            <tr><td>Dimanche</td><td>9:00 — 21:00</td></tr>
          </table>'''
            new_hours_table = '''<table class="hours-table">
            <tr><td>Lundi</td><td>8:00 — 20:00</td></tr>
            <tr><td>Mardi</td><td>8:00 — 20:00</td></tr>
            <tr><td>Mercredi</td><td>8:00 — 20:00</td></tr>
            <tr><td>Jeudi</td><td>8:00 — 20:00</td></tr>
            <tr><td>Vendredi</td><td>8:00 — 20:00</td></tr>
            <tr><td>Samedi</td><td>8:00 — 19:00</td></tr>
            <tr><td>Dimanche</td><td>8:00 — 19:00</td></tr>
          </table>'''
        else:
            old_hours_table = '''<table class="hours-table">
            <tr class="today"><td>Monday</td><td>9:00 — 21:00</td></tr>
            <tr><td>Tuesday</td><td>9:00 — 21:00</td></tr>
            <tr><td>Wednesday</td><td>9:00 — 21:00</td></tr>
            <tr><td>Thursday</td><td>9:00 — 21:00</td></tr>
            <tr><td>Friday</td><td>9:00 — 21:00</td></tr>
            <tr><td>Saturday</td><td>9:00 — 21:00</td></tr>
            <tr><td>Sunday</td><td>9:00 — 21:00</td></tr>
          </table>'''
            new_hours_table = '''<table class="hours-table">
            <tr><td>Monday</td><td>8:00 — 20:00</td></tr>
            <tr><td>Tuesday</td><td>8:00 — 20:00</td></tr>
            <tr><td>Wednesday</td><td>8:00 — 20:00</td></tr>
            <tr><td>Thursday</td><td>8:00 — 20:00</td></tr>
            <tr><td>Friday</td><td>8:00 — 20:00</td></tr>
            <tr><td>Saturday</td><td>8:00 — 19:00</td></tr>
            <tr><td>Sunday</td><td>8:00 — 19:00</td></tr>
          </table>'''

        content = content.replace(old_hours_table, new_hours_table)

        # ── GOOGLE MAP embed ──
        google_map = '''<iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2796.0!2d-73.6414!3d45.4734!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cc91a8f6c1b1b1b%3A0x1234567890abcdef!2s6010+Sherbrooke+St+W%2C+Montr%C3%A9al%2C+QC+H4A+1X9!5e0!3m2!1sen!2sca!4v1"
            width="100%" height="380" style="border:0;border-radius:16px;display:block" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
          </iframe>'''

        # Replace EN map placeholder
        content = content.replace(
            '<div class="map-ph ph" data-label="Embed: Google Map of 6010 Sherbrooke St W (drop a Map block here in Squarespace)"></div>',
            google_map
        )
        # Replace FR map placeholder
        content = content.replace(
            '<div class="map-ph ph" data-label="Int\u00e9gration : Google Maps 6010 Sherbrooke St W"></div>',
            google_map
        )
        content = content.replace(
            '<div class="map-ph ph" data-label="Intégration : Google Maps 6010 Sherbrooke St W"></div>',
            google_map
        )

        # ── PLACEHOLDER notes cleanup ──
        content = content.replace('Placeholder — swap in real number', 'Appeler le magasin' if is_fr else 'Call the store')
        content = content.replace('Placeholder address', 'Courriel' if is_fr else 'Email')
        content = content.replace('Phone — placeholder, swap in real number', '(514) 532-1485')
        content = content.replace('Num\u00e9ro \u00e0 remplacer', 'Appeler le magasin')
        content = content.replace('Adresse temporaire', 'Courriel')

        # ── OPEN HOURS info card on homepage ──
        content = content.replace(
            '<p class="big">Mon\u2013Sun \u00b7 9am \u2013 9pm</p>',
            '<p class="big">Mon\u2013Fri \u00b7 8am\u20138pm</p>'
        )
        content = content.replace(
            '<p class="big">Mon–Sun · 9am – 9pm</p>',
            '<p class="big">Mon–Fri · 8am–8pm</p>'
        )
        content = content.replace(
            '<p class="big">Lun\u2013Dim \u00b7 9h \u2013 21h</p>',
            '<p class="big">Lun\u2013Ven \u00b7 8h\u201320h</p>'
        )

        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {fname}")
        else:
            print(f"No change: {fname}")

print("\nAll done!")
