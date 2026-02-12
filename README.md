# Calculatrice Web

## Numéro d’équipe
Équipe 66

---
## Objectif
Développer une application web de calculatrice simple à l’aide de Flask en Python.  


## Description du projet
Ce projet consiste en une application web de calculatrice simple développée avec Flask en Python.
L’application permet à un utilisateur d’effectuer des opérations arithmétiques de base
(addition, soustraction, multiplication et division) via une interface web interactive.

## Portée du projet
La calculatrice :

- Accepte une expression contenant deux opérandes et un seul opérateur
- Supporte les opérateurs : +, -, *, /
- Retourne le résultat ou un message d’erreur si l’expression est invalide

Le projet ne supporte pas :
- Les expressions complexes (ex: 2+3*4)
- Les parenthèses
- Plusieurs opérations dans une même expression

---

## Prérequis d’installation
- Python 3.11 ou version ultérieure
- Flask
- HTML / CSS
- Pytest
- pip
- Git
- Un navigateur web

## Instructions d’installation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Simonbri/TP3-LOG3000-Equipe66.git
   ```
2. Installer les dépendances :
   ```bash
   cd TP3-LOG3000-Equipe66
   pip install -r requirements.txt
   ```
3. Lancer l'application :
   ```bash
   python app.py
   ```
4. Ouvrir dans un navigateur :
   ```cpp
   http://127.0.0.1:5000
   ```
## Utilisation
1. Cliquer sur les boutons numériques pour entrer un premier nombre
2. Sélectionner un opérateur (+, -, *, /)
3. Entrer le second nombre
4. Appuyer sur "="
5. Le résultat s’affiche dans l’écran de la calculatrice

En cas d’erreur (expression invalide, opérandes incorrectes), un message d’erreur est affiché.

---

## Tests
Les tests unitaires sont situés dans le dossier :
   ```bash
   tests/
   ```
Pour exécuter les tests :
   ```bash
   pytest
   ```

## Flux de contribution
Le projet suit un workflow basé sur les bonnes pratiques Git :
1. Création d’une Issue GitHub lorsqu'il y a détection d’un bogue
2. Création d’une branche dédiée pour un issue
3. Implémentation de la correction nécessaire
4. Exécution des tests
5. Commit avec message explicatif
6. Ouverture d’une Pull Request
7. Révision et fusion dans la branche main