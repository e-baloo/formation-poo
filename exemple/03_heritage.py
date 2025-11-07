"""
03 – Héritage : Vehicule -> Voiture/Moto avec override
"""


class Vehicule:
    def __init__(self, marque: str) -> None:
        self.marque = marque

    def demarrer(self) -> str:
        return "Le véhicule démarre"


class Voiture(Vehicule):
    def demarrer(self) -> str:  # override
        return f"La voiture {self.marque} démarre en douceur"


class Moto(Vehicule):
    def demarrer(self) -> str:  # override
        return f"La moto {self.marque} vrombit au démarrage"


if __name__ == "__main__":
    v = Voiture("Peugeot")
    m = Moto("Yamaha")
    print(v.demarrer())
    print(m.demarrer())
