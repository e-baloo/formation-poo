# Les méthodes et attributs statiques

## Qu'est-ce que le static ?

Le mot-clé **static** (ou équivalent selon les langages) permet de définir des **méthodes** et **attributs** qui appartiennent à la **classe elle-même** plutôt qu'aux **instances** de la classe.

### Analogie

Pensez à une **école** :
- **Attribut d'instance** : Chaque élève a son propre nom, âge, notes → différent pour chaque élève
- **Attribut statique** : Le nom de l'école, l'adresse → partagé par tous les élèves, appartient à l'école

```
Classe École:
    static adresse ← "123 rue de l'École"    // ← Même pour tous
    static nombreÉlèves ← 0                  // ← Compteur partagé
    
    nom    // ← Différent pour chaque élève
    age    // ← Différent pour chaque élève
```

## Attributs statiques (de classe)

Un **attribut statique** est partagé par toutes les instances de la classe. Il existe **une seule copie** en mémoire.

### Syntaxe de base

```
classe Exemple:
    static attributStatique ← valeur    // Attribut de classe
    attributInstance                     // Attribut d'instance
    
    constructeur():
        ce.attributInstance ← valeur
```

### Exemple : Compteur d'instances

```
classe Voiture:
    static nombreVoitures ← 0    // Compteur partagé
    
    marque
    modèle
    
    constructeur(marque, modèle):
        ce.marque ← marque
        ce.modèle ← modèle
        
        // Incrémenter le compteur à chaque création
        Voiture.nombreVoitures ← Voiture.nombreVoitures + 1
    
    static obtenirNombreVoitures():
        retourner Voiture.nombreVoitures

// Utilisation
voiture1 ← nouveau Voiture("Renault", "Clio")
afficher(Voiture.nombreVoitures)  // 1

voiture2 ← nouveau Voiture("Peugeot", "208")
afficher(Voiture.nombreVoitures)  // 2

voiture3 ← nouveau Voiture("Citroën", "C3")
afficher(Voiture.nombreVoitures)  // 3

// Accessible via la classe (recommandé)
afficher(Voiture.obtenirNombreVoitures())  // 3

// Ou via une instance (déconseillé, peut prêter à confusion)
afficher(voiture1.nombreVoitures)  // 3 (même valeur pour toutes)
```

### Exemple : Constantes de classe

```
classe Cercle:
    static PI ← 3.14159265359    // Constante partagée
    
    rayon
    
    constructeur(rayon):
        ce.rayon ← rayon
    
    calculerAire():
        retourner Cercle.PI * ce.rayon * ce.rayon
    
    calculerCirconférence():
        retourner 2 * Cercle.PI * ce.rayon

// Utilisation
cercle1 ← nouveau Cercle(5)
cercle2 ← nouveau Cercle(10)

// Les deux utilisent la même valeur de PI
afficher(cercle1.calculerAire())        // Utilise Cercle.PI
afficher(cercle2.calculerCirconférence())  // Utilise Cercle.PI

// Accès direct à la constante
afficher(Cercle.PI)  // 3.14159265359
```

### Exemple : Configuration partagée

```
classe Connexion:
    static serveur ← "localhost"
    static port ← 5432
    static timeout ← 30
    
    utilisateur
    motDePasse
    
    constructeur(utilisateur, motDePasse):
        ce.utilisateur ← utilisateur
        ce.motDePasse ← motDePasse
    
    seConnecter():
        // Utilise les paramètres statiques partagés
        afficher("Connexion à " + Connexion.serveur + ":" + Connexion.port)
    
    static configurerServeur(nouveauServeur, nouveauPort):
        Connexion.serveur ← nouveauServeur
        Connexion.port ← nouveauPort

// Toutes les connexions utilisent les mêmes paramètres
connexion1 ← nouveau Connexion("user1", "pass1")
connexion2 ← nouveau Connexion("user2", "pass2")

connexion1.seConnecter()  // "Connexion à localhost:5432"
connexion2.seConnecter()  // "Connexion à localhost:5432"

// Changer la configuration pour TOUTES les connexions
Connexion.configurerServeur("prod.example.com", 3306)

connexion1.seConnecter()  // "Connexion à prod.example.com:3306"
connexion2.seConnecter()  // "Connexion à prod.example.com:3306"
```

