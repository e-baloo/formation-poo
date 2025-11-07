"""
Classe PionSimple - Pion standard du jeu de Dames
"""

from ..position import Position
from ...enums import Couleur, TypePion
from .pion import APion


class PionSimple(APion):
    """
    Représente un pion simple (non-dame).

    Démontre :
    - Héritage d'une classe abstraite
    - Implémentation de méthodes abstraites
    - Redéfinition de comportement
    """

    def peut_se_deplacer_vers(self, destination: Position) -> bool:
        """
        Un pion simple se déplace en diagonale vers l'avant d'une case.

        :param destination: Position de destination
        :return: True si le mouvement est valide
        """
        diff_ligne = destination.get_ligne() - self._position.get_ligne()
        diff_colonne = abs(destination.get_colonne() -
                           self._position.get_colonne())

        # Déplacement en diagonale d'une case
        if diff_colonne != 1:
            return False

        # Direction selon la couleur
        if self._couleur == Couleur.BLANC:
            # Les blancs montent (ligne croissante)
            return diff_ligne == 1
        else:
            # Les noirs descendent (ligne décroissante)
            return diff_ligne == -1

    def obtenir_symbole(self) -> str:
        """Symbole pour l'affichage"""
        return "⚪" if self._couleur == Couleur.BLANC else "⚫"

    def get_type(self) -> TypePion:
        """Retourne le type de pion"""
        return TypePion.SIMPLE

    def peut_etre_promu(self) -> bool:
        """
        Vérifie si le pion peut être promu en dame.

        :return: True si le pion atteint la dernière ligne
        """
        if self._couleur == Couleur.BLANC:
            return self._position.get_ligne() == 10
        else:
            return self._position.get_ligne() == 1
