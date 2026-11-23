# Site baramo.fr

Site statique de Baramo : accueil, page d'Orburst (présentation, assistance, règles de
confidentialité), mentions légales. Français à la racine, anglais sous `/en/`.

## Modifier le site

Les pages HTML sont produites par `build.py` (Python seul, aucune dépendance) :

    python build.py

Tout le texte est dans ce fichier. Les pages produites sont versionnées : après une
modification, relancer le script puis commiter l'ensemble. `404.html`, `assets/`,
`app-ads.txt` et `CNAME` s'éditent à la main.

Aperçu local : `python -m http.server 8765`, puis http://localhost:8765/

## Fichiers qui comptent pour les stores

- `app-ads.txt` : déclare le compte AdMob autorisé à vendre la publicité des applications.
  Doit rester à la racine du domaine indiqué comme site du développeur dans les stores.
- `orburst/confidentialite.html` et `en/orburst/privacy.html` : adresses données à AdMob,
  à l'App Store et à Google Play. Ne pas les renommer.
- `orburst/` : sert aussi de page d'assistance (exigée par l'App Store).

## Hébergement

GitHub Pages, dépôt public, branche `main`, dossier racine. Le fichier `CNAME` porte le
domaine. DNS chez OVH :

- `baramo.fr` : quatre enregistrements A vers 185.199.108.153, 185.199.109.153,
  185.199.110.153 et 185.199.111.153 ;
- `www.baramo.fr` : CNAME vers `baramo-corp.github.io.` ;
- ne pas toucher aux enregistrements MX et TXT (courrier).

## Ajouter une application ou un jeu

Dans `build.py` : une carte de plus dans `home()`, une fonction de page sur le modèle
d'`orburst()`, ses chemins dans `PATHS` et son entrée dans `PAGES`.
