# Module Templates

## Raison d’être

Ce module contient les fichiers HTML utilisés pour l’interface utilisateur.
Il définit la structure visuelle de la calculatrice.

---

## Fichiers principaux

### index.html

Responsabilités :

- Afficher l’interface de la calculatrice
- Envoyer les expressions au backend via une requête POST
- Afficher le résultat retourné par Flask
- Gérer les interactions simples via JavaScript

---

## Dépendances

- Flask (moteur de templates Jinja2)
- Fichiers CSS situés dans le module `static`

---

## Hypothèses

- Le backend fournit une variable `result`
- Le formulaire POST envoie la valeur du champ `display`
