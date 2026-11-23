"""Génère les pages du site baramo.fr (français à la racine, anglais sous /en/).

    python build.py

Les pages produites sont versionnées : GitHub Pages sert le dépôt tel quel, sans
étape de construction. Modifier ce fichier, relancer, puis commiter le tout.
"""
import os
import posixpath

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://baramo.fr"
MAIL = "contact@baramo.fr"
UPDATED = {"fr": "23 novembre 2026", "en": "23 November 2026"}

# chemin de chaque page, par langue
PATHS = {
    "home":    {"fr": "index.html",                    "en": "en/index.html"},
    "orburst": {"fr": "orburst/index.html",            "en": "en/orburst/index.html"},
    "privacy": {"fr": "orburst/confidentialite.html",  "en": "en/orburst/privacy.html"},
    "legal":   {"fr": "mentions-legales.html",         "en": "en/legal.html"},
}


def url(path):
    """Adresse publique : les index se désignent par leur dossier."""
    return path[:-len("index.html")] if path.endswith("index.html") else path


def rel(src, dst):
    """Lien relatif de la page `src` vers le fichier `dst` (le site marche aussi hors de la racine)."""
    r = posixpath.relpath(url(dst) or ".", posixpath.dirname(src) or ".")
    if dst.endswith("index.html"):
        r = "./" if r == "." else r + "/"
    return r


def page(key, lang, title, desc, body):
    src = PATHS[key][lang]
    other = "en" if lang == "fr" else "fr"
    L = lambda k, anchor="": rel(src, PATHS[k][lang]) + anchor
    A = lambda f: rel(src, "assets/" + f)
    fr = lang == "fr"
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{url(src)}">
<link rel="alternate" hreflang="fr" href="{SITE}/{url(PATHS[key]['fr'])}">
<link rel="alternate" hreflang="en" href="{SITE}/{url(PATHS[key]['en'])}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/img/orburst-banner.webp">
<link rel="icon" type="image/png" href="{A('img/baramo-mark.png')}">
<link rel="stylesheet" href="{A('styles.css')}">
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{L('home')}"><img src="{A('img/baramo-mark.png')}" alt="">Baramo.</a>
    <nav>
      <a class="hide-s" href="{L('home', '#creations')}">{'Créations' if fr else 'Work'}</a>
      <a class="hide-s" href="{L('home', '#services')}">Services</a>
      <a href="{L('home', '#contact')}">Contact</a>
      <a class="lang" href="{rel(src, PATHS[key][other])}" hreflang="{other}" lang="{other}">{'English' if fr else 'Français'}</a>
    </nav>
  </div>
</header>
<main>
{body(lang, L, A)}
</main>
<footer>
  <div class="wrap">
    <span class="grow">© 2026 Baramo</span>
    <a href="{L('orburst')}">Orburst</a>
    <a href="https://onsmo.app">ONSMO</a>
    <a href="{L('legal')}">{'Mentions légales' if fr else 'Legal notice'}</a>
    <a href="mailto:{MAIL}">{MAIL}</a>
  </div>
