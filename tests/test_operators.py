"""
Tests unitaires pour le module operators.py.

Ce fichier vérifie le bon fonctionnement des opérations
arithmétiques de base.
"""

from operators import add, subtract, multiply, divide
import pytest


def test_add():
    """
    Vérifie que l'addition retourne le bon résultat.
    """
    assert add(2, 3) == 5


def test_subtract():
    """
    Vérifie que la soustraction retourne a - b.
    """
    assert subtract(5, 3) == 2


def test_multiply():
    """
    Vérifie que la multiplication retourne a * b.
    """
    assert multiply(4, 3) == 12


def test_divide():
    """
    Vérifie que la division retourne a / b.
    """
    assert divide(7, 2) == 2.5


def test_divide_by_zero():
    """
    Vérifie qu'une division par zéro lève une exception.
    """
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
