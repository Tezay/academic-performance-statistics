# Facteurs influençant les résultats académiques des étudiant·es

> Projet d'étude statistique – SM403 Analyse de données  
> EFREI Paris – Cycle préparatoire P2 – Semestre de printemps 2026

[![Compiler le rapport PDF](https://github.com/Tezay/academic-performance-statistics/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/Tezay/academic-performance-statistics/actions/workflows/build-pdf.yml)
&nbsp;
**[⬇ Télécharger le rapport (PDF)](https://github.com/Tezay/academic-performance-statistics/releases/latest/download/rapport-performance-academique-efrei.pdf)**

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
| **Python 3** | Calcul des statistiques et génération des figures |
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

## Script Python – Calcul des statistiques et génération des figures

Le script `rapport/figures_gen.py` calcule tous les paramètres statistiques du rapport (statistiques descriptives, IC, tests de conformité, tests du χ²) et génère les figures PDF dans `rapport/figures/`.

### Installer les dépendances

```bash
# Créer et activer l'environnement virtuel
python3 -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### Lancer le script

```bash
# Depuis la racine du projet, avec le venv activé
python rapport/figures_gen.py
```

Le script affiche dans le terminal toutes les valeurs numériques (x̄, Me, Q1, Q3, σ², IC, critères de test, χ²_obs) et génère les figures dans `rapport/figures/`. Les figures sont automatiquement incluses dans le rapport LaTeX via `\includegraphics`.

> Les fonctions statistiques implémentant les formules du cours SM403 sont définies dans `rapport/stats_utils.py`.

---

## Compiler le PDF avec LaTeX

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

---

## Structure du dépôt

```
academic-performance-statistics/
│
├── rapport/                      # Source LaTeX du rapport
│   ├── main.tex                  # Fichier maître (à compiler)
│   ├── preambule.tex             # Packages et macros LaTeX
│   ├── figures_gen.py            # Script Python – statistiques et figures
│   ├── stats_utils.py            # Fonctions statistiques (formules du cours)
│   ├── sections/
│   │   ├── 01_cadre.tex          # Section 1 – Cadre de l'étude
│   │   ├── 02_formulation.tex    # Section 2 – Formulation statistique
│   │   ├── 03_methodologie.tex   # Section 3 – Choix méthodologiques
│   │   ├── 04_analyse.tex        # Section 4 – Analyse des données (dispatcher)
│   │   ├── 04a_desc_quantitatives.tex
│   │   ├── 04b_desc_qualitatives.tex
│   │   ├── 04c_intervalles.tex
│   │   ├── 04d_conformite.tex
│   │   ├── 04e_chi2.tex
│   │   └── 05_interpretation.tex # Section 5 – Interprétation et discussion
│   ├── figures/                  # Figures PDF générées par figures_gen.py
│   └── annexes/                  # Fichiers d'annexes .tex
│
├── data/                         # Données des sondages
│   ├── README.md                 # Dictionnaire des variables
│   ├── ADD_SC3_SC4.csv           # Sondage principal (n = 68)
│   └── ADD_SC5_SC6.csv           # Sondage complémentaire (n = 84)
│
├── requirements.txt              # Dépendances Python
└── README.md
```
