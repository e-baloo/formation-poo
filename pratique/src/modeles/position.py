"""
Classe Position - Représente une position sur le plateau
"""


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
        return self.get_ligne() == other.get_ligne() and self.get_colonne() == other.get_colonne()

    def __str__(self) -> str:
        """Représentation en chaîne"""
        return self.vers_notation()

    def __repr__(self) -> str:
        """Représentation pour le débogage"""
        return f"Position({self.__ligne}, {self.__colonne})"