## Méthodes statiques

Une **méthode statique** appartient à la classe et peut être appelée **sans créer d'instance**. Elle ne peut pas accéder aux attributs d'instance (pas de `ce`/`this`).

### Syntaxe de base

```
classe Exemple:
    static méthodeStatique(paramètres):
        // Pas d'accès à "ce" ou aux attributs d'instance
        // Peut accéder aux attributs statiques
        retourner résultat
```

### Quand utiliser une méthode statique ?

✅ **Utilisez une méthode statique quand :**
- La méthode ne dépend pas de l'état d'une instance
- C'est une fonction utilitaire liée à la classe
- C'est une méthode de fabrication (factory method)
- La méthode fait un calcul indépendant

### Exemple : Méthodes utilitaires

```
classe Math:
    static PI ← 3.14159265359
    
    static max(a, b):
        si a > b:
            retourner a
        sinon:
            retourner b
    
    static min(a, b):
        si a < b:
            retourner a
        sinon:
            retourner b
    
    static abs(nombre):
        si nombre < 0:
            retourner -nombre
        sinon:
            retourner nombre
    
    static puissance(base, exposant):
        résultat ← 1
        pour i de 1 à exposant:
            résultat ← résultat * base
        retourner résultat

// Utilisation sans créer d'instance
afficher(Math.max(10, 5))       // 10
afficher(Math.min(10, 5))       // 5
afficher(Math.abs(-42))         // 42
afficher(Math.puissance(2, 8))  // 256

// Pas besoin de : m ← nouveau Math()
```

### Exemple : Méthode de fabrication (Factory Method)

```
classe Date:
    jour
    mois
    année
    
    constructeur(jour, mois, année):
        ce.jour ← jour
        ce.mois ← mois
        ce.année ← année
    
    // Méthode statique de fabrication
    static aujourdHui():
        // Obtenir la date actuelle du système
        dateSysteme ← obtenirDateSysteme()
        retourner nouveau Date(dateSysteme.jour, dateSysteme.mois, dateSysteme.année)
    
    static depuisChaîne(chaîne):
        // Parser une chaîne "JJ/MM/AAAA"
        parties ← chaîne.diviser("/")
        jour ← entier(parties[0])
        mois ← entier(parties[1])
        année ← entier(parties[2])
        retourner nouveau Date(jour, mois, année)
    
    static premierJourAnnée(année):
        retourner nouveau Date(1, 1, année)
    
    afficher():
        afficher(ce.jour + "/" + ce.mois + "/" + ce.année)

// Utilisation des méthodes de fabrication
date1 ← Date.aujourdHui()              // Date du jour
date2 ← Date.depuisChaîne("25/12/2025")  // À partir d'une chaîne
date3 ← Date.premierJourAnnée(2026)     // 01/01/2026

date1.afficher()
date2.afficher()
date3.afficher()
```

### Exemple : Validation et conversion

```
classe Email:
    static DOMAINES_VALIDES ← ["gmail.com", "yahoo.com", "outlook.com"]
    
    adresse
    
    constructeur(adresse):
        si Email.estValide(adresse):
            ce.adresse ← adresse
        sinon:
            erreur("Email invalide")
    
    static estValide(adresse):
        // Vérifications basiques
        si non adresse.contient("@"):
            retourner faux
        
        si non adresse.contient("."):
            retourner faux
        
        parties ← adresse.diviser("@")
        si parties.taille() != 2:
            retourner faux
        
        retourner vrai
    
    static normaliser(adresse):
        // Convertir en minuscules et supprimer les espaces
        retourner adresse.minuscules().supprimerEspaces()
    
    static extraireDomaine(adresse):
        parties ← adresse.diviser("@")
        si parties.taille() == 2:
            retourner parties[1]
        retourner null

// Utilisation
// Validation avant création
si Email.estValide("user@example.com"):
    email ← nouveau Email("user@example.com")

// Utilitaires sans instance
domaine ← Email.extraireDomaine("contact@company.com")
afficher(domaine)  // "company.com"

adresseNormalisée ← Email.normaliser("  User@EXAMPLE.COM  ")
afficher(adresseNormalisée)  // "user@example.com"
```

