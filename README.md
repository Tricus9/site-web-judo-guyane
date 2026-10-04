# Ligue de Judo de Guyane — refonte

Maquette du site de la ligue centrée sur Suzini.

## Lancer localement

```sh
python3 -m http.server 8000 --directory dist
```

Ouvrir http://localhost:8000. Aucun paquet ni compilation nécessaire.

## Pages

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
