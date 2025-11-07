"""
05 – Encapsulation : CompteBancaire
"""


class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0.0) -> None:
        self.titulaire = titulaire        # public
        self._solde = solde_initial       # protected (convention)
        self.__historique = []            # private (name mangling)

    def deposer(self, montant: float) -> None:
        if montant <= 0:
            raise ValueError("Montant de dépôt invalide")
        self._solde += montant
        self.__historique.append(("DEPOT", montant))

    def retirer(self, montant: float) -> bool:
        if montant <= 0 or montant > self._solde:
            return False
        self._solde -= montant
        self.__historique.append(("RETRAIT", montant))
        return True

    def get_solde(self) -> float:
        return self._solde

    def _etat_interne(self):  # méthode 'protected'
        return f"Historique: {len(self.__historique)} opérations"

    def get_historique(self):  # expose lecture contrôlée
        return list(self.__historique)


if __name__ == "__main__":
    c = CompteBancaire("Alice", 100)
    c.deposer(50)
    c.retirer(30)
    print("Solde:", c.get_solde())
    print(c._etat_interne())
    print("Historique:", c.get_historique())
