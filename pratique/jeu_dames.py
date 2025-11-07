"""
Jeu de Dames - Exemple pratique de POO
======================================

Ce programme implémente un jeu de Dames complet en Python,
démontrant tous les concepts de la POO :
- Classes et objets
- Héritage
- Interfaces (via classes abstraites)
- Encapsulation (public, protected, private)
- Getters et setters
- Polymorphisme

Pour jouer :
1. Exécutez : python jeu_dames.py
2. Entrez les coordonnées au format : A1 B2 (de la case A1 vers B2)
3. Les pions blancs commencent en bas (lignes 1-4)
4. Les pions noirs commencent en haut (lignes 6-10)
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Tuple
from enum import Enum
import os


# ============================================================================
# ÉNUMÉRATIONS (Types énumérés)
# ============================================================================

class Couleur(Enum):
    """Énumération des couleurs des pions"""
    BLANC = "blanc"
    NOIR = "noir"


class TypePion(Enum):
    """Énumération des types de pions"""
    SIMPLE = "simple"
    DAME = "dame"


# ============================================================================
# POSITION - Classe simple pour encapsuler les coordonnées
# ============================================================================

class Position:
    """
    Représente une position sur le plateau (ligne, colonne).

    Démontre :
    - Encapsulation (attributs privés)
    - Getters/Setters avec validation
    - Méthodes utilitaires
    """

    def __init__(self, ligne: int, colonne: int):
        """
        Constructeur avec validation.

        :param ligne: Numéro de ligne (1-10)
        :param colonne: Numéro de colonne (1-10)
        """
        self.__ligne = 0
        self.__colonne = 0
        self.set_ligne(ligne)
        self.set_colonne(colonne)

    # ---- Getters ----
    def get_ligne(self) -> int:
        """Retourne le numéro de ligne"""
        return self.__ligne

    def get_colonne(self) -> int:
        """Retourne le numéro de colonne"""
        return self.__colonne

    # ---- Setters avec validation ----
    def set_ligne(self, ligne: int):
        """
        Définit la ligne avec validation.

        :param ligne: Numéro de ligne (1-10)
        :raises ValueError: Si la ligne est invalide
        """
        if 1 <= ligne <= 10:
            self.__ligne = ligne
        else:
            raise ValueError(
                f"Ligne invalide : {ligne}. Doit être entre 1 et 10.")

    def set_colonne(self, colonne: int):
        """
        Définit la colonne avec validation.

        :param colonne: Numéro de colonne (1-10)
        :raises ValueError: Si la colonne est invalide
        """
        if 1 <= colonne <= 10:
            self.__colonne = colonne
        else:
            raise ValueError(
                f"Colonne invalide : {colonne}. Doit être entre 1 et 10.")

    # ---- Méthodes utilitaires ----
    def est_valide(self) -> bool:
        """Vérifie si la position est valide sur le plateau"""
        return 1 <= self.__ligne <= 10 and 1 <= self.__colonne <= 10

    def vers_notation(self) -> str:
        """
        Convertit en notation d'échecs (ex: A1, B2).

        :return: Notation de la position (ex: "A1")
        """
        colonne_lettre = chr(ord('A') + self.__colonne - 1)
        return f"{colonne_lettre}{self.__ligne}"

    @staticmethod
    def depuis_notation(notation: str) -> 'Position':
        """
        Crée une Position depuis une notation (ex: "A1").

        :param notation: Notation de la position (ex: "A1")
        :return: Objet Position
        """
        notation = notation.upper().strip()
        if len(notation) < 2:
            raise ValueError(f"Notation invalide : {notation}")

        colonne_lettre = notation[0]
        ligne_str = notation[1:]

        colonne = ord(colonne_lettre) - ord('A') + 1
        ligne = int(ligne_str)

        return Position(ligne, colonne)

    def __eq__(self, other) -> bool:
        """Comparaison d'égalité entre positions"""
        if not isinstance(other, Position):
            return False
        return self.__ligne == other.__ligne and self.__colonne == other.__colonne

    def __str__(self) -> str:
        """Représentation en chaîne"""
        return self.vers_notation()

    def __repr__(self) -> str:
        """Représentation pour le débogage"""
        return f"Position({self.__ligne}, {self.__colonne})"


# ============================================================================
# CLASSE ABSTRAITE PION - Démontre l'héritage et l'abstraction
# ============================================================================

class Pion(ABC):
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


# ============================================================================
# PION SIMPLE - Héritage de Pion
# ============================================================================

class PionSimple(Pion):
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


# ============================================================================
# DAME - Héritage de Pion avec comportement spécialisé
# ============================================================================

class Dame(Pion):
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
        return "◯" if self._couleur == Couleur.BLANC else "●"

    def get_type(self) -> TypePion:
        """Retourne le type de pion"""
        return TypePion.DAME


# ============================================================================
# MOUVEMENT - Encapsulation d'une action de jeu
# ============================================================================

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


# ============================================================================
# PLATEAU - Gestion du plateau de jeu
# ============================================================================

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
        self.__pions: List[Pion] = []
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
    def get_pion_a(self, position: Position) -> Optional[Pion]:
        """
        Retourne le pion à une position donnée.

        :param position: Position à vérifier
        :return: Le pion s'il existe, None sinon
        """
        for pion in self.__pions:
            if pion.est_en_jeu() and pion.get_position() == position:
                return pion
        return None

    def get_pions_couleur(self, couleur: Couleur) -> List[Pion]:
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