## Attributs vs Méthodes : Instance vs Statique

### Tableau comparatif

| Critère | Instance | Statique |
|---------|----------|----------|
| **Appartient à** | Un objet spécifique | La classe |
| **Accès via** | `objet.attribut` | `Classe.attribut` |
| **Nombre de copies** | Une par instance | Une seule partagée |
| **Accès à `ce`** | ✅ Oui | ❌ Non |
| **Quand l'utiliser** | État spécifique à chaque objet | Partagé entre tous les objets |

### Exemple complet

```
classe CompteBancaire:
    // Attributs statiques (partagés)
    static tauxIntérêt ← 0.03
    static nombreComptes ← 0
    static fraisTransfert ← 2.50
    
    // Attributs d'instance (spécifiques)
    numéro
    titulaire
    solde
    
    constructeur(titulaire, soldeInitial):
        ce.titulaire ← titulaire
        ce.solde ← soldeInitial
        
        // Générer un numéro unique
        CompteBancaire.nombreComptes ← CompteBancaire.nombreComptes + 1
        ce.numéro ← "COMPTE" + CompteBancaire.nombreComptes
    
    // Méthode d'instance
    calculerIntérêts():
        intérêts ← ce.solde * CompteBancaire.tauxIntérêt
        ce.solde ← ce.solde + intérêts
        retourner intérêts
    
    // Méthode d'instance
    transférerVers(autreCompte, montant):
        si ce.solde >= montant + CompteBancaire.fraisTransfert:
            ce.solde ← ce.solde - montant - CompteBancaire.fraisTransfert
            autreCompte.solde ← autreCompte.solde + montant
            afficher("Frais de " + CompteBancaire.fraisTransfert + "€ appliqués")
            retourner vrai
        retourner faux
    
    // Méthodes statiques
    static modifierTauxIntérêt(nouveauTaux):
        si nouveauTaux >= 0 et nouveauTaux <= 0.10:
            CompteBancaire.tauxIntérêt ← nouveauTaux
            afficher("Nouveau taux : " + nouveauTaux)
    
    static obtenirStatistiques():
        afficher("Nombre de comptes : " + CompteBancaire.nombreComptes)
        afficher("Taux d'intérêt : " + (CompteBancaire.tauxIntérêt * 100) + "%")
        afficher("Frais de transfert : " + CompteBancaire.fraisTransfert + "€")

// Utilisation
compte1 ← nouveau CompteBancaire("Alice", 1000)
compte2 ← nouveau CompteBancaire("Bob", 500)

// Attributs d'instance : différents pour chaque compte
afficher(compte1.solde)  // 1000
afficher(compte2.solde)  // 500

// Méthode d'instance
compte1.calculerIntérêts()  // Intérêts sur 1000€

// Méthode statique : pas besoin d'instance
CompteBancaire.obtenirStatistiques()
// Nombre de comptes : 2
// Taux d'intérêt : 3%
// Frais de transfert : 2.50€

// Changer le taux pour TOUS les comptes
CompteBancaire.modifierTauxIntérêt(0.04)

compte1.calculerIntérêts()  // Utilise le nouveau taux (4%)
compte2.calculerIntérêts()  // Utilise le nouveau taux (4%)
```

## Cas d'usage courants

### 1. Compteurs et statistiques

