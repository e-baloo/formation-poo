"""
Classe Jeu - Contrôleur principal du jeu de Dames
"""

import os
from typing import Optional
from ..enums import Couleur
from ..modeles import Position, Mouvement
from ..logique import Plateau, ValidateurMouvement


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
        print(f"Pions blancs (O): {blancs}  |  Pions noirs (X): {noirs}")
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
        print("- Les pions blancs (O) commencent en bas")
        print("- Les pions noirs (X) commencent en haut")
        print("- Entrez les mouvements au format : A3 B4")
        print("- Un pion devient une DAME (0/Y) en atteignant le bord opposé")
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
                    print("\n💥 Capture effectuée !")
                self.__nombre_coups += 1
                self.__changer_joueur()
            else:
                print("\n❌ Erreur lors du déplacement")
                input("Appuyez sur Entrée pour continuer...")

        print(f"\n\nPartie terminée en {self.__nombre_coups} coups.")
        print("Merci d'avoir joué ! 👋\n")
