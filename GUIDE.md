# Guide de travail – SM403 Analyse de données

> **Règle absolue** : toute démarche mathématique et scientifique doit s'appuyer exclusivement sur le **cours SM403** (`ressources/COURS.pdf`). Lire les définitions et points méthode correspondants **avant** de rédiger.

**Rendu Moodle : samedi 30 mai 2026 à 23h59** – fichier nommé `ADD-SC3-4-1>.pdf`  
**Soutenance** : 10 min de présentation + 20 min de questions individuelles  
**Format rapport** : 4 pages maximum (hors annexes), LaTeX

---

## Vue d'ensemble – Dépendances entre parties

```
Partie 1 ──────────────────────────────────────┐
Partie 2 (stats desc. quant.)  ──────────────┐ │
Partie 3 (stats desc. qual. + formulation)   │ │
         └──► Partie 4 (IC + conformité)     │ │
         └──► Partie 5 (χ² + interprétation) ┘ ┘
```

Les parties 1, 2 et 3 sont **totalement indépendantes** et peuvent démarrer immédiatement en parallèle.  
Les parties 4 et 5 nécessitent que les hypothèses H0/H1 (Partie 3) soient formulées – prévoir 2 à 3 jours.

---

## Partie 1 – Cadre de l'étude + nettoyage des données

**Responsable : Membre 1**  
**Fichiers à modifier** : `rapport/sections/01_cadre.tex`, `data/README.md`  
**Peut démarrer immédiatement.**

### Étapes

#### 1.1 Lire et comprendre les données

- Ouvrir `data/ADD_SC3_SC4.csv` (sondage principal, n = 72 réponses)
- Identifier chaque colonne : nom de variable, type, plage de valeurs
- Parcourir également les trois autres CSV pour comprendre le contexte global (307 réponses au total)

#### 1.2 Décrire la population et l'échantillon

En s'appuyant sur la **Définition 1.1** du cours (individus, population, échantillon, effectif total) :

- **Population cible** : l'ensemble des étudiant·es de P1 EFREI ayant effectué le semestre 1 à l'EFREI dans les classes SC5, SC6, SC7 et BDX
- **Échantillon principal** : les n = 72 répondant·es du sondage SC3/SC4 ayant coché "Oui" à la question de présence à l'EFREI
- Préciser le mode de recueil (Google Forms, anonyme, diffusion par le département de mathématiques)
- Discuter si l'échantillon est représentatif (tirage aléatoire ou non ?)

#### 1.3 Classifier chaque variable (Définition 1.3 du cours)

Pour **chaque colonne** du CSV, préciser dans `data/README.md` :

| Variable | Type | Modalités / Plage | Rôle |
|---|---|---|---|
| Annales travaillées | Quantitative discrète | 0 à 4+ | Habitudes de travail |
| Équilibre vie/études | Qualitative ordinale | 1 à 5 | Bien-être |
| ... | ... | ... | ... |

Rappel des types (Déf. 1.3) :
- **Qualitative** : modalités nommées (ex. : "Jamais", "Rarement"…) – peut être **ordinale** si les modalités ont un ordre naturel
- **Quantitative** : valeur numérique, **discrète** (entiers) ou **continue** (réels)

#### 1.4 Identifier les valeurs aberrantes et manquantes

- Repérer les lignes avec des réponses incohérentes ou manquantes
- Repérer les étudiant·es ayant répondu "Non" à "Avez-vous fait le semestre à l'EFREI ?" → **exclure ces lignes de l'analyse**
- Noter le nombre de réponses retenues après nettoyage

#### 1.5 Lister les biais potentiels

- **Biais de sélection** : seul·es les étudiant·es qui ont répondu volontairement sont inclus·es
- **Biais de déclaration** : les réponses sont auto-évaluées (ex. : "combien d'heures dormez-vous ?")
- **Biais de non-réponse** : certaines questions peuvent avoir été laissées vides
- **Biais de désirabilité sociale** : tendance à se présenter sous un jour favorable

#### 1.6 Rédiger en LaTeX

- Remplir `rapport/sections/01_cadre.tex` (section 1 du rapport)
- Remplir `data/README.md` (dictionnaire complet des variables – utile pour tous les membres)
- Limiter à environ **0,5 page** dans le rapport final (contrainte des 4 pages)

---

## Partie 2 – Statistiques descriptives (variables quantitatives)

**Responsable : Membre 2**  
**Fichiers à modifier** : `rapport/sections/04_analyse.tex` (sous-section 4.1), `rapport/figures/`  
**Peut démarrer immédiatement** – s'appuyer sur `data/ADD_SC3_SC4.csv`.

