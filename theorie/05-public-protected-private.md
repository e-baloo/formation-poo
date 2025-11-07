# Public, Protected, Private

## Qu'est-ce que l'encapsulation ?

L'**encapsulation** est le principe de **cacher les détails internes** d'une classe et de ne rendre accessible que ce qui est nécessaire. Les modificateurs de visibilité (**public**, **protected**, **private**) contrôlent qui peut accéder à quoi.

### Analogie

Pensez à une **voiture** :
- **Public** : Le volant, les pédales, le klaxon → tout le monde peut les utiliser
- **Protected** : Le moteur sous le capot → accessible pour maintenance, mais pas pour l'usage normal
- **Private** : L'électronique interne du calculateur → personne ne doit y toucher directement

## Les trois niveaux de visibilité

```
classe Exemple:
    
    public attributPublic         // ← Accessible partout
    protected attributProtected   // ← Accessible dans la classe et ses héritiers
    private attributPrivé         // ← Accessible uniquement dans la classe
    
    public méthodePublique():
        // Accessible partout
    
    protected méthodeProtected():
        // Accessible dans la classe et ses héritiers
    
    private méthodePrivée():
        // Accessible uniquement dans cette classe
```

### Tableau récapitulatif

| Visibilité | Depuis la classe elle-même | Depuis les classes héritières | Depuis l'extérieur |
|------------|---------------------------|-------------------------------|-------------------|
| **public** | ✅ | ✅ | ✅ |
| **protected** | ✅ | ✅ | ❌ |
| **private** | ✅ | ❌ | ❌ |

## Public

Accessible **partout** : dans la classe, dans les classes héritières, et depuis l'extérieur.

```
classe CompteBancaire:
    public titulaire
    private solde
    
    public constructeur(titulaire, soldeInitial):
        ce.titulaire ← titulaire
        ce.solde ← soldeInitial
    
    public afficherTitulaire():
        afficher("Titulaire: " + ce.titulaire)

// Utilisation
compte ← nouveau CompteBancaire("Alice", 1000)

// Accès public : OK
afficher(compte.titulaire)      // ✅ OK
compte.afficherTitulaire()      // ✅ OK

// Accès privé : ERREUR
afficher(compte.solde)          // ❌ ERREUR
```

### Quand utiliser public ?

- **Interface publique de la classe** : méthodes que les utilisateurs doivent appeler
- **Constantes** qui ne changeront jamais
- **Attributs** qui peuvent être lus/modifiés librement (rare, souvent déconseillé)

## Private

Accessible **uniquement** depuis la classe elle-même. Même les classes héritières ne peuvent pas y accéder directement.

```
classe CompteBancaire:
    private solde
    private historique[]
    
    public constructeur(soldeInitial):
        ce.solde ← soldeInitial
        ce.historique ← []
    
    public déposer(montant):
        si ce.validerMontant(montant):  // ✅ Méthode privée appelée depuis la classe
            ce.solde ← ce.solde + montant
            ce.ajouterÀHistorique("Dépôt: " + montant)
    
    public retirer(montant):
        si ce.validerMontant(montant) et montant <= ce.solde:
            ce.solde ← ce.solde - montant
            ce.ajouterÀHistorique("Retrait: " + montant)
    
    public obtenirSolde():
        retourner ce.solde  // ✅ Accès privé depuis la classe
    
    private validerMontant(montant):
        retourner montant > 0
    
    private ajouterÀHistorique(opération):
        ce.historique.ajouter(opération)

// Utilisation
compte ← nouveau CompteBancaire(1000)

// Méthodes publiques : OK
compte.déposer(500)              // ✅ OK
afficher(compte.obtenirSolde())  // ✅ OK : 1500

// Accès direct : ERREUR
afficher(compte.solde)           // ❌ ERREUR : attribut privé
compte.validerMontant(100)       // ❌ ERREUR : méthode privée
compte.historique.ajouter("X")   // ❌ ERREUR : attribut privé
```

### Quand utiliser private ?

- **Détails d'implémentation** qui peuvent changer
- **Méthodes utilitaires internes**
- **Attributs** dont la modification doit être contrôlée
- **État interne** que personne ne doit modifier directement

### Avantages de private

1. **Protection des données** : impossible de mettre l'objet dans un état invalide
2. **Liberté de modification** : on peut changer l'implémentation sans casser le code externe
3. **Encapsulation forte** : les détails internes sont cachés

## Protected

