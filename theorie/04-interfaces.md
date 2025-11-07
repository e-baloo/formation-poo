# Les Interfaces

## Qu'est-ce qu'une interface ?

Une **interface** est un contrat qui définit **ce qu'une classe doit faire**, sans spécifier **comment** elle doit le faire. C'est une liste de méthodes que les classes s'engagent à implémenter.

### Différence avec une classe

| Classe | Interface |
|--------|-----------|
| Définit **quoi** et **comment** | Définit seulement **quoi** |
| Contient des attributs et des méthodes implémentées | Contient uniquement des signatures de méthodes |
| On peut en hériter (extends/hérite de) | On l'implémente (implements) |
| Une classe = un seul parent | Une classe = plusieurs interfaces |

### Analogie

Une interface, c'est comme un **contrat de travail** :
- Le contrat dit : "Vous devez livrer les colis, répondre au téléphone, etc."
- Il ne dit PAS : "Vous devez livrer les colis **en voiture bleue** avec **telle méthode précise**"
- Plusieurs personnes différentes peuvent signer le même contrat et travailler différemment

## Syntaxe de base

```
interface NomInterface:
    méthode1(paramètres)
    méthode2(paramètres)
    méthode3()

classe MaClasse implémente NomInterface:
    // DOIT implémenter toutes les méthodes de l'interface
    méthode1(paramètres):
        // implémentation concrète
    
    méthode2(paramètres):
        // implémentation concrète
    
    méthode3():
        // implémentation concrète
```

## Exemple simple : Formes géométriques

```
interface FormeGeometrique:
    calculerAire()
    calculerPerimetre()
    afficher()

classe Rectangle implémente FormeGeometrique:
    longueur
    largeur
    
    constructeur(longueur, largeur):
        ce.longueur ← longueur
        ce.largeur ← largeur
    
    calculerAire():
        retourner ce.longueur * ce.largeur
    
    calculerPerimetre():
        retourner 2 * (ce.longueur + ce.largeur)
    
    afficher():
        afficher("Rectangle " + ce.longueur + "x" + ce.largeur)

classe Cercle implémente FormeGeometrique:
    rayon
    
    constructeur(rayon):
        ce.rayon ← rayon
    
    calculerAire():
        retourner 3.14159 * ce.rayon * ce.rayon
    
    calculerPerimetre():
        retourner 2 * 3.14159 * ce.rayon
    
    afficher():
        afficher("Cercle de rayon " + ce.rayon)

classe Triangle implémente FormeGeometrique:
    base
    hauteur
    cote1, cote2, cote3
    
    constructeur(base, hauteur, cote1, cote2, cote3):
        ce.base ← base
        ce.hauteur ← hauteur
        ce.cote1 ← cote1
        ce.cote2 ← cote2
        ce.cote3 ← cote3
    
    calculerAire():
        retourner (ce.base * ce.hauteur) / 2
    
    calculerPerimetre():
        retourner ce.cote1 + ce.cote2 + ce.cote3
    
    afficher():
        afficher("Triangle")
```

### Utilisation : Polymorphisme

```
fonction afficherInfosFormes(formes[]):
    pour chaque forme dans formes:
        forme.afficher()
        afficher("Aire: " + forme.calculerAire())
        afficher("Périmètre: " + forme.calculerPerimetre())
        afficher("---")

// Toutes ces formes implémentent la même interface
formes ← [
    nouveau Rectangle(5, 3),
    nouveau Cercle(4),
    nouveau Triangle(6, 4, 5, 5, 6)
]

afficherInfosFormes(formes)
```

## Pourquoi utiliser des interfaces ?

### 1. Contrat explicite

```
interface Volant:
    décoller()
    atterrir()
    voler()

// Toute classe qui implémente Volant GARANTIT qu'elle sait voler
classe Avion implémente Volant:
    // DOIT implémenter décoller(), atterrir(), voler()

classe Oiseau implémente Volant:
    // DOIT implémenter décoller(), atterrir(), voler()
```

### 2. Indépendance de l'implémentation

Le code client n'a pas besoin de savoir **comment** c'est fait, juste **que** c'est fait.

```
fonction planVol(vehiculeVolant: Volant):
    vehiculeVolant.décoller()
    vehiculeVolant.voler()
    vehiculeVolant.atterrir()

// Fonctionne avec n'importe quelle classe qui implémente Volant
avion ← nouveau Avion()
hélicoptère ← nouveau Hélicoptère()
drone ← nouveau Drone()

planVol(avion)         // OK
planVol(hélicoptère)   // OK
planVol(drone)         // OK
```

