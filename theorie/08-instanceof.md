# L'opérateur instanceof

## Qu'est-ce que instanceof ?

L'opérateur **instanceof** permet de vérifier si un objet est une **instance** d'une classe particulière ou d'une de ses classes parentes. C'est un outil essentiel pour le **polymorphisme** et la gestion dynamique des types.

### Syntaxe de base

```
objet instanceof NomClasse
```

Retourne :
- **vrai** si l'objet est une instance de la classe (ou d'une classe fille)
- **faux** sinon

### Analogie

Pensez à une question du type "Est-ce que... ?" :
- "Est-ce qu'un chien **est-un** animal ?" → **Oui**
- "Est-ce qu'un chien **est-un** mammifère ?" → **Oui**
- "Est-ce qu'un chien **est-une** voiture ?" → **Non**

```
chien instanceof Animal      // vrai
chien instanceof Mammifere   // vrai
chien instanceof Voiture     // faux
```

## Utilisation basique

```
classe Animal:
    nom
    
    constructeur(nom):
        ce.nom ← nom

classe Chien hérite de Animal:
    race
    
    constructeur(nom, race):
        parent.constructeur(nom)
        ce.race ← race
    
    aboyer():
        afficher("Wouf!")

classe Chat hérite de Animal:
    couleur
    
    constructeur(nom, couleur):
        parent.constructeur(nom)
        ce.couleur ← couleur
    
    miauler():
        afficher("Miaou!")

// Création d'objets
chien ← nouveau Chien("Rex", "Berger Allemand")
chat ← nouveau Chat("Minou", "Tigré")

// Tests avec instanceof
afficher(chien instanceof Chien)    // vrai
afficher(chien instanceof Animal)   // vrai (héritage)
afficher(chien instanceof Chat)     // faux

afficher(chat instanceof Chat)      // vrai
afficher(chat instanceof Animal)    // vrai (héritage)
afficher(chat instanceof Chien)     // faux
```

## Vérification de type avec hiérarchie

L'opérateur **instanceof** vérifie toute la **chaîne d'héritage**.

```
classe EtreVivant:
    respirer()

classe Animal hérite de EtreVivant:
    manger()

classe Mammifere hérite de Animal:
    allaiter()

classe Chien hérite de Mammifere:
    aboyer()

// Création d'un chien
monChien ← nouveau Chien()

// Tests dans toute la hiérarchie
afficher(monChien instanceof Chien)         // vrai ✅
afficher(monChien instanceof Mammifere)     // vrai ✅
afficher(monChien instanceof Animal)        // vrai ✅
afficher(monChien instanceof EtreVivant)    // vrai ✅

// Test avec une classe non liée
afficher(monChien instanceof Voiture)       // faux ❌
```

## Polymorphisme et instanceof

L'opérateur **instanceof** est particulièrement utile avec le polymorphisme pour déterminer le type réel d'un objet.

```
classe Forme:
    couleur
    
    constructeur(couleur):
        ce.couleur ← couleur
    
    abstraite calculerAire()

classe Cercle hérite de Forme:
    rayon
    
    constructeur(couleur, rayon):
        parent.constructeur(couleur)
        ce.rayon ← rayon
    
    calculerAire():
        retourner 3.14159 * ce.rayon * ce.rayon

classe Rectangle hérite de Forme:
    longueur
    largeur
    
    constructeur(couleur, longueur, largeur):
        parent.constructeur(couleur)
        ce.longueur ← longueur
        ce.largeur ← largeur
    
    calculerAire():
        retourner ce.longueur * ce.largeur

classe Triangle hérite de Forme:
    base
    hauteur
    
    constructeur(couleur, base, hauteur):
        parent.constructeur(couleur)
        ce.base ← base
        ce.hauteur ← hauteur
    
    calculerAire():
        retourner (ce.base * ce.hauteur) / 2

// Collection polymorphique
formes ← [
    nouveau Cercle("rouge", 5),
    nouveau Rectangle("bleu", 4, 6),
    nouveau Triangle("vert", 3, 4),
    nouveau Cercle("jaune", 3)
]

// Traitement selon le type
pour chaque forme dans formes:
    afficher("Couleur: " + forme.couleur)
    afficher("Aire: " + forme.calculerAire())
    
    // Actions spécifiques selon le type
    si forme instanceof Cercle:
        afficher("  → C'est un cercle de rayon " + forme.rayon)
    sinon si forme instanceof Rectangle:
        afficher("  → C'est un rectangle " + forme.longueur + "x" + forme.largeur)
    sinon si forme instanceof Triangle:
        afficher("  → C'est un triangle")
```

