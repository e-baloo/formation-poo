"""
Énumérations pour le jeu de Dames
"""

from enum import Enum


class Couleur(Enum):
    """Énumération des couleurs des pions"""
    BLANC = "blanc"
    NOIR = "noir"


class TypePion(Enum):
    """Énumération des types de pions"""
    SIMPLE = "simple"
    DAME = "dame"
