import os

BASE = "/Volumes/Untitled/Work/Nasser Ajabi - Shahran Marche/website/Marche Shahran Website/fr"

def topbar(custom=""):
    if not custom:
        custom = '<span><strong>Ouvert \u00e0 NDG</strong> \u00b7 6010 Sherbrooke St W</span><span class="dot"></span><span>Viande 100% Halal</span><span class="dot hide-sm"></span><span class="hide-sm">Produits frais quotidiens \u00b7 9h\u201321h</span>'
    return f'<div class="topbar"><div class="wrap">{custom}</div></div>'

def nav(active):
    pages = [
        ("../index.html",   "Accueil",      "index"),
        ("produits.html",   "Produits",     "produits"),
        ("speciaux.html",   "Sp\u00e9ciaux",    "speciaux"),
        ("restaurant.html", "Restaurant",   "restaurant"),
        ("a-propos.html",   "\u00c0 propos",    "a-propos"),
        ("contact.html",    "Contact",      "contact"),
    ]
    items = ""
    for href, label, slug in pages:
        cls = ' class="active"' if slug == active else ""
        items += f'      <li><a href="{href}"{cls}>{label}</a></li>\n'
    return f'''<header class="site-head">
  <div class="wrap nav">
    <a class="brand" href="../index.html" aria-label="March\u00e9 Shahran accueil">
      <img src="../assets/logo.png" alt="March\u00e9 Shahran logo">
      <span class="brand-text"><span class="bt">March\u00e9 Shahran</span><span class="bs">\u00c9picerie persane \u00b7 NDG</span></span>
    </a>
    <button class="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <ul class="nav-links" id="nav">
{items}      <li class="nav-cta"><a class="btn btn-primary" href="../index.html">EN</a></li>
    </ul>
  </div>
</header>
<div class="nav-backdrop" id="backdrop"></div>'''

def footer():
    return '''<footer class="site-foot">
  <div class="wrap foot-top">
    <div class="foot-brand">
      <img src="../assets/logo.png" alt="March\u00e9 Shahran">
      <p>\u00c9picerie persane &amp; march\u00e9 Halal \u00e0 Notre-Dame-de-Gr\u00e2ce. Produits frais, kabab chaud et saveurs du foyer.</p>
    </div>
    <div><h4>Nous visiter</h4><ul class="foot-links"><li>6010 Sherbrooke St W</li><li>Montr\u00e9al, QC \u00b7 H4A 1X9</li><li><a href="contact.html">Itin\u00e9raire \u2192</a></li></ul></div>
    <div><h4>Explorer</h4><ul class="foot-links"><li><a href="produits.html">Produits</a></li><li><a href="speciaux.html">Sp\u00e9ciaux</a></li><li><a href="restaurant.html">Restaurant</a></li><li><a href="a-propos.html">\u00c0 propos</a></li></ul></div>
    <div><h4>Heures &amp; Contact</h4><ul class="foot-links"><li>Ouvert quotidiennement \u00b7 9h \u2013 21h</li><li>(514) 000-0000</li><li>info@marcheshahran.ca</li><li><a href="#">Instagram</a> \u00b7 <a href="#">Facebook</a></li></ul></div>
  </div>
  <div class="wrap foot-bottom">
    <span>\u00a9 2026 March\u00e9 Shahran \u00b7 \u0641\u0631\u0648\u0634\u06af\u0627\u0647 \u0634\u0647\u0631\u0627\u0646</span>
    <span class="foot-flags">
      <span style="background:linear-gradient(180deg,#239f40 33%,#fff 33% 66%,#da0000 66%)" title="Iran"></span>
      <span style="background:linear-gradient(90deg,#ff0000 25%,#fff 25% 75%,#ff0000 75%)" title="Canada"></span>
      <span style="background:#003da5" title="Qu\u00e9bec"></span>
    </span>
  </div>
</footer>
<script src="../site.js"></script>'''

def page(title, meta, active, topbar_html, body):
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="stylesheet" href="../styles.css">
<script>document.documentElement.className='js';</script>
</head>
<body>
{topbar_html}
{nav(active)}
{body}
{footer()}
</body>
</html>'''

index_body = '''<section class="hero">
  <div class="hero-media"><img src="../assets/storefront.webp" alt="Devanture du March\u00e9 Shahran sur Sherbrooke Ouest"></div>
  <div class="hero-scrim"></div>
  <div class="wrap">
    <div class="hero-inner reveal">
      <span class="kicker is-light">\u00c9picerie persane \u00b7 March\u00e9 Halal \u00b7 NDG</span>
      <h1 class="h-xl">Un go\u00fbt du foyer,<br>sur Sherbrooke Ouest.</h1>
      <p class="lead">Produits frais, viande &amp; volaille 100% Halal, comptoir ouvert d\u2019olives et fromages, produits d\u2019\u00e9picerie du pays \u2014 et une cuisine kabab chaleureuse au fond du magasin. Votre \u00e9picerie persane de quartier \u00e0 Notre-Dame-de-Gr\u00e2ce.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="produits.html">Explorer le magasin <span class="arr">\u2192</span></a>
        <a class="btn btn-red" href="restaurant.html">Voir le menu kabab</a>
      </div>
      <div class="hero-tags">
        <span class="tag">Boucherie Halal</span>
        <span class="tag">Comptoir olives &amp; fromages</span>
        <span class="tag">Produits frais</span>
        <span class="tag">Kabab grill\u00e9</span>
      </div>
    </div>
  </div>
</section>