## Downcasting sécurisé

Le **downcasting** consiste à traiter un objet de type parent comme son type réel (plus spécifique). **instanceof** permet de le faire de manière sécurisée.

```
classe Animal:
    nom
    
    constructeur(nom):
        ce.nom ← nom
    
    faireDuBruit():
        afficher("...")

classe Chien hérite de Animal:
    race
    
    constructeur(nom, race):
        parent.constructeur(nom)
        ce.race ← race
    
    faireDuBruit():
        afficher("Wouf!")
    
    rapporterBalle():
        afficher(ce.nom + " rapporte la balle!")

classe Chat hérite de Animal:
    couleur
    
    constructeur(nom, couleur):
        parent.constructeur(nom)
        ce.couleur ← couleur
    
    faireDuBruit():
        afficher("Miaou!")
    
    grimperArbre():
        afficher(ce.nom + " grimpe à l'arbre!")

// Liste polymorphique (type Animal)
animaux: Animal[] ← [
    nouveau Chien("Rex", "Labrador"),
    nouveau Chat("Minou", "Roux"),
    nouveau Chien("Max", "Berger")
]

// Traitement avec downcasting sécurisé
pour chaque animal dans animaux:
    animal.faireDuBruit()  // Polymorphisme
    
    // Appeler des méthodes spécifiques
    si animal instanceof Chien:
        chien: Chien ← (Chien) animal  // Downcasting
        chien.rapporterBalle()
    
    sinon si animal instanceof Chat:
        chat: Chat ← (Chat) animal  // Downcasting
        chat.grimperArbre()

// Affiche :
// Wouf!
// Rex rapporte la balle!
// Miaou!
// Minou grimpe à l'arbre!
// Wouf!
// Max rapporte la balle!
```

## Filtrage par type

**instanceof** est idéal pour filtrer une collection selon le type.

```
classe Produit:
    nom
    prix

classe Livre hérite de Produit:
    auteur
    isbn

classe DVD hérite de Produit:
    durée
    réalisateur

classe Vêtement hérite de Produit:
    taille
    couleur

// Collection mixte
produits ← [
    nouveau Livre("POO en pratique", 29.99, "John Doe", "123-456"),
    nouveau DVD("Film X", 15.99, 120, "Jane Smith"),
    nouveau Vêtement("T-Shirt", 19.99, "M", "Bleu"),
    nouveau Livre("Clean Code", 39.99, "Robert Martin", "789-012"),
    nouveau Vêtement("Pantalon", 49.99, "L", "Noir")
]

// Fonction de filtrage
fonction filtrerParType(collection, typeRecherché):
    résultat ← []
    pour chaque élément dans collection:
        si élément instanceof typeRecherché:
            résultat.ajouter(élément)
    retourner résultat

// Filtrer les livres
livres ← filtrerParType(produits, Livre)
afficher("Nombre de livres : " + livres.taille())  // 2

// Filtrer les vêtements
vêtements ← filtrerParType(produits, Vêtement)
afficher("Nombre de vêtements : " + vêtements.taille())  // 2
```

## Validation des paramètres

**instanceof** permet de valider les types des paramètres dans les fonctions.

