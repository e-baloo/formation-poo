# La Classe : un contrat

## Qu'est-ce qu'une classe ?

Une **classe** est un modèle, un plan de construction, un "moule" qui définit :
- Les **données** (attributs, propriétés) que contiendront les objets
- Les **comportements** (méthodes, fonctions) que pourront effectuer les objets

### Analogie

Pensez à une classe comme à un **plan architectural** :
- Le plan d'une maison (classe) définit : nombre de pièces, superficie, étages, etc.
- Chaque maison construite selon ce plan (objet) est unique : adresse différente, couleur différente, habitants différents

```
Plan Maison (classe) → Maison 123 rue X (objet 1)
                     → Maison 456 rue Y (objet 2)
                     → Maison 789 rue Z (objet 3)
```

## Structure d'une classe

```
classe NomDeLaClasse:
    
    // Attributs (données)
    attribut1
    attribut2
    attribut3
    
    // Constructeur (initialisation)
    constructeur(paramètres):
        initialiser les attributs
    
    // Méthodes (comportements)
    méthode1():
        // actions
    
    méthode2(paramètres):
        // actions
```

## Exemple : Classe Voiture

```
classe Voiture:
    
    // Attributs
    marque
    modèle
    couleur
    vitesseActuelle
    moteurAllumé
    
    // Constructeur
    constructeur(marque, modèle, couleur):
        ce.marque ← marque
        ce.modèle ← modèle
        ce.couleur ← couleur
        ce.vitesseActuelle ← 0
        ce.moteurAllumé ← faux
    
    // Méthodes
    démarrer():
        si non ce.moteurAllumé:
            ce.moteurAllumé ← vrai
            afficher("Le moteur démarre")
    
    arrêter():
        si ce.moteurAllumé:
            ce.moteurAllumé ← faux
            ce.vitesseActuelle ← 0
            afficher("Le moteur s'arrête")
    
    accélérer(augmentation):
        si ce.moteurAllumé:
            ce.vitesseActuelle ← ce.vitesseActuelle + augmentation
    
    freiner(diminution):
        ce.vitesseActuelle ← max(0, ce.vitesseActuelle - diminution)
    
    obtenirVitesse():
        retourner ce.vitesseActuelle
```

## Instanciation : Créer des objets

Une fois la classe définie, on peut créer des **instances** (objets) :

```
// Création de trois voitures différentes
voiture1 ← nouveau Voiture("Renault", "Clio", "rouge")
voiture2 ← nouveau Voiture("Peugeot", "208", "bleue")
voiture3 ← nouveau Voiture("Citroën", "C3", "blanche")

// Chaque objet a son propre état
voiture1.démarrer()
voiture1.accélérer(50)

voiture2.démarrer()
voiture2.accélérer(30)

// voiture1.vitesseActuelle = 50
// voiture2.vitesseActuelle = 30
// voiture3.vitesseActuelle = 0 (pas démarrée)
```

## La classe comme contrat

Une classe définit un **contrat** qui garantit :

### 1. Qu'est-ce que l'objet POSSÈDE (attributs)

```
classe Étudiant:
    nom
    prénom
    numéroÉtudiant
    notes[]
```

Tout objet de type `Étudiant` aura nécessairement ces informations.

### 2. Ce que l'objet PEUT FAIRE (méthodes)

```
classe Étudiant:
    // ...
    
    ajouterNote(note)
    calculerMoyenne()
    afficherInformations()
```

Tout objet de type `Étudiant` pourra effectuer ces actions.

### 3. Comment INTERAGIR avec l'objet

```
// Le contrat dit : "Pour créer un étudiant, donnez-moi nom et prénom"
étudiant1 ← nouveau Étudiant("Dupont", "Jean")

// Le contrat dit : "Vous pouvez ajouter une note"
étudiant1.ajouterNote(15)

// Le contrat dit : "Vous pouvez calculer la moyenne"
moyenne ← étudiant1.calculerMoyenne()
```

## Cohésion : Une classe, une responsabilité

Une bonne classe doit avoir une **responsabilité unique** et claire.

### ✅ Bonne cohésion :

```
classe CompteBancaire:
    solde
    titulaire
    
    déposer(montant)
    retirer(montant)
    consulterSolde()
```

Cette classe gère **uniquement** les opérations sur un compte bancaire.

### ❌ Mauvaise cohésion :

```
classe CompteBancaire:
    solde
    titulaire
    
    déposer(montant)
    retirer(montant)
    envoyerEmail()          // ← Pas la responsabilité du compte
    générerRapportPDF()     // ← Pas la responsabilité du compte
    vérifierMétéo()         // ← Pas la responsabilité du compte
```