<section class="band band-cream">
  <div class="wrap section" style="padding-block:clamp(32px,4vw,48px)">
    <div class="info-row">
      <div class="info-card reveal">
        <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg></div>
        <h3>Nous trouver</h3><p class="big">6010 Sherbrooke St W</p><p>Montr\u00e9al, QC \u00b7 H4A 1X9 (NDG)</p>
      </div>
      <div class="info-card reveal">
        <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div>
        <h3>Ouvert chaque jour</h3><p class="big">Lun\u2013Dim \u00b7 9h \u2013 21h</p><p>Livraisons fra\u00eeches chaque matin</p>
      </div>
      <div class="info-card reveal">
        <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg></div>
        <h3>T\u00e9l\u00e9phoner</h3><p class="big">(514) 000-0000</p><p>Num\u00e9ro \u00e0 remplacer</p>
      </div>
      <div class="info-card reveal">
        <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg></div>
        <h3>Toujours Halal</h3><p class="big">Viande 100% Halal</p><p>Certifi\u00e9e \u00b7 \u062d\u0644\u0627\u0644</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center reveal" style="max-width:640px;margin-inline:auto;margin-bottom:2.6rem">
      <span class="kicker center-line">Ce que nous offrons</span>
      <h2 class="h-lg" style="margin-top:.6rem">Tout pour une table persane</h2>
      <p class="lead" style="margin:.8rem auto 0">Du mur de produits frais au comptoir d\u2019olives, nos 6\u202f000 pi\u00b2 regorgent des produits et sp\u00e9cialit\u00e9s de votre enfance.</p>
    </div>
    <div class="cat-grid">
      <a class="cat reveal" href="produits.html#produce">
        <img src="../assets/produce.webp" alt="Mur de produits frais">
        <span class="pin"><span class="halal-badge" style="background:var(--saffron);color:var(--ink)">Frais quotidien</span></span>
        <span class="lbl"><h3>Fruits &amp; L\u00e9gumes</h3><p>Frais, r\u00e9approvisionn\u00e9 chaque matin</p></span>
      </a>
      <a class="cat reveal" href="produits.html#meat">
        <span class="img ph" data-label="Photo : comptoir boucherie Halal"></span>
        <span class="pin"><span class="halal-badge">\u2713 Halal</span></span>
        <span class="lbl"><h3>Viande &amp; Volaille Halal</h3><p>B\u0153uf, agneau &amp; volaille frais</p></span>
      </a>
      <a class="cat reveal" href="produits.html#marinated">
        <span class="img ph" data-label="Photo : plateaux de kabab marin\u00e9"></span>
        <span class="pin"><span class="halal-badge">\u2713 Halal</span></span>
        <span class="lbl"><h3>Viande marin\u00e9e</h3><p>Kabab &amp; joojeh pr\u00eats \u00e0 griller</p></span>
      </a>
      <a class="cat reveal" href="produits.html#counter">
        <img src="../assets/olive-counter.webp" alt="Comptoir ouvert olives et fromages">
        <span class="lbl"><h3>Olives, Fromages &amp; Noix</h3><p>Comptoir ouvert \u2014 servi \u00e0 la main</p></span>
      </a>
      <a class="cat reveal" href="produits.html#pantry">
        <img src="../assets/bulk-aisle.webp" alt="Rayon riz l\u00e9gumineuses et \u00e9picerie">
        <span class="lbl"><h3>Riz, L\u00e9gumineuses &amp; \u00c9picerie</h3><p>Basmati, l\u00e9gumineuses, \u00e9pices &amp; plus</p></span>
      </a>
      <a class="cat reveal" href="produits.html#frozen">
        <span class="img ph" data-label="Photo : rayon surgel\u00e9s"></span>
        <span class="lbl"><h3>Surgel\u00e9s</h3><p>Herbes, pains, sabzi &amp; plats cuisin\u00e9s</p></span>
      </a>
      <a class="cat reveal" href="produits.html#bakery">
        <span class="img ph" data-label="Photo : pain frais et lavash"></span>
        <span class="lbl"><h3>Pain &amp; Boulangerie</h3><p>Barbari, lavash &amp; sangak</p></span>
      </a>
      <a class="cat reveal" href="produits.html#sweets">
        <span class="img ph" data-label="Photo : sucreries persanes"></span>
        <span class="lbl"><h3>Sucreries &amp; P\u00e2tisseries</h3><p>Baklava, sohan &amp; douceurs du th\u00e9</p></span>
      </a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap section">
    <div class="split">
      <div class="split-media reveal"><span class="ph" data-label="Photo : boucher Halal au comptoir"></span></div>
      <div class="split-body reveal">
        <span class="kicker is-light">Notre promesse</span>
        <h2 class="h-lg" style="margin:.6rem 0 1rem">100% Halal \u2014 chaque coupe, chaque jour</h2>
        <p class="lead">Toute notre viande et volaille est certifi\u00e9e Halal, coup\u00e9e fra\u00eeche en magasin par nos bouchers. Dites-nous comment vous la voulez \u2014 enti\u00e8re, en morceaux, hach\u00e9e ou marin\u00e9e pour le gril.</p>
        <ul class="ticks" style="margin-top:1.4rem">
          <li>B\u0153uf, agneau &amp; poulet frais \u2014 jamais pr\u00e9-congel\u00e9 en rayon</li>
          <li>Kabab, joojeh &amp; barg marin\u00e9s maison, pr\u00eats \u00e0 cuire</li>
          <li>Coupes personnalis\u00e9es et commandes en gros pour vos r\u00e9ceptions</li>
        </ul>
        <a class="btn btn-light" href="produits.html#meat" style="margin-top:1.8rem">Voir la boucherie <span class="arr">\u2192</span></a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split flip">
      <div class="split-media reveal"><img src="../assets/olive-counter.webp" alt="Comptoir ouvert olives et fromages"></div>
      <div class="split-body reveal">
        <span class="kicker">Servi \u00e0 la main</span>
        <h2 class="h-lg" style="margin:.6rem 0 1rem">Le comptoir d\u2019olives &amp; fromages</h2>
        <p class="lead">Plus d\u2019une douzaine d\u2019olives, cornichons et fromages feta, servis frais \u00e0 la commande. Go\u00fbtez avant d\u2019acheter et repartez avec exactement ce qu\u2019il vous faut.</p>
        <ul class="ticks" style="margin-top:1.4rem">
          <li>Kalamata, olives vertes libanaises, noires marocaines &amp; plus</li>
          <li>Fromages feta bulgares, iraniens &amp; grecs</li>
          <li>Noix fra\u00eeches et grill\u00e9es, fruits secs &amp; m\u00e9langes</li>
        </ul>
        <a class="btn btn-ghost" href="produits.html#counter" style="margin-top:1.8rem">Voir le comptoir <span class="arr">\u2192</span></a>
      </div>
    </div>
  </div>
</section>

<section class="hero" style="background:var(--red-deep)">
  <div class="hero-media"><span class="ph" data-label="Photo : koobideh et joojeh kabab grill\u00e9s" style="width:100%;height:100%"></span></div>
  <div class="hero-scrim"></div>
  <div class="wrap">
    <div class="hero-inner reveal" style="max-width:620px">
      <span class="kicker is-light">Cuisine sur place</span>
      <h2 class="h-xl" style="color:#fff;margin:.5rem 0 .3rem">Plats chauds &amp;<br>kabab grill\u00e9</h2>
      <p class="lead" style="color:rgba(255,255,255,.88)">Au fond du march\u00e9, nos cuisiniers allument le mangal chaque jour pour du koobideh et joojeh kabab grill\u00e9s au charbon, des rago\u00fbts persans mijot\u00e9s et des plats r\u00e9confortants \u2014 sur place ou \u00e0 emporter.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="restaurant.html">Voir le menu <span class="arr">\u2192</span></a>
      </div>
    </div>
  </div>
</section>

