"""
Classe ValidateurMouvement - Validation des règles du jeu
"""

from typing import Tuple
from ..modeles import Position, Mouvement, APion
from .plateau import Plateau


class ValidateurMouvement:
    """
    Valide les mouvements selon les règles des dames.

    Démontre :
    - Séparation des responsabilités
    - Méthodes statiques
    - Logique métier complexe
    """

    @staticmethod
    def est_mouvement_valide(plateau: Plateau, mouvement: Mouvement) -> Tuple[bool, str]:
        """
        Valide un mouvement complet.

        :param plateau: Plateau de jeu
        :param mouvement: Mouvement à valider
        :return: (valide, message_erreur)
        """
        # Vérifier qu'il y a un pion à la position de départ
        pion = plateau.get_pion_a(mouvement.get_depart())
        if pion is None:
            return False, "Aucun pion à cette position"

        # Vérifier que la destination est libre
        if not plateau.est_case_libre(mouvement.get_arrivee()):
            return False, "La case de destination est occupée"

        # Calculs de base
        depart = mouvement.get_depart()
        arrivee = mouvement.get_arrivee()
        diff_ligne = arrivee.get_ligne() - depart.get_ligne()
        diff_colonne = arrivee.get_colonne() - depart.get_colonne()

        # 1) Tentative de capture (saut de 2 cases ou plus en diagonale)
        if abs(diff_ligne) >= 2 and abs(diff_ligne) == abs(diff_colonne):
            return ValidateurMouvement.__valider_capture(plateau, pion, mouvement)

        # 2) Déplacement simple (une seule case en diagonale) -> selon le type de pion
        if abs(diff_ligne) == 1 and abs(diff_colonne) == 1:
            if pion.peut_se_deplacer_vers(arrivee):
                return True, ""
            return False, "Mouvement invalide pour ce type de pion"

        # 3) Sinon, mouvement invalide
        return False, "Mouvement invalide"

    @staticmethod
    def __valider_capture(plateau: Plateau, pion: APion, mouvement: Mouvement) -> Tuple[bool, str]:
        """
        Valide une capture éventuelle.
        Méthode privée.

        :param plateau: Plateau de jeu
        :param pion: Pion qui se déplace
        :param mouvement: Mouvement à valider
        :return: (valide, message_erreur)
        """
        depart = mouvement.get_depart()
        arrivee = mouvement.get_arrivee()

        diff_ligne = arrivee.get_ligne() - depart.get_ligne()
        diff_colonne = arrivee.get_colonne() - depart.get_colonne()

        # Déplacement simple (1 case en diagonale)
        if abs(diff_ligne) == 1 and abs(diff_colonne) == 1:
            return True, ""

        # Capture (2 cases ou plus en diagonale)
        if abs(diff_ligne) >= 2 and abs(diff_ligne) == abs(diff_colonne):
            # Calculer la position du pion à capturer (au milieu)
            ligne_milieu = depart.get_ligne() + (diff_ligne // abs(diff_ligne))
            colonne_milieu = depart.get_colonne() + (diff_colonne // abs(diff_colonne))
            position_milieu = Position(ligne_milieu, colonne_milieu)

            pion_capture = plateau.get_pion_a(position_milieu)

            if pion_capture is None:
                return False, "Pas de pion à capturer"

            if pion_capture.get_couleur() == pion.get_couleur():
                return False, "On ne peut pas capturer ses propres pions"

            # Enregistrer la position du pion capturé
            mouvement.set_pion_capture(position_milieu)
            return True, ""

        return False, "Mouvement invalide"