```
classe GestionnaireAnimaux:
    animaux: Animal[]
    
    constructeur():
        ce.animaux ← []
    
    ajouterAnimal(animal):
        // Validation du type
        si animal instanceof Animal:
            ce.animaux.ajouter(animal)
            afficher("✅ Animal ajouté : " + animal.nom)
        sinon:
            erreur("❌ Seuls les objets de type Animal sont acceptés")
    
    ajouterChien(chien):
        // Validation plus spécifique
        si chien instanceof Chien:
            ce.animaux.ajouter(chien)
            afficher("✅ Chien ajouté : " + chien.nom)
        sinon:
            erreur("❌ Seuls les objets de type Chien sont acceptés")

// Utilisation
gestionnaire ← nouveau GestionnaireAnimaux()

chien ← nouveau Chien("Rex", "Labrador")
chat ← nouveau Chat("Minou", "Siamois")
voiture ← nouveau Voiture("Renault", "Clio")

gestionnaire.ajouterAnimal(chien)     // ✅ OK
gestionnaire.ajouterAnimal(chat)      // ✅ OK
gestionnaire.ajouterAnimal(voiture)   // ❌ Erreur

gestionnaire.ajouterChien(chien)      // ✅ OK
gestionnaire.ajouterChien(chat)       // ❌ Erreur (pas un Chien)
```

## Pattern Visitor avec instanceof

Le pattern Visitor utilise souvent **instanceof** pour traiter différents types.

```
classe Document:
    titre

classe DocumentTexte hérite de Document:
    contenu
    nombreMots

classe DocumentImage hérite de Document:
    largeur
    hauteur
    format

classe DocumentPDF hérite de Document:
    nombrePages
    tailleFichier

classe ExportateurDocument:
    
    exporter(document):
        si document instanceof DocumentTexte:
            retourner ce.exporterTexte(document)
        sinon si document instanceof DocumentImage:
            retourner ce.exporterImage(document)
        sinon si document instanceof DocumentPDF:
            retourner ce.exporterPDF(document)
        sinon:
            erreur("Type de document non supporté")
    
    exporterTexte(doc: DocumentTexte):
        afficher("Export texte : " + doc.titre)
        afficher("Nombre de mots : " + doc.nombreMots)
        retourner "texte_export"
    
    exporterImage(doc: DocumentImage):
        afficher("Export image : " + doc.titre)
        afficher("Format : " + doc.format)
        retourner "image_export"
    
    exporterPDF(doc: DocumentPDF):
        afficher("Export PDF : " + doc.titre)
        afficher("Pages : " + doc.nombrePages)
        retourner "pdf_export"

// Utilisation
documents ← [
    nouveau DocumentTexte("Rapport", "...", 500),
    nouveau DocumentImage("Photo", 1920, 1080, "PNG"),
    nouveau DocumentPDF("Manuel", 150, 2048)
]

exportateur ← nouveau ExportateurDocument()

pour chaque doc dans documents:
    exportateur.exporter(doc)
```

## Comptage par type

```
classe Statistiques:
    
    static compterParType(collection, type):
        compteur ← 0
        pour chaque élément dans collection:
            si élément instanceof type:
                compteur ← compteur + 1
        retourner compteur
    
    static obtenirStatistiques(collection):
        stats ← {}
        
        // Compter chaque type
        typesVus ← []
        pour chaque élément dans collection:
            typeElement ← typeOf(élément)
            si typeElement non dans typesVus:
                typesVus.ajouter(typeElement)
                stats[typeElement.nom] ← Statistiques.compterParType(collection, typeElement)
        
        retourner stats

// Utilisation avec notre collection de produits
stats ← Statistiques.obtenirStatistiques(produits)
afficher(stats)
// {
//   "Livre": 2,
//   "DVD": 1,
//   "Vêtement": 2
// }
```

## Interfaces et instanceof

**instanceof** fonctionne aussi avec les interfaces (dans les langages qui les supportent explicitement).