<section class="section band-saffron">
  <div class="wrap">
    <div class="split">
      <div class="split-body reveal">
        <span class="kicker">\u00c9conomisez en magasin</span>
        <h2 class="h-lg" style="margin:.6rem 0 1rem">Les sp\u00e9ciaux de la semaine</h2>
        <p class="lead">Nouvelles promotions chaque semaine sur les produits frais, la viande Halal et vos essentiels d\u2019\u00e9picerie. Mis \u00e0 jour en magasin et ici sur le site \u2014 sans abonnement, sans application.</p>
        <a class="btn btn-red" href="speciaux.html" style="margin-top:1.6rem">Voir le circulaire <span class="arr">\u2192</span></a>
      </div>
      <div class="reveal" style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
        <div class="deal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">SP\u00c9CIAL</span></div>
          <div class="d-body"><h3>Riz Basmati 10 kg</h3><p class="d-sub">Vieilli premium</p>
          <div class="d-price"><span class="price"><span class="cur">$</span>18<span class="unit">/sac</span></span><span class="was">$24.99</span></div></div></div>
        <div class="deal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">SP\u00c9CIAL</span></div>
          <div class="d-body"><h3>\u00c9paule d\u2019agneau fra\u00eeche</h3><p class="d-sub">Halal \u00b7 coup\u00e9 sur commande</p>
          <div class="d-price"><span class="price"><span class="cur">$</span>9<span class="unit">/lb</span></span><span class="was">$12.99</span></div></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split-media reveal"><img src="../assets/storefront-snow.webp" alt="Devanture du March\u00e9 Shahran en hiver"></div>
      <div class="split-body reveal">
        <span class="kicker">Bonjour \u00b7 \u0633\u0644\u0627\u0645 \u00b7 Welcome</span>
        <h2 class="h-lg" style="margin:.6rem 0 1rem">Votre \u00e9picerie persane de quartier</h2>
        <p class="lead">March\u00e9 Shahran apporte les saveurs de l\u2019Iran au c\u0153ur de NDG. G\u00e9r\u00e9 en famille et fi\u00e8rement montr\u00e9alais, nous proposons les ingr\u00e9dients, sucreries et sp\u00e9cialit\u00e9s qui donnent \u00e0 une cuisine persane toute sa chaleur.</p>
        <a class="btn btn-ghost" href="a-propos.html" style="margin-top:1.6rem">Notre histoire <span class="arr">\u2192</span></a>
      </div>
    </div>
  </div>
</section>'''

about_body = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Accueil</a> / \u00c0 propos</p>
    <span class="kicker is-light" style="margin-top:.8rem">\u0633\u0644\u0627\u0645 \u00b7 Bonjour \u00b7 Welcome</span>
    <h1 class="h-xl">Notre histoire</h1>
    <p class="lead">Un march\u00e9 persan de quartier, fi\u00e8rement montr\u00e9alais \u2014 o\u00f9 les saveurs de l\u2019Iran se retrouvent au coin de Sherbrooke et du foyer.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split-media reveal"><img src="../assets/storefront-snow.webp" alt="Devanture du March\u00e9 Shahran en hiver"></div>
      <div class="split-body reveal">
        <span class="kicker">Depuis notre grande ouverture</span>
        <h2 class="h-lg" style="margin:.6rem 0 1rem">Un go\u00fbt du foyer \u00e0 NDG</h2>
        <p class="lead" style="margin-bottom:1rem">March\u00e9 Shahran a ouvert ses portes au 6010 Sherbrooke Ouest pour apporter l\u2019exp\u00e9rience de l\u2019\u00e9picerie iranienne \u00e0 Notre-Dame-de-Gr\u00e2ce \u2014 les rayons, les ar\u00f4mes et l\u2019accueil chaleureux dont vous vous souvenez.</p>
        <p style="color:var(--ink-soft)">\u00c0 environ 6\u202f000 pieds carr\u00e9s, nous sommes plus petits que les grandes surfaces \u2014 et c\u2019est voulu. Tout est \u00e0 port\u00e9e de main, l\u2019\u00e9quipe conna\u00eet les produits, et il y a toujours quelqu\u2019un au comptoir pour vous aider. Que vous ayez grandi avec cette cuisine ou que vous la d\u00e9couvriez pour la premi\u00e8re fois, vous avez votre place ici.</p>
      </div>
    </div>
  </div>
</section>

<section class="section band-cream">
  <div class="wrap">
    <div class="center reveal" style="max-width:620px;margin-inline:auto;margin-bottom:2.6rem">
      <span class="kicker center-line">Ce en quoi nous croyons</span>
      <h2 class="h-lg" style="margin-top:.6rem">Petit magasin, grand soin</h2>
    </div>
    <div class="info-row">
      <div class="info-card reveal"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg></div><h3>Toujours Halal</h3><p>Chaque coupe de viande et volaille est certifi\u00e9e Halal et pr\u00e9par\u00e9e en magasin par nos bouchers.</p></div>
      <div class="info-card reveal"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M5 8c0-2 3-3 7-3s7 1 7 3"/><path d="M5 8c0 6 3 9 7 9s7-3 7-9"/></svg></div><h3>La fra\u00eecheur d\u2019abord</h3><p>Produits, herbes et pains r\u00e9approvisionn\u00e9s chaque jour, et un comptoir ouvert \u00e0 go\u00fbter avant d\u2019acheter.</p></div>
      <div class="info-card reveal"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/></svg></div><h3>Commerce familial</h3><p>Ind\u00e9pendant et local \u2014 de vraies personnes qui se souviennent de votre nom et de vos habitudes.</p></div>
      <div class="info-card reveal"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V7l8-4 8 4v14M9 9h.01M9 13h.01M9 17h.01M15 9h.01M15 13h.01M15 17h.01"/></svg></div><h3>Ancr\u00e9 dans la communaut\u00e9</h3><p>Iranien de c\u0153ur, montr\u00e9alais d\u2019esprit \u2014 un march\u00e9 qui appartient au quartier.</p></div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap center" style="max-width:760px">
    <span class="kicker is-light center-line">\u062e\u0648\u0634 \u0622\u0645\u062f\u06cc\u062f</span>
    <h2 class="h-lg" style="margin:1rem 0;color:#fff">\u00ab\u00a0Un march\u00e9 devrait ressembler \u00e0 la cuisine de quelqu\u2019un \u2014 g\u00e9n\u00e9reux, frais et plein d\u2019histoires.\u00a0\u00bb</h2>
    <p class="lead">Du safran dans le rayon des \u00e9pices au kabab sur le gril, chaque recoin du March\u00e9 Shahran est l\u00e0 pour que votre table ressemble un peu plus \u00e0 la maison.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split flip">
      <div class="split-media reveal"><img src="../assets/olive-counter.webp" alt="Comptoir ouvert d\u2019olives"></div>
      <div class="split-body reveal">
        <span class="kicker">Venez nous dire bonjour</span>
        <h2 class="h-lg" style="margin:.6rem 0 1rem">Trouvez-nous sur Sherbrooke Ouest</h2>
        <p class="lead">Cherchez l\u2019auvent rouge au 6010 Sherbrooke Ouest, au c\u0153ur de NDG. Nous sommes ouverts tous les jours \u2014 entrez, go\u00fbtez quelque chose de nouveau, et laissez-nous vous aider \u00e0 trouver un bout de chez vous.</p>
        <div style="display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.6rem">
          <a class="btn btn-primary" href="contact.html">Itin\u00e9raire <span class="arr">\u2192</span></a>
          <a class="btn btn-ghost" href="produits.html">Voir les produits</a>
        </div>
      </div>
    </div>
  </div>
</section>'''

