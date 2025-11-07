# Les Getters et Setters

## Qu'est-ce qu'un Getter et un Setter ?

Les **getters** et **setters** sont des méthodes qui permettent de **lire** (get) et **modifier** (set) les attributs privés d'une classe de manière contrôlée.

```
classe Exemple:
    private attribut
    
    // Getter : lire la valeur
    public obtenirAttribut():
        retourner ce.attribut
    
    // Setter : modifier la valeur
    public définirAttribut(valeur):
        ce.attribut ← valeur
```

### Pourquoi ne pas rendre les attributs publics ?

```
// ❌ Sans getters/setters
classe Personne:
    public age

personne ← nouveau Personne()
personne.age ← -5        // Aucune validation !
personne.age ← "abc"     // Type invalide !

// ✅ Avec getters/setters
classe Personne:
    private age
    
    public définirAge(nouvelAge):
        si nouvelAge >= 0 et nouvelAge <= 150:
            ce.age ← nouvelAge
        sinon:
            erreur("Âge invalide")
    
    public obtenirAge():
        retourner ce.age

personne ← nouveau Personne()
personne.définirAge(-5)  // Erreur : validation
personne.définirAge(25)  // ✅ OK
```

## Getter (Accesseur)

Un **getter** permet de **lire** la valeur d'un attribut privé.

```
classe Rectangle:
    private longueur
    private largeur
    
    public constructeur(longueur, largeur):
        ce.longueur ← longueur
        ce.largeur ← largeur
    
    // Getters
    public obtenirLongueur():
        retourner ce.longueur
    
    public obtenirLargeur():
        retourner ce.largeur
    
    public obtenirAire():
        retourner ce.longueur * ce.largeur

// Utilisation
rect ← nouveau Rectangle(5, 3)
afficher(rect.obtenirLongueur())  // 5
afficher(rect.obtenirAire())      // 15
```

### Types de getters

#### 1. Getter simple (lecture directe)

```
classe Personne:
    private nom
    
    public obtenirNom():
        retourner ce.nom
```

#### 2. Getter calculé (propriété dérivée)

```
classe Rectangle:
    private longueur
    private largeur
    
    // Propriété calculée à la demande
    public obtenirAire():
        retourner ce.longueur * ce.largeur
    
    public obtenirPerimetre():
        retourner 2 * (ce.longueur + ce.largeur)
```

#### 3. Getter avec transformation

```
classe Personne:
    private nom
    private prenom
    
    public obtenirNomComplet():
        retourner ce.prenom + " " + ce.nom
    
    public obtenirInitiales():
        retourner ce.prenom[0] + "." + ce.nom[0] + "."

personne ← nouveau Personne()
personne.nom ← "Dupont"
personne.prenom ← "Jean"

afficher(personne.obtenirNomComplet())  // "Jean Dupont"
afficher(personne.obtenirInitiales())    // "J.D."
```

#### 4. Getter avec copie défensive

```
classe ClasseExamen:
    private notes[]
    
    // ❌ Mauvais : retourne la référence directe
    public obtenirNotesMauvais():
        retourner ce.notes  // Modifiable depuis l'extérieur !
    
    // ✅ Bon : retourne une copie
    public obtenirNotes():
        retourner copier(ce.notes)  // L'original est protégé

classe ← nouveau ClasseExamen()
notes ← classe.obtenirNotes()
notes.ajouter(20)  // Modifie la copie, pas l'original
```

## Setter (Mutateur)

Un **setter** permet de **modifier** la valeur d'un attribut privé avec validation.

```
classe CompteBancaire:
    private solde
    
    public constructeur():
        ce.solde ← 0
    
    // Setter avec validation
    public définirSolde(nouveauSolde):
        si nouveauSolde >= 0:
            ce.solde ← nouveauSolde
        sinon:
            erreur("Le solde ne peut pas être négatif")
    
    public obtenirSolde():
        retourner ce.solde

// Utilisation
compte ← nouveau CompteBancaire()
compte.définirSolde(1000)  // ✅ OK
compte.définirSolde(-500)  // ❌ Erreur
```

### Types de setters

#### 1. Setter avec validation

```
classe Personne:
    private age
    private email
    
    public définirAge(nouvelAge):
        si nouvelAge >= 0 et nouvelAge <= 150:
            ce.age ← nouvelAge
        sinon:
            erreur("Âge invalide : doit être entre 0 et 150")
    
    public définirEmail(nouvelEmail):
        si nouvelEmail.contient("@") et nouvelEmail.contient("."):
            ce.email ← nouvelEmail
        sinon:
            erreur("Email invalide")
```

#### 2. Setter avec transformation