```
classe Produit:
    static nombreProduits ← 0
    static valeurTotaleStock ← 0
    
    nom
    prix
    quantité
    
    constructeur(nom, prix, quantité):
        ce.nom ← nom
        ce.prix ← prix
        ce.quantité ← quantité
        
        Produit.nombreProduits ← Produit.nombreProduits + 1
        Produit.valeurTotaleStock ← Produit.valeurTotaleStock + (prix * quantité)
    
    static obtenirValeurMoyenne():
        si Produit.nombreProduits > 0:
            retourner Produit.valeurTotaleStock / Produit.nombreProduits
        retourner 0
```

### 2. Configuration globale

```
classe Application:
    static debug ← faux
    static langue ← "fr"
    static thème ← "clair"
    
    static activer Debug():
        Application.debug ← vrai
    
    static changerLangue(nouvelleLangue):
        Application.langue ← nouvelleLangue
    
    static obtenirConfiguration():
        retourner {
            "debug": Application.debug,
            "langue": Application.langue,
            "thème": Application.thème
        }
```

### 3. Singleton (instance unique)

```
classe BaseDeDonnées:
    static instance ← null    // Instance unique
    
    connexion
    
    constructeur():
        // Constructeur privé (selon le langage)
        ce.connexion ← créerConnexion()
    
    static obtenirInstance():
        si BaseDeDonnées.instance == null:
            BaseDeDonnées.instance ← nouveau BaseDeDonnées()
        retourner BaseDeDonnées.instance
    
    exécuterRequête(sql):
        // Utiliser ce.connexion
        retourner résultat

// Utilisation : toujours la même instance
db1 ← BaseDeDonnées.obtenirInstance()
db2 ← BaseDeDonnées.obtenirInstance()

// db1 et db2 pointent vers le même objet
```

### 4. Méthodes utilitaires de classe

```
classe Chaîne:
    static inverser(texte):
        résultat ← ""
        pour i de texte.longueur() - 1 à 0:
            résultat ← résultat + texte[i]
        retourner résultat
    
    static estPalindrome(texte):
        retourner texte == Chaîne.inverser(texte)
    
    static compterMots(texte):
        mots ← texte.diviser(" ")
        retourner mots.taille()
    
    static capitaliser(texte):
        si texte.longueur() > 0:
            retourner texte[0].majuscule() + texte.sousChaine(1)
        retourner texte

// Utilisation
afficher(Chaîne.inverser("hello"))           // "olleh"
afficher(Chaîne.estPalindrome("kayak"))      // vrai
afficher(Chaîne.compterMots("Bonjour le monde"))  // 3
afficher(Chaîne.capitaliser("python"))       // "Python"
```

## Bonnes pratiques

### ✅ À faire

1. **Utilisez static pour les constantes de classe**
```
classe Constantes:
    static PI ← 3.14159
    static VERSION ← "1.0.0"
    static MAX_UTILISATEURS ← 100
```

2. **Utilisez static pour les méthodes utilitaires**
```
classe Math:
    static max(a, b)
    static min(a, b)
```

3. **Nommez clairement les attributs statiques**
```
classe Voiture:
    static nombreVoituresCréées ← 0    // ✅ Clair
    static count ← 0                    // ❌ Ambigu
```

4. **Accédez aux statiques via le nom de classe**
```
afficher(Math.PI)        // ✅ Clair
afficher(monObjet.PI)    // ❌ Confus (même si techniquement possible)
```

### ❌ À éviter

1. **Ne pas abuser des attributs statiques mutables**
```
// ❌ Risqué : état partagé mutable
classe Utilisateur:
    static dernierEmail ← ""  // Peut causer des bugs
```

2. **Ne pas utiliser static quand l'état d'instance est nécessaire**
```
// ❌ Mauvais : a besoin de l'instance
classe Personne:
    nom
    
    static sePresenter():  // ❌ Ne peut pas accéder à ce.nom
        afficher("Je suis " + nom)  // Erreur !
```

3. **Ne pas utiliser d'attributs d'instance dans des méthodes statiques**
```
classe Exemple:
    attributInstance ← 10
    
    static méthodeStatique():
        // ❌ Erreur : pas d'accès à ce.attributInstance
        afficher(ce.attributInstance)
```