</footer>
</body>
</html>
"""
    out = os.path.join(ROOT, src)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(src)


# ─── ACCUEIL ──────────────────────────────────────────────────────────────────

def home(lang, L, A):
    if lang == "fr":
        t = dict(
            h1="Des applications et des jeux, <em>faits avec soin.</em>",
            lead="Baramo est un studio indépendant français. Nous éditons nos propres applications et jeux mobiles, et nous réalisons ceux de nos clients.",
            cta1="Voir nos créations", cta2="Nous contacter",
            work_eye="Créations", work_h="Ce que nous éditons",
            o_tags=("Jeu mobile", "iOS et Android", "Bientôt disponible"),
            o_p="Une file de billes colorées avance sur le sentier. Visez, tirez, alignez-en trois de la même couleur avant qu'elles n'atteignent le bout du chemin. 80 niveaux, 8 mondes, un mode infini.",
            o_more="Découvrir Orburst →",
            n_tags=("Application", "iOS et Android", "Bêta ouverte"),
            n_p="Des défis entre amis : 100 pompes, 5 livres, 30 jours de méditation. Fixez un objectif, notez vos avancées et regardez qui progresse, ensemble ou les uns contre les autres.",
            n_more="Aller sur onsmo.app →",
            k_eye="Sur mesure", k_h="Ce que nous réalisons pour nos clients",
            k_tags=("Application sur mesure", "iOS et Android", "Depuis 2021"),
            k_name="Application métier, secteur de la santé",
            k_p="Une application mobile pour des professionnels de santé libéraux. En déplacement, ils photographient leurs documents et les transmettent en quelques gestes, sans attendre le retour au cabinet.",
            k_facts=["Conçue, développée et publiée sur les stores par Baramo",
                     "En service depuis 2021, régulièrement mise à jour"],
            s_eye="Services", s_h="Ce que nous faisons pour vous",
            services=[
                ("Applications mobiles", "iOS et Android, de la première maquette à la publication sur les stores, puis le suivi des mises à jour."),
                ("Jeux", "Jeux mobiles et jeux pour le Web : conception, graphismes, sons, réglage de la difficulté."),
                ("Sites web", "Des sites rapides et sobres, faciles à faire évoluer, hébergés sans abonnement inutile."),
                ("Design d'interface", "Des écrans clairs, pensés pour être compris au premier coup d'œil et agréables à utiliser."),
            ],
            c_h="Donner vie<br>à vos idées.",
            c_p="Un projet d'application, de jeu ou de site ? Écrivez-nous.",
        )
    else:
        t = dict(
            h1="Apps and games, <em>made with care.</em>",
            lead="Baramo is an independent French studio. We publish our own mobile apps and games, and we build them for our clients.",
            cta1="See our work", cta2="Get in touch",
            work_eye="Work", work_h="What we publish",
            o_tags=("Mobile game", "iOS and Android", "Coming soon"),
            o_p="A line of colourful marbles is rolling down the path. Aim, shoot, and match three of the same colour before they reach the end. 80 levels, 8 worlds, an endless mode.",
            o_more="Discover Orburst →",
            n_tags=("App", "iOS and Android", "Open beta"),
            n_p="Challenges between friends: 100 push-ups, 5 books, 30 days of meditation. Set a goal, log your progress and see who is moving forward, together or against each other. (In French for now.)",
            n_more="Go to onsmo.app →",
            k_eye="Custom work", k_h="What we build for our clients",
            k_tags=("Custom app", "iOS and Android", "Since 2021"),
            k_name="Business app, healthcare",
            k_p="A mobile app for self-employed healthcare professionals. On the move, they photograph their documents and send them in a few taps, without waiting to be back at the office.",
            k_facts=["Designed, developed and published on the stores by Baramo",
                     "In service since 2021, regularly updated"],
            s_eye="Services", s_h="What we do for you",
            services=[
                ("Mobile apps", "iOS and Android, from the first mock-up to the store release, then the updates that follow."),
                ("Games", "Mobile and web games: design, artwork, sound, difficulty tuning."),
                ("Websites", "Fast, uncluttered sites that are easy to grow, hosted without needless subscriptions."),
                ("Interface design", "Clear screens, meant to be understood at a glance and pleasant to use."),
            ],
            c_h="Bring your<br>ideas to life.",
            c_p="An app, a game or a website in mind? Write to us.",
        )
    tags = lambda ts: "".join(
        f'<span class="tag{" status" if i == 2 else ""}">{x}</span>' for i, x in enumerate(ts))
    services = "\n".join(
        f'      <div><span class="n">{i:02d}</span><h3>{h}</h3><p>{p}</p></div>'
        for i, (h, p) in enumerate(t["services"], 1))
    facts = "\n".join(f"          <li>{x}</li>" for x in t["k_facts"])
    return f"""<div class="wrap hero">
  <h1>{t['h1']}</h1>
  <p>{t['lead']}</p>
  <div class="actions">
    <a class="btn" href="#creations">{t['cta1']}</a>
    <a class="btn ghost" href="#contact">{t['cta2']}</a>
  </div>
</div>

<section id="creations">
  <div class="wrap">
    <span class="eyebrow">{t['work_eye']}</span>
    <h2 class="title">{t['work_h']}</h2>
    <div class="work">
      <a class="card" href="{L('orburst')}">
        <div class="media"><img class="cover" src="{A('img/orburst-banner.webp')}" alt="Orburst" width="1024" height="500"></div>
        <div class="text">
          <div class="tags">{tags(t['o_tags'])}</div>
          <h3>Orburst</h3>
          <p>{t['o_p']}</p>
          <span class="more">{t['o_more']}</span>
        </div>
      </a>
      <a class="card onsmo" href="https://onsmo.app">
        <div class="media">
          <img src="{A('img/onsmo-1.webp')}" alt="" width="720" height="1558" loading="lazy">
          <img src="{A('img/onsmo-2.webp')}" alt="" width="720" height="1558" loading="lazy">
        </div>
        <div class="text">
          <div class="tags">{tags(t['n_tags'])}</div>
          <h3><img class="logo" src="{A('img/onsmo.svg')}" alt="ONSMO"></h3>
          <p>{t['n_p']}</p>
          <span class="more">{t['n_more']}</span>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- client non nommé tant qu'il n'a pas donné son accord -->
