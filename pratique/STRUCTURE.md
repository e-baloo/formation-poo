# Structure du Code - Jeu de Dames

## 📂 Organisation des fichiers

Le code est organisé de manière modulaire et fonctionnelle :

```
pratique/
│
├── main.py                          # Point d'entrée du programme
├── jeu_dames.py                     # Version monolithique (ancienne)
│
└── src/                             # Code source modulaire
    │
    ├── __init__.py
    │
    ├── enums/                       # Énumérations et types
    │   ├── __init__.py
    │   └── types.py                 # Couleur, TypePion
    │
    ├── modeles/                     # Modèles de données
    │   ├── __init__.py
    │   ├── position.py              # Classe Position
    │   ├── mouvement.py             # Classe Mouvement
    │   │
    │   └── pions/                   # Hiérarchie des pions
    │       ├── __init__.py
    │       ├── pion.py              # Classe abstraite Pion
    │       ├── pion_simple.py       # Classe PionSimple
    │       └── dame.py              # Classe Dame
    │
    ├── logique/                     # Logique métier
    │   ├── __init__.py
    │   ├── plateau.py               # Classe Plateau
    │   └── validateur_mouvement.py  # Classe ValidateurMouvement
    │
    └── interface/                   # Interface utilisateur
        ├── __init__.py
        └── jeu.py                   # Classe Jeu (contrôleur)
```

## 🎯 Principe d'organisation

### 1. **enums/** - Énumérations
Contient les types énumérés utilisés dans tout le projet :
- `Couleur` : BLANC, NOIR
- `TypePion` : SIMPLE, DAME

### 2. **modeles/** - Modèles de données
Contient les classes représentant les entités du jeu :
- `Position` : Coordonnées sur le plateau
- `Mouvement` : Déplacement d'un pion
- `pions/` : Hiérarchie des pions
  - `Pion` : Classe abstraite de base
  - `PionSimple` : Pion standard
  - `Dame` : Pion promu

### 3. **logique/** - Logique métier
Contient les règles et la gestion du jeu :
- `Plateau` : Gestion du plateau 10x10
- `ValidateurMouvement` : Validation des règles

### 4. **interface/** - Interface utilisateur
Contient le contrôleur et l'affichage :
- `Jeu` : Boucle de jeu et interactions

## 🚀 Comment utiliser

### Exécuter le jeu

```bash
# Nouvelle version modulaire
python main.py

# Ancienne version monolithique (toujours fonctionnelle)
python jeu_dames.py
```

### Importer des composants

```python
# Importer les énumérations
from src.enums import Couleur, TypePion

# Importer les modèles
from src.modeles import Position, Mouvement
from src.modeles import Pion, PionSimple, Dame

# Importer la logique
from src.logique import Plateau, ValidateurMouvement

# Importer l'interface
from src.interface import Jeu
```

## 📚 Concepts POO démontrés

### Séparation des responsabilités
- **enums/** : Constantes et types
- **modeles/** : Données et état
- **logique/** : Règles et traitements
- **interface/** : Interaction et affichage

### Encapsulation par modules
Chaque module expose clairement son API publique via `__init__.py`

### Hiérarchie et héritage
```
modeles/pions/
    ├── pion.py (Classe abstraite)
    ├── pion_simple.py (Hérite de Pion)
    └── dame.py (Hérite de Pion)
```

### Composition
```
Jeu
 └── Plateau
      └── List[Pion]
           ├── PionSimple
           └── Dame
```

## 🔧 Avantages de cette structure

### ✅ Maintenabilité
- Chaque classe dans son propre fichier
- Facile à localiser et modifier

### ✅ Réutilisabilité
- Les modules peuvent être importés indépendamment
- Exemple : `Position` peut être utilisée dans d'autres projets

### ✅ Testabilité
- Chaque composant peut être testé isolément
- Structure adaptée pour les tests unitaires

### ✅ Scalabilité
- Facile d'ajouter de nouvelles classes
- Structure claire pour l'extension

### ✅ Collaboration
- Plusieurs développeurs peuvent travailler simultanément
- Moins de conflits Git

## 📖 Correspondance avec les concepts théoriques

| Concept | Localisation |
|---------|--------------|
| Classes et objets | Tous les fichiers `.py` |
| Héritage | `modeles/pions/` |
| Classe abstraite | `pion.py` |
| Encapsulation | Tous les modèles |
| Public/Protected/Private | Attributs dans les classes |
| Getters/Setters | `Position`, `Mouvement`, `Pion` |
| Composition | `Plateau` contient des `Pion` |
| Méthodes statiques | `ValidateurMouvement`, `Position.depuis_notation()` |
| Polymorphisme | `Pion` → `PionSimple` / `Dame` |

## 🎓 Exercices

Pour vous entraîner avec cette structure :

1. **Ajouter un nouveau type de pion** : Créez `super_dame.py` dans `modeles/pions/`
2. **Ajouter des statistiques** : Créez `statistiques.py` dans `logique/`
3. **Améliorer l'affichage** : Créez `affichage.py` dans `interface/`
4. **Ajouter des tests** : Créez `tests/` à la racine
5. **Sauvegarder les parties** : Créez `sauvegarde.py` dans `logique/`

## 💡 Comparaison : Monolithique vs Modulaire

### Version monolithique (`jeu_dames.py`)
```
✅ Tout dans un fichier
✅ Simple pour démarrer
❌ Difficile à maintenir
❌ Difficile à tester
❌ Difficile à réutiliser
```

### Version modulaire (`src/`)
```
✅ Organisation claire
✅ Facile à maintenir
✅ Facile à tester
✅ Réutilisable
❌ Plus de fichiers à gérer
```

---

**Cette structure démontre les bonnes pratiques de développement logiciel tout en restant accessible et compréhensible pour l'apprentissage ! 🚀**
