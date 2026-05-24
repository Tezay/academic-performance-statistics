# Dictionnaire des variables – Données de sondage

> Ce fichier décrit les variables contenues dans chaque CSV.  
> Classification selon la **Définition 1.3** du cours SM403 (qualitative / quantitative).

---

## ADD_SC3_SC4.csv – Sondage principal (n = 72)

Sondage conçu par les classes SC3 et SC4 de P2, administré aux classes SC5, SC6, SC7 et BDX de P1 sur leur semestre 1.

| # | Variable (intitulé dans le CSV) | Type | Modalités / Plage | Rôle dans l'étude |
|---|---|---|---|---|
| 1 | Horodateur | – | Date/heure | Identification (exclure de l'analyse) |
| 2 | Annales travaillées avant CE/DE | Quantitative discrète | 0 à 4+ (0, 1, 2, 3, 4+) | Habitudes de préparation aux examens |
| 3 | Équilibre vie personnelle / études (0 à 5) | Qualitative ordinale | 0 à 5 | Bien-être général |
| 4 | Confiance avant DE vs performance finale (1 à 5) | Qualitative ordinale | 1 à 5 | Auto-évaluation de la confiance |
| 5 | Répartition des examens influence résultats (1 à 5) | Qualitative ordinale | 1 à 5 | Perception de l'organisation académique |
| 6 | Heures de sommeil avant un DE (1 à 5) | Qualitative ordinale | 1 (< 4h) à 5 | Hygiène de sommeil |
| 7 | Organisation de travail en dehors des cours (1 à 5) | Qualitative ordinale | 1 à 5 | Méthode de travail |
| 8 | Jours avant CE/DE pour commencer révisions (0 à 5) | Quantitative discrète | 0 à 5 | Anticipation des révisions |
| 9 | Niveau d'implication associative à l'EFREI (0 à 4) | Qualitative ordinale | 0 (aucune) à 4 (bureau) | Engagement associatif |
| 10 | Temps avant DE pour réviser (1 à 5) | Qualitative ordinale | 1 à 5 | Durée des révisions |
| 11 | Heures de sport par semaine (0 à 4) | Qualitative ordinale | 0 (ne fait pas) à 4 | Activité physique |
| 12 | Moyenne au bac en spécialités scientifiques (1 à 5) | Qualitative ordinale | 1 à 5 | Niveau académique antérieur |
| 13 | Relecture des cours hors révisions (0 à 4) | Qualitative ordinale | 0 (jamais) à 4 | Régularité du travail |
| 14 | Assiduité aux CMs (0 à 3) | Qualitative ordinale | 0 à 3 (tous les CMs) | Présence en cours |
| 15 | Temps de trajet vers l'EFREI (1 à 6) | Qualitative ordinale | 1 à 6 | Contrainte logistique |
| 16 | Classe | Qualitative nominale | P1-SC5, P1-SC6, P1-SC7, P1-BDX | Sous-groupe de l'échantillon |
| 17 | A fait le semestre à l'EFREI | Qualitative nominale | Oui / Non | **Filtre : exclure les "Non"** |

**Notes de nettoyage :**
- Réponses brutes : 71
- Exclues : 3 (2 réponses "Non" à V17 + 1 réponse incomplète)
- Effectif après nettoyage : **n = 68**
- Répartition : P1-SC5 (25), P1-SC6 (16), P1-SC7 (13), P1-BDX (14)
- Valeur aberrante détectée : V12 modalité "1 : -8 (je suis une fraude)" → 1 occurrence (à exclure des tests χ²)

---

## ADD_PP1_PP2.csv – Sondage PP1/PP2 (n = 49)

Sondage conçu par les classes PP1 et PP2 de P2, administré aux classes PrépaPlus-MP et PrépaPlus-P de P1.  
Format différent (questionnaire Microsoft Forms avec colonnes Points/Feedback).

Variables principales identifiées :

| Variable | Type | Plage / Modalités |
|---|---|---|
| Heures de sommeil par nuit | Quantitative discrète | h/nuit |
| Activité extrascolaire (h/jour) | Quantitative continue | h/jour |
| Fréquence consommation d'alcool | Qualitative ordinale | fois/semaine |
| Moyenne générale au lycée | Quantitative continue | /20 |
| Temps de trajet domicile-EFREI | Qualitative ordinale | plages horaires |
| Intérêt pour les cours (1 à 5) | Qualitative ordinale | 1 à 5 |
| Temps de révision par jour | Quantitative continue | h/jour |
| Charge de travail perçue (1 à 5) | Qualitative ordinale | 1 à 5 |
| Concentration le lendemain de soirée (0 à 10) | Quantitative discrète | 0 à 10 |
| Nombre de fois triché aux examens | Quantitative discrète | entier |
| Temps sur les écrans par jour | Quantitative continue | h/jour |

---

## ADD_SC1_SC2.csv – Sondage SC1/SC2 (n = 101)

Sondage conçu par les classes SC1 et SC2 de P2.  
Variables principales identifiées :

| Variable | Type | Plage / Modalités |
|---|---|---|
| Qualité du sommeil (1 à 10) | Qualitative ordinale | 1 à 10 |
| Impact d'être en couple sur les études | Quantitative | écart de moyenne |
| Moyenne au bac | Quantitative discrète | 10 à 20 |
| Situation de logement (parents / seul·e) | Qualitative nominale | catégories |

---

## ADD_SC5_SC6.csv – Sondage SC5/SC6 (n = 85)

Sondage conçu par les classes SC5 et SC6 de P2.  
Variables principales identifiées :

| Variable | Type | Plage / Modalités |
|---|---|---|
| Note de bac en Mathématiques | Quantitative discrète | /20 |
| Heures de sommeil par nuit | Quantitative discrète | h/nuit |
| Temps de révision avant un examen important | Qualitative ordinale | catégories |
| Spécialité Master envisagée à l'EFREI | Qualitative nominale | liste de spécialités |
| Note en Analyse 1 à l'EFREI | Quantitative continue | /20 |
| Difficulté Algèbre Générale (1 à 10) | Qualitative ordinale | 1 à 10 |
| Fréquence activités extra-scolaires | Qualitative ordinale | catégories |
| Fréquence permanences pédagogiques | Qualitative ordinale | catégories |
| Demi-journée préférée pour dormir (matin/après-midi) | Qualitative nominale | 2 modalités |
| Fréquence d'événements sociaux | Qualitative ordinale | catégories |
| Moyenne au S1 à l'EFREI | Quantitative continue | /20 |
| Fréquence CM | Qualitative ordinale | catégories |
| Répartition des épreuves dans l'année (perception) | Qualitative ordinale | Oui/Non/Neutre |
| Nombre de cohabitants | Quantitative discrète | entier |
| Fréquence passage au tableau en TD | Qualitative ordinale | catégories |

---

## Notes générales

- **Sondage principal** pour l'analyse : `ADD_SC3_SC4.csv` (sondage du groupe)
- Les trois autres sondages peuvent enrichir la réflexion mais ont des questions différentes
- Les variables mesurées sur des échelles ordinales (1 à 5) sont **qualitatives ordinales** au sens de la Définition 1.3 du cours – les traiter comme quantitatives est une approximation à mentionner explicitement dans la section "Limites de l'étude"