# ============================================================================
# VALIDATEUR DE MOUVEMENT - Logique de validation séparée
# ============================================================================

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

        # Vérifier que le pion peut se déplacer vers cette position
        if not pion.peut_se_deplacer_vers(mouvement.get_arrivee()):
            return False, "Mouvement invalide pour ce type de pion"

        # Vérifier les captures
        return ValidateurMouvement.__valider_capture(plateau, pion, mouvement)

    @staticmethod
    def __valider_capture(plateau: Plateau, pion: Pion, mouvement: Mouvement) -> Tuple[bool, str]:
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


# ============================================================================
# JEU - Contrôleur principal
# ============================================================================

class Jeu:
    """
    Contrôleur principal du jeu de dames.

    Démontre :
    - Composition (a un Plateau)
    - Gestion de l'état du jeu
    - Boucle de jeu
    - Interface utilisateur
    """

    def __init__(self):
        """Initialise une nouvelle partie"""
        self.__plateau = Plateau()
        self.__joueur_actuel = Couleur.BLANC
        self.__partie_terminee = False
        self.__nombre_coups = 0

    def __effacer_ecran(self):
        """Efface l'écran du terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def __afficher_entete(self):
        """Affiche l'en-tête du jeu"""
        print("=" * 50)
        print(" " * 15 + "🎮 JEU DE DAMES 🎮")
        print("=" * 50)
        print(f"Tour n°{self.__nombre_coups + 1}")
        print(f"Joueur actuel : {self.__joueur_actuel.value.upper()}")
        print()
        blancs = self.__plateau.compter_pions(Couleur.BLANC)
        noirs = self.__plateau.compter_pions(Couleur.NOIR)
        print(f"Pions blancs (⚪): {blancs}  |  Pions noirs (⚫): {noirs}")
        print()

    def __changer_joueur(self):
        """Change le joueur actuel"""
        self.__joueur_actuel = Couleur.NOIR if self.__joueur_actuel == Couleur.BLANC else Couleur.BLANC

    def __verifier_fin_partie(self) -> bool:
        """
        Vérifie si la partie est terminée.

        :return: True si la partie est terminée
        """
        blancs = self.__plateau.compter_pions(Couleur.BLANC)
        noirs = self.__plateau.compter_pions(Couleur.NOIR)

        if blancs == 0:
            print("\n🏆 Les NOIRS ont gagné !")
            return True

        if noirs == 0:
            print("\n🏆 Les BLANCS ont gagné !")
            return True

        return False

    def __demander_mouvement(self) -> Optional[Mouvement]:
        """
        Demande au joueur de saisir un mouvement.

        :return: Mouvement saisi ou None si abandon
        """
        try:
            entree = input(
                "\nEntrez votre mouvement (ex: A3 B4) ou 'q' pour quitter : ").strip()

            if entree.lower() == 'q':
                return None

            parties = entree.split()
            if len(parties) != 2:
                print("❌ Format invalide. Utilisez : A3 B4")
                return self.__demander_mouvement()

            depart = Position.depuis_notation(parties[0])
            arrivee = Position.depuis_notation(parties[1])

            # Vérifier que le pion appartient au joueur actuel
            pion = self.__plateau.get_pion_a(depart)
            if pion is None:
                print("❌ Aucun pion à cette position")
                return self.__demander_mouvement()

            if pion.get_couleur() != self.__joueur_actuel:
                print(
                    f"❌ Ce pion ne vous appartient pas ! C'est au tour des {self.__joueur_actuel.value}s")
                return self.__demander_mouvement()

            return Mouvement(depart, arrivee)

        except (ValueError, IndexError) as e:
            print(f"❌ Erreur : {e}")
            return self.__demander_mouvement()

    def jouer(self):
        """Lance la boucle de jeu principale"""
        print("\n🎮 Bienvenue dans le jeu de Dames ! 🎮\n")
        print("Instructions :")
        print("- Les pions blancs (⚪) commencent en bas")
        print("- Les pions noirs (⚫) commencent en haut")
        print("- Entrez les mouvements au format : A3 B4")
        print("- Un pion devient une DAME (◯/●) en atteignant le bord opposé")
        print("- Tapez 'q' pour quitter\n")
        input("Appuyez sur Entrée pour commencer...")

        while not self.__partie_terminee:
            self.__effacer_ecran()
            self.__afficher_entete()
            self.__plateau.afficher()

            # Vérifier la fin de partie
            if self.__verifier_fin_partie():
                self.__partie_terminee = True
                break

            # Demander le mouvement
            mouvement = self.__demander_mouvement()

            if mouvement is None:
                print("\n👋 Partie abandonnée.")
                break

            # Valider le mouvement
            valide, message = ValidateurMouvement.est_mouvement_valide(
                self.__plateau, mouvement)

            if not valide:
                print(f"\n❌ {message}")
                input("Appuyez sur Entrée pour continuer...")
                continue

            # Effectuer le mouvement
            if self.__plateau.deplacer_pion(mouvement):
                if mouvement.est_capture():
                    print(f"\n💥 Capture effectuée !")
                self.__nombre_coups += 1
                self.__changer_joueur()
            else:
                print("\n❌ Erreur lors du déplacement")
                input("Appuyez sur Entrée pour continuer...")

        print(f"\n\nPartie terminée en {self.__nombre_coups} coups.")
        print("Merci d'avoir joué ! 👋\n")


# ============================================================================
# POINT D'ENTRÉE
# ============================================================================

def main():
    """Point d'entrée du programme"""
    jeu = Jeu()
    jeu.jouer()


if __name__ == "__main__":
    main()
