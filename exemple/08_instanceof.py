"""
08 – instanceof (isinstance en Python) : hiérarchie Animal
"""


class Animal:
    def parler(self) -> str:
        return "(silence)"


class Chien(Animal):
    def parler(self) -> str:
        return "Wouf"


class Chat(Animal):
    def parler(self) -> str:
        return "Miaou"


def faire_parler(animal: Animal) -> None:
    if isinstance(animal, Chien):
        print("C'est un chien ->", animal.parler())
    elif isinstance(animal, Chat):
        print("C'est un chat ->", animal.parler())
    else:
        print("Animal inconnu ->", animal.parler())


if __name__ == "__main__":
    animaux = [Animal(), Chien(), Chat()]
    for instance in animaux:
        faire_parler(instance)