Accessible depuis la classe elle-même **et** depuis les classes héritières, mais pas depuis l'extérieur.

```
classe Animal:
    protected energie
    private estVivant
    
    public constructeur(energieInitiale):
        ce.energie ← energieInitiale
        ce.estVivant ← vrai
    
    protected consommerEnergie(quantité):
        ce.energie ← ce.energie - quantité
        si ce.energie <= 0:
            ce.estVivant ← faux
    
    public obtenirEnergie():
        retourner ce.energie

classe Chien hérite de Animal:
    
    public constructeur():
        parent.constructeur(100)
    
    public courir():
        afficher("Le chien court")
        // ✅ Accès protected depuis la classe héritière
        ce.consommerEnergie(10)
        afficher("Énergie restante: " + ce.energie)
    
    public manger():
        // ✅ Modification de l'attribut protected
        ce.energie ← ce.energie + 20

classe Chat hérite de Animal:
    
    public constructeur():
        parent.constructeur(80)
    
    public chasser():
        afficher("Le chat chasse")
        // ✅ Accès protected depuis la classe héritière
        ce.consommerEnergie(15)

// Utilisation
chien ← nouveau Chien()
chien.courir()                   // ✅ OK : méthode publique
afficher(chien.obtenirEnergie()) // ✅ OK : méthode publique

// Accès protected : ERREUR depuis l'extérieur
afficher(chien.energie)          // ❌ ERREUR : attribut protected
chien.consommerEnergie(5)        // ❌ ERREUR : méthode protected

// Accès private : ERREUR même depuis héritier
classe Lion hérite de Animal:
    public rugir():
        ce.estVivant ← vrai      // ❌ ERREUR : attribut private du parent
```

### Quand utiliser protected ?

- **Méthodes utilitaires** pour les classes héritières
- **Attributs** que les classes filles peuvent modifier de manière contrôlée
- **Hooks** ou points d'extension pour les sous-classes

## Exemple complet : Système de véhicules

```
classe Vehicule:
    private immatriculation
    protected vitesseActuelle
    protected vitesseMax
    public marque
    
    public constructeur(immatriculation, marque, vitesseMax):
        ce.immatriculation ← immatriculation
        ce.marque ← marque
        ce.vitesseMax ← vitesseMax
        ce.vitesseActuelle ← 0
    
    // Méthode publique : interface externe
    public accélérer(augmentation):
        nouvelleVitesse ← ce.vitesseActuelle + augmentation
        si ce.validerVitesse(nouvelleVitesse):
            ce.modifierVitesse(nouvelleVitesse)
            afficher("Accélération : " + ce.vitesseActuelle + " km/h")
        sinon:
            afficher("Vitesse maximale atteinte")
    
    // Méthode publique : interface externe
    public freiner():
        ce.modifierVitesse(0)
        afficher("Freinage complet")
    
    // Méthode protected : utilisable par les héritiers
    protected modifierVitesse(nouvelleVitesse):
        ce.vitesseActuelle ← nouvelleVitesse
    
    // Méthode private : détail d'implémentation
    private validerVitesse(vitesse):
        retourner vitesse >= 0 et vitesse <= ce.vitesseMax
    
    // Méthode publique
    public obtenirImmatriculation():
        retourner ce.immatriculation

classe VoitureSport hérite de Vehicule:
    private turboActivé
    
    public constructeur(immatriculation, marque):
        parent.constructeur(immatriculation, marque, 250)
        ce.turboActivé ← faux
    
    public activerTurbo():
        si non ce.turboActivé:
            ce.turboActivé ← vrai
            // ✅ Accès à l'attribut protected du parent
            ce.vitesseMax ← 300
            afficher("🔥 Turbo activé! Nouvelle vitesse max: " + ce.vitesseMax)
    
    public désactiverTurbo():
        si ce.turboActivé:
            ce.turboActivé ← faux
            ce.vitesseMax ← 250
            // ✅ Utilisation de la méthode protected du parent
            si ce.vitesseActuelle > ce.vitesseMax:
                ce.modifierVitesse(ce.vitesseMax)

classe Camion hérite de Vehicule:
    private charge
    
    public constructeur(immatriculation, marque):
        parent.constructeur(immatriculation, marque, 110)
        ce.charge ← 0
    
    public charger(poids):
        ce.charge ← ce.charge + poids
        // La vitesse max diminue avec la charge
        // ✅ Accès protected
        ce.vitesseMax ← 110 - (ce.charge / 100)
        
        // Si on roule trop vite pour la charge
        si ce.vitesseActuelle > ce.vitesseMax:
            ce.modifierVitesse(ce.vitesseMax)

// Utilisation
ferrari ← nouveau VoitureSport("AB-123-CD", "Ferrari")
ferrari.accélérer(200)           // ✅ Méthode publique
ferrari.activerTurbo()           // ✅ Méthode publique
ferrari.accélérer(80)            // ✅ OK grâce au turbo

camion ← nouveau Camion("TT-456-XX", "Volvo")
camion.accélérer(100)            // ✅ Méthode publique
camion.charger(500)              // ✅ Méthode publique

// ❌ Accès impossibles depuis l'extérieur
afficher(ferrari.vitesseActuelle)  // ❌ Protected
ferrari.modifierVitesse(350)       // ❌ Protected
afficher(ferrari.immatriculation)  // ❌ Private
camion.validerVitesse(80)          // ❌ Private
```