<section id="clients" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">{t['k_eye']}</span>
    <h2 class="title">{t['k_h']}</h2>
    <div class="card case">
      <div class="text">
        <div class="tags">{tags(t['k_tags'])}</div>
        <h3>{t['k_name']}</h3>
      </div>
      <div class="text">
        <p>{t['k_p']}</p>
        <ul class="list">
{facts}
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="services" class="band">
  <div class="wrap">
    <span class="eyebrow">{t['s_eye']}</span>
    <h2 class="title">{t['s_h']}</h2>
    <div class="services">
{services}
    </div>
  </div>
</section>

<section id="contact" class="contact">
  <div class="wrap">
    <h2>{t['c_h']}</h2>
    <p>{t['c_p']}</p>
    <a class="btn blue" href="mailto:{MAIL}">{MAIL}</a>
  </div>
</section>"""


# ─── ORBURST ──────────────────────────────────────────────────────────────────

def orburst(lang, L, A):
    if lang == "fr":
        t = dict(
            lead="Une file de billes colorées avance sur le sentier. Visez, tirez, et alignez-en trois de la même couleur pour les faire éclater avant qu'elles n'atteignent le bout du chemin !",
            p="Orburst est un jeu d'adresse et de réflexion simple à prendre en main : un doigt suffit. Mais les billes accélèrent, les couleurs se multiplient, et chaque tir compte.",
            soon="Bientôt disponible sur iPhone, iPad et Android. Gratuit, avec des publicités.",
            feats=["80 niveaux à travers 8 mondes, de la jungle à l'espace",
                   "Un bonus propre à chaque monde, à découvrir en avançant",
                   "Des sentiers qui serpentent, se croisent et passent sous des tunnels",
                   "Jusqu'à trois étoiles à décrocher par niveau",
                   "Un mode infini pour battre votre record",
                   "Des combos à enchaîner pour multiplier votre score"],
            help_h="Assistance",
            help_p=f'Besoin d\'aide, un bug à signaler, une idée ? Écrivez-nous : <a href="mailto:{MAIL}">{MAIL}</a>. Nous répondons en français et en anglais.',
            priv="Règles de confidentialité d'Orburst", shot="Capture d'écran d'Orburst",
        )
    else:
        t = dict(
            lead="A line of colourful marbles is rolling down the path. Aim, shoot, and match three of the same colour to pop them before they reach the end!",
            p="Orburst is a game of skill and quick thinking that's easy to pick up: one finger is all you need. But the marbles speed up, the colours multiply, and every shot counts.",
            soon="Coming soon to iPhone, iPad and Android. Free, with ads.",
            feats=["80 levels across 8 worlds, from the jungle to outer space",
                   "A unique bonus in every world, unlocked as you progress",
                   "Paths that wind, cross and dive through tunnels",
                   "Up to three stars to earn on each level",
                   "An endless mode to beat your high score",
                   "Combos to chain to multiply your score"],
            help_h="Support",
            help_p=f'Need help, found a bug, or have a suggestion? Write to us: <a href="mailto:{MAIL}">{MAIL}</a>. We answer in English and French.',
            priv="Orburst privacy policy", shot="Orburst screenshot",
        )
    feats = "\n".join(f"        <li>{x}</li>" for x in t["feats"])
    shots = "\n".join(
        f'      <img src="{A("img/orburst-%d.webp" % i)}" alt="{t["shot"]}" width="540" height="960" loading="lazy">'
        for i in (1, 2, 3))
    return f"""<div class="wrap game-head">
  <img class="banner" src="{A('img/orburst-banner.webp')}" alt="" width="1024" height="500">
  <div class="game-id">
    <img src="{A('img/orburst-icon.webp')}" alt="" width="256" height="256">
    <h1>Orburst</h1>
  </div>
  <p class="lead">{t['lead']}</p>