contact_body = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Accueil</a> / Contact</p>
    <span class="kicker is-light" style="margin-top:.8rem">Venez nous rendre visite</span>
    <h1 class="h-xl">Nous trouver &amp; dire bonjour</h1>
    <p class="lead">Au c\u0153ur de NDG, sous l\u2019auvent rouge sur Sherbrooke Ouest. Ouvert tous les jours \u2014 passez, appelez \u00e0 l\u2019avance ou planifiez votre visite ci-dessous.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="contact-grid">
      <div class="reveal">
        <span class="kicker">Informations du magasin</span>
        <h2 class="h-lg" style="margin:.6rem 0 1.6rem">March\u00e9 Shahran</h2>
        <div class="info-card" style="margin-bottom:1rem">
          <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg></div>
          <h3>Adresse</h3><p class="big">6010 Sherbrooke St W</p><p>Montr\u00e9al, Qu\u00e9bec \u00b7 H4A 1X9 (NDG)</p>
          <a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&query=6010+Sherbrooke+St+W+Montreal+H4A+1X9" target="_blank" rel="noopener" style="margin-top:1rem;padding:.55em 1.1em;font-size:.9rem">Ouvrir dans Google Maps <span class="arr">\u2192</span></a>
        </div>
        <div class="info-row" style="grid-template-columns:1fr 1fr">
          <div class="info-card"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg></div><h3>T\u00e9l\u00e9phone</h3><p class="big">(514) 000-0000</p><p>Num\u00e9ro \u00e0 remplacer</p></div>
          <div class="info-card"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></div><h3>Courriel</h3><p class="big">info@marcheshahran.ca</p><p>Adresse temporaire</p></div>
        </div>
        <div class="info-card" style="margin-top:1rem">
          <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div>
          <h3>Comment nous rejoindre</h3>
          <p>Lignes de bus 105 &amp; 24 sur Sherbrooke Ouest \u00b7 M\u00e9tros Vend\u00f4me &amp; Villa-Maria \u00e0 proximit\u00e9 \u00b7 Stationnement dans la rue disponible.</p>
        </div>
        <div style="display:flex;gap:.8rem;margin-top:1.4rem">
          <a class="btn btn-primary" href="#" aria-label="Instagram">Instagram</a>
          <a class="btn btn-ghost" href="#" aria-label="Facebook">Facebook</a>
        </div>
      </div>
      <div class="reveal">
        <div class="info-card" style="margin-bottom:1.4rem">
          <span class="kicker">Heures d\u2019ouverture</span>
          <h3 class="h-md" style="margin:.5rem 0 .4rem">Ouvert 7 jours sur 7</h3>
          <table class="hours-table">
            <tr class="today"><td>Lundi</td><td>9:00 \u2014 21:00</td></tr>
            <tr><td>Mardi</td><td>9:00 \u2014 21:00</td></tr>
            <tr><td>Mercredi</td><td>9:00 \u2014 21:00</td></tr>
            <tr><td>Jeudi</td><td>9:00 \u2014 21:00</td></tr>
            <tr><td>Vendredi</td><td>9:00 \u2014 21:00</td></tr>
            <tr><td>Samedi</td><td>9:00 \u2014 21:00</td></tr>
            <tr><td>Dimanche</td><td>9:00 \u2014 21:00</td></tr>
          </table>
          <p style="margin-top:1rem;font-family:var(--f-mono);font-size:.76rem;color:var(--ink-soft)">Cuisine \u00b7 11:00 \u2014 20:00 quotidiennement \u00b7 Heures \u00e0 confirmer</p>
        </div>
        <div class="map-ph ph" data-label="Int\u00e9gration : Google Maps 6010 Sherbrooke St W"></div>
      </div>
    </div>
  </div>
</section>
<section class="section band-cream" style="padding-block:0">
  <div style="position:relative;overflow:hidden;max-height:420px">
    <img src="../assets/storefront.webp" alt="Devanture March\u00e9 Shahran" style="width:100%;height:420px;object-fit:cover">
  </div>
</section>
<section class="section center">
  <div class="wrap" style="max-width:620px">
    <span class="kicker center-line">On a h\u00e2te de vous rencontrer</span>
    <h2 class="h-lg" style="margin:.6rem 0 1rem">\u00c0 bient\u00f4t sous l\u2019auvent rouge</h2>
    <p class="lead" style="margin-inline:auto">Le March\u00e9 Shahran, c\u2019est en magasin \u2014 la meilleure fa\u00e7on de le d\u00e9couvrir, c\u2019est d\u2019entrer. Venez avec votre app\u00e9tit et votre liste d\u2019\u00e9picerie.</p>
    <div style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;margin-top:1.8rem">
      <a class="btn btn-primary" href="produits.html">Voir les produits <span class="arr">\u2192</span></a>
      <a class="btn btn-red" href="restaurant.html">Voir le menu kabab</a>
    </div>
  </div>
</section>'''

restaurant_topbar = '<span><strong>Ouvert \u00e0 NDG</strong> \u00b7 6010 Sherbrooke St W</span><span class="dot"></span><span>Kabab grill\u00e9 frais \u00b7 sur place ou \u00e0 emporter</span><span class="dot hide-sm"></span><span class="hide-sm">Cuisine ouverte quotidiennement \u00b7 11h\u201320h</span>'

restaurant_body = '''<section class="hero" style="background:var(--red-deep)">
  <div class="hero-media"><span class="ph" data-label="Photo : koobideh et joojeh grill\u00e9s sur le mangal" style="width:100%;height:100%"></span></div>
  <div class="hero-scrim" style="background:linear-gradient(100deg,rgba(60,16,12,.94) 0%,rgba(60,16,12,.8) 40%,rgba(60,16,12,.4) 75%,rgba(60,16,12,.25) 100%)"></div>
  <div class="wrap">
    <div class="hero-inner reveal">
      <span class="kicker is-light">Cuisine sur place \u00b7 \u0622\u0634\u067e\u0632\u062e\u0627\u0646\u0647</span>
      <h1 class="h-xl" style="color:#fff">Tout juste sorti du gril.</h1>
      <p class="lead" style="color:rgba(255,255,255,.88)">Au fond du march\u00e9, nos cuisiniers allument le mangal chaque jour pour du koobideh et joojeh kabab grill\u00e9s au charbon, des rago\u00fbts persans mijot\u00e9s et des plats r\u00e9confortants. Mangez sur place \u00e0 quelques tables confortables, ou repartez avec vos emplettes.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="#menu">Voir le menu <span class="arr">\u2192</span></a>
        <a class="btn btn-red" href="contact.html" style="background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.4)">Nous trouver</a>
      </div>
    </div>
  </div>
</section>
<section class="band band-cream">
  <div class="wrap section" style="padding-block:clamp(32px,4vw,48px)">
    <div class="info-row">
      <div class="info-card reveal"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div><h3>Heures de cuisine</h3><p class="big">Quotidien \u00b7 11h \u2013 20h</p><p>Gril allum\u00e9 frais \u00e0 la commande</p></div>
      <div class="info-card reveal"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11h18M5 11V7a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v4M5 11v8M19 11v8"/></svg></div><h3>Sur place ou \u00e0 emporter</h3><p class="big">Quelques tables en magasin</p><p>Chaud, emball\u00e9 &amp; pr\u00eat \u00e0 partir</p></div>
      <div class="info-card reveal"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg></div><h3>100% Halal</h3><p class="big">M\u00eame boucher, m\u00eame gril</p><p>Toute viande coup\u00e9e en magasin</p></div>
      <div class="info-card reveal"><div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg></div><h3>Appelez \u00e0 l\u2019avance</h3><p class="big">(514) 000-0000</p><p>Num\u00e9ro \u00e0 remplacer</p></div>
    </div>
  </div>
