"""
Classe Plateau - Gestion du plateau de jeu
"""

from typing import Optional, List
from ..enums import Couleur
from ..modeles import Position, Mouvement, APion, PionSimple, Dame


class Plateau:
    """
    Représente le plateau de jeu 10x10.

    Démontre :
    - Composition (a des Pions)
    - Gestion de collection d'objets
    - Logique métier complexe
    - Méthodes privées pour l'organisation
    """

    TAILLE = 10

    def __init__(self):
        """Initialise un plateau vide"""
        self.__pions: List[APion] = []
        self.__initialiser_plateau()

    # ---- Méthode privée d'initialisation ----
    def __initialiser_plateau(self):
        """
        Initialise le plateau avec les pions de départ.
        Méthode privée (convention __ en Python).
        """
        # Pions blancs (lignes 1 à 4)
        for ligne in range(1, 5):
            for colonne in range(1, 11):
                if self.__est_case_jouable(ligne, colonne):
                    position = Position(ligne, colonne)
                    self.__pions.append(PionSimple(Couleur.BLANC, position))

        # Pions noirs (lignes 7 à 10)
        for ligne in range(7, 11):
            for colonne in range(1, 11):
                if self.__est_case_jouable(ligne, colonne):
                    position = Position(ligne, colonne)
                    self.__pions.append(PionSimple(Couleur.NOIR, position))

    @staticmethod
    def __est_case_jouable(ligne: int, colonne: int) -> bool:
        """
        Vérifie si une case est jouable (cases noires).

        :param ligne: Numéro de ligne
        :param colonne: Numéro de colonne
        :return: True si la case est jouable
        """
        return (ligne + colonne) % 2 == 0

    # ---- Getters ----
    def get_pion_a(self, position: Position) -> Optional[APion]:
        """
        Retourne le pion à une position donnée.

        :param position: Position à vérifier
        :return: Le pion s'il existe, None sinon
        """
        for pion in self.__pions:
            if pion.est_en_jeu() and pion.get_position() == position:
                return pion
        return None

    def get_pions_couleur(self, couleur: Couleur) -> List[APion]:
        """
        Retourne tous les pions d'une couleur.

        :param couleur: Couleur des pions
        :return: Liste des pions de cette couleur
        """
        return [p for p in self.__pions if p.est_en_jeu() and p.get_couleur() == couleur]

    # ---- Méthodes de manipulation ----
    def deplacer_pion(self, mouvement: Mouvement) -> bool:
        """
        Déplace un pion sur le plateau.

        :param mouvement: Mouvement à effectuer
        :return: True si le déplacement a réussi
        """
        pion = self.get_pion_a(mouvement.get_depart())

        if pion is None:
            return False

        # Capturer un pion si nécessaire
        if mouvement.est_capture() and mouvement.get_pion_capture():
            pion_capture = self.get_pion_a(mouvement.get_pion_capture())
            if pion_capture:
                pion_capture.capturer()

        # Déplacer le pion
        pion.set_position(mouvement.get_arrivee())

        # Promotion en dame si nécessaire
        if isinstance(pion, PionSimple) and pion.peut_etre_promu():
            self.__promouvoir_en_dame(pion)

        return True

    def __promouvoir_en_dame(self, pion: PionSimple):
        """
        Transforme un pion simple en dame.
        Méthode privée.

        :param pion: Pion à promouvoir
        """
        # Retirer le pion simple
        self.__pions.remove(pion)

        # Ajouter une dame à la même position
        dame = Dame(pion.get_couleur(), pion.get_position())
        self.__pions.append(dame)

        print(f"🎉 {pion.get_couleur().value.upper()} : Promotion en DAME !")

    def est_case_libre(self, position: Position) -> bool:
        """
        Vérifie si une case est libre.

        :param position: Position à vérifier
        :return: True si la case est libre
        """
        return self.get_pion_a(position) is None

    # ---- Affichage ----
    def afficher(self):
        """Affiche le plateau dans le terminal"""
        print("\n   " + " ".join([chr(65 + i) for i in range(10)]))
        print("  +" + "-" * 20 + "+")

        for ligne in range(10, 0, -1):
            ligne_str = f"{ligne:2}|"

            for colonne in range(1, 11):
                position = Position(ligne, colonne)
                pion = self.get_pion_a(position)

                if pion:
                    ligne_str += pion.obtenir_symbole() + " "
                elif self.__est_case_jouable(ligne, colonne):
                    ligne_str += "· "
                else:
                    ligne_str += "  "

            ligne_str += f"|{ligne}"
            print(ligne_str)

        print("  +" + "-" * 20 + "+")
        print("   " + " ".join([chr(65 + i) for i in range(10)]))

    def compter_pions(self, couleur: Couleur) -> int:
        """
        Compte le nombre de pions d'une couleur.

        :param couleur: Couleur à compter
        :return: Nombre de pions
        """
        return len(self.get_pions_couleur(couleur))