### 3. Implémentation multiple

Une classe peut implémenter **plusieurs interfaces** (contrairement à l'héritage simple).

```
interface Nageur:
    nager()

interface Volant:
    voler()

interface Marcheur:
    marcher()

// Un canard peut faire les 3 !
classe Canard implémente Nageur, Volant, Marcheur:
    nager():
        afficher("Le canard nage")
    
    voler():
        afficher("Le canard vole")
    
    marcher():
        afficher("Le canard marche")

// Un poisson ne fait qu'une chose
classe Poisson implémente Nageur:
    nager():
        afficher("Le poisson nage")

// Un avion aussi
classe Avion implémente Volant:
    voler():
        afficher("L'avion vole")
```

## Interface vs Classe abstraite

### Classe abstraite
```
classe abstraite Animal:
    nom                    // ← Peut avoir des attributs
    
    constructeur(nom):     // ← Peut avoir un constructeur
        ce.nom ← nom
    
    manger():              // ← Peut avoir des méthodes concrètes
        afficher(ce.nom + " mange")
    
    abstraite faireDuBruit()  // ← Méthodes abstraites
```

### Interface
```
interface Animal:
    faireDuBruit()        // ← Uniquement des signatures
    manger()              // ← Pas d'implémentation
    // Pas d'attributs
    // Pas de constructeur
```

### Quand utiliser quoi ?

| Critère | Interface | Classe abstraite |
|---------|-----------|------------------|
| Besoin d'attributs communs | ❌ | ✅ |
| Besoin de méthodes concrètes communes | ❌ | ✅ |
| Implémentation multiple | ✅ | ❌ |
| Définir un contrat pur | ✅ | ❌ |
| Relation "est-un" | ❌ | ✅ |
| Définir des capacités | ✅ | ❌ |

## Exemple : Système de paiement

```
interface MoyenDePaiement:
    validerPaiement(montant)
    annulerPaiement(idTransaction)
    obtenirHistorique()

classe CarteBancaire implémente MoyenDePaiement:
    numéro
    dateExpiration
    cryptogramme
    
    constructeur(numéro, dateExpiration, cryptogramme):
        ce.numéro ← numéro
        ce.dateExpiration ← dateExpiration
        ce.cryptogramme ← cryptogramme
    
    validerPaiement(montant):
        // Connexion à la banque
        afficher("Paiement de " + montant + " € par carte")
        retourner vrai
    
    annulerPaiement(idTransaction):
        afficher("Annulation transaction " + idTransaction)
    
    obtenirHistorique():
        // Récupérer l'historique depuis la banque
        retourner []

classe PayPal implémente MoyenDePaiement:
    email
    
    constructeur(email):
        ce.email ← email
    
    validerPaiement(montant):
        // API PayPal
        afficher("Paiement de " + montant + " € via PayPal")
        retourner vrai
    
    annulerPaiement(idTransaction):
        afficher("Remboursement PayPal " + idTransaction)
    
    obtenirHistorique():
        // API PayPal
        retourner []

classe Cryptomonnaie implémente MoyenDePaiement:
    adresseWallet
    typeCrypto
    
    constructeur(adresseWallet, typeCrypto):
        ce.adresseWallet ← adresseWallet
        ce.typeCrypto ← typeCrypto
    
    validerPaiement(montant):
        // Blockchain
        afficher("Paiement de " + montant + " " + ce.typeCrypto)
        retourner vrai
    
    annulerPaiement(idTransaction):
        afficher("Les transactions crypto sont irréversibles")
    
    obtenirHistorique():
        // Explorer blockchain
        retourner []

// Le système de paiement ne dépend pas de l'implémentation
classe Boutique:
    
    fonction effectuerAchat(moyenPaiement: MoyenDePaiement, montant):
        si moyenPaiement.validerPaiement(montant):
            afficher("Achat validé!")
            ce.envoyerConfirmation()
        sinon:
            afficher("Échec du paiement")

// Utilisation
boutique ← nouveau Boutique()

// On peut payer de différentes manières
boutique.effectuerAchat(nouveau CarteBancaire("1234", "12/25", "123"), 49.99)
boutique.effectuerAchat(nouveau PayPal("user@email.com"), 29.99)
boutique.effectuerAchat(nouveau Cryptomonnaie("0xABC123", "Bitcoin"), 99.99)
```

## Interfaces et composition

Les interfaces encouragent la **composition** plutôt que l'héritage.

```
interface Serialisable:
    versChaîne()
    depuisChaîne(data)

interface Sauvegardable:
    sauvegarder(fichier)
    charger(fichier)

interface Validable:
    estValide()
    obtenirErreurs()

// Une classe peut combiner plusieurs capacités
classe Utilisateur implémente Serialisable, Sauvegardable, Validable:
    nom
    email
    age
    
    versChaîne():
        retourner "nom:" + ce.nom + ",email:" + ce.email + ",age:" + ce.age
    
    depuisChaîne(data):
        // Parser la chaîne et créer un objet
    
    sauvegarder(fichier):
        données ← ce.versChaîne()
        écrireDansFichier(fichier, données)
    
    charger(fichier):
        données ← lireFichier(fichier)
        ce.depuisChaîne(données)
    
    estValide():
        retourner ce.nom != "" et ce.email.contient("@") et ce.age > 0
    
    obtenirErreurs():
        erreurs ← []
        si ce.nom == "":
            erreurs.ajouter("Le nom est requis")
        si non ce.email.contient("@"):
            erreurs.ajouter("Email invalide")
        si ce.age <= 0:
            erreurs.ajouter("Âge invalide")
        retourner erreurs
```

## Exemple complet : Système de notifications

```
interface ServiceNotification:
    envoyerNotification(destinataire, message)
    estDisponible()

classe NotificationEmail implémente ServiceNotification:
    serveurSMTP
    port
    
    constructeur(serveurSMTP, port):
        ce.serveurSMTP ← serveurSMTP
        ce.port ← port
    
    envoyerNotification(destinataire, message):
        afficher("📧 Envoi email à " + destinataire)
        afficher("Message: " + message)
        // Connexion SMTP et envoi
        retourner vrai
    
    estDisponible():
        // Vérifier connexion au serveur
        retourner vrai

classe NotificationSMS implémente ServiceNotification:
    apiKey
    
    constructeur(apiKey):
        ce.apiKey ← apiKey
    
    envoyerNotification(destinataire, message):
        afficher("📱 Envoi SMS au " + destinataire)
        afficher("Message: " + message)
        // Appel API SMS
        retourner vrai
    
    estDisponible():
        // Vérifier crédit SMS
        retourner vrai

classe NotificationPush implémente ServiceNotification:
    
    envoyerNotification(destinataire, message):
        afficher("🔔 Notification push à " + destinataire)
        afficher("Message: " + message)
        // Service de push notification
        retourner vrai
    
    estDisponible():
        retourner vrai

// Gestionnaire qui peut utiliser n'importe quel service
classe GestionnaireNotifications:
    services[]
    
    constructeur():
        ce.services ← []
    
    ajouterService(service: ServiceNotification):
        ce.services.ajouter(service)
    
    notifierTous(destinataire, message):
        pour chaque service dans ce.services:
            si service.estDisponible():
                service.envoyerNotification(destinataire, message)

// Utilisation
gestionnaire ← nouveau GestionnaireNotifications()
gestionnaire.ajouterService(nouveau NotificationEmail("smtp.gmail.com", 587))
gestionnaire.ajouterService(nouveau NotificationSMS("API_KEY_123"))
gestionnaire.ajouterService(nouveau NotificationPush())

gestionnaire.notifierTous("user@example.com", "Votre commande est prête!")
// Envoie via email, SMS et push notification
```

## Interfaces de marquage

Certaines interfaces ne contiennent aucune méthode. Elles servent juste à **marquer** une classe.

```
interface Clonable:
    // Interface vide = marqueur

classe Document implémente Clonable:
    contenu
    
    constructeur(contenu):
        ce.contenu ← contenu

fonction dupliquerSiPossible(objet):
    si objet implémente Clonable:
        retourner copier(objet)
    sinon:
        afficher("Cet objet ne peut pas être cloné")
        retourner null
```

## Conclusion

Les interfaces sont essentielles pour :
- Définir des **contrats clairs**
- Favoriser le **polymorphisme**
- Permettre l'**implémentation multiple**
- Découpler le code (principe SOLID : **D**ependency Inversion)
- Rendre le code **testable** et **extensible**

**Règle d'or** : Programmez vers une interface, pas vers une implémentation concrète !

```
// ❌ Mauvais
fonction traiter(email: NotificationEmail):
    email.envoyerNotification(...)

// ✅ Bon
fonction traiter(service: ServiceNotification):
    service.envoyerNotification(...)
```