```
classe Produit:
    private nom
    private prix
    
    public définirNom(nouveauNom):
        // Normalisation : majuscules
        ce.nom ← nouveauNom.enMajuscules()
    
    public définirPrix(nouveauPrix):
        // Arrondi à 2 décimales
        ce.prix ← arrondir(nouveauPrix, 2)

produit ← nouveau Produit()
produit.définirNom("ordinateur")
afficher(produit.obtenirNom())  // "ORDINATEUR"

produit.définirPrix(19.999)
afficher(produit.obtenirPrix())  // 20.00
```

#### 3. Setter avec effet de bord

```
classe Lumiere:
    private intensité
    private allumée
    
    public définirIntensité(nouvelleIntensité):
        si nouvelleIntensité >= 0 et nouvelleIntensité <= 100:
            ce.intensité ← nouvelleIntensité
            
            // Effet de bord : allumer automatiquement si intensité > 0
            si nouvelleIntensité > 0:
                ce.allumée ← vrai
            sinon:
                ce.allumée ← faux

lumiere ← nouveau Lumiere()
lumiere.définirIntensité(50)
afficher(lumiere.estAllumée())  // vrai
```

#### 4. Setter avec notification

```
classe Observable:
    private valeur
    private observateurs[]
    
    public définirValeur(nouvelleValeur):
        ancienneValeur ← ce.valeur
        ce.valeur ← nouvelleValeur
        
        // Notifier tous les observateurs du changement
        pour chaque obs dans ce.observateurs:
            obs.notifier(ancienneValeur, nouvelleValeur)
```

## Attributs en lecture seule

Parfois, on veut qu'un attribut soit **lisible** mais **non modifiable** après l'initialisation.

```
classe Personne:
    private numeroSecuritéSociale
    private nom
    
    public constructeur(numero, nom):
        ce.numeroSecuritéSociale ← numero
        ce.nom ← nom
    
    // Getter uniquement (pas de setter)
    public obtenirNumero():
        retourner ce.numeroSecuritéSociale
    
    // Getter et setter pour le nom
    public obtenirNom():
        retourner ce.nom
    
    public définirNom(nouveauNom):
        ce.nom ← nouveauNom

personne ← nouveau Personne("1234567890", "Dupont")

// ✅ Lecture possible
afficher(personne.obtenirNumero())  // OK

// ❌ Modification impossible (pas de setter)
// personne.définirNumero("xxx")  // Méthode inexistante

// ✅ Modification du nom possible
personne.définirNom("Martin")  // OK
```

## Attributs calculés (sans stockage)

Certains attributs sont calculés à la demande sans être stockés.

```
classe Cercle:
    private rayon
    
    public constructeur(rayon):
        ce.rayon ← rayon
    
    public obtenirRayon():
        retourner ce.rayon
    
    public définirRayon(nouveauRayon):
        si nouveauRayon > 0:
            ce.rayon ← nouveauRayon
    
    // Attributs calculés (pas stockés)
    public obtenirDiametre():
        retourner ce.rayon * 2
    
    public obtenirCirconférence():
        retourner 2 * 3.14159 * ce.rayon
    
    public obtenirAire():
        retourner 3.14159 * ce.rayon * ce.rayon
    
    // Setter pour le diamètre (met à jour le rayon)
    public définirDiametre(diametre):
        ce.rayon ← diametre / 2

cercle ← nouveau Cercle(5)
afficher(cercle.obtenirDiametre())  // 10
afficher(cercle.obtenirAire())      // 78.54

cercle.définirDiametre(20)
afficher(cercle.obtenirRayon())     // 10
```

## Chaînage de setters (Fluent Interface)

Pour une syntaxe plus élégante, on peut retourner `ce` dans les setters.

```
classe PersonneBuilder:
    private nom
    private prenom
    private age
    private email
    
    public définirNom(nom):
        ce.nom ← nom
        retourner ce  // ← Permet le chaînage
    
    public définirPrenom(prenom):
        ce.prenom ← prenom
        retourner ce
    
    public définirAge(age):
        ce.age ← age
        retourner ce
    
    public définirEmail(email):
        ce.email ← email
        retourner ce

// Utilisation avec chaînage
personne ← nouveau PersonneBuilder()
    .définirNom("Dupont")
    .définirPrenom("Jean")
    .définirAge(30)
    .définirEmail("jean@example.com")
```

## Getters/Setters vs Accès direct

### ❌ Accès direct (déconseillé pour les attributs mutables)

```
classe Voiture:
    public vitesse
    public carburant

voiture ← nouveau Voiture()
voiture.vitesse ← 300      // Pas de validation
voiture.carburant ← -10    // Valeur impossible
```

### ✅ Avec getters/setters

