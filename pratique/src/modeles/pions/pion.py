"""
Classe abstraite Pion - Base pour tous les types de pions
"""

from abc import ABC, abstractmethod
from ...enums import Couleur, TypePion
from ..position import Position


class APion(ABC):
    """
    Classe abstraite représentant un pion (simple ou dame).

    Démontre :
    - Classe abstraite avec méthode abstraite
    - Attributs protected (convention _ en Python)
    - Méthodes concrètes communes
    - Encapsulation
    """

    def __init__(self, couleur: Couleur, position: Position):
        """
        Constructeur de base pour tous les pions.

        :param couleur: Couleur du pion
        :param position: Position initiale
        """
        self._couleur = couleur  # Protected
        self._position = position  # Protected
        self._en_jeu = True  # Protected

    # ---- Getters ----
    def get_couleur(self) -> Couleur:
        """Retourne la couleur du pion"""
        return self._couleur

    def get_position(self) -> Position:
        """Retourne la position actuelle"""
        return self._position

    def est_en_jeu(self) -> bool:
        """Vérifie si le pion est encore en jeu"""
        return self._en_jeu

    # ---- Setters ----
    def set_position(self, position: Position):
        """Définit la nouvelle position"""
        self._position = position

    def capturer(self):
        """Marque le pion comme capturé"""
        self._en_jeu = False

    # ---- Méthodes abstraites (doivent être implémentées par les sous-classes) ----
    @abstractmethod
    def peut_se_deplacer_vers(self, destination: Position) -> bool:
        """
        Vérifie si le pion peut se déplacer vers une destination.

        :param destination: Position de destination
        :return: True si le déplacement est possible
        """
        pass

    @abstractmethod
    def obtenir_symbole(self) -> str:
        """
        Retourne le symbole à afficher pour ce pion.

        :return: Symbole du pion (pour l'affichage)
        """
        pass

    @abstractmethod
    def get_type(self) -> TypePion:
        """
        Retourne le type du pion.

        :return: Type du pion (SIMPLE ou DAME)
        """
        pass

    # ---- Méthodes concrètes communes ----
    def __str__(self) -> str:
        """Représentation en chaîne"""
        return f"{self.get_type().value} {self._couleur.value} en {self._position}"

    def __repr__(self) -> str:
        """Représentation pour le débogage"""
        return f"{self.__class__.__name__}({self._couleur}, {self._position})"