```
interface Volant:
    décoller()
    atterrir()
    voler()

interface Nageur:
    nager()

classe Canard implémente Volant, Nageur:
    décoller():
        afficher("Le canard décolle")
    
    atterrir():
        afficher("Le canard atterrit")
    
    voler():
        afficher("Le canard vole")
    
    nager():
        afficher("Le canard nage")

classe Poisson implémente Nageur:
    nager():
        afficher("Le poisson nage")

classe Avion implémente Volant:
    décoller():
        afficher("L'avion décolle")
    
    atterrir():
        afficher("L'avion atterrit")
    
    voler():
        afficher("L'avion vole")

// Tests
canard ← nouveau Canard()
poisson ← nouveau Poisson()
avion ← nouveau Avion()

afficher(canard instanceof Volant)    // vrai ✅
afficher(canard instanceof Nageur)    // vrai ✅

afficher(poisson instanceof Volant)   // faux ❌
afficher(poisson instanceof Nageur)   // vrai ✅

afficher(avion instanceof Volant)     // vrai ✅
afficher(avion instanceof Nageur)     // faux ❌

// Fonction polymorphique
fonction faireDécoller(objet):
    si objet instanceof Volant:
        objet.décoller()
        objet.voler()
        objet.atterrir()
    sinon:
        afficher("Cet objet ne peut pas voler")

faireDécoller(canard)   // ✅ Fonctionne
faireDécoller(avion)    // ✅ Fonctionne
faireDécoller(poisson)  // ❌ Message d'erreur
```

## Vérification de null

**instanceof** retourne toujours **faux** pour les valeurs null.

```
animal ← null

afficher(animal instanceof Animal)  // faux (null n'est instance d'aucune classe)

// Vérification sécurisée
si animal != null et animal instanceof Chien:
    chien ← (Chien) animal
    chien.aboyer()
```

## Bonnes pratiques

### ✅ À faire

1. **Utilisez instanceof pour le downcasting sécurisé**
```
si animal instanceof Chien:
    chien ← (Chien) animal
    chien.rapporterBalle()
```

2. **Utilisez instanceof pour la validation de paramètres**
```
fonction traiter(objet):
    si objet instanceof TypeAttendu:
        // Traitement
    sinon:
        erreur("Type invalide")
```

3. **Utilisez instanceof avec le polymorphisme**
```
pour chaque forme dans formes:
    si forme instanceof Cercle:
        // Traitement spécifique aux cercles
```

4. **Vérifiez null avant instanceof**
```
si objet != null et objet instanceof MaClasse:
    // Traitement sécurisé
```

### ❌ À éviter

1. **N'abusez pas de instanceof (anti-pattern)**
```
// ❌ Mauvais : trop de instanceof indique un mauvais design
fonction traiter(animal):
    si animal instanceof Chien:
        // Code pour chien
    sinon si animal instanceof Chat:
        // Code pour chat
    sinon si animal instanceof Oiseau:
        // Code pour oiseau
    // ... 50 autres types

// ✅ Meilleur : utilisez le polymorphisme
fonction traiter(animal):
    animal.faireDuBruit()  // Chaque classe implémente sa propre version
```

2. **N'utilisez pas instanceof à la place de l'interface appropriée**
```
// ❌ Mauvais
si objet instanceof Chien ou objet instanceof Chat ou objet instanceof Oiseau:
    objet.faireDuBruit()

// ✅ Meilleur
interface Animal:
    faireDuBruit()

si objet instanceof Animal:
    objet.faireDuBruit()
```

3. **N'utilisez pas instanceof pour la logique métier principale**
```
// ❌ Mauvais design
fonction calculerPrix(produit):
    si produit instanceof Livre:
        retourner produit.prix * 0.9  // 10% de réduction
    sinon si produit instanceof DVD:
        retourner produit.prix * 0.8  // 20% de réduction
    sinon:
        retourner produit.prix

// ✅ Meilleur : méthode polymorphique
classe Produit:
    abstraite calculerPrixFinal()

classe Livre:
    calculerPrixFinal():
        retourner ce.prix * 0.9

classe DVD:
    calculerPrixFinal():
        retourner ce.prix * 0.8
```

## Alternatives à instanceof

### 1. Polymorphisme (préféré)

```
// Au lieu de :
si animal instanceof Chien:
    afficher("Wouf!")
sinon si animal instanceof Chat:
    afficher("Miaou!")

// Préférez :
animal.faireDuBruit()  // Chaque classe implémente sa version
```

### 2. Pattern Strategy

```
// Au lieu de vérifier le type
si exportateur instanceof ExportateurPDF:
    // ...
sinon si exportateur instanceof ExportateurWord:
    // ...

// Utilisez une interface commune
interface Exportateur:
    exporter(document)
```