```
classe Voiture:
    private vitesse
    private carburant
    private vitesseMax ← 200
    
    public obtenirVitesse():
        retourner ce.vitesse
    
    public définirVitesse(nouvelleVitesse):
        si nouvelleVitesse >= 0 et nouvelleVitesse <= ce.vitesseMax:
            ce.vitesse ← nouvelleVitesse
        sinon:
            erreur("Vitesse invalide")
    
    public obtenirCarburant():
        retourner ce.carburant
    
    public définirCarburant(quantité):
        si quantité >= 0 et quantité <= 100:
            ce.carburant ← quantité
        sinon:
            erreur("Quantité de carburant invalide")

voiture ← nouveau Voiture()
voiture.définirVitesse(300)   // ❌ Erreur : dépasse vitesseMax
voiture.définirVitesse(150)   // ✅ OK
voiture.définirCarburant(-10) // ❌ Erreur : valeur négative
```

## Exemple complet : Classe Temperature

```
classe Temperature:
    private celsius
    
    public constructeur(celsius):
        ce.définirCelsius(celsius)
    
    // Getter/Setter pour Celsius
    public obtenirCelsius():
        retourner ce.celsius
    
    public définirCelsius(valeur):
        si valeur >= -273.15:  // Zéro absolu
            ce.celsius ← valeur
        sinon:
            erreur("Température sous le zéro absolu")
    
    // Getters/Setters pour Fahrenheit (calculés)
    public obtenirFahrenheit():
        retourner (ce.celsius * 9/5) + 32
    
    public définirFahrenheit(valeur):
        celsius ← (valeur - 32) * 5/9
        ce.définirCelsius(celsius)
    
    // Getters/Setters pour Kelvin (calculés)
    public obtenirKelvin():
        retourner ce.celsius + 273.15
    
    public définirKelvin(valeur):
        ce.définirCelsius(valeur - 273.15)
    
    // Méthodes utilitaires
    public afficher():
        afficher(ce.celsius + "°C")
        afficher(ce.obtenirFahrenheit() + "°F")
        afficher(ce.obtenirKelvin() + "K")

// Utilisation
temp ← nouveau Temperature(25)
temp.afficher()
// 25°C
// 77°F
// 298.15K

temp.définirFahrenheit(32)  // 0°C (point de congélation de l'eau)
temp.afficher()
// 0°C
// 32°F
// 273.15K

temp.définirKelvin(373.15)  // 100°C (point d'ébullition de l'eau)
temp.afficher()
// 100°C
// 212°F
// 373.15K

temp.définirCelsius(-300)  // ❌ Erreur : sous le zéro absolu
```

## Cas d'usage avancés

### 1. Lazy Loading (chargement paresseux)

```
classe Article:
    private id
    private contenu  // null au départ
    
    public obtenirContenu():
        si ce.contenu == null:
            // Charger depuis la base de données seulement si nécessaire
            ce.contenu ← chargerDepuisDB(ce.id)
        retourner ce.contenu
```

### 2. Cache/Memoization

```
classe Calculateur:
    private n
    private factorielleCache  // null au départ
    
    public définirN(valeur):
        ce.n ← valeur
        ce.factorielleCache ← null  // Invalider le cache
    
    public obtenirFactorielle():
        si ce.factorielleCache == null:
            ce.factorielleCache ← calculerFactorielle(ce.n)
        retourner ce.factorielleCache
```

### 3. Validation croisée

```
classe Reservation:
    private dateDebut
    private dateFin
    
    public définirDateDebut(date):
        si ce.dateFin != null et date > ce.dateFin:
            erreur("La date de début doit être avant la date de fin")
        ce.dateDebut ← date
    
    public définirDateFin(date):
        si ce.dateDebut != null et date < ce.dateDebut:
            erreur("La date de fin doit être après la date de début")
        ce.dateFin ← date
```

## Bonnes pratiques

### ✅ À faire

1. **Toujours valider** dans les setters
2. **Retourner des copies** pour les collections dans les getters
3. **Nommer clairement** : `obtenirX()`, `définirX()`
4. **Calculer** plutôt que stocker quand c'est possible
5. **Documenter** les contraintes et effets de bord

### ❌ À éviter

1. **Getter/Setter pour tout** : réfléchir à ce qui doit vraiment être exposé
2. **Setters sans validation** : autant rendre l'attribut public
3. **Trop de logique dans les getters** : peut être coûteux
4. **Setters qui font trop de choses** : principe de responsabilité unique

## Conclusion

Les getters et setters sont essentiels pour :
- **Contrôler** l'accès aux données
- **Valider** les modifications
- **Encapsuler** la logique métier
- **Permettre l'évolution** du code sans casser l'API
- **Calculer** des propriétés dérivées
- **Protéger** l'intégrité des objets

**Règle d'or** : Ne créez pas automatiquement un getter/setter pour chaque attribut. Demandez-vous d'abord si cet attribut doit vraiment être accessible ou modifiable depuis l'extérieur.