Ces méthodes devraient être dans d'autres classes.

## État et comportement

### État (attributs)

L'**état** d'un objet est l'ensemble des valeurs de ses attributs à un instant donné.

```
classe Lampe:
    allumée
    intensité
    couleur
```

État de lampe1 à 10h : `{allumée: vrai, intensité: 80, couleur: "blanc"}`
État de lampe1 à 11h : `{allumée: faux, intensité: 0, couleur: "blanc"}`

### Comportement (méthodes)

Le **comportement** définit comment l'objet réagit aux actions et comment son état peut changer.

```
classe Lampe:
    allumée ← faux
    intensité ← 0
    couleur ← "blanc"
    
    allumer():
        ce.allumée ← vrai
        ce.intensité ← 100
    
    éteindre():
        ce.allumée ← faux
        ce.intensité ← 0
    
    réglerIntensité(valeur):
        si ce.allumée et valeur >= 0 et valeur <= 100:
            ce.intensité ← valeur
```

## Le mot-clé "ce" (self, this)

Le mot-clé `ce` (souvent appelé `self` ou `this`) fait référence à **l'instance actuelle** de l'objet.

```
classe Personne:
    nom
    
    constructeur(nom):
        ce.nom ← nom        // "ce.nom" = attribut de l'objet
                            // "nom" = paramètre du constructeur
    
    sePresenter():
        afficher("Je m'appelle " + ce.nom)

// Utilisation
personne1 ← nouveau Personne("Alice")
personne2 ← nouveau Personne("Bob")

personne1.sePresenter()  // "ce" pointe vers personne1
// Affiche: "Je m'appelle Alice"

personne2.sePresenter()  // "ce" pointe vers personne2
// Affiche: "Je m'appelle Bob"
```

## Attributs de classe vs attributs d'instance

### Attributs d'instance

Chaque objet a sa propre copie.

```
classe Voiture:
    couleur  // ← Attribut d'instance
    
v1 ← nouveau Voiture()
v1.couleur ← "rouge"

v2 ← nouveau Voiture()
v2.couleur ← "bleu"

// v1 et v2 ont des couleurs différentes
```

### Attributs de classe

Partagé par toutes les instances de la classe.

```
classe Voiture:
    nombreRoues ← 4  // ← Attribut de classe (toutes les voitures ont 4 roues)
    couleur          // ← Attribut d'instance
```

## Exemple complet : Classe Rectangle

```
classe Rectangle:
    
    // Attributs d'instance
    longueur
    largeur
    
    // Constructeur
    constructeur(longueur, largeur):
        si longueur > 0 et largeur > 0:
            ce.longueur ← longueur
            ce.largeur ← largeur
        sinon:
            erreur("Les dimensions doivent être positives")
    
    // Méthodes
    calculerAire():
        retourner ce.longueur * ce.largeur
    
    calculerPérimètre():
        retourner 2 * (ce.longueur + ce.largeur)
    
    estCarré():
        retourner ce.longueur == ce.largeur
    
    redimensionner(nouvelleLongueur, nouvelleLargeur):
        si nouvelleLongueur > 0 et nouvelleLargeur > 0:
            ce.longueur ← nouvelleLongueur
            ce.largeur ← nouvelleLargeur
    
    afficher():
        afficher("Rectangle: " + ce.longueur + " x " + ce.largeur)
        afficher("Aire: " + ce.calculerAire())
        afficher("Périmètre: " + ce.calculerPérimètre())

// Utilisation
rect1 ← nouveau Rectangle(5, 3)
rect1.afficher()
// Rectangle: 5 x 3
// Aire: 15
// Périmètre: 16

si rect1.estCarré():
    afficher("C'est un carré")
sinon:
    afficher("Ce n'est pas un carré")

rect1.redimensionner(4, 4)
si rect1.estCarré():
    afficher("Maintenant c'est un carré")
```

## Conclusion

La classe est le fondement de la POO :
- Elle définit un **modèle** pour créer des objets
- Elle établit un **contrat** clair sur ce que les objets peuvent faire
- Elle regroupe **données** et **comportements** liés
- Elle permet de créer **plusieurs instances** indépendantes
- Elle favorise la **cohésion** et l'organisation du code

Une classe bien conçue est :
- **Cohérente** : une seule responsabilité
- **Complète** : tous les comportements nécessaires
- **Claire** : facile à comprendre et à utiliser
- **Correcte** : garantit la validité des données
