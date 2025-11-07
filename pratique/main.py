#!/usr/bin/env python3
"""
Jeu de Dames - Point d'entrée principal
======================================

Ce programme implémente un jeu de Dames complet en Python,
démontrant tous les concepts de la POO.

Pour jouer :
1. Exécutez : python main.py
2. Entrez les coordonnées au format : A1 B2 (de la case A1 vers B2)
3. Les pions blancs commencent en bas (lignes 1-4)
4. Les pions noirs commencent en haut (lignes 6-10)
"""

from src.interface import Jeu


def main():
    """Point d'entrée du programme"""
    jeu = Jeu()
    jeu.jouer()


if __name__ == "__main__":
    main()
