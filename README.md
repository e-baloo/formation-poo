# Formation POO - Programmation Orientée Objet

Bienvenue dans cette formation complète sur la Programmation Orientée Objet (POO) ! 🎓

Cette formation est divisée en deux parties :
1. **Théorie** : Concepts fondamentaux avec du pseudo-code agnostique
2. **Pratique** : Jeu de Dames complet en Python démontrant tous les concepts

## 📚 Table des matières

### 🎯 Partie théorique

Les exemples théoriques utilisent du **pseudo-code agnostique** de tout langage de programmation pour se concentrer sur les concepts, pas sur les détails d'implémentation.

1. [**Pourquoi la POO ?**](theorie/01-pourquoi-la-poo.md)
   - Les limites de la programmation procédurale
   - Les apports de la POO
   - Quand utiliser la POO

2. [**La Classe : un contrat**](theorie/02-la-classe-un-contrat.md)
   - Qu'est-ce qu'une classe ?
   - Structure d'une classe
   - Instanciation et objets
   - Cohésion et responsabilité unique

3. [**L'héritage**](theorie/03-heritage.md)
   - Principe de l'héritage
   - Relation "est-un"
   - Redéfinition de méthodes
   - Classes abstraites
   - Polymorphisme

4. [**Les Interfaces**](theorie/04-interfaces.md)
   - Qu'est-ce qu'une interface ?
   - Différence avec les classes abstraites
   - Implémentation multiple
   - Contrats et polymorphisme

5. [**Public, Protected, Private**](theorie/05-public-protected-private.md)
   - Les trois niveaux de visibilité
   - Encapsulation
   - Principes de conception
   - Bonnes pratiques

6. [**Les Getters et Setters**](theorie/06-getters-setters.md)
   - Pourquoi utiliser des getters/setters ?
   - Validation et transformation
   - Propriétés calculées
   - Cas d'usage avancés

7. [**Les méthodes et attributs statiques**](theorie/07-static.md)
   - Qu'est-ce que le static ?
   - Attributs statiques (de classe)
   - Méthodes statiques
   - Instance vs Static : quand utiliser quoi ?

8. [**L'opérateur instanceof**](theorie/08-instanceof.md)
   - Vérification du type d'un objet
   - Polymorphisme et downcasting sécurisé
   - Filtrage par type
   - Bonnes pratiques et alternatives

### 🎮 Partie pratique

Le cas pratique est un **jeu de Dames** complet implémenté en Python, démontrant **tous** les concepts de la POO vus en théorie.

- [**Jeu de Dames**](pratique/README.md)
  - Code Python complet et commenté
  - Affichage dans le terminal
  - Démonstration de tous les concepts POO
  - Exercices d'extension

## 🚀 Comment utiliser cette formation

### Parcours recommandé

1. **Lisez la théorie dans l'ordre** (chapitres 1 à 6)
   - Chaque chapitre construit sur les précédents
   - Prenez le temps de comprendre les exemples en pseudo-code

2. **Étudiez le code du jeu de Dames**
   - Lisez d'abord le [README pratique](pratique/README.md)
   - Parcourez le code source `jeu_dames.py`
   - Identifiez où chaque concept est utilisé

3. **Jouez et expérimentez**
   - Lancez le jeu : `python pratique/jeu_dames.py`
   - Testez les fonctionnalités
   - Modifiez le code pour voir les effets

4. **Faites les exercices d'extension**
   - Proposés dans le README pratique
   - Mettez en pratique ce que vous avez appris

### Pour les formateurs

Cette formation peut être présentée :
- **En présentiel** : 1 jour (6-8 heures)
  - Matin : Théorie (chapitres 1-8)
  - Après-midi : Étude du cas pratique + exercices

- **En e-learning** : À votre rythme
  - 1 heure par chapitre théorique
  - 2-3 heures pour le cas pratique

- **En atelier** : Focus pratique
  - Présentation rapide des concepts (1h)
  - Étude collaborative du code (2-3h)

## 🎯 Objectifs pédagogiques

À l'issue de cette formation, vous serez capable de :

✅ **Comprendre** les principes fondamentaux de la POO
✅ **Identifier** quand et pourquoi utiliser la POO
✅ **Concevoir** des classes cohérentes et bien structurées
✅ **Utiliser** l'héritage de manière appropriée
✅ **Créer** des interfaces pour définir des contrats
✅ **Appliquer** l'encapsulation (public/protected/private)
✅ **Implémenter** des getters/setters avec validation
✅ **Maîtriser** le polymorphisme
✅ **Lire et comprendre** du code POO existant
✅ **Développer** une application complète en POO

## 📊 Correspondance Théorie ↔ Pratique

| Concept théorique | Où le trouver dans le jeu de Dames |
|-------------------|-------------------------------------|
| Classe et objets | `Position`, `Mouvement` |
| Classe abstraite | `Pion` (ABC) |
| Héritage | `PionSimple` et `Dame` héritent de `Pion` |
| Interfaces | `Pion` définit un contrat (méthodes abstraites) |
| Public | Méthodes comme `get_ligne()`, `jouer()` |
| Protected | Attributs `_couleur`, `_position` dans `Pion` |
| Private | Attributs `__ligne`, `__pions` |
| Getters | `get_ligne()`, `get_couleur()` |
| Setters | `set_ligne()`, `set_position()` |
| Polymorphisme | `obtenir_symbole()` selon le type de pion |
| Composition | `Plateau` contient des `Pion` |
| Encapsulation | Validation dans `Position`, `Plateau` |

## 🛠️ Prérequis

### Pour la partie théorique
- Aucun prérequis spécifique
- Bases de programmation recommandées

### Pour la partie pratique
- **Python 3.7+** installé
- Éditeur de code (VS Code, PyCharm, etc.)
- Terminal/console

### Installation Python

Si Python n'est pas installé :
- **Windows** : https://www.python.org/downloads/
- **Mac** : `brew install python3`
- **Linux** : `sudo apt install python3`

Vérifier l'installation :
```bash
python --version
# ou
python3 --version
```

## 📂 Structure du projet

```
formation-poo/
│
├── README.md                           # Ce fichier
│
├── theorie/                            # Partie théorique
│   ├── 01-pourquoi-la-poo.md
│   ├── 02-la-classe-un-contrat.md
│   ├── 03-heritage.md
│   ├── 04-interfaces.md
│   ├── 05-public-protected-private.md
│   ├── 06-getters-setters.md
│   ├── 07-static.md
│   └── 08-instanceof.md
│
└── pratique/                           # Partie pratique
    ├── README.md                       # Documentation du jeu
    └── jeu_dames.py                    # Code complet du jeu
```

## 🎓 Concepts POO couverts

### Concepts de base
- [x] Classes et objets
- [x] Attributs et méthodes
- [x] Constructeur
- [x] Instanciation

### Concepts intermédiaires
- [x] Héritage simple
- [x] Redéfinition de méthodes (override)
- [x] Classe abstraite
- [x] Encapsulation (public/protected/private)
- [x] Getters et setters

### Concepts avancés
- [x] Polymorphisme
- [x] Composition vs héritage
- [x] Interfaces (via classes abstraites)
- [x] Méthodes abstraites
- [x] Séparation des responsabilités
- [x] Validation et intégrité des données

## 🎮 Le jeu de Dames

Le cas pratique est un jeu de Dames avec :
- ✅ Plateau 10x10 avec affichage dans le terminal
- ✅ Pions simples et dames
- ✅ Déplacements et captures
- ✅ Promotion automatique en dame
- ✅ Validation complète des règles
- ✅ Interface utilisateur textuelle
- ✅ Gestion des tours et fin de partie

### Démo rapide

```bash
cd pratique
python jeu_dames.py
```

```
==================================================
               🎮 JEU DE DAMES 🎮
==================================================
Tour n°1
Joueur actuel : BLANC

Pions blancs (⚪): 20  |  Pions noirs (⚫): 20

   A B C D E F G H I J
  +--------------------+
10|⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫|10
 9|⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫ ⚫|9
 8|· · · · · · · · · ·|8
 7|· · · · · · · · · ·|7
 6|· · · · · · · · · ·|6
 5|· · · · · · · · · ·|5
 4|· · · · · · · · · ·|4
 3|⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪|3
 2|⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪|2
 1|· · · · · · · · · ·|1
  +--------------------+
   A B C D E F G H I J

Entrez votre mouvement (ex: A3 B4) ou 'q' pour quitter :
```

## 📖 Ressources complémentaires

### Documentation
- Tous les chapitres sont commentés et expliqués
- Le code Python est abondamment documenté
- Exemples concrets pour chaque concept

### Pour aller plus loin
- Consultez les exercices d'extension dans [pratique/README.md](pratique/README.md)
- Expérimentez avec le code
- Créez vos propres variations

## 🤝 Contributions

Cette formation est un support pédagogique. N'hésitez pas à :
- Signaler des erreurs ou imprécisions
- Proposer des améliorations
- Partager vos exercices d'extension
- Adapter le contenu à vos besoins

## 📝 Licence et utilisation

Ce contenu est fourni à des fins éducatives. Vous êtes libre de :
- L'utiliser pour vous former
- Le partager avec d'autres apprenants
- L'adapter à vos besoins de formation

## ✨ Conclusion

La POO est un paradigme puissant qui permet de :
- Structurer le code de manière intuitive
- Modéliser des concepts du monde réel
- Réutiliser et maintenir le code facilement
- Collaborer efficacement en équipe

Cette formation vous donne les clés pour maîtriser ces concepts et les appliquer dans vos projets.

**Bonne formation ! 🚀**

---

*Dernière mise à jour : Novembre 2025*