</div>

<section>
  <div class="wrap cols">
    <div>
      <p>{t['p']}</p>
      <ul class="list">
{feats}
      </ul>
    </div>
    <div class="box">
      <h2>{t['soon'].split('.')[0]}.</h2>
      <p>{t['soon'].split('. ', 1)[1]}</p>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap shots">
{shots}
  </div>
</section>

<section id="assistance" style="padding-top:0">
  <div class="wrap">
    <div class="box">
      <h2>{t['help_h']}</h2>
      <p>{t['help_p']}</p>
      <p><a href="{L('privacy')}">{t['priv']}</a></p>
    </div>
  </div>
</section>"""


# ─── CONFIDENTIALITÉ D'ORBURST ────────────────────────────────────────────────

def privacy(lang, L, A):
    if lang == "fr":
        return f"""<div class="wrap prose">
<h1>Orburst – Règles de confidentialité</h1>
<p class="date">Dernière mise à jour : {UPDATED['fr']}</p>

<p>Orburst est un jeu mobile édité par Baramo (« nous »), société française dont les coordonnées
figurent dans les <a href="{L('legal')}">mentions légales</a>. Cette page explique quelles données sont
traitées quand vous jouez, et pourquoi.</p>

<h2>Ce que nous collectons nous-mêmes</h2>
<p>Rien. Orburst n'a ni compte, ni connexion, ni serveur en ligne. Votre progression, vos étoiles, vos
scores et vos réglages sont enregistrés uniquement sur votre appareil. Ils sont effacés si vous
désinstallez le jeu ou videz ses données.</p>

<h2>Publicité</h2>
<p>Orburst est gratuit et affiche des publicités fournies par Google AdMob. Pour afficher les
publicités, les mesurer et lutter contre la fraude, le logiciel publicitaire de Google intégré au jeu
peut collecter et traiter :</p>
<ul>
  <li>l'identifiant publicitaire de votre appareil ;</li>
  <li>votre adresse IP, dont peut être déduite une localisation approximative (pays, ville) ;</li>
  <li>des informations techniques sur votre appareil (modèle, version du système, langue) et des
      diagnostics ;</li>
  <li>vos interactions avec les publicités (publicités affichées, appuis).</li>
</ul>
<p>Ces données sont transmises à Google et traitées selon ses propres règles :
<a href="https://policies.google.com/technologies/partner-sites?hl=fr">Comment Google utilise les
informations provenant des applications qui utilisent ses services</a>. Nous ne les recevons pas sous une
forme qui vous identifie.</p>

<h2>Vos choix</h2>
<ul>
  <li>Là où la loi l'exige (Espace économique européen, Royaume-Uni, Suisse), le jeu demande votre
      consentement avant d'afficher des publicités personnalisées. Vous pouvez modifier votre réponse à
      tout moment avec le bouton « Confidentialité » des paramètres du jeu.</li>
  <li>Vous pouvez réinitialiser ou supprimer votre identifiant publicitaire dans les réglages de votre
      appareil (Android : Paramètres &gt; Google &gt; Annonces ; iOS : Réglages &gt; Confidentialité et
      sécurité &gt; Suivi).</li>
  <li>Sur iOS, le jeu demande votre autorisation avant tout suivi entre applications.</li>
</ul>

<h2>Achats</h2>
<p>Si vous achetez l'option qui retire les publicités, le paiement est entièrement géré par Google Play
ou l'App Store. Nous ne voyons jamais vos informations de paiement.</p>

<h2>Enfants</h2>
<p>Orburst ne s'adresse pas aux enfants de moins de 13 ans, et nous ne collectons pas sciemment de
données personnelles les concernant.</p>

<h2>Vos droits</h2>
<p>Le règlement européen sur la protection des données (RGPD) vous donne un droit d'accès, de
rectification, d'effacement et d'opposition. Comme nous ne détenons aucune donnée vous concernant, ces
droits s'exercent auprès de Google pour les données publicitaires. Vous pouvez aussi nous écrire, et
saisir la CNIL (<a href="https://www.cnil.fr">cnil.fr</a>) si vous estimez que vos droits ne sont pas
respectés.</p>

<h2>Modifications</h2>
<p>Si ces règles changent, la nouvelle version est publiée sur cette page avec sa date.</p>

