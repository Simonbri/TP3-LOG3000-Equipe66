"""
Module principal de l'application Flask.

Ce module :
- Initialise l'application Flask
- Définit les opérations mathématiques disponibles
- Gère la logique de traitement des expressions
- Définit la route principale du site web
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Création de l'application Flask
app = Flask(__name__)

# Dictionnaire associant les symboles d'opérations aux fonctions correspondantes
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Analyse et évalue une expression mathématique simple contenant
    deux opérandes et un seul opérateur.

    Exemple d'expression valide : "2+3"

    Paramètres :
        expr (str) : Expression entrée par l'utilisateur.

    Retour :
        float : Résultat de l'opération.

    Exceptions :
        ValueError : Si l'expression est vide, invalide ou mal formatée.
    """

    # Vérifie que l'expression est valide
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Supprime les espaces pour éviter les erreurs de parsing
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de l'opérateur dans l'expression
    for i, ch in enumerate(s):
        if ch in OPS:
            # On n'autorise qu'un seul opérateur
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l'opérateur n'est pas au début ou à la fin
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Séparation des deux opérandes
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Appel de la fonction correspondant à l'opérateur
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.

    - GET  : Affiche la calculatrice vide.
    - POST : Traite l'expression soumise par l'utilisateur
             et affiche le résultat ou un message d'erreur.

    Retour :
        Template HTML rendu avec le résultat.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # On retourne le message d'erreur à l'utilisateur
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lance le serveur Flask en mode debug (développement uniquement)
    app.run(debug=True)