## Principe de l'encapsulation

### ❌ Sans encapsulation (tout public)

```
classe CompteBancaire:
    public solde
    public decouvertAutorisé
    
    public retirer(montant):
        ce.solde ← ce.solde - montant

// Problèmes !
compte.solde ← -9999           // ❌ Solde négatif non contrôlé
compte.solde ← "abc"           // ❌ Type invalide
compte.decouvertAutorisé ← -1  // ❌ Valeur invalide
```

### ✅ Avec encapsulation (private + méthodes publiques)

```
classe CompteBancaire:
    private solde
    private decouvertAutorisé
    
    public constructeur(soldeInitial, decouvert):
        si soldeInitial >= 0 et decouvert >= 0:
            ce.solde ← soldeInitial
            ce.decouvertAutorisé ← decouvert
        sinon:
            erreur("Valeurs invalides")
    
    public retirer(montant):
        si montant > 0:
            soldeApres ← ce.solde - montant
            si soldeApres >= -ce.decouvertAutorisé:
                ce.solde ← soldeApres
                retourner vrai
            sinon:
                afficher("Découvert dépassé")
                retourner faux
        retourner faux
    
    public obtenirSolde():
        retourner ce.solde

// Utilisation sécurisée
compte ← nouveau CompteBancaire(1000, 200)

// ✅ Toutes les opérations sont contrôlées
compte.retirer(1150)  // OK (solde = -150, dans la limite du découvert)
compte.retirer(100)   // Refusé (dépasserait le découvert)

// ❌ Impossible de mettre l'objet dans un état invalide
// compte.solde ← -9999  // ERREUR : attribut privé
```

## Conseils de conception

### 1. Par défaut, tout est privé

```
classe MaClasse:
    private attribut1
    private attribut2
    
    private méthodeInterne()
    
    // Exposer seulement ce qui est nécessaire
    public méthodeDeLAPI()
```

### 2. Exposer le minimum

Ne rendez publique que l'interface strictement nécessaire.

```
// ❌ Trop exposé
classe Utilisateur:
    public id
    public motDePasse
    public dateCreation
    public tentativesConnexion
    
    public crypterMotDePasse()
    public validerEmail()

// ✅ Encapsulation appropriée
classe Utilisateur:
    private id
    private motDePasseHashé
    private dateCreation
    private tentativesConnexion
    
    public seConnecter(motDePasse)
    public changerMotDePasse(ancienMdp, nouveauMdp)
    
    private crypterMotDePasse()
    private validerEmail()
    private vérifierTentatives()
```

### 3. Protected avec prudence

N'utilisez `protected` que si vous êtes sûr que les classes héritières en auront besoin.

```
classe Base:
    // ❌ Trop ouvert "au cas où"
    protected tout
    protected ces
    protected attributs
    
    // ✅ Seulement ce qui est utile aux héritiers
    protected méthodeUtilitaireCommune()
```

## Conclusion

Les modificateurs de visibilité sont essentiels pour :
- **Protéger** l'intégrité des données
- **Cacher** les détails d'implémentation
- **Contrôler** l'accès aux fonctionnalités
- **Faciliter** la maintenance (changer l'implémentation sans casser le code externe)
- **Documenter** l'intention (ce qui est public = l'API, ce qui est privé = les détails)

**Règle d'or** : Le moins exposé est le mieux ! Commencez toujours par `private`, et rendez public uniquement ce qui doit l'être.
