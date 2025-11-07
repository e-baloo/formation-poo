"""
07 – Static : compteur d'instances + utilitaires
"""
from __future__ import annotations


class Voiture:
    compteur = 0  # attribut de classe

    def __init__(self, marque: str) -> None:
        self.marque = marque
        Voiture.compteur += 1

    @classmethod
    def nombre_instances(cls) -> int:
        return cls.compteur

    @staticmethod
    def formater_marque(marque: str) -> str:
        return marque.upper()

    def __repr__(self) -> str:
        return f"Voiture({self.marque})"


class MathUtil:
    @staticmethod
    def carre(x: float) -> float:
        return x * x

    @staticmethod
    def moyenne(vals: list[float]) -> float:
        return sum(vals) / len(vals) if vals else 0.0


if __name__ == "__main__":
    v1 = Voiture("Renault")
    v2 = Voiture("Peugeot")
    print("Instances:", Voiture.nombre_instances())
    print("Marque formatée:", Voiture.formater_marque("citroen"))
    print("Carre 5:", MathUtil.carre(5))
    print("Moyenne:", MathUtil.moyenne([10, 15, 20]))