</section>
<section class="section" id="menu">
  <div class="wrap">
    <div class="center reveal" style="max-width:620px;margin-inline:auto;margin-bottom:2.8rem">
      <span class="kicker center-line">Le menu</span>
      <h2 class="h-lg" style="margin-top:.6rem">Kabab &amp; plats chauds</h2>
      <p class="lead" style="margin:.8rem auto 0">Servi avec du riz basmati au safran ou du pain frais, tomate et oignon grill\u00e9s. Les prix sont des exemples \u00e0 remplacer par vos tarifs r\u00e9els.</p>
    </div>
    <div style="display:grid;gap:clamp(34px,5vw,56px);grid-template-columns:1fr;max-width:780px;margin-inline:auto">
      <div class="reveal">
        <h3 class="h-md" style="color:var(--red);margin-bottom:1.4rem">Du gril \u2014 \u06a9\u0628\u0627\u0628</h3>
        <div class="menu-list">
          <div class="menu-item"><span class="mi-name">Koobideh Kabab <span class="mi-fa">\u06a9\u0648\u0628\u06cc\u062f\u0647</span></span><span class="mi-price">14,99\u00a0$</span><span class="mi-desc">Deux brochettes de b\u0153uf hach\u00e9 assaisonn\u00e9, grill\u00e9 au charbon, avec riz au safran.</span></div>
          <div class="menu-item"><span class="mi-name">Joojeh Kabab <span class="mi-fa">\u062c\u0648\u062c\u0647</span></span><span class="mi-price">15,99\u00a0$</span><span class="mi-desc">Brochettes de poulet marin\u00e9 au safran, grill\u00e9es tendres et juteuses.</span></div>
          <div class="menu-item"><span class="mi-name">Barg Kabab <span class="mi-fa">\u0628\u0631\u06af</span></span><span class="mi-price">18,99\u00a0$</span><span class="mi-desc">Filet de b\u0153uf marin\u00e9 finement tranch\u00e9, grill\u00e9 et servi sur riz.</span></div>
          <div class="menu-item"><span class="mi-name">Soltani <span class="mi-fa">\u0633\u0644\u0637\u0627\u0646\u06cc</span></span><span class="mi-price">21,99\u00a0$</span><span class="mi-desc">Un koobideh et un barg \u2014 la combinaison royale.</span></div>
          <div class="menu-item"><span class="mi-name">C\u00f4telettes d\u2019agneau <span class="mi-fa">\u0634\u06cc\u0634\u0644\u06cc\u06a9</span></span><span class="mi-price">22,99\u00a0$</span><span class="mi-desc">C\u00f4telettes d\u2019agneau marin\u00e9es grill\u00e9es au charbon.</span></div>
          <div class="menu-item"><span class="mi-name">Plateau mixte grill\u00e9</span><span class="mi-price">26,99\u00a0$</span><span class="mi-desc">Koobideh, joojeh et barg \u00e0 partager, avec riz et l\u00e9gumes grill\u00e9s.</span></div>
        </div>
      </div>
      <div class="reveal">
        <h3 class="h-md" style="color:var(--red);margin-bottom:1.4rem">Rago\u00fbts &amp; plats chauds \u2014 \u062e\u0648\u0631\u0634</h3>
        <div class="menu-list">
          <div class="menu-item"><span class="mi-name">Ghormeh Sabzi <span class="mi-fa">\u0642\u0648\u0631\u0645\u0647\u200c\u0633\u0628\u0632\u06cc</span></span><span class="mi-price">13,99\u00a0$</span><span class="mi-desc">Rago\u00fbt d\u2019herbes avec b\u0153uf, haricots rouges et citron s\u00e9ch\u00e9, sur riz.</span></div>
          <div class="menu-item"><span class="mi-name">Gheymeh <span class="mi-fa">\u0642\u06cc\u0645\u0647</span></span><span class="mi-price">13,99\u00a0$</span><span class="mi-desc">Rago\u00fbt de pois cass\u00e9s et b\u0153uf garni de frites croustillantes.</span></div>
          <div class="menu-item"><span class="mi-name">Fesenjan <span class="mi-fa">\u0641\u0633\u0646\u062c\u0627\u0646</span></span><span class="mi-price">15,99\u00a0$</span><span class="mi-desc">Rago\u00fbt de noix et grenade avec poulet \u2014 sucr\u00e9 et acidul\u00e9.</span></div>
          <div class="menu-item"><span class="mi-name">Plat du jour <span class="mi-fa">\u063a\u0630\u0627\u06cc \u0631\u0648\u0632</span></span><span class="mi-price">Demandez</span><span class="mi-desc">Un plat maison en rotation \u2014 demandez \u00e0 la cuisine ce qui mijote aujourd\u2019hui.</span></div>
        </div>
      </div>
      <div class="reveal">
        <h3 class="h-md" style="color:var(--red);margin-bottom:1.4rem">Accompagnements &amp; Boissons</h3>
        <div class="menu-list">
          <div class="menu-item"><span class="mi-name">Riz basmati au safran</span><span class="mi-price">4,99\u00a0$</span></div>
          <div class="menu-item"><span class="mi-name">Tomate &amp; oignon grill\u00e9s</span><span class="mi-price">2,99\u00a0$</span></div>
          <div class="menu-item"><span class="mi-name">Salade Shirazi</span><span class="mi-price">4,99\u00a0$</span><span class="mi-desc">Concombre, tomate et oignon avec citron vert et menthe.</span></div>
          <div class="menu-item"><span class="mi-name">Mast-o-Khiar <span class="mi-fa">\u0645\u0627\u0633\u062a\u200c\u0648\u062e\u06cc\u0627\u0631</span></span><span class="mi-price">3,99\u00a0$</span><span class="mi-desc">Yaourt au concombre, menthe et herbes fra\u00eeches.</span></div>
          <div class="menu-item"><span class="mi-name">Doogh <span class="mi-fa">\u062f\u0648\u063a</span></span><span class="mi-price">2,49\u00a0$</span><span class="mi-desc">Boisson yaourt menthol\u00e9e fra\u00eeche.</span></div>
          <div class="menu-item"><span class="mi-name">Th\u00e9 noir &amp; sucre de roche au safran</span><span class="mi-price">1,99\u00a0$</span></div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="split">
      <div class="split-media reveal"><span class="ph" data-label="Photo : le comptoir kabab et le gril mangal"></span></div>
      <div class="split-body reveal">
        <span class="kicker is-light">Pr\u00eat \u00e0 emporter</span>
        <h2 class="h-lg" style="margin:.6rem 0 1rem">Le souper est r\u00e9gl\u00e9 \u2014 avec vos courses</h2>
        <p class="lead">Terminez vos achats, prenez un plateau chaud en partant, et le repas est pr\u00eat. Pas d\u2019application, pas de frais de livraison \u2014 juste de la vraie cuisine persane, pr\u00e9par\u00e9e fra\u00eeche pendant que vous magasinez.</p>
        <a class="btn btn-light" href="contact.html" style="margin-top:1.6rem">Heures &amp; itin\u00e9raire <span class="arr">\u2192</span></a>
      </div>
    </div>
  </div>
