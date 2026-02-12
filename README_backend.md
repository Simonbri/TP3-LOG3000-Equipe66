# Module Backend

## Raison d’être

Le module backend contient la logique serveur de l’application.
Il est responsable :

- Du traitement des requêtes HTTP
- De l’analyse des expressions mathématiques
- De l’exécution des opérations
- Du rendu des résultats vers l’interface web

---

## Fichiers principaux

### app.py
Point d’entrée de l’application Flask.

Responsabilités :
- Initialiser l’application
- Définir les routes HTTP
- Gérer les requêtes GET et POST
- Appeler la fonction `calculate()` pour traiter les expressions

### operators.py
Contient les fonctions d’opérations mathématiques :

- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)

Chaque fonction exécute une opération arithmétique simple.

---

## Dépendances

- Flask
- Python 3.11.9
- Module interne `operators`

---

## Hypothèses

- L’expression entrée contient exactement deux opérandes
- Une seule opération est autorisée par calcul
- Les opérandes doivent être numériques
