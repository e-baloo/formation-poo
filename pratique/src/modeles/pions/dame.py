"""
Classe Dame - Pion promu avec déplacements étendus
"""

from ..position import Position
from ...enums import TypePion, Couleur
from .pion import APion


class Dame(APion):
    """
    Représente une dame (pion promu).

    Démontre :
    - Héritage et spécialisation
    - Comportement différent du parent
    - Redéfinition complète de méthodes
    """

    def peut_se_deplacer_vers(self, destination: Position) -> bool:
        """
        Une dame se déplace en diagonale sur n'importe quelle distance.

        :param destination: Position de destination
        :return: True si le mouvement est valide
        """
        diff_ligne = abs(destination.get_ligne() - self._position.get_ligne())
        diff_colonne = abs(destination.get_colonne() -
                           self._position.get_colonne())

        # Déplacement en diagonale (distance quelconque)
        return diff_ligne == diff_colonne and diff_ligne > 0

    def obtenir_symbole(self) -> str:
        """Symbole pour l'affichage (différent du pion simple)"""
        return "0" if self._couleur == Couleur.BLANC else "Y"

    def get_type(self) -> TypePion:
        """Retourne le type de pion"""
        return TypePion.DAME
