# Trame de présentation – SM403 Analyse de données
## Groupe 1 – SC4 | Soutenance ~10 min | 30 mai 2026

> **Mode d'emploi** : ce fichier est une trame narrative diapo par diapo.
> Pour chaque diapo : une accroche à l'oral (en italique), puis le contenu visuel suggéré.
> Le ton est volontairement conversationnel pour la soutenance.

---

## Diapo 1 – Contexte et problématique

**Accroche orale :**
> *"On s'est posé la question que vous vous posez peut-être tous : est-ce que les habitudes de la vie quotidienne – dormir peu, bosser ses annales, aller aux CMs – ont vraiment un impact sur les résultats académiques ? Et si oui, peut-on le prouver statistiquement ?"*

**Contenu visuel :**
- Titre : **"Facteurs influençant les résultats académiques des étudiant·es de P1 EFREI"**
- Sous-titre : *Étude statistique par sondage et inférence – SM403*
- Groupe 1 – SC4 : Eliot Cupillard, Eliot Cousseau, Eliot Masson, Romain Denoual, Edouard Torres
- Visuel : photo/icône salle de cours ou feuille d'exam

---

## Diapo 2 – Notre démarche scientifique

**Accroche orale :**
> *"Pour répondre rigoureusement, on ne pouvait pas simplement dire 'oui' ou 'non' sur un feeling. On a appliqué la méthode scientifique complète : sondage → statistiques descriptives → intervalles de confiance → tests d'hypothèses → conclusions au risque α. On va vous montrer chacune de ces étapes."*

**Contenu visuel :**
Schéma en flèches horizontales :

```
Sondage (n=68)
   ↓
Stats descriptives (moyennes, médianes, distributions)
   ↓
Intervalles de confiance (IC proportion & moyenne)
   ↓
Tests de conformité (proportion & moyenne – loi N(0,1) / Student)
   ↓
Tests du χ² (indépendance entre variables)
   ↓
Conclusions – au risque α = 5 %
```

---

## Diapo 3 – Nos données

**Accroche orale :**
> *"Notre matière première : deux sondages. Le principal, que nos classes SC3/SC4 ont conçu, a recueilli 68 réponses valides auprès de P1. Et pour avoir les vraies notes EFREI – absentes de notre sondage – on a utilisé un second dataset complémentaire qui, lui, les contient."*

**Contenu visuel :**

| Jeu de données | Créateurs | Répondants | n valide | Variables clés |
|---|---|---|---|---|
| ADD_SC3_SC4 | SC3/SC4 (P2) | SC5, SC6, SC7, BDX (P1) | **68** | Habitudes de travail (16 variables) |
| ADD_SC5_SC6 | SC5/SC6 (P2) | P1 divers | 85 | + Moyenne S1, Note Analyse 1 à l'EFREI |

- Mode de recueil : Google Forms anonyme – 14 au 23 avril 2026
- Nettoyage : 71 réponses brutes → 3 exclues (2 « Non » + 1 incomplète) → **N = 68**

---

## Diapo 4 – Nos 4 variables d'étude

**Accroche orale :**
> *"Parmi les 15 variables analysables, on en a sélectionné 4 – une par outil du cours. Ça nous permet de couvrir toute la boîte à outils statistique : intervalles de confiance, tests de conformité, et tests du χ² d'indépendance."*

**Contenu visuel :**

| Variable | Description | Type | Tests associés |
|---|---|---|---|
| **V12** | Moyenne au bac (spé. sci.) | Qual. ordinale | χ² d'indépendance |
| **V2** | Annales travaillées avant CE/DE | Quant. discrète | IC moyenne + conformité (Student) |
| **V14** | Assiduité aux CMs | Qual. ordinale | IC proportion + conformité proportion |
| **V6** | Sommeil avant un DE | Qual. ordinale | Conformité proportion (bilatéral) |

> *"V12 représente le niveau académique initial. V2, V6 et V14 représentent trois habitudes de travail différentes. La question centrale : est-ce que le niveau au bac est indépendant de ces habitudes ?"*

---

## Diapo 5 – Statistiques descriptives (V2 : Annales)

**Accroche orale :**
> *"Avant les tests, on regarde les données. Sur V2 – le nombre d'annales – la majorité des répondants en travaillent 2. La distribution est quasi-symétrique autour de 2."*

**Contenu visuel :**
- Histogramme de V2 (0, 1, 2, 3, 4+) – `rapport/figures/`
- Tableau : x̄ ≈ 2,19 | Me = 2 | Mo = 2 | σ ≈ 0,88 | IC₉₅% = [1,98 ; 2,41]
- Boîte à moustaches (1 valeur aberrante à 0)

---

## Diapo 6 – Statistiques descriptives (V6, V12, V14)

**Accroche orale :**
> *"Pour les variables qualitatives ordinales : on présente les fréquences et le mode. À noter : 81 % des répondants dorment moins de 7 heures avant un DE – ce qui est considéré comme insuffisant."*

