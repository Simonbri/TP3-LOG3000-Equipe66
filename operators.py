"""
Module contenant les opérations mathématiques de base
utilisées par la calculatrice.
"""

def add(a,b):
    """
    Effectue l'addition de deux nombres.

    Paramètres :
        a (float) : Premier nombre.
        b (float) : Deuxième nombre.

    Retour :
        float : Résultat de a + b.
    """
    return a + b

def subtract(a,b):
    """
    Effectue la soustraction de deux nombres.

    Paramètres :
        a (float) : Premier nombre.
        b (float) : Deuxième nombre.

    Retour :
        float : Résultat de la soustraction.

    Note :
        Le comportement attendu est a - b.
    """
    return b - a

def multiply(a,b):
    """
    Effectue la multiplication de deux nombres.

    Paramètres :
        a (float) : Premier nombre.
        b (float) : Deuxième nombre.

    Retour :
        float : Résultat de la multiplication.

    Note :
        Le comportement attendu est a * b.
    """
    return a ** b

def divide(a,b):
    """
    Effectue la division de deux nombres.

    Paramètres :
        a (float) : Numérateur.
        b (float) : Dénominateur.

    Retour :
        float : Résultat de la division.

    Note :
        Devrait gérer la division par zéro de manière appropriée.
    """
    return a // b