### 3. Pattern Visitor (pour les cas complexes)

```
interface VisiteurDocument:
    visiter(doc: DocumentTexte)
    visiter(doc: DocumentImage)
    visiter(doc: DocumentPDF)

classe Document:
    accepter(visiteur: VisiteurDocument)
```

## Exemple complet : Système de paiement

```
classe MoyenPaiement:
    montant

classe CarteBancaire hérite de MoyenPaiement:
    numéro
    dateExpiration
    
    constructeur(montant, numéro, dateExpiration):
        ce.montant ← montant
        ce.numéro ← numéro
        ce.dateExpiration ← dateExpiration

classe PayPal hérite de MoyenPaiement:
    email
    
    constructeur(montant, email):
        ce.montant ← montant
        ce.email ← email

classe Espèces hérite de MoyenPaiement:
    montantDonné
    
    constructeur(montant, montantDonné):
        ce.montant ← montant
        ce.montantDonné ← montantDonné

classe ProcesseurPaiement:
    
    traiterPaiement(moyenPaiement):
        // Validation du type
        si non (moyenPaiement instanceof MoyenPaiement):
            erreur("Moyen de paiement invalide")
        
        afficher("Traitement de " + moyenPaiement.montant + "€")
        
        // Traitement spécifique selon le type
        si moyenPaiement instanceof CarteBancaire:
            retourner ce.traiterCarte(moyenPaiement)
        
        sinon si moyenPaiement instanceof PayPal:
            retourner ce.traiterPayPal(moyenPaiement)
        
        sinon si moyenPaiement instanceof Espèces:
            retourner ce.traiterEspèces(moyenPaiement)
        
        sinon:
            erreur("Type de paiement non supporté")
    
    traiterCarte(carte: CarteBancaire):
        afficher("💳 Paiement par carte : " + carte.numéro)
        // Vérifier la date d'expiration
        si carte.dateExpiration < dateActuelle():
            retourner faux, "Carte expirée"
        retourner vrai, "Paiement accepté"
    
    traiterPayPal(paypal: PayPal):
        afficher("💰 Paiement PayPal : " + paypal.email)
        // Appel API PayPal
        retourner vrai, "Paiement accepté"
    
    traiterEspèces(espèces: Espèces):
        afficher("💵 Paiement en espèces")
        monnaieRendue ← espèces.montantDonné - espèces.montant
        si monnaieRendue < 0:
            retourner faux, "Montant insuffisant"
        afficher("Monnaie à rendre : " + monnaieRendue + "€")
        retourner vrai, "Paiement accepté"

// Utilisation
processeur ← nouveau ProcesseurPaiement()

paiements ← [
    nouveau CarteBancaire(49.99, "1234-5678-9012-3456", "12/2027"),
    nouveau PayPal(29.99, "user@example.com"),
    nouveau Espèces(15.50, 20.00)
]

pour chaque paiement dans paiements:
    succès, message ← processeur.traiterPaiement(paiement)
    afficher(message)
```

## Cas d'usage légitimes

**instanceof** est approprié dans ces situations :

1. **Downcasting dans du code polymorphique**
2. **Validation de paramètres dans les API publiques**
3. **Filtrage de collections hétérogènes**
4. **Implémentation de visiteurs ou d'exportateurs**
5. **Gestion d'événements avec types variés**
6. **Désérialisation de données**
7. **Interopérabilité avec du code externe**

## Conclusion

L'opérateur **instanceof** est un outil puissant pour :
- **Vérifier** le type d'un objet à l'exécution
- **Sécuriser** le downcasting
- **Filtrer** des collections par type
- **Valider** les paramètres de méthodes
- **Gérer** le polymorphisme dynamique

**Règles d'or** :
- Utilisez instanceof **avec modération**
- Préférez le **polymorphisme** quand c'est possible
- Utilisez instanceof pour des cas **légitimes** (validation, downcasting)
- N'en faites pas la **base de votre logique métier**

Un usage excessif de **instanceof** est souvent le signe d'un mauvais design orienté objet. Dans la plupart des cas, le polymorphisme offre une meilleure solution.
