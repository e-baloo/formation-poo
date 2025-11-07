# L'héritage

## Qu'est-ce que l'héritage ?

L'**héritage** est un mécanisme qui permet à une classe (classe fille, sous-classe) de **réutiliser** et **étendre** les caractéristiques d'une autre classe (classe parente, super-classe).

### Principe fondamental

```
classe Parent:
    attributs et méthodes communes

classe Enfant hérite de Parent:
    hérite de tout ce que Parent possède
    + peut ajouter ses propres attributs et méthodes
    + peut modifier (redéfinir) certaines méthodes
```

### Analogie

Pensez à la classification biologique :
- **Animal** → a des caractéristiques générales (respire, se nourrit, se déplace)
  - **Mammifère** → hérite de Animal + spécificités (allaite ses petits, sang chaud)
    - **Chien** → hérite de Mammifère + spécificités (aboie, remue la queue)
    - **Chat** → hérite de Mammifère + spécificités (miaule, ronronne)

## Syntaxe de base

```
classe ClasseParente:
    attributsCommuns
    méthodesCommunes()

classe ClasseEnfant hérite de ClasseParente:
    attributsSpécifiques
    méthodesSpécifiques()
```

## Exemple simple : Véhicules

```
classe Vehicule:
    marque
    modèle
    vitesseActuelle
    
    constructeur(marque, modèle):
        ce.marque ← marque
        ce.modèle ← modèle
        ce.vitesseActuelle ← 0
    
    accélérer(vitesse):
        ce.vitesseActuelle ← ce.vitesseActuelle + vitesse
    
    freiner():
        ce.vitesseActuelle ← 0
    
    afficherInfo():
        afficher(ce.marque + " " + ce.modèle)

classe Voiture hérite de Vehicule:
    nombrePortes
    
    constructeur(marque, modèle, nombrePortes):
        parent.constructeur(marque, modèle)  // Appel du constructeur parent
        ce.nombrePortes ← nombrePortes
    
    ouvrirCoffre():
        afficher("Coffre ouvert")

classe Moto hérite de Vehicule:
    typeMoto  // (sportive, routière, etc.)
    
    constructeur(marque, modèle, typeMoto):
        parent.constructeur(marque, modèle)
        ce.typeMoto ← typeMoto
    
    faireCavalier():
        afficher("Roue arrière levée!")
```

### Utilisation

```
voiture ← nouveau Voiture("Renault", "Clio", 5)
moto ← nouveau Moto("Yamaha", "MT-07", "sportive")

// Méthodes héritées de Vehicule
voiture.accélérer(50)
moto.accélérer(80)

// Méthodes spécifiques
voiture.ouvrirCoffre()    // OK pour Voiture
moto.faireCavalier()      // OK pour Moto

// voiture.faireCavalier()  ← ERREUR : Voiture n'a pas cette méthode
// moto.ouvrirCoffre()      ← ERREUR : Moto n'a pas cette méthode
```

## Relation "est-un"

L'héritage représente une relation **"est-un"** (is-a) :
- Un Chien **est-un** Animal
- Une Voiture **est-un** Véhicule
- Un Carré **est-un** Rectangle

```
classe Animal:
    nom
    manger()
    dormir()

classe Chien hérite de Animal:
    aboyer()

// Un Chien EST-UN Animal
// Donc un Chien peut faire tout ce qu'un Animal fait
// + ses comportements spécifiques
```