### Étapes

#### 2.1 Identifier les variables quantitatives

À partir de `data/README.md` (fourni par Membre 1, ou à identifier soi-même), lister les variables quantitatives du sondage SC3/SC4. Exemples attendus : nombre d'annales travaillées, heures de sommeil, jours de révision avant DE, etc.

#### 2.2 Calculer les paramètres de tendance centrale (Chapitre 1 du cours)

Pour chaque variable quantitative :

- **Moyenne empirique** x̄ (Définition 1.4) : x̄ = (1/n) Σ xᵢ
- **Médiane** Me (Définition 1.5) : valeur centrale après tri – si n pair : moyenne des rangs n/2 et n/2+1 ; si n impair : valeur au rang (n+1)/2 (Point méthode 1.1)
- **Quartiles** Q1 et Q3 (Définition 1.6) – Point méthode 1.2
- **Mode** Mo (Définition 1.7)

#### 2.3 Calculer les paramètres de dispersion (Chapitre 1 du cours)

- **Variance empirique** σ² (Définition 1.9) : σ² = (1/n) Σ(xᵢ − x̄)² = x̄² − x̄²  
  *Nota bene* : utiliser aussi la formule σ² = x² − x̄² (démontrée dans le cours)
- **Écart-type** σ (même définition)
- **Fréquences** fᵢ = nᵢ/n (Définition 1.8)
- **Variable centrée réduite** (Définition 1.11) si pertinent pour comparer des variables d'unités différentes

#### 2.4 Calculer les corrélations avec la variable de performance

