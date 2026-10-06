# Ligue de Judo de Guyane — refonte

Maquette du site de la ligue centrée sur Suzini.

## Lancer localement

```sh
python3 -m http.server 8000 --directory dist
```

Ouvrir http://localhost:8000. Aucun paquet ni compilation nécessaire.

## V2 (lots 1 et 2)

Base : révision cccb442 conservée dans l’archive d’origine (non modifiée). Menu et lien d’évitement communs (`common.js`), annuaire partagé (`clubs-data.js`), filtres de période du journal corrigés (`matchPeriod`), nouvelles pages La Ligue, Commencer le judo, Suzini et Clubs. Champs sans donnée validée : « À confirmer ».

## Pages

- La Ligue : `dist/la-ligue.html`. Commencer le judo : `dist/commencer-judo.html`. Suzini : `dist/suzini.html`. Clubs : `dist/clubs.html`.

- Accueil : `dist/index.html`, agenda et annuaire des clubs.
- Journal : `dist/journal.html`, recherche et archives datées.
- Disciplines : `dist/disciplines.html`.
- Photos et vidéos : `dist/galerie.html`.
- Présentation et interactions : fichiers CSS et JavaScript de `dist/`.

## État

Maquette : administration sans code non implémentée. Calendrier, horaires, contacts et affiliations à valider. Les archives restent datées. Polices Google Fonts et vidéos YouTube nécessitent Internet ; leur disponibilité dépend de leurs fournisseurs.

## Médias

Photos du dojo : Collectivité Territoriale de Guyane via https://www.sports.gouv.fr/sport-nature-guyane-centre-aquatique-de-cayenne-hall-seraphin-dojo-de-suzini . Images et vidéos d’archives : https://www.ldjguyane.com/blog . Crédits conservés ; droits de republication à confirmer avant la mise en ligne officielle. La présence des fichiers dans ce dépôt n’accorde pas de licence de réutilisation.

## Synchronisation

Synchroniser ce dépôt à chaque modification du site, avec un commit descriptif. Préserver les contributions existantes. Ne jamais committer de secrets ou jetons.

## Corrections techniques et préparation du lot 3

Calendrier et résultats avec états vides filtrables, pages permanentes des sept archives existantes, favicon provisoire (lettre J, pas un logo officiel), page 404, mentions légales et confidentialité provisoires. Navigation conservée, contrastes renforcés, images WebP avec dimensions, vidéos chargées uniquement après information et acceptation explicite. Aucun événement ni classement inventé.

Avant production : compléter et faire valider les mentions légales et la confidentialité selon l’hébergeur retenu ; valider les droits des médias et les informations officielles. Logo, coordonnées, dates et données des clubs restent différés. Un domaine personnalisé pourra être relié à l’hébergement choisi ; aucun domaine n’est configuré ici. L’hébergement doit servir dist/404.html pour les URL inconnues.

Validation : syntaxe JavaScript, liens locaux, titres, métadonnées et filtres vérifiés. Le téléchargement Chromium a échoué dans l’environnement de travail : la validation visuelle ordinateur/tablette/mobile et la console navigateur restent à effectuer avant production.
