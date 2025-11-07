"""
01 – Pourquoi la POO : comparaison procédural vs orienté objet
"""

# Procédural : des fonctions manipulant des dictionnaires


def aire_rectangle_procedural(rect: dict) -> int:
    return rect["largeur"] * rect["hauteur"]


rect1 = {"largeur": 5, "hauteur": 3}
print("Procédural -> Aire rect1:", aire_rectangle_procedural(rect1))


# Orienté Objet : une classe avec des méthodes
class Rectangle:
    def __init__(self, largeur: int, hauteur: int) -> None:
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self) -> int:
        return self.largeur * self.hauteur


rect2 = Rectangle(5, 3)
print("OO -> Aire rect2:", rect2.aire())