⚠️ **Attention** : Ne pas confondre avec "a-un" (composition) :
- Une Voiture **a-une** Roue (pas d'héritage, mais composition)
- Une Voiture **est-un** Véhicule (héritage correct)

## Redéfinition (Override)

Une classe enfant peut **redéfinir** une méthode héritée pour l'adapter à ses besoins.

```
classe Animal:
    nom
    
    constructeur(nom):
        ce.nom ← nom
    
    faireDuBruit():
        afficher("L'animal fait du bruit")
    
    sePresenter():
        afficher("Je suis " + ce.nom)

classe Chien hérite de Animal:
    
    // Redéfinition de faireDuBruit
    faireDuBruit():
        afficher(ce.nom + " aboie: Wouf Wouf!")

classe Chat hérite de Animal:
    
    // Redéfinition de faireDuBruit
    faireDuBruit():
        afficher(ce.nom + " miaule: Miaou!")

classe Vache hérite de Animal:
    
    // Redéfinition de faireDuBruit
    faireDuBruit():
        afficher(ce.nom + " meugle: Meuh!")

// Utilisation
chien ← nouveau Chien("Rex")
chat ← nouveau Chat("Minou")
vache ← nouveau Vache("Marguerite")

chien.faireDuBruit()  // Affiche: "Rex aboie: Wouf Wouf!"
chat.faireDuBruit()   // Affiche: "Minou miaule: Miaou!"
vache.faireDuBruit()  // Affiche: "Marguerite meugle: Meuh!"

// Méthode non redéfinie : même comportement pour tous
chien.sePresenter()   // Affiche: "Je suis Rex"
chat.sePresenter()    // Affiche: "Je suis Minou"
```

## Appel à la méthode parente

Parfois, on veut **étendre** une méthode plutôt que la remplacer complètement.

```
classe Employe:
    nom
    salaire
    
    constructeur(nom, salaire):
        ce.nom ← nom
        ce.salaire ← salaire
    
    afficherInfos():
        afficher("Employé: " + ce.nom)
        afficher("Salaire: " + ce.salaire)

classe Manager hérite de Employe:
    équipe[]  // Liste des employés gérés
    
    constructeur(nom, salaire):
        parent.constructeur(nom, salaire)
        ce.équipe ← []
    
    ajouterMembre(employé):
        ce.équipe.ajouter(employé)
    
    // On veut afficher les infos de base + l'équipe
    afficherInfos():
        parent.afficherInfos()  // Appel de la méthode parente
        afficher("Nombre de personnes dans l'équipe: " + ce.équipe.taille())

// Utilisation
manager ← nouveau Manager("Alice", 5000)
manager.ajouterMembre(nouveau Employe("Bob", 3000))
manager.ajouterMembre(nouveau Employe("Charlie", 3200))

manager.afficherInfos()
// Affiche:
// Employé: Alice
// Salaire: 5000
// Nombre de personnes dans l'équipe: 2
```

## Héritage multiple niveaux

On peut avoir plusieurs niveaux d'héritage.

```
classe EtreVivant:
    respirer()
    seReproduire()

classe Animal hérite de EtreVivant:
    seDeplacer()
    manger()

classe Mammifere hérite de Animal:
    allaiter()

classe Chien hérite de Mammifere:
    aboyer()

// Un Chien hérite de toute la hiérarchie
chien ← nouveau Chien()
chien.respirer()     // de EtreVivant
chien.seDeplacer()   // de Animal
chien.allaiter()     // de Mammifere
chien.aboyer()       // de Chien
```

## Classe abstraite

Une **classe abstraite** est une classe qui ne peut pas être instanciée directement. Elle sert uniquement de modèle pour ses classes filles.

```
classe abstraite Forme:
    couleur
    
    constructeur(couleur):
        ce.couleur ← couleur
    
    // Méthode concrète (implémentée)
    afficherCouleur():
        afficher("Couleur: " + ce.couleur)
    
    // Méthode abstraite (doit être implémentée par les classes filles)
    abstraite calculerAire()
    abstraite calculerPérimètre()

classe Rectangle hérite de Forme:
    longueur
    largeur
    
    constructeur(couleur, longueur, largeur):
        parent.constructeur(couleur)
        ce.longueur ← longueur
        ce.largeur ← largeur
    
    // Implémentation obligatoire
    calculerAire():
        retourner ce.longueur * ce.largeur
    
    calculerPérimètre():
        retourner 2 * (ce.longueur + ce.largeur)

classe Cercle hérite de Forme:
    rayon
    
    constructeur(couleur, rayon):
        parent.constructeur(couleur)
        ce.rayon ← rayon
    
    // Implémentation obligatoire
    calculerAire():
        retourner 3.14159 * ce.rayon * ce.rayon
    
    calculerPérimètre():
        retourner 2 * 3.14159 * ce.rayon

// Utilisation
// forme ← nouveau Forme("rouge")  ← ERREUR : Forme est abstraite

rectangle ← nouveau Rectangle("bleu", 5, 3)
cercle ← nouveau Cercle("vert", 4)

afficher(rectangle.calculerAire())     // 15
afficher(cercle.calculerPérimètre())   // 25.13...
```

## Polymorphisme et héritage

Le polymorphisme permet de traiter des objets de classes différentes de manière uniforme, via leur classe parente.

```
classe Animal:
    nom
    
    constructeur(nom):
        ce.nom ← nom
    
    faireDuBruit():
        // Méthode de base

classe Chien hérite de Animal:
    faireDuBruit():
        afficher("Wouf!")

classe Chat hérite de Animal:
    faireDuBruit():
        afficher("Miaou!")

classe Oiseau hérite de Animal:
    faireDuBruit():
        afficher("Cui cui!")

// Polymorphisme en action
fonction faireParlerLesAnimaux(animaux[]):
    pour chaque animal dans animaux:
        animal.faireDuBruit()  // Appelle la bonne méthode selon le type réel

// Utilisation
zoo ← [
    nouveau Chien("Rex"),
    nouveau Chat("Félix"),
    nouveau Oiseau("Titi"),
    nouveau Chien("Max")
]

faireParlerLesAnimaux(zoo)
// Affiche:
// Wouf!
// Miaou!
// Cui cui!
// Wouf!
```

## Quand utiliser l'héritage ?

### ✅ Utiliser l'héritage quand :

1. Il y a une vraie relation **"est-un"**
2. Les classes partagent des **attributs et comportements communs**
3. On veut **spécialiser** une classe existante
4. On veut bénéficier du **polymorphisme**

### ❌ Éviter l'héritage quand :

1. La relation est plutôt **"a-un"** (utiliser la composition)
2. On veut juste **réutiliser du code** sans lien logique
3. La hiérarchie devient **trop profonde** (plus de 3-4 niveaux)
4. Les classes filles redéfinissent **trop de méthodes** (mauvais signe)

## Exemple complet : Système de personnages

```
classe abstraite Personnage:
    nom
    pointsDeVie
    pointsDeVieMax
    
    constructeur(nom, pointsDeVieMax):
        ce.nom ← nom
        ce.pointsDeVieMax ← pointsDeVieMax
        ce.pointsDeVie ← pointsDeVieMax
    
    recevoirDegats(degats):
        ce.pointsDeVie ← max(0, ce.pointsDeVie - degats)
        si ce.pointsDeVie == 0:
            afficher(ce.nom + " est K.O.")
    
    soigner(soin):
        ce.pointsDeVie ← min(ce.pointsDeVieMax, ce.pointsDeVie + soin)
    
    estEnVie():
        retourner ce.pointsDeVie > 0
    
    abstraite attaquer(cible)

classe Guerrier hérite de Personnage:
    force
    
    constructeur(nom):
        parent.constructeur(nom, 150)
        ce.force ← 20
    
    attaquer(cible):
        degats ← ce.force
        afficher(ce.nom + " attaque avec son épée!")
        cible.recevoirDegats(degats)

classe Mage hérite de Personnage:
    mana
    puissanceMagique
    
    constructeur(nom):
        parent.constructeur(nom, 80)
        ce.mana ← 100
        ce.puissanceMagique ← 30
    
    attaquer(cible):
        si ce.mana >= 10:
            ce.mana ← ce.mana - 10
            degats ← ce.puissanceMagique
            afficher(ce.nom + " lance une boule de feu!")
            cible.recevoirDegats(degats)
        sinon:
            afficher(ce.nom + " n'a plus de mana!")

classe Archer hérite de Personnage:
    précision
    flèches
    
    constructeur(nom):
        parent.constructeur(nom, 100)
        ce.précision ← 15
        ce.flèches ← 20
    
    attaquer(cible):
        si ce.flèches > 0:
            ce.flèches ← ce.flèches - 1
            degats ← ce.précision
            afficher(ce.nom + " tire une flèche!")
            cible.recevoirDegats(degats)
        sinon:
            afficher(ce.nom + " n'a plus de flèches!")

// Combat
guerrier ← nouveau Guerrier("Conan")
mage ← nouveau Mage("Gandalf")
archer ← nouveau Archer("Legolas")

guerrier.attaquer(mage)
mage.attaquer(guerrier)
archer.attaquer(guerrier)
```

## Conclusion

L'héritage est un pilier de la POO qui permet :
- La **réutilisation** du code
- La **spécialisation** des comportements
- L'organisation **hiérarchique** des concepts
- Le **polymorphisme**

Utilisé correctement, l'héritage rend le code plus maintenable et expressif. Mais attention à ne pas en abuser : parfois, la composition est plus appropriée que l'héritage.
