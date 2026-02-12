# Module Static

## Raison d’être

Ce module contient les ressources statiques utilisées par l’application,
principalement les fichiers de style (CSS).

---

## Fichiers principaux

### style.css

Responsabilités :

- Définir le style visuel de la calculatrice
- Gérer la mise en page
- Appliquer les styles aux boutons et à l’affichage

---

## Dépendances

- Chargé dynamiquement par Flask via `url_for('static', ...)`

---

## Hypothèses

- Les classes CSS correspondent aux éléments définis dans `index.html`
