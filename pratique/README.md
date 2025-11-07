# Jeu de Dames - Cas Pratique POO

Ce dossier contient l'implémentation complète d'un jeu de Dames en Python, démontrant tous les concepts de la Programmation Orientée Objet.

## 🎯 Objectifs pédagogiques

Ce projet illustre concrètement :
- ✅ **Classes et objets**
- ✅ **Héritage** (Pion → PionSimple, Dame)
- ✅ **Classes abstraites** (Pion avec méthodes abstraites)
- ✅ **Encapsulation** (attributs privés, protected)
- ✅ **Getters et Setters** avec validation
- ✅ **Polymorphisme** (différents types de pions)
- ✅ **Composition** (Plateau contient des Pions)
- ✅ **Énumérations** (Couleur, TypePion)

## 📁 Structure du code

```
jeu_dames.py
├── Énumérations
│   ├── Couleur (BLANC, NOIR)
│   └── TypePion (SIMPLE, DAME)
│
├── Position
│   ├── Encapsulation des coordonnées
│   ├── Validation des positions
│   └── Conversion notation (A1, B2, etc.)
│
├── Pion (Classe abstraite)
│   ├── Attributs protected
│   ├── Méthodes abstraites
│   └── Méthodes concrètes communes
│
├── Héritiers de Pion
│   ├── PionSimple (mouvement limité)
│   └── Dame (mouvement étendu)
│
├── Mouvement
│   ├── Encapsulation d'une action
│   └── Gestion des captures
│
├── Plateau
│   ├── Composition (contient des Pions)
│   ├── Initialisation du jeu
│   ├── Gestion des déplacements
│   └── Affichage du plateau
│
├── ValidateurMouvement
│   ├── Validation des règles
│   └── Logique de capture
│
└── Jeu (Contrôleur)
    ├── Boucle de jeu
    ├── Gestion des tours
    └── Interface utilisateur
```

## 🎮 Comment jouer

### Installation

Aucune dépendance externe nécessaire. Python 3.7+ suffit.

### Lancer le jeu

```bash
cd pratique
python jeu_dames.py
```

### Règles simplifiées

1. **Déplacement** : Les pions se déplacent en diagonale d'une case
   - Blancs (⚪) : vers le haut
   - Noirs (⚫) : vers le bas

2. **Capture** : Sauter par-dessus un pion adverse pour le capturer
   - Format : `A3 C5` (saute le pion en B4)

3. **Promotion** : Un pion devient **DAME** (◯/●) en atteignant la dernière ligne
   - Les dames se déplacent en diagonale sur plusieurs cases

4. **Victoire** : Capturer tous les pions adverses

### Exemples de commandes

```
A3 B4    # Déplacement simple
C3 E5    # Capture (saute le pion en D4)
q        # Quitter
```

## 🔍 Concepts POO démontrés

### 1. Classe abstraite et héritage

```python
class Pion(ABC):
    """Classe abstraite de base"""
    
    @abstractmethod
    def peut_se_deplacer_vers(self, destination: Position) -> bool:
        pass
    
    @abstractmethod
    def obtenir_symbole(self) -> str:
        pass

class PionSimple(Pion):
    """Implémentation concrète"""
    def peut_se_deplacer_vers(self, destination: Position) -> bool:
        # Logique spécifique au pion simple
        ...

class Dame(Pion):
    """Implémentation avec comportement différent"""
    def peut_se_deplacer_vers(self, destination: Position) -> bool:
        # Logique spécifique à la dame
        ...
```

**Démonstration** :
- `Pion` est abstraite : impossible de créer `Pion()` directement
- `PionSimple` et `Dame` héritent et implémentent les méthodes abstraites
- Polymorphisme : on peut manipuler tous les pions via la classe `Pion`

### 2. Encapsulation avec getters/setters

```python
class Position:
    def __init__(self, ligne: int, colonne: int):
        self.__ligne = 0      # Attribut privé (__)
        self.__colonne = 0
        self.set_ligne(ligne)  # Validation via setter
    
    def get_ligne(self) -> int:
        """Getter : lecture contrôlée"""
        return self.__ligne
    
    def set_ligne(self, ligne: int):
        """Setter : modification avec validation"""
        if 1 <= ligne <= 10:
            self.__ligne = ligne
        else:
            raise ValueError(f"Ligne invalide : {ligne}")
```

**Démonstration** :
- Attributs privés (`__ligne`) : inaccessibles depuis l'extérieur
- Validation dans les setters : impossible de créer une position invalide
- Protection de l'intégrité des données

### 3. Protected et héritage

```python
class Pion(ABC):
    def __init__(self, couleur: Couleur, position: Position):
        self._couleur = couleur    # Protected (_)
        self._position = position  # Accessible aux héritiers
        self._en_jeu = True

class PionSimple(Pion):
    def peut_etre_promu(self) -> bool:
        # Accès aux attributs protected du parent
        if self._couleur == Couleur.BLANC:
            return self._position.get_ligne() == 10
        ...
```

**Démonstration** :
- `_couleur`, `_position` : accessible dans les classes filles
- Partage d'état entre parent et enfants
- Encapsulation intermédiaire (ni public, ni complètement privé)