## Static vs Instance : Quand utiliser quoi ?

### Utilisez des méthodes/attributs d'instance quand :
- Les données sont **spécifiques à chaque objet**
- Vous avez besoin d'accéder à `ce` / `this`
- L'état varie entre les instances

### Utilisez des méthodes/attributs statiques quand :
- Les données sont **partagées** par toutes les instances
- La méthode est **utilitaire** et ne dépend pas d'un objet
- Vous créez des **factory methods**
- Vous gérez des **constantes** de classe
- Vous comptez les instances ou gérez des statistiques globales

## Exemple complet : Système de gestion d'employés

```
classe Employé:
    // Attributs statiques
    static nombreEmployés ← 0
    static salaireMinimum ← 1800
    static entreprise ← "TechCorp"
    
    // Attributs d'instance
    id
    nom
    prénom
    salaire
    dateEmbauche
    
    constructeur(nom, prénom, salaire):
        ce.nom ← nom
        ce.prénom ← prénom
        ce.dateEmbauche ← Date.aujourdHui()
        
        // Générer un ID unique
        Employé.nombreEmployés ← Employé.nombreEmployés + 1
        ce.id ← "EMP" + Employé.nombreEmployés
        
        // Valider et assigner le salaire
        si salaire >= Employé.salaireMinimum:
            ce.salaire ← salaire
        sinon:
            ce.salaire ← Employé.salaireMinimum
            afficher("Salaire ajusté au minimum : " + Employé.salaireMinimum)
    
    // Méthodes d'instance
    obtenirNomComplet():
        retourner ce.prénom + " " + ce.nom
    
    augmenterSalaire(pourcentage):
        augmentation ← ce.salaire * (pourcentage / 100)
        ce.salaire ← ce.salaire + augmentation
        afficher("Nouveau salaire : " + ce.salaire + "€")
    
    afficherFichePaie():
        afficher("=== Fiche de paie ===")
        afficher("Entreprise : " + Employé.entreprise)
        afficher("ID : " + ce.id)
        afficher("Nom : " + ce.obtenirNomComplet())
        afficher("Salaire : " + ce.salaire + "€")
    
    // Méthodes statiques
    static modifierSalaireMinimum(nouveauMinimum):
        si nouveauMinimum > 0:
            Employé.salaireMinimum ← nouveauMinimum
            afficher("Nouveau salaire minimum : " + nouveauMinimum + "€")
    
    static obtenirNombreEmployés():
        retourner Employé.nombreEmployés
    
    static obtenirStatistiques():
        afficher("Entreprise : " + Employé.entreprise)
        afficher("Nombre d'employés : " + Employé.nombreEmployés)
        afficher("Salaire minimum : " + Employé.salaireMinimum + "€")

// Utilisation
emp1 ← nouveau Employé("Dupont", "Jean", 2500)
emp2 ← nouveau Employé("Martin", "Marie", 2800)
emp3 ← nouveau Employé("Bernard", "Luc", 1500)  // Ajusté au minimum

// Méthodes d'instance
emp1.afficherFichePaie()
emp2.augmenterSalaire(10)  // Augmentation de 10%

// Méthodes statiques
Employé.obtenirStatistiques()
// Entreprise : TechCorp
// Nombre d'employés : 3
// Salaire minimum : 1800€

// Modifier le minimum pour tous
Employé.modifierSalaireMinimum(2000)

emp4 ← nouveau Employé("Petit", "Sophie", 1900)  // ❌ Ajusté à 2000
```

## Conclusion

Les méthodes et attributs **statiques** sont essentiels pour :
- **Partager** des données entre toutes les instances
- Créer des **utilitaires** sans instanciation
- Gérer des **constantes** de classe
- Implémenter des **factory methods**
- Compter et gérer des **statistiques** globales

**Règle d'or** : 
- Si ça dépend d'un objet spécifique → **instance**
- Si c'est partagé ou indépendant → **static**
