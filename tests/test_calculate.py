"""
Tests unitaires pour la fonction calculate dans app.py.
"""

from app import calculate
import pytest


def test_calculate_add():
    """
    Vérifie le calcul d'une addition simple.
    """
    assert calculate("2+3") == 5


def test_calculate_invalid_format():
    """
    Vérifie qu'une expression invalide lève une erreur.
    """
    with pytest.raises(ValueError):
        calculate("+3")


def test_calculate_multiple_operators():
    """
    Vérifie qu'une expression avec plusieurs opérateurs
    lève une erreur.
    """
    with pytest.raises(ValueError):
        calculate("2+3+4")
