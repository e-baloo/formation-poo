"""
04 – Interfaces (contrats) avec ABC : MoyenDePaiement
"""
from abc import ABC, abstractmethod


class MoyenDePaiement(ABC):
    @abstractmethod
    def payer(self, montant: float) -> None:
        pass


class CB(MoyenDePaiement):
    def payer(self, montant: float) -> None:
        print(f"Paiement CB accepté : {montant:.2f}€")


class Paypal(MoyenDePaiement):
    def payer(self, montant: float) -> None:
        print(f"Paiement PayPal confirmé : {montant:.2f}€")


class Crypto(MoyenDePaiement):
    def payer(self, montant: float) -> None:
        print(f"Paiement Crypto validé : {montant:.2f}€")


def traiter_paiement(process: MoyenDePaiement, montant: float) -> None:
    process.payer(montant)  # polymorphisme


if __name__ == "__main__":
    traiter_paiement(CB(), 49.99)
    traiter_paiement(Paypal(), 12.5)
    traiter_paiement(Crypto(), 1000)