<h2>Contact</h2>
<p>Pour toute question : <a href="mailto:{MAIL}">{MAIL}</a></p>
</div>"""
    return f"""<div class="wrap prose">
<h1>Orburst – Privacy Policy</h1>
<p class="date">Last updated: {UPDATED['en']}</p>

<p>Orburst is a mobile game published by Baramo ("we"), a French company whose details are given in the
<a href="{L('legal')}">legal notice</a>. This page explains what data is processed when you play, and
why.</p>

<h2>What we collect ourselves</h2>
<p>Nothing. Orburst has no account, no sign-in and no online server of its own. Your progress, stars,
scores and settings are saved only on your device. They are erased if you uninstall the game or clear
its data.</p>

<h2>Advertising</h2>
<p>Orburst is free and shows ads provided by Google AdMob. To display ads, measure them and prevent
fraud, Google's advertising software included in the game may collect and process:</p>
<ul>
  <li>your device's advertising identifier;</li>
  <li>your IP address, from which an approximate location (country, city) can be derived;</li>
  <li>technical information about your device (model, system version, language) and diagnostics;</li>
  <li>your interactions with the ads (ads shown, taps).</li>
</ul>
<p>This data is sent to Google and handled under Google's own policy:
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps
that use its services</a>. We do not receive it in a form that identifies you.</p>

<h2>Your choices</h2>
<ul>
  <li>Where the law requires it (European Economic Area, United Kingdom, Switzerland), the game asks for
      your consent before showing personalised ads. You can change your answer at any time with the
      "Privacy" button in the game's settings.</li>
  <li>You can reset or delete your advertising identifier in your device settings (Android:
      Settings &gt; Google &gt; Ads; iOS: Settings &gt; Privacy &amp; Security &gt; Tracking).</li>
  <li>On iOS, the game asks for your permission before any tracking across apps.</li>
</ul>

<h2>Purchases</h2>
<p>If you buy the option that removes ads, the payment is handled entirely by Google Play or the
App Store. We never see your payment details.</p>

<h2>Children</h2>
<p>Orburst is not directed at children under 13, and we do not knowingly collect personal data from
them.</p>

<h2>Your rights</h2>
<p>The EU General Data Protection Regulation (GDPR) gives you rights of access, rectification, erasure
and objection. As we hold no data about you, these rights are exercised with Google for advertising
data. You can also write to us, and lodge a complaint with the French data protection authority, the
CNIL (<a href="https://www.cnil.fr/en">cnil.fr</a>), if you believe your rights are not respected.</p>

<h2>Changes</h2>
<p>If this policy changes, the new version is published on this page with its date.</p>

<h2>Contact</h2>
<p>Questions about this policy: <a href="mailto:{MAIL}">{MAIL}</a></p>
</div>"""


# ─── MENTIONS LÉGALES ─────────────────────────────────────────────────────────

def legal(lang, L, A):
    if lang == "fr":
        return f"""<div class="wrap prose">
<h1>Mentions légales</h1>
<p class="date">Dernière mise à jour : {UPDATED['fr']}</p>

<h2>Éditeur du site</h2>
<address>
Baramo, société par actions simplifiée à associé unique (SASU) au capital de 150 €<br>
Siège social : 15 impasse des Souches, 83500 La Seyne-sur-Mer, France<br>
SIRET : 899 210 686 00015<br>
TVA intracommunautaire : FR87899210686<br>
Président et directeur de la publication : Lucas Ramadour<br>
Contact : <a href="mailto:{MAIL}">{MAIL}</a>
</address>

<h2>Hébergeur</h2>
<address>
GitHub, Inc. (service GitHub Pages)<br>
88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis<br>
<a href="https://pages.github.com">pages.github.com</a>
</address>

<h2>Propriété intellectuelle</h2>
<p>Ce site et son contenu (textes, images, logos, captures des applications et des jeux) appartiennent à
Baramo, sauf mention contraire. Toute reproduction ou adaptation, totale ou partielle, sans autorisation
écrite préalable est interdite.</p>

<h2>Données personnelles</h2>
<p>Ce site ne dépose aucun cookie, n'utilise aucun outil de mesure d'audience et ne contient aucun
formulaire. Comme tout hébergeur, GitHub enregistre des journaux techniques (dont l'adresse IP des
visiteurs) pour assurer la sécurité du service.</p>
<p>Si vous nous écrivez, votre adresse e-mail et votre message servent uniquement à vous répondre et ne
sont transmis à personne. Vous pouvez demander leur suppression à tout moment à la même adresse, et saisir
la CNIL (<a href="https://www.cnil.fr">cnil.fr</a>) si vous estimez que vos droits ne sont pas
respectés.</p>
<p>Chaque application ou jeu a ses propres règles de confidentialité :
<a href="{L('privacy')}">Orburst</a>,
<a href="https://onsmo.app/confidentialite">ONSMO</a>.</p>