</section>'''

specials_body = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Accueil</a> / Sp\u00e9ciaux</p>
    <span class="kicker is-light" style="margin-top:.8rem">Valide lun 1 juin \u2013 dim 7 juin 2026</span>
    <h1 class="h-xl">Les sp\u00e9ciaux de la semaine</h1>
    <p class="lead">Nouvelles promotions chaque semaine sur les produits frais, la viande Halal et les essentiels d\u2019\u00e9picerie. Sans abonnement, sans application \u2014 apportez simplement cette liste en magasin. Prix en dollars canadiens, valables jusqu\u2019\u00e0 \u00e9puisement des stocks.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="deal-hero reveal">
      <div class="dh-media"><span class="ph" data-label="Photo : riz basmati premium"></span></div>
      <div class="dh-body">
        <span class="save">Coup de la semaine \u00b7 \u00c9conomisez 28%</span>
        <h2 class="h-lg" style="margin:1rem 0 .4rem">Basmati vieilli premium \u00b7 10 kg</h2>
        <p class="lead" style="margin-bottom:1.4rem">Basmati \u00e0 long grain, doublement vieilli \u2014 le sac qui dure un mois dans un foyer persan.</p>
        <div style="display:flex;align-items:baseline;gap:1rem;flex-wrap:wrap">
          <span class="price" style="font-size:4rem"><span class="cur">$</span>17<span class="unit">/ sac de 10 kg</span></span>
          <span class="was" style="font-size:1.2rem">$24.99</span>
        </div>
        <p style="margin-top:1.4rem;font-family:var(--f-mono);font-size:.78rem;color:var(--ink-soft)">Limite de 2 sacs par client \u00b7 En magasin seulement</p>
      </div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2 class="h-md reveal" style="margin-bottom:1.4rem;display:flex;align-items:center;gap:.7rem">
      <span style="width:10px;height:10px;border-radius:50%;background:var(--green);display:inline-block"></span>Produits frais
    </h2>
    <div class="flyer">
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">PRODUITS FRAIS</span></div><div class="d-body"><h3>Concombres persans</h3><p class="d-sub">Croquants &amp; sucr\u00e9s</p><div class="d-price"><span class="price"><span class="cur">$</span>1<sup style="font-size:.5em">49</sup><span class="unit">/lb</span></span><span class="was">$2.49</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">PRODUITS FRAIS</span></div><div class="d-body"><h3>Bottes de sabzi fra\u00eeches</h3><p class="d-sub">Persil \u00b7 coriandre \u00b7 aneth</p><div class="d-price"><span class="price"><span class="cur">$</span>0<sup style="font-size:.5em">99</sup><span class="unit">/botte</span></span><span class="was">$1.49</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">PRODUITS FRAIS</span></div><div class="d-body"><h3>Grenades</h3><p class="d-sub">Grosses et juteuses</p><div class="d-price"><span class="price"><span class="cur">$</span>2<sup style="font-size:.5em">99</sup><span class="unit">/pi\u00e8ce</span></span><span class="was">$3.99</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">PRODUITS FRAIS</span></div><div class="d-body"><h3>Tomates Roma</h3><p class="d-sub">Fra\u00eeches de caisse</p><div class="d-price"><span class="price"><span class="cur">$</span>1<sup style="font-size:.5em">29</sup><span class="unit">/lb</span></span><span class="was">$1.99</span></div></div></div>
    </div>
  </div>
</section>
<section class="section band-cream">
  <div class="wrap">
    <h2 class="h-md reveal" style="margin-bottom:1.4rem;display:flex;align-items:center;gap:.7rem">
      <span style="width:10px;height:10px;border-radius:50%;background:var(--red);display:inline-block"></span>Viande &amp; Volaille Halal
      <span class="halal-badge" style="font-size:.68rem;padding:.35em .7em">\u2713 Halal</span>
    </h2>
    <div class="flyer">
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">BOUCHERIE</span></div><div class="d-body"><h3>\u00c9paule d\u2019agneau fra\u00eeche</h3><p class="d-sub">Coup\u00e9e sur commande</p><div class="d-price"><span class="price"><span class="cur">$</span>8<sup style="font-size:.5em">99</sup><span class="unit">/lb</span></span><span class="was">$12.99</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">BOUCHERIE</span></div><div class="d-body"><h3>B\u0153uf hach\u00e9</h3><p class="d-sub">Frais quotidien \u00b7 moyen</p><div class="d-price"><span class="price"><span class="cur">$</span>4<sup style="font-size:.5em">99</sup><span class="unit">/lb</span></span><span class="was">$6.49</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">BOUCHERIE</span></div><div class="d-body"><h3>Poulet entier</h3><p class="d-sub">Nourri aux grains \u00b7 Halal</p><div class="d-price"><span class="price"><span class="cur">$</span>2<sup style="font-size:.5em">79</sup><span class="unit">/lb</span></span><span class="was">$3.49</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">MARIN\u00c9</span></div><div class="d-body"><h3>Joojeh Kabab</h3><p class="d-sub">Marin\u00e9 au safran \u00b7 pr\u00eat \u00e0 griller</p><div class="d-price"><span class="price"><span class="cur">$</span>7<sup style="font-size:.5em">99</sup><span class="unit">/lb</span></span><span class="was">$9.99</span></div></div></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2 class="h-md reveal" style="margin-bottom:1.4rem;display:flex;align-items:center;gap:.7rem">
      <span style="width:10px;height:10px;border-radius:50%;background:var(--saffron);display:inline-block"></span>\u00c9picerie &amp; Comptoir
    </h2>
    <div class="flyer">
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">\u00c9PICERIE</span></div><div class="d-body"><h3>Olives Kalamata</h3><p class="d-sub">Du comptoir ouvert</p><div class="d-price"><span class="price"><span class="cur">$</span>9<sup style="font-size:.5em">99</sup><span class="unit">/kg</span></span><span class="was">$13.99</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">\u00c9PICERIE</span></div><div class="d-body"><h3>Feta bulgare</h3><p class="d-sub">Cr\u00e9meux &amp; acidul\u00e9</p><div class="d-price"><span class="price"><span class="cur">$</span>11<sup style="font-size:.5em">99</sup><span class="unit">/kg</span></span><span class="was">$15.99</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">\u00c9PICERIE</span></div><div class="d-body"><h3>M\u00e9lange ajil de noix</h3><p class="d-sub">Grill\u00e9 &amp; sal\u00e9</p><div class="d-price"><span class="price"><span class="cur">$</span>14<sup style="font-size:.5em">99</sup><span class="unit">/kg</span></span><span class="was">$19.99</span></div></div></div>
      <div class="deal reveal"><div class="d-media"><span class="ph" data-label="Photo"></span><span class="d-tag">\u00c9PICERIE</span></div><div class="d-body"><h3>Th\u00e9 noir Sadaf \u00b7 454g</h3><p class="d-sub">Earl Grey &amp; Ceylan</p><div class="d-price"><span class="price"><span class="cur">$</span>5<sup style="font-size:.5em">99</sup><span class="unit">/bo\u00eete</span></span><span class="was">$7.99</span></div></div></div>
    </div>
  </div>
</section>
<section class="section band-saffron center">
  <div class="wrap" style="max-width:680px">
    <span class="kicker center-line">Comment \u00e7a fonctionne</span>
    <h2 class="h-md" style="margin:.6rem 0 1rem">Les sp\u00e9ciaux changent chaque lundi</h2>
    <p class="lead" style="margin-inline:auto">Les prix affich\u00e9s ici sont un exemple de circulaire \u2014 remplacez-les par les vrais chiffres hebdomadaires. Il n\u2019y a pas de commande en ligne\u00a0: si une offre vous int\u00e9resse, venez en magasin avant qu\u2019elle disparaisse.</p>
    <a class="btn btn-red" href="contact.html" style="margin-top:1.6rem">Planifier votre visite <span class="arr">\u2192</span></a>
  </div>
</section>'''