### 4. Composition

```python
class Plateau:
    def __init__(self):
        self.__pions: List[Pion] = []  # Le plateau "a" des pions
        self.__initialiser_plateau()
    
    def get_pion_a(self, position: Position) -> Optional[Pion]:
        """Retourne le pion à une position"""
        for pion in self.__pions:
            if pion.get_position() == position:
                return pion
        return None
```

**Démonstration** :
- Relation "a-un" : Plateau **contient** des Pions
- Gestion d'une collection d'objets
- Le plateau contrôle le cycle de vie des pions

### 5. Polymorphisme en action

```python
# Dans Plateau.afficher()
for colonne in range(1, 11):
    position = Position(ligne, colonne)
    pion = self.get_pion_a(position)
    
    if pion:
        # Polymorphisme : appelle la bonne méthode selon le type réel
        ligne_str += pion.obtenir_symbole() + " "  # ⚪ ou ◯ pour blanc
```

**Démonstration** :
- Manipulation uniforme via le type `Pion`
- Comportement différent selon le type réel (`PionSimple` ou `Dame`)
- Le code client n'a pas besoin de savoir le type exact

### 6. Séparation des responsabilités

```python
class Jeu:
    """Contrôleur - gère la boucle de jeu"""
    ...

class Plateau:
    """Modèle - gère l'état du plateau"""
    ...

class ValidateurMouvement:
    """Service - valide les règles"""
    @staticmethod
    def est_mouvement_valide(...) -> Tuple[bool, str]:
        ...
```

**Démonstration** :
- Chaque classe a une responsabilité unique
- Code modulaire et testable
- Facilite la maintenance

## 📊 Diagramme de classes simplifié

```
┌─────────────┐
│  Couleur    │ (Enum)
│  TypePion   │ (Enum)
└─────────────┘
       │
       ▼
┌─────────────┐         ┌──────────────┐
│  Position   │◄────────│  Mouvement   │
└─────────────┘         └──────────────┘
       │                       │
       ▼                       ▼
┌─────────────┐         ┌──────────────┐
│    Pion     │◄────────│   Plateau    │
│  (abstract) │         │              │
└─────────────┘         │ - pions: []  │
       △                └──────────────┘
       │                       ▲
   ┌───┴───┐                   │
   │       │                   │
┌──┴──┐ ┌──┴──┐          ┌─────────┐
│Pion │ │Dame │          │   Jeu   │
│Simple│ │     │          │         │
└─────┘ └─────┘          └─────────┘
```

## 🎓 Points d'apprentissage clés

### Pourquoi ces choix de conception ?

1. **`Position` comme classe** (pas juste un tuple)
   - Encapsulation de la logique de coordonnées
   - Validation centralisée
   - Conversion de notation

2. **`Pion` abstraite** (pas juste une classe normale)
   - Force les héritiers à implémenter les méthodes clés
   - Garantit l'uniformité de l'interface
   - Permet le polymorphisme

3. **Attributs privés** (`__ligne` vs `ligne`)
   - Protection contre les modifications invalides
   - Permet de changer l'implémentation interne
   - Force l'utilisation des getters/setters

4. **`ValidateurMouvement` séparé**
   - Logique de validation indépendante
   - Testable isolément
   - Réutilisable

5. **Méthodes privées** (`__initialiser_plateau`)
   - Détails d'implémentation cachés
   - Interface publique claire
   - Liberté de refactoring

## 🚀 Exercices d'extension

Pour approfondir votre compréhension, essayez d'ajouter :

1. **Captures multiples** : Permettre plusieurs captures en un tour
2. **Historique** : Enregistrer tous les coups joués
3. **Annulation** : Fonction "undo" du dernier coup
4. **IA simple** : Joueur automatique qui joue aléatoirement
5. **Sauvegarde** : Sauvegarder/charger une partie en JSON
6. **Interface graphique** : Utiliser tkinter ou pygame
7. **Règles avancées** : Obligation de capturer, etc.

## 📚 Concepts avancés utilisés

- **ABC (Abstract Base Class)** : Classes abstraites en Python
- **Énumérations** : Types énumérés pour les constantes
- **Type hints** : Annotations de types pour la clarté
- **Optional** : Gestion explicite des valeurs None
- **List comprehension** : Syntaxe concise pour filtrer
- **Méthodes magiques** : `__str__`, `__repr__`, `__eq__`
- **Méthodes statiques** : `@staticmethod` pour les utilitaires

## 🔧 Pour aller plus loin

Consultez les chapitres théoriques pour comprendre en détail :
- [Pourquoi la POO](../theorie/01-pourquoi-la-poo.md)
- [La classe, un contrat](../theorie/02-la-classe-un-contrat.md)
- [L'héritage](../theorie/03-heritage.md)
- [Les interfaces](../theorie/04-interfaces.md)
- [Public, Protected, Private](../theorie/05-public-protected-private.md)
- [Les Getters et Setters](../theorie/06-getters-setters.md)

---

**Bon jeu et bon apprentissage ! 🎮📚**
