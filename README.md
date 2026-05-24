# Facteurs influençant les résultats académiques des étudiant·es

> Projet d'étude statistique – SM403 Analyse de données  
> EFREI Paris – Cycle préparatoire P2 – Semestre de printemps 2026

[![Compiler le rapport PDF](https://github.com/Tezay/academic-performance-statistics/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/Tezay/academic-performance-statistics/actions/workflows/build-pdf.yml)
&nbsp;
**[⬇ Télécharger le rapport (PDF)](https://github.com/Tezay/academic-performance-statistics/releases/latest/download/rapport.pdf)**

---

## Contexte du projet

Ce projet s'inscrit dans le module **SM403 – Introduction à l'Analyse de données**. L'objectif est d'analyser, à l'aide des outils de **statistiques inférentielles** vus en cours, les facteurs de la vie quotidienne susceptibles d'influencer les résultats académiques des étudiant·es de P1 à l'EFREI.

La démarche :
1. Un **sondage Google Forms** a été conçu par nos classes de P2, administré aux classes P1.
2. Les résultats sont analysés via les outils du cours : statistiques descriptives, intervalles de confiance, tests de conformité et tests du χ².
3. Les conclusions font l'objet d'un **rapport LaTeX de 4 pages maximum** et d'une **soutenance orale de 10 minutes**.

---

## Technologies utilisées

| Outil | Rôle |
|---|---|
| **LaTeX** | Rédaction du rapport scientifique |
| **TeXstudio** | Éditeur LaTeX (coloration syntaxique, compilation intégrée) |
| **MiKTeX** *(Windows)* / **MacTeX** *(macOS)* | Distribution LaTeX (compilateur pdfLaTeX + packages) |
| **GitHub** | Versionnement du dépôt |

---

## Installer l'environnement LaTeX

### Sur Windows

1. **Installer MiKTeX** (distribution LaTeX pour Windows) :
   - Télécharger l'installateur sur [miktex.org/download](https://miktex.org/download)
   - Lancer l'installateur et choisir « Install for all users » (recommandé)
   - Cocher **« Install missing packages on-the-fly: Yes »** – MiKTeX téléchargera automatiquement les packages manquants à la première compilation

2. **Installer TeXstudio** (éditeur) :
   - Télécharger sur [texstudio.org](https://www.texstudio.org/)
   - Lancer l'installateur (accepter les options par défaut)

3. **Configurer TeXstudio** :
   - Ouvrir TeXstudio → menu **Options > Configurer TeXstudio**
   - Onglet **Compilation** → vérifier que « Compilateur par défaut » est sur **pdfLaTeX**
   - Onglet **Compilation** → vérifier que « Visionneuse PDF par défaut » est sur **Visionneuse intégrée** (ou SumatraPDF si installé)

### Sur macOS

**Option A – via Homebrew (recommandé si Homebrew est installé) :**
```bash
# Installer MacTeX (distribution LaTeX complète, ~5 Go)
brew install --cask mactex

# Installer TeXstudio
brew install --cask texstudio
```

**Option B – installateurs graphiques :**
1. **MacTeX** : télécharger le `.pkg` sur [tug.org/mactex](https://www.tug.org/mactex/) et lancer l'installation
2. **TeXstudio** : télécharger sur [texstudio.org](https://www.texstudio.org/) et glisser l'application dans `/Applications`

> Après installation de MacTeX, fermer et rouvrir le terminal pour que `pdflatex` soit disponible dans le `PATH`.

**Vérifier l'installation :**
```bash
pdflatex --version
# doit afficher : pdfTeX 3.14... (TeX Live 20XX/MacTeX)
```

---

## Utiliser le projet

### 1. Cloner le dépôt

```bash
git clone https://github.com/Tezay/academic-performance-statistics.git
cd academic-performance-statistics
```

### 2. Ouvrir le rapport dans TeXstudio

- Lancer **TeXstudio**
- **Fichier > Ouvrir** → naviguer jusqu'à `rapport/main.tex`
- TeXstudio détecte automatiquement `main.tex` comme fichier maître

### 3. Compiler le rapport

- Appuyer sur **F5** (ou le bouton ▶ vert) pour compiler et afficher le PDF
- Le PDF généré s'affiche dans la visionneuse intégrée à droite
- En cas d'erreur : consulter le panneau « Messages / Log »

> La première compilation peut télécharger quelques packages (MiKTeX uniquement) – accepter les invitations.

### 4. Travailler sur une section

Chaque membre travaille sur **son fichier de section** dans `rapport/sections/` (voir [GUIDE.md](GUIDE.md)).  
Ne pas modifier `main.tex` ou `preambule.tex` sans concertation.

### 5. Versionner ses modifications

```bash
git add .
git commit -m "feat: rédiger statistiques descriptives variables quantitatives"
git push
```

---

## Structure du dépôt

```
academic-performance-statistics/
│
├── rapport/                    # Source LaTeX du rapport
│   ├── main.tex                # Fichier maître (à compiler)
│   ├── preambule.tex           # Packages et macros LaTeX
│   ├── sections/
│   │   ├── 01_cadre.tex        # Section 1 – Cadre de l'étude
│   │   ├── 02_formulation.tex  # Section 2 – Formulation statistique
│   │   ├── 03_methodologie.tex # Section 3 – Choix méthodologiques
│   │   ├── 04_analyse.tex      # Section 4 – Analyse des données
│   │   └── 05_interpretation.tex # Section 5 – Interprétation
│   ├── figures/                # Graphiques générés (PNG/PDF)
│   └── annexes/                # Fichiers d'annexes .tex
│
├── data/                       # Données des sondages (versionnées)
│   ├── README.md               # Dictionnaire des variables
│   ├── ADD_PP1_PP2.csv         # Sondage classes PP1 et PP2
│   ├── ADD_SC1_SC2.csv         # Sondage classes SC1 et SC2
│   ├── ADD_SC3_SC4.csv         # Sondage classes SC3 et SC4 ← principal
│   └── ADD_SC5_SC6.csv         # Sondage classes SC5 et SC6
├── GUIDE.md                    # Guide de travail - répartition en 5 parties
└── README.md                   # Ce fichier
```

---

## Ressources utiles

- **Guide de travail** : [GUIDE.md](GUIDE.md)
- **Données** : [data/README.md](data/README.md)
- Documentation LaTeX : [fr.overleaf.com/learn](https://fr.overleaf.com/learn)
- Table de la loi de Student : annexe 5.1 du cours
- Table du χ² : annexe 5.3 du cours
