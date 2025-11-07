"""
02 – La classe comme contrat : exemple Voiture
"""


class Voiture:
    def __init__(self, marque: str, modele: str, annee: int) -> None:
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self._kilometrage = 0  # convention protected

    def rouler(self, km: int) -> None:
        if km < 0:
            raise ValueError("Kilométrage négatif")
        self._kilometrage += km

    def info(self) -> str:
        return f"{self.marque} {self.modele} ({self.annee}) - {self._kilometrage} km"


if __name__ == "__main__":
    v = Voiture("Renault", "Clio", 2020)
    v.rouler(150)
    v.rouler(32)
    print(v.info())