produits_body = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Accueil</a> / Produits</p>
    <span class="kicker is-light" style="margin-top:.8rem">Ce que nous offrons</span>
    <h1 class="h-xl">Nos rayons</h1>
    <p class="lead">Une \u00e9picerie persane compl\u00e8te en 6\u202f000 pi\u00b2 \u2014 frais, surgel\u00e9s, Halal et servis \u00e0 la main. Tout est en magasin seulement ; parcourez les cat\u00e9gories ci-dessous et venez les trouver en rayon.</p>
  </div>
</section>
<nav class="band band-cream" aria-label="Liens rapides par cat\u00e9gorie">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:.5rem;padding-block:1.1rem">
    <a class="btn btn-ghost" href="#produce" style="padding:.5em 1em;font-size:.9rem">Produits frais</a>
    <a class="btn btn-ghost" href="#meat" style="padding:.5em 1em;font-size:.9rem">Viande Halal</a>
    <a class="btn btn-ghost" href="#marinated" style="padding:.5em 1em;font-size:.9rem">Viande marin\u00e9e</a>
    <a class="btn btn-ghost" href="#counter" style="padding:.5em 1em;font-size:.9rem">Olives &amp; Fromages</a>
    <a class="btn btn-ghost" href="#pantry" style="padding:.5em 1em;font-size:.9rem">Riz &amp; \u00c9picerie</a>
    <a class="btn btn-ghost" href="#frozen" style="padding:.5em 1em;font-size:.9rem">Surgel\u00e9s</a>
    <a class="btn btn-ghost" href="#bakery" style="padding:.5em 1em;font-size:.9rem">Pain</a>
    <a class="btn btn-ghost" href="#sweets" style="padding:.5em 1em;font-size:.9rem">Sucreries</a>
  </div>
</nav>
<section class="section" id="produce">
  <div class="wrap"><div class="split">
    <div class="split-media reveal"><img src="../assets/produce.webp" alt="Mur de produits frais"></div>
    <div class="split-body reveal">
      <span class="kicker">Frais chaque jour</span>
      <h2 class="h-lg" style="margin:.6rem 0 1rem">Fruits &amp; L\u00e9gumes</h2>
      <p class="lead" style="margin-bottom:1rem">Notre mur de produits est r\u00e9approvisionn\u00e9 chaque matin avec une large s\u00e9lection de fruits et l\u00e9gumes frais \u2014 locaux, exotiques et tous les favoris persans que vous aimez.</p>
      <ul class="ticks"><li>Herbes persanes\u00a0: fenugrec, aneth, coriandre, persil</li><li>L\u00e9gumes-feuilles, courges, aubergines, poivrons &amp; plus</li><li>Fruits de saison \u2014 locaux du Qu\u00e9bec et import\u00e9s</li><li>Citrons s\u00e9ch\u00e9s, sumac frais &amp; \u00e9pices pour cuisiner</li></ul>
    </div>
  </div></div>
</section>
<section class="section band" id="meat">
  <div class="wrap"><div class="split flip">
    <div class="split-media reveal"><span class="ph" data-label="Photo : boucherie Halal"></span></div>
    <div class="split-body reveal">
      <span class="kicker is-light">Certifi\u00e9 Halal \u00b7 \u062d\u0644\u0627\u0644</span>
      <h2 class="h-lg" style="margin:.6rem 0 1rem;color:#fff">Viande &amp; Volaille Halal</h2>
      <p class="lead">Toute notre viande et volaille est certifi\u00e9e Halal, coup\u00e9e fra\u00eeche chaque jour en magasin. Dites-nous vos pr\u00e9f\u00e9rences \u2014 enti\u00e8re, en morceaux, hach\u00e9e ou marin\u00e9e pour le gril.</p>
      <ul class="ticks" style="margin-top:1.4rem"><li>B\u0153uf, agneau, veau &amp; poulet frais quotidiennement</li><li>Coupes personnalis\u00e9es &amp; commandes en gros disponibles</li><li>Kabab koobideh, joojeh &amp; barg marin\u00e9s maison</li><li>Viande hach\u00e9e, c\u00f4telettes &amp; d\u00e9coupes sp\u00e9ciales sur demande</li></ul>
      <a class="btn btn-light" href="#marinated" style="margin-top:1.8rem">Voir les viandes marin\u00e9es <span class="arr">\u2192</span></a>
    </div>
  </div></div>
</section>
<section class="section" id="marinated">
  <div class="wrap"><div class="split">
    <div class="split-media reveal"><span class="ph" data-label="Photo : plateaux de kabab marin\u00e9"></span></div>
    <div class="split-body reveal">
      <span class="kicker">Pr\u00eat \u00e0 griller</span>
      <h2 class="h-lg" style="margin:.6rem 0 1rem">Viande marin\u00e9e</h2>
      <p class="lead" style="margin-bottom:1rem">Nos marinades maison sont pr\u00e9par\u00e9es quotidiennement \u2014 achetez le plateau et mettez-le directement sur votre barbecue. La saveur du mangal, \u00e0 la maison.</p>
      <ul class="ticks"><li>Koobideh \u2014 b\u0153uf hach\u00e9 assaisonn\u00e9 \u00e0 l\u2019oignon et au safran</li><li>Joojeh \u2014 poulet marin\u00e9 au citron, safran et herbes</li><li>Barg \u2014 filet de b\u0153uf finement tranch\u00e9 et marin\u00e9</li><li>Plateaux de diff\u00e9rentes tailles \u2014 pour 2 \u00e0 8 personnes</li></ul>
    </div>
  </div></div>
</section>
<section class="section band-cream" id="counter">
  <div class="wrap"><div class="split flip">
    <div class="split-media reveal"><img src="../assets/olive-counter.webp" alt="Comptoir ouvert olives et fromages"></div>
    <div class="split-body reveal">
      <span class="kicker">Servi \u00e0 la main</span>
      <h2 class="h-lg" style="margin:.6rem 0 1rem">Olives, Fromages &amp; Noix</h2>
      <p class="lead" style="margin-bottom:1rem">Notre comptoir ouvert est unique en son genre \u2014 des dizaines de vari\u00e9t\u00e9s d\u2019olives, de fromages feta et de noix, servis frais \u00e0 la commande. Go\u00fbtez avant d\u2019acheter.</p>
      <ul class="ticks"><li>Kalamata, olives vertes libanaises, noires marocaines &amp; plus</li><li>Feta bulgare, iranienne &amp; grecque \u2014 cr\u00e9meuse \u00e0 ferme</li><li>Noix en vrac\u00a0: pistaches, amandes, noix de cajou, noix mixtes</li><li>Fruits secs\u00a0: abricots, figues, raisins secs, dattes &amp; baies de goji</li></ul>
    </div>
  </div></div>
