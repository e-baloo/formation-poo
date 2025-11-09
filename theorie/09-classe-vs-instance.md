# Classe vs Instance de classe

Comprendre la différence entre une CLASSE et une INSTANCE est fondamental en POO. Voici une synthèse claire, avec pseudo‑code indépendant du langage.

## Définition rapide
- Classe = le PLAN, le MODÈLE, le CONTRAT (ce qu’un objet « devrait être et faire »)
- Instance = l’OBJET CONCRET créé à partir de ce plan (avec sa propre identité et ses propres valeurs)

## Analogie
- Classe = plan d’une maison (plans architecturaux, règles, matériaux)
- Instance = une maison construite concrètement à une adresse donnée

## Vocabulaire
- Définir/declarer une classe → on écrit le contrat
- Instancier → on crée un objet à partir de la classe (via un constructeur)
- Objet = instance d’une classe

## Exemple simple (pseudo‑code)

```pseudo
Classe Personne
    Attributs (état) : nom, age
    Méthodes (comportements) : sePresenter()

    Constructeur(nom, age)
        this.nom = nom
        this.age = age

    Méthode sePresenter()
        Afficher "Je m'appelle " + this.nom + ", j'ai " + this.age + " ans."

# Création d'instances (objets concrets)
p1 = new Personne("Alice", 30)
p2 = new Personne("Bob", 25)

# Appels de méthodes (chaque objet utilise SON propre état)
p1.sePresenter()   # -> Je m'appelle Alice, j'ai 30 ans.
p2.sePresenter()   # -> Je m'appelle Bob, j'ai 25 ans.
```

Ici, `Personne` est la CLASSE. `p1` et `p2` sont des INSTANCES différentes partageant le même contrat mais ayant des valeurs distinctes.

## Identité, Égalité, État
- Identité (ID) : chaque instance a une identité unique (adresse, référence, handle)
- Égalité : deux instances peuvent être « égales » par valeur (mêmes attributs) tout en restant des objets différents
- État : l’ensemble des valeurs des attributs à un instant T

```pseudo
p1 = new Personne("Alice", 30)
p2 = new Personne("Alice", 30)

(p1 == p2) ?  # selon les langages :
    # vrai si comparaison par valeur redéfinie
    # faux si comparaison par identité par défaut
```

## Méthodes d’INSTANCE vs de CLASSE
- Méthode d’instance : agit sur l’état d’un objet précis (utilise `this`)
- Méthode de classe (statique) : attachée à la classe elle‑même, pas à une instance (ne connaît pas `this`)

```pseudo
Classe Compteur
    Statique total = 0

    Constructeur()
        Compteur.total = Compteur.total + 1

    Statique getTotal()
        Retourner Compteur.total

c1 = new Compteur()
c2 = new Compteur()
Compteur.getTotal()  # -> 2
```

`total` appartient à la CLASSE (partagé par toutes les instances). L’état d’instance (non statique) appartient à CHAQUE objet.

## Constructeur : du contrat à l’objet
Le constructeur est la « porte d’entrée » pour passer du monde de la classe au monde de l’instance.

```pseudo
Classe Rectangle
    largeur, hauteur

    Constructeur(L, H)
        this.largeur = L
        this.hauteur = H

    aire()
        Retourner this.largeur * this.hauteur

r = new Rectangle(5, 3)   # r est une instance
r.aire()                  # calcule selon l'état propre de r
```

## Mémoire et cycle de vie (vue conceptuelle)
- Classe : chargée une fois (métadonnées, méthodes, attributs statiques)
- Instance : allouée pour chaque `new` ; détruite/libérée quand plus référencée

## UML (mini notation)
```
+-------------------+
| Personne          |  <<classe>>
+-------------------+
| - nom : String    |
| - age : int       |
+-------------------+
| + sePresenter()   |
+-------------------+

p1:Personne    p2:Personne      <<instances>>
nom="Alice"    nom="Bob"
age=30         age=25
```

## Erreurs fréquentes
- Confondre la classe (définition) et l’objet (utilisation)
- Mettre des données variables dans des attributs statiques (partagés)
- Penser qu’une méthode statique peut accéder au `this` d’une instance

## Bonnes pratiques
- Utiliser des constructeurs (ou des fabriques) pour garantir des instances valides
- Distinguer clairement attributs d’instance vs attributs/méthodes de classe
- Documenter le contrat de la classe (responsabilités, invariants)

## Exercices
1. Créer une classe `Compte` avec `solde` et `deposer(m)`/`retirer(m)` puis instancier 2 comptes aux soldes indépendants.
2. Ajouter un compteur statique `nbComptes` qui augmente à chaque nouvelle instance et l’afficher via une méthode de classe.
3. Créer deux instances avec les mêmes valeurs et comparer selon identité vs valeur (en redéfinissant l’égalité si le langage le permet).