**Contenu visuel :**
- 3 diagrammes en barres (V6, V12, V14) côte à côte
- Principales fréquences :
  - V6 : Mo = 4–6 h | 80,9 % dorment < 7 h (n=55/68)
  - V12 : Mo = 12–14 | 58,2 % (n=39/67, anomalie exclue)
  - V14 : Mo = Presque tous | 42,6 % assistent à tous les CMs (n=29/68)

---

## Diapo 7 – Intervalles de confiance

**Accroche orale :**
> *"Maintenant on estime. On cherche à encadrer la vraie proportion (ou moyenne) dans la population avec un niveau de confiance de 95 %."*

**Contenu visuel :**
- IC proportion (V14 – proportion assistant à tous les CMs) :
  - Formule : `IC = p̂ ± √(p̂(1−p̂)/n) × z_α` – *Déf. 2.11*
  - Résultat : IC = [ ___ ; ___ ] à 95 %
- IC moyenne (V2 – nombre moyen d'annales) :
  - Formule : `IC = x̄ ± (σ_e/√n) × t_{n−1,α}` – *Déf. 2.14*
  - Résultat : IC = [ ___ ; ___ ] à 95 %

*[À compléter par Membre 4 – Section 4.3]*

---

## Diapo 8 – Tests de conformité

**Accroche orale :**
> *"On passe aux tests. On applique la méthodologie en 5 étapes du cours – H0, distribution sous H0, région critique, critère, conclusion. Mais avant ça, pourquoi ces valeurs de référence ?"*

**Justification des H₀ (à l'oral) :**
- T1 (π = 0,50) : on veut savoir si la *majorité* dort insuffisamment — le seuil naturel est la moitié
- T2 (π = 1/3) : si les 3 modalités de V14 étaient équiréparties, on attendrait 1/3 dans chacune
- T3 (m = 2) : 2 est à la fois le mode et la médiane de V2 — valeur centrale observée
- T4 (loi uniforme) : référence naturelle en l'absence de distribution théorique connue pour V12

**Contenu visuel :**

**Test 1 – Proportion bilatéral (V6 : < 7h = 50 % ?)**
- H₀ : p = 0,50 vs H₁ : p ≠ 0,50 – *§3.4.1*
- Critère : z = (p̂ − p₀) / √(p₀(1−p₀)/n)
- Conclusion : [ à compléter ]

**Test 2 – Moyenne Student (V2 : μ = 2 ?)**
- H₀ : μ = 2 vs H₁ : μ ≠ 2 – loi T(n−1)
- Critère : t = (x̄ − μ₀) / (σ_e/√n)
- Conclusion : [ à compléter ]

*[À compléter par Membre 4 – Section 4.4]*

---

## Diapo 9 – Tests du χ² d'indépendance

**Accroche orale :**
> *"La question centrale : le niveau au bac est-il indépendant des habitudes de travail ? On répond avec les tests du χ²."*

**Contenu visuel :**

| Test | Variables | χ²_obs | Seuil (ddl=1) | Conclusion |
|---|---|---|---|---|
| T5 — χ² ind. (SC3/SC4) | V2 × V14 | 0,26 | 3,841 | Non-rejet H₀ |
| T6 — χ² ind. (SC5/SC6) | Permanences × Moy. S1 | 3,95 | 3,841 | Rejet H₀ |

> *Note : les tests V12×V2 et V12×V14 ont été abandonnés — conditions de validité non satisfaites (effectifs théoriques < 5 dans plusieurs cellules, §3.4.2).*

- Formule : χ² = ΣΣ (o_{i,j} − n_{i,j})² / n_{i,j} – *§3.4.2*
- ddl = (k₁−1)(k₂−1)

*[À compléter par Membre 5 – Section 4.5]*

---

## Diapo 10 – Conclusion et limites

**Accroche orale :**
> *"En conclusion : [résumé des tests]. Ce qu'il faut garder en tête : association n'est pas causalité. Et nos résultats sont valables pour notre population de 68 répondants – toute généralisation est une extrapolation."*

**Contenu visuel :**

**Ce qu'on a montré :**
- [ χ² V12 × V2 : indépendants / liés ? ]
- [ χ² V12 × V14 : indépendants / liés ? ]
- [ Proportion dormant < 7h significativement ≠ 50 % ? ]

**Limites :**
- Auto-déclaration → biais de désirabilité sociale
- Population = 68 répondants volontaires → non représentatif de toute la P1
- Variables ordinales traitées parfois comme quantitatives (approximation)

**Message final :**
> *"Les statistiques ne prouvent pas, elles quantifient l'incertitude. Nos conclusions valent au risque α = 5 %."*

---

*Ce document est une trame – les cellules vides seront complétées au fur et à mesure de l'avancement du rapport.*