Choisir une variable de performance académique (ex. : note de bac en maths, résultats académiques à l'EFREI si disponible).

Pour chaque autre variable quantitative, calculer le **coefficient de corrélation** r (Définition 1.16) :

r = Cov(X, Y) / (σₓ × σᵧ)

avec Cov(X, Y) = (1/n) Σ(xᵢ − x̄)(yᵢ − ȳ) (Définition 1.15).

Interpréter : |r| proche de 1 → forte corrélation linéaire ; r proche de 0 → pas de corrélation linéaire.

#### 2.5 Produire les représentations graphiques

Pour chaque variable quantitative :
- **Histogramme** (classes d'égale amplitude) – voir Figure 1.3 du cours pour l'exemple
- **Boîte à moustaches** (box-plot) avec Q1, Me, Q3, moustaches = min/max hors valeurs aberrantes

Sauvegarder les figures en PNG ou PDF dans `rapport/figures/`. Exemple : `rapport/figures/hist_annales.png`.

Inclure dans LaTeX avec :
```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.45\textwidth]{figures/hist_annales.png}
  \caption{Distribution du nombre d'annales travaillées (n = 72)}
\end{figure}
```

#### 2.6 Rédiger en LaTeX

- Remplir la sous-section `\subsection{Statistiques descriptives --- variables quantitatives}` dans `04_analyse.tex`
- Présenter les résultats dans des tableaux (`booktabs`) avec x̄, Me, Q1, Q3, σ, r
- Citer les définitions du cours (ex. : "selon la Définition 1.9...")

---

## Partie 3 – Statistiques descriptives (qualitatives) + Formulation statistique

**Responsable : Membre 3**  
**Fichiers à modifier** : `rapport/sections/02_formulation.tex`, sous-section 4.2 de `04_analyse.tex`  
**Peut démarrer immédiatement.**

### Étapes

#### 3.1 Statistiques descriptives – variables qualitatives

Pour chaque variable qualitative du sondage SC3/SC4 :

- Construire le **tableau de fréquences** (effectifs nᵢ et fréquences fᵢ = nᵢ/n, Définition 1.8)
- Identifier le **mode** Mo (Définition 1.7 – modalité la plus fréquente)
- Produire un **diagramme à bâtons** ou **diagramme circulaire** selon la nature de la variable (voir Figure 1.2 du cours)
- Sauvegarder les figures dans `rapport/figures/`

#### 3.2 Expliquer l'intérêt de la formulation statistique

Rédiger un court paragraphe expliquant pourquoi reformuler une question intuitive en termes de paramètres statistiques est nécessaire :
- Une question comme "les étudiant·es qui dorment davantage ont-ils de meilleurs résultats ?" ne peut pas recevoir de réponse "vrai ou faux" directe sur un échantillon
- Il faut définir un paramètre (proportion p ou moyenne µ), formuler H0/H1, et conclure au risque α – c'est la méthode scientifique (§ 3.3 du cours)

#### 3.3 Définir les paramètres d'intérêt

Pour **chaque question statistique** envisagée dans le projet, définir :
- Le **paramètre** testé : proportion π (si variable qualitative binaire) ou moyenne m (si variable quantitative)
- La **valeur de référence** p ou µ sous H0 (à justifier : peut être une valeur théorique, la proportion dans la population globale, etc.)

Exemples :
- "La proportion d'étudiant·es assistant à tous les CMs est-elle différente de 50 % ?" → π vs p = 0,5
- "La moyenne de notes de bac en sciences diffère-t-elle d'une valeur de référence ?" → m vs µ = valeur choisie

#### 3.4 Formuler les hypothèses H0 et H1 (≥ 3 tests)

Pour **chaque test** envisagé, écrire :

| Test | H0 | H1 | Bilatéral / Unilatéral | Type de test |
|---|---|---|---|---|
| Test 1 | π = p₀ | π ≠ p₀ | Bilatéral | Conformité proportion |
| Test 2 | m = µ₀ | m > µ₀ | Unilatéral | Conformité moyenne |
| Test 3 | L₀ = L | L₀ ≠ L | – (unilatéral) | χ² de conformité |
| Test 4 | X et Y indépendantes | X et Y dépendantes | – (unilatéral) | χ² d'indépendance |

**Définitions à appliquer** : Définition 3.1 (H0/H1), Définition 3.2 (unilatéral/bilatéral) du cours.

#### 3.5 Rédiger en LaTeX

- Remplir `rapport/sections/02_formulation.tex`
- Remplir la sous-section 4.2 de `04_analyse.tex` (tableaux et figures des variables qualitatives)
- Cible : environ **0,5 page** pour la section 2, **0,5 page** pour la partie 4.2

---

## Partie 4 – Méthodologie + Intervalles de confiance + Tests de conformité

**Responsable : Membre 4**  
**Fichiers à modifier** : `rapport/sections/03_methodologie.tex`, sous-sections 4.3 et 4.4 de `04_analyse.tex`  
**Démarrer dès que Partie 3 a formulé les hypothèses H0/H1 (2–3 jours).**

### Étapes

#### 4.1 Rédiger les choix méthodologiques (Section 3 du rapport)

Pour chaque test retenu (liste fournie par Partie 3), justifier :

- **Pourquoi Student et non normale ?** → σ inconnu dans la population → on estime σ avec la **variance estimée** Se² = n/(n−1) × σ²obs (cours § 2.3.1) → statistique T(n−1) ; si σ est connu → loi N(0,1)
- **Pourquoi conformité et non indépendance ?** → on compare un échantillon à une valeur de référence (pas deux variables entre elles)
- **Pourquoi χ² et non conformité classique ?** → variable qualitative à plus de deux modalités

Présenter un tableau récapitulatif :

| Test | Outil | Loi sous H0 | Condition de validité |
|---|---|---|---|
| Conformité proportion | § 3.4.1 | N(0,1) | n≥30, np≥5, n(1−p)≥5 |
| Conformité moyenne | § 3.4.1 | T(n−1) | n≥30 |
| χ² conformité | § 3.4.2 | χ²(k−1) | n≥50, nᵢ≥5 |
| χ² indépendance | § 3.4.2 | χ²((k₁−1)(k₂−1)) | n≥50, nᵢⱼ≥5 |

**Si les conditions ne sont pas réunies** (ce qui peut arriver avec n=72) : le signaler explicitement, présenter quand même le test en mentionnant la limite de validité – conformément à la consigne du professeur.

#### 4.2 Calculer les intervalles de confiance de la proportion

Appliquer la **Définition 2.11** du cours pour les sous-groupes pertinents.

Formule : IC = [ p₀ − √(p₀(1−p₀)/n) × zα ; p₀ + √(p₀(1−p₀)/n) × zα ]

Conditions : n ≥ 30, np₀ ≥ 5, n(1−p₀) ≥ 5

Pour chaque IC calculé :
1. Identifier la proportion p₀ observée dans l'échantillon
2. Vérifier les conditions
3. Choisir le risque α (souvent 5 %)
4. Lire zα dans la table de la loi Normale (Annexe 5.2 du cours) : z₅% = 1,96
5. Calculer et interpréter l'intervalle en langage courant

#### 4.3 Calculer les intervalles de confiance de la moyenne

Appliquer la **Définition 2.14** du cours.

Formule : IC = [ x̄ − (σe/√n) × t_{n−1,α} ; x̄ + (σe/√n) × t_{n−1,α} ]

avec σe = √(Se²) et Se² = (n/(n−1)) × σ²obs (variance estimée, § 2.3.1)

Lire t_{n−1,α} dans la **table de Student bilatérale** (Annexe 5.1 du cours) avec n−1 degrés de liberté.

#### 4.4 Conduire les tests de conformité (§ 3.4.1 du cours)

Pour **chaque test de conformité**, suivre rigoureusement la **méthodologie en 5 étapes** (§ 3.2.2) :

1. **Définir H0 et H1** (reprendre la formulation de Partie 3)
2. **Distribution sous H0** : préciser la loi (N(0,1) ou T(n−1))
3. **Région critique** : intervalle [−zα; +zα] en bilatéral, ou seuil z₂α en unilatéral
4. **Calculer le critère** :
   - Proportion : z = (p₀ − p) / √(p(1−p)/n)
   - Moyenne : t = (x̄ − µ) / (σe/√n)
5. **Conclure** : critère dans la région → ne pas rejeter H0 ; hors région → rejeter H0

Présenter chaque test dans un cadre clair dans le rapport.

---

## Partie 5 – Tests du χ² + Interprétation + Conclusion

**Responsable : Membre 5**  
**Fichiers à modifier** : fin de `04_analyse.tex` (sous-section 4.5), `rapport/sections/05_interpretation.tex`  
**Démarrer dès que Partie 3 a formulé les hypothèses H0/H1 (2–3 jours).**

### Étapes

#### 5.1 Tests du χ² de conformité (§ 3.4.2 du cours)

Pour une variable qualitative à k modalités, tester si sa distribution suit une loi de référence L.

H0 : "la distribution de X dans la population suit la loi L"  
H1 : "la distribution de X ne suit pas L"

**Étapes** (§ 3.2.2 du cours) :
1. H0 / H1
2. Distribution sous H0 : loi χ²(k−1)
3. Trouver le seuil χ²_{k−1, α} dans la table du χ² (Annexe 5.3 du cours)
4. Construire le tableau des effectifs observés oᵢ et théoriques nᵢ = n × P(X ∈ classe i | loi L)
5. Calculer le critère : χ² = Σ (oᵢ − nᵢ)² / nᵢ
6. Conclure : critère < seuil → ne pas rejeter H0 ; critère > seuil → rejeter H0

**Conditions de validité** : n ≥ 50 et nᵢ ≥ 5 pour toutes les classes.  
Si non vérifiées : le préciser et présenter quand même le test (consigne prof).

#### 5.2 Tests du χ² d'indépendance (§ 3.4.2 du cours)

Tester si deux variables qualitatives X et Y sont indépendantes dans la population.

H0 : "X et Y sont indépendantes"  
H1 : "X et Y sont dépendantes" (= il existe une association)

**Étapes** :
1. H0 / H1
2. Construire le **tableau de contingence observé** (lignes = modalités de X, colonnes = modalités de Y, cellule = effectif observé oᵢⱼ)
3. Calculer les effectifs théoriques sous H0 :

   nᵢⱼ = (oᵢ,• × o•,ⱼ) / n

   avec oᵢ,• = total ligne i et o•,ⱼ = total colonne j

4. Vérifier conditions : n ≥ 50 et nᵢⱼ ≥ 5
5. Trouver le seuil χ²_{(k₁−1)(k₂−1), α} dans la table du χ² (Annexe 5.3)
6. Calculer : χ² = Σᵢ Σⱼ (oᵢⱼ − nᵢⱼ)² / nᵢⱼ
7. Conclure

> Présenter les deux tableaux (observé et théorique) côte à côte dans le rapport pour faciliter la lecture.

Exemple de paires de variables intéressantes à tester :
- Fréquence de révision × résultats académiques
- Participation aux CMs × note de bac en sciences
- Implication associative × équilibre vie/études

#### 5.3 Interprétation des résultats en langage courant

Pour chaque test (parties 4 et 5), rédiger **une ou deux phrases** traduisant la conclusion statistique :

- "Au risque de 5 %, on rejette H0 : il existe une association significative entre [X] et [Y]."
- "Au risque de 5 %, on ne peut pas rejeter H0 : aucune association significative n'est mise en évidence entre [X] et [Y]."

#### 5.4 Distinction association statistique / causalité – OBLIGATOIRE

Ce point est **explicitement exigé par le sujet**. Développer pour chaque résultat significatif :

- Reformuler la conclusion en termes d'**association** et non de causalité
- Identifier des **variables confondantes** possibles (ex. : un facteur tiers qui expliquerait les deux variables à la fois)
- Citer le sujet : "la distinction entre association statistique et causalité doit être discutée"

Exemple :
> "On observe une association significative entre le nombre d'annales travaillées et les résultats académiques. Cependant, on ne peut pas conclure que travailler plus d'annales *cause* de meilleurs résultats : d'autres facteurs (motivation générale, niveau initial) pourraient expliquer simultanément les deux."

#### 5.5 Limites de l'étude

- **Taille de l'échantillon** : n = 72 rend certains tests χ² fragiles (condition nᵢⱼ ≥ 5 difficile à satisfaire pour des tableaux à nombreuses modalités)
- **Validité externe** : les résultats sont valides pour la population échantillonnée (P1 EFREI SC5/SC6/SC7/BDX) ; la généralisation à d'autres établissements n'est pas garantie
- **Qualité des questions** : variables mesurées sur des échelles ordinales (1 à 5) traitées parfois comme quantitatives
- **Auto-déclaration** : les réponses reflètent la perception des étudiant·es, pas des mesures objectives

#### 5.6 Conclusion générale

- Résumer en 3 à 5 phrases les principales conclusions de l'étude
- Répondre à la problématique initiale (quels facteurs sont associés aux résultats académiques ?)
- Ouvrir sur ce que l'étude ne peut pas trancher (causalité, autres facteurs)

---

## Calendrier suggéré

| Étape | Tâche | Responsable | Délai suggéré |
|---|---|---|---|
| J0 | Cloner le dépôt, lire le cours (Ch. 1–3) | Tous | Immédiatement |
| J0–J2 | Parties 1, 2, 3 en parallèle | M1, M2, M3 | 2 jours |
| J2 | Partager data/README.md + liste des H0/H1 | M1 + M3 | Fin J2 |
| J2–J5 | Parties 4 et 5 | M4, M5 | 3 jours |
| J5–J6 | Intégration LaTeX, vérification cohérence | Tous | 1–2 jours |
| J6 | Relecture croisée, compilation finale | Tous | La veille du rendu |
| J7 | **Dépôt sur Moodle** | Chef de groupe | 30 mai 23h59 |

---

## Rappel des formules clés du cours (SM403)

> Ces formules ne doivent pas être copiées sans justification dans le rapport.  
> Toujours citer la Définition ou le Théorème du cours correspondant.

### Statistiques descriptives (Chapitre 1)

| Paramètre | Formule | Référence cours |
|---|---|---|
| Moyenne | x̄ = (1/n) Σ xᵢ | Déf. 1.4 |
| Variance | σ² = (1/n) Σ(xᵢ−x̄)² = x²̄ − x̄² | Déf. 1.9 |
| Covariance | Cov(X,Y) = (1/n) Σ(xᵢ−x̄)(yᵢ−ȳ) | Déf. 1.15 |
| Corrélation | r = Cov(X,Y) / (σₓ σᵧ) | Déf. 1.16 |
| Variance estimée | Se² = n/(n−1) × σ²obs | § 2.3.1 |

### Intervalles de confiance (Chapitre 2)

| IC | Formule | Conditions | Référence cours |
|---|---|---|---|
| IC proportion | p₀ ± √(p₀(1−p₀)/n) × zα | n≥30, np₀≥5, n(1−p₀)≥5 | Déf. 2.11 |
| IC moyenne | x̄ ± (σe/√n) × t_{n−1,α} | n≥30 | Déf. 2.14 |

### Tests inférentiels (Chapitre 3)

| Test | Critère | Seuil | Conditions | Référence cours |
|---|---|---|---|---|
| Conformité proportion | z = (p₀−p) / √(p(1−p)/n) | zα (bilatéral) ou z₂α (unilatéral) | n≥30, np≥5, n(1−p)≥5 | § 3.4.1 |
| Conformité moyenne | t = (x̄−µ) / (σe/√n) | t_{n−1,α} (Student) | n≥30 | § 3.4.1 |
| χ² conformité | χ² = Σ(oᵢ−nᵢ)²/nᵢ | χ²_{k−1, α} | n≥50, nᵢ≥5 | § 3.4.2 |
| χ² indépendance | χ² = ΣΣ(oᵢⱼ−nᵢⱼ)²/nᵢⱼ | χ²_{(k₁−1)(k₂−1), α} | n≥50, nᵢⱼ≥5 | § 3.4.2 |

### Valeurs usuelles à connaître (tables en Annexe du cours)

- z₅% = 1,96 (bilatéral, Annexe 5.2)
- z₁₀% = 1,645 (bilatéral)
- z₁% = 2,576 (bilatéral)
- t_{n−1, α} : lire dans la table de Student bilatérale (Annexe 5.1) avec n−1 degrés de liberté
- χ²_{k, α} : lire dans la table du khi-deux (Annexe 5.3)