<h2>Responsabilité</h2>
<p>Baramo s'efforce de tenir à jour les informations publiées ici, sans pouvoir en garantir
l'exhaustivité. Ce site contient des liens vers des sites tiers, dont le contenu ne relève pas de sa
responsabilité.</p>

<h2>Droit applicable</h2>
<p>Les présentes mentions sont régies par le droit français.</p>
</div>"""
    return f"""<div class="wrap prose">
<h1>Legal notice</h1>
<p class="date">Last updated: {UPDATED['en']}</p>

<h2>Publisher</h2>
<address>
Baramo, a French single-shareholder simplified joint-stock company (SASU), share capital €150<br>
Registered office: 15 impasse des Souches, 83500 La Seyne-sur-Mer, France<br>
SIRET: 899 210 686 00015<br>
EU VAT number: FR87899210686<br>
President and publication director: Lucas Ramadour<br>
Contact: <a href="mailto:{MAIL}">{MAIL}</a>
</address>

<h2>Hosting</h2>
<address>
GitHub, Inc. (GitHub Pages)<br>
88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA<br>
<a href="https://pages.github.com">pages.github.com</a>
</address>

<h2>Intellectual property</h2>
<p>This site and its content (text, images, logos, screenshots of the apps and games) belong to Baramo
unless stated otherwise. Any reproduction or adaptation, in whole or in part, without prior written
permission is prohibited.</p>

<h2>Personal data</h2>
<p>This site sets no cookies, uses no analytics and contains no forms. Like any host, GitHub keeps
technical logs (including visitors' IP addresses) to keep the service secure.</p>
<p>If you write to us, your e-mail address and your message are used only to answer you and are not
passed on to anyone. You can ask us to delete them at any time at the same address, and lodge a complaint
with the French data protection authority, the CNIL (<a href="https://www.cnil.fr/en">cnil.fr</a>), if you
believe your rights are not respected.</p>
<p>Each app or game has its own privacy policy:
<a href="{L('privacy')}">Orburst</a>,
<a href="https://onsmo.app/confidentialite">ONSMO</a> (in French).</p>

<h2>Liability</h2>
<p>Baramo does its best to keep the information published here up to date, without being able to
guarantee that it is complete. This site links to third-party sites whose content is not its
responsibility.</p>

<h2>Governing law</h2>
<p>This notice is governed by French law.</p>
</div>"""


PAGES = [
    ("home", home, {
        "fr": ("Baramo – Applications et jeux mobiles", "Baramo est un studio indépendant français : nous éditons nos applications et jeux mobiles (Orburst, ONSMO) et réalisons ceux de nos clients."),
        "en": ("Baramo – Mobile apps and games", "Baramo is an independent French studio: we publish our own mobile apps and games (Orburst, ONSMO) and build them for our clients."),
    }),
    ("orburst", orburst, {
        "fr": ("Orburst – Jeu de tir de billes | Baramo", "Orburst : visez, tirez, alignez trois billes. 80 niveaux, 8 mondes, un mode infini. Bientôt sur iOS et Android."),
        "en": ("Orburst – Marble shooter game | Baramo", "Orburst: aim, shoot, match three marbles. 80 levels, 8 worlds, an endless mode. Coming soon to iOS and Android."),
    }),
    ("privacy", privacy, {
        "fr": ("Orburst – Règles de confidentialité", "Quelles données sont traitées quand vous jouez à Orburst, et pourquoi."),
        "en": ("Orburst – Privacy Policy", "What data is processed when you play Orburst, and why."),
    }),
    ("legal", legal, {
        "fr": ("Mentions légales – Baramo", "Éditeur, hébergeur et données personnelles du site baramo.fr."),
        "en": ("Legal notice – Baramo", "Publisher, hosting and personal data for baramo.fr."),
    }),
]

if __name__ == "__main__":
    for key, body, meta in PAGES:
        for lang in ("fr", "en"):
            page(key, lang, meta[lang][0], meta[lang][1], body)