</section>
<section class="section" id="pantry">
  <div class="wrap"><div class="split">
    <div class="split-media reveal"><img src="../assets/bulk-aisle.webp" alt="Rayon riz et \u00e9picerie"></div>
    <div class="split-body reveal">
      <span class="kicker">L\u2019\u00e9picerie persane</span>
      <h2 class="h-lg" style="margin:.6rem 0 1rem">Riz, L\u00e9gumineuses &amp; \u00c9picerie</h2>
      <p class="lead" style="margin-bottom:1rem">Tout ce qu\u2019il vous faut pour une cuisine persane compl\u00e8te \u2014 du riz basmati vieilli premium jusqu\u2019au safran iranien, en passant par les conserves et les produits import\u00e9s.</p>
      <ul class="ticks"><li>Riz basmati vieilli &amp; Tilda en toutes tailles \u2014 1\u00a0kg \u00e0 20\u00a0kg</li><li>Lentilles, pois chiches, f\u00e8ves, haricots &amp; pois cass\u00e9s</li><li>Safran iranien, eau de rose, citrons s\u00e9ch\u00e9s &amp; advieh</li><li>Conserves, p\u00e2tes, sauces &amp; condiments import\u00e9s</li></ul>
    </div>
  </div></div>
</section>
<section class="section band-cream" id="frozen">
  <div class="wrap"><div class="split flip">
    <div class="split-media reveal"><span class="ph" data-label="Photo : rayon surgel\u00e9s"></span></div>
    <div class="split-body reveal">
      <span class="kicker">Toujours en stock</span>
      <h2 class="h-lg" style="margin:.6rem 0 1rem">Surgel\u00e9s</h2>
      <p class="lead" style="margin-bottom:1rem">Des herbes fra\u00eechement surgel\u00e9es aux plats cuisin\u00e9s en passant par les pains et le sabzi \u2014 notre rayon surgel\u00e9 est aussi complet que le rayon frais.</p>
      <ul class="ticks"><li>Sabzi surgel\u00e9 \u2014 ghormeh, aash &amp; kuku</li><li>Pains surgel\u00e9s\u00a0: barbari, lavash, sangak &amp; taftoun</li><li>Plats cuisin\u00e9s persans &amp; kouftehs surgel\u00e9s</li><li>L\u00e9gumes, \u00e9damames &amp; m\u00e9langes de l\u00e9gumes import\u00e9s</li></ul>
    </div>
  </div></div>
</section>
<section class="section" id="bakery">
  <div class="wrap"><div class="split">
    <div class="split-media reveal"><span class="ph" data-label="Photo : pain frais et lavash"></span></div>
    <div class="split-body reveal">
      <span class="kicker">Cuit quotidiennement</span>
      <h2 class="h-lg" style="margin:.6rem 0 1rem">Pain &amp; Boulangerie</h2>
      <p class="lead" style="margin-bottom:1rem">Le pain est au c\u0153ur de la table persane. Nous proposons une s\u00e9lection de pains traditionnels frais et surgel\u00e9s, ainsi que des p\u00e2tisseries pour accompagner votre th\u00e9.</p>
      <ul class="ticks"><li>Barbari \u2014 pain plat \u00e9pais et croustillant, parsem\u00e9 de graines</li><li>Lavash \u2014 pain fin et souple, parfait pour le kabab</li><li>Sangak \u2014 pain persan traditionnel aux grains entiers</li><li>Pains libanais, pitas &amp; pain naan disponibles</li></ul>
    </div>
  </div></div>
</section>
<section class="section band-cream" id="sweets">
  <div class="wrap"><div class="split flip">
    <div class="split-media reveal"><span class="ph" data-label="Photo : sucreries persanes et p\u00e2tisseries"></span></div>
    <div class="split-body reveal">
      <span class="kicker">Pour le th\u00e9 du soir</span>
      <h2 class="h-lg" style="margin:.6rem 0 1rem">Sucreries &amp; P\u00e2tisseries</h2>
      <p class="lead" style="margin-bottom:1rem">Des classiques persans aux nouvelles douceurs moyen-orientales, notre rayon sucreries est fait pour accompagner un bon th\u00e9 noir et du sucre de roche au safran.</p>
      <ul class="ticks"><li>Baklava \u2014 aux noix, pistaches ou amandes</li><li>Sohan \u2014 toffee au safran et aux pistaches, sp\u00e9cialit\u00e9 de Qom</li><li>Gaz \u2014 nougat persan aux pistaches &amp; eau de rose</li><li>Shirini tari \u2014 assortiments de p\u00e2tisseries persanes fra\u00eeches</li></ul>
      <a class="btn btn-ghost" href="contact.html" style="margin-top:1.8rem">Nous visiter <span class="arr">\u2192</span></a>
    </div>
  </div></div>
</section>'''

files = [
    ("index.html",      "March\u00e9 Shahran \u2014 \u00c9picerie persane & March\u00e9 Halal \u00b7 NDG, Montr\u00e9al",
     "March\u00e9 Shahran est une \u00e9picerie persane et un march\u00e9 Halal \u00e0 NDG, Montr\u00e9al.",
     "index", topbar(), index_body),
    ("a-propos.html",   "\u00c0 propos \u2014 March\u00e9 Shahran \u00b7 \u00c9picerie persane, NDG Montr\u00e9al",
     "March\u00e9 Shahran est une \u00e9picerie persane familiale et un march\u00e9 Halal \u00e0 NDG, Montr\u00e9al.",
     "a-propos", topbar(), about_body),
    ("contact.html",    "Contact & Heures \u2014 March\u00e9 Shahran \u00b7 NDG Montr\u00e9al",
     "Visitez le March\u00e9 Shahran au 6010 Sherbrooke Ouest, Montr\u00e9al, QC H4A 1X9.",
     "contact", topbar(), contact_body),
    ("restaurant.html", "Restaurant & Kabab \u2014 March\u00e9 Shahran \u00b7 NDG Montr\u00e9al",
     "La cuisine sur place du March\u00e9 Shahran sert du koobideh et joojeh kabab grill\u00e9s frais.",
     "restaurant", topbar(restaurant_topbar), restaurant_body),
    ("speciaux.html",   "Sp\u00e9ciaux de la semaine \u2014 March\u00e9 Shahran \u00b7 NDG Montr\u00e9al",
     "Les sp\u00e9ciaux de la semaine au March\u00e9 Shahran \u2014 produits frais, viande Halal et promotions.",
     "speciaux", topbar(), specials_body),
    ("produits.html",   "Produits \u2014 March\u00e9 Shahran \u00b7 \u00c9picerie persane, NDG Montr\u00e9al",
     "D\u00e9couvrez ce que le March\u00e9 Shahran propose : produits frais, viande Halal, olives, riz et sucreries persanes.",
     "produits", topbar(), produits_body),
]

for filename, title, meta, active, topbar_html, body in files:
    path = os.path.join(BASE, filename)
    html = page(title, meta, active, topbar_html, body)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Written: fr/{filename}")

print("\nAll 6 French pages done!")
