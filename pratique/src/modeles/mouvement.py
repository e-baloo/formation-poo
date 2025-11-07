"""
Classe Mouvement - Représente un mouvement dans le jeu
"""

from typing import Optional
from .position import Position


class Mouvement:
    """
    Représente un mouvement dans le jeu.

    Démontre :
    - Classe de données
    - Encapsulation
    - Validation
    """

    def __init__(self, depart: Position, arrivee: Position, est_capture: bool = False):
        """
        Constructeur de mouvement.

        :param depart: Position de départ
        :param arrivee: Position d'arrivée
        :param est_capture: Indique si c'est une capture
        """
        self.__depart = depart
        self.__arrivee = arrivee
        self.__est_capture = est_capture
        self.__pion_capture: Optional[Position] = None

    # ---- Getters ----
    def get_depart(self) -> Position:
        """Retourne la position de départ"""
        return self.__depart

    def get_arrivee(self) -> Position:
        """Retourne la position d'arrivée"""
        return self.__arrivee

    def est_capture(self) -> bool:
        """Indique si c'est une capture"""
        return self.__est_capture

    def get_pion_capture(self) -> Optional[Position]:
        """Retourne la position du pion capturé"""
        return self.__pion_capture

    # ---- Setters ----
    def set_pion_capture(self, position: Position):
        """Définit la position du pion capturé"""
        self.__pion_capture = position
        self.__est_capture = True

    def __str__(self) -> str:
        """Représentation en chaîne"""
        capture_info = f" (capture en {self.__pion_capture})" if self.__est_capture else ""
        return f"{self.__depart} → {self.__arrivee}{capture_info}"
