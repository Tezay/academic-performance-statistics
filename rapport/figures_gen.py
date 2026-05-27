#!/usr/bin/env python3
"""
figures_gen.py - Génération des figures et calcul des statistiques
SM403 - Analyse de données - Groupe 1 SC4

Génère dans rapport/figures/ :
    hist_v2.pdf, box_v2.pdf, bar_v6.pdf, bar_v12.pdf, bar_v14.pdf

Affiche dans le terminal tous les paramètres statistiques nécesaires

Fonctions statistiques -> rapport/stats_utils.py  (formules du cours)
"""

import math
import re
import sys
from pathlib import Path
from collections import Counter, OrderedDict

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")   # export PDF sans fenêtre
import matplotlib.pyplot as plt

# stats_utils.py est dans le même répertoire que ce script
sys.path.insert(0, str(Path(__file__).parent))
from stats_utils import (
    moyenne, mediane, quartiles,
    variance_obs, variance_estimee,
    covariance, correlation,
)

# ─────────────────────────────────────────────────────────────────────────────
# Chemins
# ─────────────────────────────────────────────────────────────────────────────
ROOT    = Path(__file__).parent.parent
SC3_CSV = ROOT / "data" / "ADD_SC3_SC4.csv"
SC5_CSV = ROOT / "data" / "ADD_SC5_SC6.csv"
FIG_DIR = Path(__file__).parent / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# Style matplotlib
# ─────────────────────────────────────────────────────────────────────────────
BLEU  = "#2B6CB0"
BLEU2 = "#63B3ED"
FIG_W = 5.0
FIG_H = 3.2

plt.rcParams.update({
    "font.family":       "sans-serif",
    "font.size":         9,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.labelsize":    9,
    "xtick.labelsize":   8,
    "ytick.labelsize":   8,
    "figure.dpi":        150,
})


def sep(titre=""):
    print("\n" + "─" * 62)
    if titre:
        print(f"  {titre}")
        print("─" * 62)


def chi2_calc(obs_table, row_labels, col_labels, titre=""):
    """§3.4.2 : χ² indépendance - calcul + affichage du tableau."""
    obs  = np.array(obs_table, dtype=float)
    n    = obs.sum()
    rows = obs.sum(axis=1)
    cols = obs.sum(axis=0)
    theo = np.outer(rows, cols) / n
    k1, k2 = obs.shape
    ddl  = (k1 - 1) * (k2 - 1)
    chi2 = float(((obs - theo) ** 2 / theo).sum())

    if titre:
        sep(titre)
    print(f"  n = {int(n)},  ddl = ({k1}-1)×({k2}-1) = {ddl}")

    W = 12
    hdr = f"  {'':>16}" + "".join(f"{l:>{W}}" for l in col_labels) + f"  {'Total':>{W}}"

    print("\n  Effectifs OBSERVÉS (oi,j) :")
    print(hdr)
    for i, rl in enumerate(row_labels):
        print(f"  {rl:>16}" + "".join(f"{int(obs[i,j]):>{W}}" for j in range(k2))
              + f"  {int(rows[i]):>{W}}")
    print(f"  {'Total':>16}" + "".join(f"{int(cols[j]):>{W}}" for j in range(k2))
          + f"  {int(n):>{W}}")

    print("\n  Effectifs THEORIQUES (ni,j = Li x Cj / n, avec Li=total ligne i, Cj=total col j) :")
    print(hdr)
    min_theo = float("inf")
    for i, rl in enumerate(row_labels):
        print(f"  {rl:>16}" + "".join(f"{theo[i,j]:>{W}.2f}" for j in range(k2))
              + f"  {rows[i]:>{W}.1f}")
        min_theo = min(min_theo, float(theo[i].min()))
    print(f"  {'Total':>16}" + "".join(f"{cols[j]:>{W}.1f}" for j in range(k2))
          + f"  {n:>{W}.0f}")

    valid = min_theo >= 5 and n >= 50
    print(f"\n  Condition n≥50 : {'✓' if n >= 50 else '✗'}  "
          f"ni,j min = {min_theo:.2f} -> {'✓' if valid else '✗ (conditions NON satisfaites)'}")
    print(f"\n  χ²_obs = {chi2:.4f}")
    print(f"  Seuil χ²_{{{ddl}, 5%}} = ? (lire table Annexe 5.3 du cours)")
    return chi2, theo, valid


# ─────────────────────────────────────────────────────────────────────────────
# Chargement SC3/SC4
# ─────────────────────────────────────────────────────────────────────────────
df_raw = pd.read_csv(SC3_CSV, dtype=str)
df     = df_raw[df_raw.iloc[:, 16].str.strip() == "Oui"].copy()
N      = len(df)
sep(f"Dataset SC3/SC4  -  n = {N} répondants valides")

COL_V2  = df.columns[1]
COL_V6  = df.columns[5]
COL_V12 = df.columns[11]
COL_V14 = df.columns[13]


# ─────────────────────────────────────────────────────────────────────────────
# V2 - Annales travaillées (quantitative discrète, Déf. 1.3)
# ─────────────────────────────────────────────────────────────────────────────
sep("V2 - Annales travaillées  (variable quantitative discrète)")

V2_MAP  = {"0": 0, "1": 1, "2": 2, "3": 3, "4+": 4}
v2_raw  = df[COL_V2].str.strip()
v2_vals = [V2_MAP[v] for v in v2_raw if v in V2_MAP]
n2      = len(v2_vals)
v2_s    = sorted(v2_vals)

xbar2      = moyenne(v2_vals)
me2        = mediane(v2_s, n2)
q1_2, q3_2 = quartiles(v2_s, n2)
mo2        = Counter(v2_vals).most_common(1)[0][0]
sig2_obs   = variance_obs(v2_vals, xbar2)
sig2       = math.sqrt(sig2_obs)
se2_obs    = variance_estimee(sig2_obs, n2)
se2        = math.sqrt(se2_obs)

print(f"  n    = {n2}")
print(f"  x̄    = {xbar2:.4f}  (Déf. 1.4)")
print(f"  Me   = {me2}       (Déf. 1.5 + PM 1.1,  n pair : moy. rangs {n2//2} et {n2//2+1})")
print(f"  Q1   = {q1_2}       (Déf. 1.6 + PM 1.2,  n%4={n2%4} -> moy. rangs {n2//4} et {n2//4+1})")
print(f"  Q3   = {q3_2}       (Déf. 1.6 + PM 1.2,  moy. rangs {3*n2//4} et {3*n2//4+1})")
print(f"  Mo   = {mo2}       (Déf. 1.7)")
print(f"  σ²   = {sig2_obs:.4f}  (Déf. 1.9)")
print(f"  σ    = {sig2:.4f}  (Déf. 1.9)")
print(f"  Se²  = {se2_obs:.4f}  (§2.3.1 : {n2}/({n2}-1) × {sig2_obs:.4f})")
print(f"  Se   = {se2:.4f}  (§2.3.1)")

print("\n  Tableau de fréquences (Déf. 1.8) :")
print(f"  {'Modalité':>10}  {'ni':>5}  {'fi':>8}  {'fi (%)':>8}")
for v in [0, 1, 2, 3, 4]:
    ni  = v2_vals.count(v)
    lbl = "4+" if v == 4 else str(v)
    print(f"  {lbl:>10}  {ni:>5}  {ni/n2:>8.4f}  {ni/n2*100:>7.1f}%")

# Corrélation V2 × V12 (Déf. 1.16) - V12 traitée comme numérique 2–5
v12_num = {"2": 2, "3": 3, "4": 4, "5": 5}
pairs   = [(V2_MAP[df.iloc[i][COL_V2].strip()],
            v12_num[df.iloc[i][COL_V12].strip()[:1]])
           for i in range(len(df))
           if df.iloc[i][COL_V2].strip() in V2_MAP
           and df.iloc[i][COL_V12].strip()[:1] in v12_num]
xs_c = [p[0] for p in pairs]
ys_c = [p[1] for p in pairs]
r_v2v12 = correlation(xs_c, ys_c)
print(f"\n  r(V2, V12) = {r_v2v12:.4f}  (Déf. 1.16, n={len(xs_c)})")
print("  Note : V12 ordinale traitée comme numérique 2–5 (approximation §1.2)")

# Figures V2
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
counts  = [v2_vals.count(v) for v in range(5)]
bars    = ax.bar(range(5), counts, color=BLEU, edgecolor="white", linewidth=0.5)
ax.set_xticks(range(5))
ax.set_xticklabels(["0", "1", "2", "3", "4+"])
ax.set_xlabel("Nombre d'annales travaillées")
ax.set_ylabel("Effectif")
ax.axvline(xbar2, color="tomato", linewidth=1.2, linestyle="--",
           label=f"$\\bar{{x}} = {xbar2:.2f}$")
ax.axvline(me2,   color="orange", linewidth=1.2, linestyle=":",
           label=f"$M_e = {me2}$")
ax.legend(fontsize=8)
for bar, ni in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            str(ni), ha="center", va="bottom", fontsize=8)
fig.tight_layout()
fig.savefig(FIG_DIR / "hist_v2.pdf", bbox_inches="tight")
plt.close(fig)
print("\n  -> hist_v2.pdf généré")

fig, ax = plt.subplots(figsize=(FIG_W * 0.6, FIG_H))
ax.boxplot(v2_vals, vert=True, patch_artist=True,
           medianprops=dict(color="tomato", linewidth=2),
           boxprops=dict(facecolor=BLEU2, color=BLEU),
           whiskerprops=dict(color=BLEU),
           capprops=dict(color=BLEU),
           flierprops=dict(marker="o", color=BLEU, alpha=0.4))
ax.set_ylabel("Nombre d'annales travaillées")
ax.set_xticks([])
for val, lbl in [(q1_2, f"Q1={q1_2}"), (me2, f"Me={me2}"), (q3_2, f"Q3={q3_2}")]:
    ax.text(1.35, val, lbl, va="center", fontsize=8, color=BLEU)
fig.tight_layout()
fig.savefig(FIG_DIR / "box_v2.pdf", bbox_inches="tight")
plt.close(fig)
print("  -> box_v2.pdf généré")


# ─────────────────────────────────────────────────────────────────────────────
# V6 - Sommeil avant DE (qualitative ordinale, Déf. 1.3)
# ─────────────────────────────────────────────────────────────────────────────
sep("V6 - Sommeil avant un DE  (variable qualitative ordinale)")

V6_LABELS = OrderedDict([
    ("1 : Moins de 4 heures",  "< 4 h"),
    ("2 : Entre 4 à 6 heures", "4–6 h"),
    ("3 : Entre 6 à 7 heures", "6–7 h"),
    ("4 : Entre 7 à 8 heures", "7–8 h"),
    ("5 : Plus de 8 heures",   "> 8 h"),
])
v6_raw    = df[COL_V6].str.strip()
v6_cnt    = {k: int((v6_raw == k).sum()) for k in V6_LABELS}
n6        = sum(v6_cnt.values())
v6_mo_key = max(v6_cnt, key=v6_cnt.get)

print(f"  n  = {n6},  Mo = {V6_LABELS[v6_mo_key]}  (Déf. 1.7)")
print(f"\n  Tableau de fréquences (Déf. 1.8) :")
print(f"  {'Modalité':>22}  {'Label':>7}  {'ni':>5}  {'fi':>8}  {'fi (%)':>8}")
for key, lbl in V6_LABELS.items():
    ni = v6_cnt[key]
    print(f"  {key[:22]:>22}  {lbl:>7}  {ni:>5}  {ni/n6:>8.4f}  {ni/n6*100:>7.1f}%"
          + (" <- Mo" if key == v6_mo_key else ""))

p_lt7h = sum(v6_cnt[k] for k in list(V6_LABELS)[:3]) / n6
print(f"\n  p̂(< 7h) = {p_lt7h:.4f} ({p_lt7h*100:.1f}%)  [modalités 1+2+3]")

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
lbls6   = list(V6_LABELS.values())
vals6   = [v6_cnt[k] for k in V6_LABELS]
colors6 = [BLEU if l in ("< 4 h", "4–6 h", "6–7 h") else BLEU2 for l in lbls6]
bars    = ax.bar(lbls6, vals6, color=colors6, edgecolor="white", linewidth=0.5)
ax.set_xlabel("Heures de sommeil")
ax.set_ylabel("Effectif")
for bar, ni in zip(bars, vals6):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            str(ni), ha="center", va="bottom", fontsize=8)
fig.tight_layout()
fig.savefig(FIG_DIR / "bar_v6.pdf", bbox_inches="tight")
plt.close(fig)
print("\n  -> bar_v6.pdf généré")


# ─────────────────────────────────────────────────────────────────────────────
# V12 - Note bac (qualitative ordinale, Déf. 1.3)
# Modalité "1 : -8 (je suis une fraude)" exclue - valeur aberrante
# ─────────────────────────────────────────────────────────────────────────────
sep("V12 - Note bac spécialités scientifiques  (qualitative ordinale)")

V12_LABELS = OrderedDict([
    ("2 : 8-11",  "8–11"),
    ("3 : 12-14", "12–14"),
    ("4 : 15-17", "15–17"),
    ("5 : 18-20", "18–20"),
])
v12_raw    = df[COL_V12].str.strip()
v12_cnt    = {k: int((v12_raw == k).sum()) for k in V12_LABELS}
n12        = sum(v12_cnt.values())
v12_mo_key = max(v12_cnt, key=v12_cnt.get)
anomalie   = int((v12_raw == "1 : -8 (je suis une fraude)").sum())

print(f"  Anomalie exclue : {anomalie}  ('1 : -8 (je suis une fraude)')")
print(f"  n (après exclusion) = {n12},  Mo = {V12_LABELS[v12_mo_key]}  (Déf. 1.7)")
print(f"\n  Tableau de fréquences (Déf. 1.8) :")
print(f"  {'Modalité':>15}  {'Label':>7}  {'ni':>5}  {'fi':>8}  {'fi (%)':>8}")
for key, lbl in V12_LABELS.items():
    ni = v12_cnt[key]
    print(f"  {key:>15}  {lbl:>7}  {ni:>5}  {ni/n12:>8.4f}  {ni/n12*100:>7.1f}%"
          + (" <- Mo" if key == v12_mo_key else ""))

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
bars = ax.bar(list(V12_LABELS.values()),
              [v12_cnt[k] for k in V12_LABELS],
              color=BLEU, edgecolor="white", linewidth=0.5)
ax.set_xlabel("Moyenne au bac (spécialités scientifiques)")
ax.set_ylabel("Effectif")
for bar, ni in zip(bars, [v12_cnt[k] for k in V12_LABELS]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            str(ni), ha="center", va="bottom", fontsize=8)
fig.tight_layout()
fig.savefig(FIG_DIR / "bar_v12.pdf", bbox_inches="tight")
plt.close(fig)
print("\n  -> bar_v12.pdf généré")


# ─────────────────────────────────────────────────────────────────────────────
# V14 - Assiduité aux CMs (qualitative ordinale, Déf. 1.3)
# ─────────────────────────────────────────────────────────────────────────────
sep("V14 - Assiduité aux CMs  (variable qualitative ordinale)")

V14_LABELS = OrderedDict([
    ("1 : Rarement",                    "Rarement"),
    ("2 : Presque tous",                "Presque tous"),
    ("3 : J'assiste à tous les CMs",    "Tous"),
])
v14_raw    = df[COL_V14].str.strip()
v14_cnt    = {k: int((v14_raw == k).sum()) for k in V14_LABELS}
n14        = sum(v14_cnt.values())
v14_mo_key = max(v14_cnt, key=v14_cnt.get)
p14_tous   = v14_cnt["3 : J'assiste à tous les CMs"] / n14

print(f"  n  = {n14},  Mo = {V14_LABELS[v14_mo_key]}  (Déf. 1.7)")
print(f"  p̂(Tous) = {p14_tous:.4f} ({p14_tous*100:.1f}%)")
print(f"\n  Tableau de fréquences (Déf. 1.8) :")
print(f"  {'Modalité':>32}  {'Label':>14}  {'ni':>5}  {'fi':>8}  {'fi (%)':>8}")
for key, lbl in V14_LABELS.items():
    ni = v14_cnt[key]
    print(f"  {key:>32}  {lbl:>14}  {ni:>5}  {ni/n14:>8.4f}  {ni/n14*100:>7.1f}%"
          + (" <- Mo" if key == v14_mo_key else ""))

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
bars = ax.bar(list(V14_LABELS.values()),
              [v14_cnt[k] for k in V14_LABELS],
              color=BLEU, edgecolor="white", linewidth=0.5)
ax.set_xlabel("Assiduité aux cours magistraux")
ax.set_ylabel("Effectif")
for bar, ni in zip(bars, [v14_cnt[k] for k in V14_LABELS]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            str(ni), ha="center", va="bottom", fontsize=8)
fig.tight_layout()
fig.savefig(FIG_DIR / "bar_v14.pdf", bbox_inches="tight")
plt.close(fig)
print("\n  -> bar_v14.pdf généré")


# ─────────────────────────────────────────────────────────────────────────────
# T5 - χ² d'indépendance : V2 × V14  (§3.4.2)
# V2  regroupée : ≤2 annales  |  ≥3 annales
# V14 regroupée : Pas tous (Rarement+Presque tous)  |  Tous
#
# Justification du regroupement V14 :
#   "Rarement" (n=6) seul rend ni,j < 5 partout.
#   "Pas tous" = ne se déplace pas systématiquement en cours (modalités 1+2).
#   "Tous" = présence totale (modalité 3). Dichotomie logique et symétrique.
# ─────────────────────────────────────────────────────────────────────────────
sep("T5 - χ² indépendance : V2 (annales) × V14 (assiduité CMs)")

def v2_cat_t5(x):
    x = x.strip()
    if x in ("0", "1", "2"): return "≤2 annales"
    if x in ("3", "4+"):     return "≥3 annales"
    return None

def v14_cat_t5(x):
    x = x.strip()
    if x in ("1 : Rarement", "2 : Presque tous"):  return "Pas tous"
    if x == "3 : J'assiste à tous les CMs":         return "Tous"
    return None

V2_T5  = ["≤2 annales", "≥3 annales"]
V14_T5 = ["Pas tous", "Tous"]

obs_t5 = [[0] * len(V14_T5) for _ in range(len(V2_T5))]
for _, row in df.iterrows():
    c2  = v2_cat_t5(row[COL_V2])
    c14 = v14_cat_t5(row[COL_V14])
    if c2 and c14:
        obs_t5[V2_T5.index(c2)][V14_T5.index(c14)] += 1

print("  [V14 regroupée : Rarement+Presque tous -> «Pas tous» ; Tous -> «Tous»]")
chi2_t5, _, ok_t5 = chi2_calc(obs_t5, V2_T5, V14_T5)


# ─────────────────────────────────────────────────────────────────────────────
# Tests χ² initialement prévus - IMPOSSIBLES (conditions non satisfaites)
# ─────────────────────────────────────────────────────────────────────────────
sep("Tests χ² abandonnés - conditions non satisfaites (§3.4.2)")

print("""
  V12×V2 (prévu) :
    Même avec regroupement maximal 2×2, ni,j min = 4,70 < 5.
    V12 "8–11" ne compte que 13 individus : aucun regroupement
    ne peut satisfaire ni,j ≥ 5 tout en restant interprétable.
    -> Test abandonné ; mentionné dans §3 (limites méthodologiques).

  V12×V14 (prévu) :
    V14 "Rarement" ne compte que 6 individus.
    Quel que soit le regroupement de V12, ni,j min ≤ 1,34 < 5.
    -> Test abandonné ; mentionné dans §3 (limites méthodologiques).
""")


# ─────────────────────────────────────────────────────────────────────────────
# Dataset SC5/SC6
# ─────────────────────────────────────────────────────────────────────────────
sep("Dataset SC5/SC6  -  Exploration")

df5 = pd.read_csv(SC5_CSV, dtype=str)
N5  = len(df5)
print(f"  n brut SC5/SC6 = {N5}")

COL_PERM   = df5.columns[8]
COL_MOY_S1 = df5.columns[11]
COL_FREQ   = df5.columns[12]
COL_AN1    = df5.columns[5]

def parse_float(s):
    m = re.search(r"\d+[.,]?\d*", s.strip().replace(",", "."))
    return float(m.group()) if m else None

moy_s1_vals = [(i, parse_float(df5.iloc[i][COL_MOY_S1]))
               for i in range(N5)
               if parse_float(df5.iloc[i][COL_MOY_S1]) is not None]
print(f"  Moy. S1 : {len(moy_s1_vals)} valeurs sur {N5}")

perm_cnt = Counter(df5[COL_PERM].str.strip())
print(f"\n  Permanences pédagogiques :")
for k, v in sorted(perm_cnt.items(), key=lambda x: -x[1]):
    print(f"    {k:>20} : {v}")

freq_cnt = Counter(df5[COL_FREQ].str.strip())
print(f"\n  Fréquence CMs (info) :")
for k, v in sorted(freq_cnt.items(), key=lambda x: -x[1]):
    print(f"    {k:>25} : {v}")
print("  ⚠  Fréq. CMs : 98% dans Systématiquement/Souvent -> χ² d'indépendance impossible.")


# ─────────────────────────────────────────────────────────────────────────────
# T6 - χ² d'indépendance : Permanences × Moy. S1  (SC5/SC6)
# Permanences regroupées : Peu (Jamais+Rarement)  |  Régulièrement (Régul.+Systém.)
# Moy. S1     regroupées : ≤13                    |  >13
#
# Justification :
#   Régul.+Systém. = 18 obs -> ni,j min acceptable avec 2×2 (min=5,42 ✓).
#   Moy. ≤13 vs >13 : seuil autour de la mention Assez Bien (>13/20).
# ─────────────────────────────────────────────────────────────────────────────
sep("T6 - χ² indépendance : Permanences × Moy. S1 (SC5/SC6)")

def perm_cat(x):
    x = x.strip()
    if x in ("Jamais", "Rarement"):                  return "Peu"
    if x in ("Régulièrement", "Systématiquement"):   return "Régulièrement"
    return None

def moy_cat(v):
    return "≤ 13" if v <= 13 else "> 13"

PERM_CATS = ["Peu", "Régulièrement"]
MOY_CATS  = ["≤ 13", "> 13"]

obs_t6 = [[0] * len(MOY_CATS) for _ in range(len(PERM_CATS))]
for idx, moy in moy_s1_vals:
    pc = perm_cat(df5.iloc[idx][COL_PERM])
    mc = moy_cat(moy)
    if pc:
        obs_t6[PERM_CATS.index(pc)][MOY_CATS.index(mc)] += 1

print("  [Permanences : Peu (Jamais+Rarement) | Régulièrement (Régul.+Systém.)]")
print("  [Moy. S1 : ≤13 | >13  - seuil mention Assez Bien]")
chi2_t6, _, ok_t6 = chi2_calc(obs_t6, PERM_CATS, MOY_CATS)


# ─────────────────────────────────────────────────────────────────────────────
# Récapitulatif
# ─────────────────────────────────────────────────────────────────────────────
sep("RÉCAPITULATIF - Valeurs pour les tableaux LaTeX")

ic_v14_marge = 1.96 * math.sqrt(p14_tous * (1 - p14_tous) / n14)
ic_v2_marge  = 2.000 * se2 / math.sqrt(n2)
z_t1 = (p_lt7h - 0.5) / math.sqrt(0.25 / n6)
z_t2 = (p14_tous - 1/3) / math.sqrt((1/3) * (2/3) / n14)
t_t3 = (xbar2 - 2) / (se2 / math.sqrt(n2))
chi2_t4 = ((13 - n12/3)**2 + (39 - n12/3)**2 + (15 - n12/3)**2) / (n12/3)

print(f"""
  ── Variables ──────────────────────────────────────────────
  V2  n={n2}  x̄={xbar2:.4f}  Me={me2}  Q1={q1_2}  Q3={q3_2}  Mo={mo2}
      σ²={sig2_obs:.4f}  σ={sig2:.4f}  Se²={se2_obs:.4f}  Se={se2:.4f}
      r(V2,V12) = {r_v2v12:.4f}

  V6  n={n6}  Mo=4–6h  p̂(<7h) = {p_lt7h:.4f} ({p_lt7h*100:.1f}%)

  V12 n={n12} (anomalie exclue)  Mo=12–14
      Obs fusionnées χ²T4 : [13, 39, 15]  (8-11 | 12-14 | 15-20)

  V14 n={n14}  Mo=Presque tous  p̂(Tous) = {p14_tous:.4f} ({p14_tous*100:.1f}%)

  ── Intervalles de confiance (α=5%) ────────────────────────
  IC proportion V14  z=1,96 :
    marge = {ic_v14_marge:.4f}
    IC = [{p14_tous - ic_v14_marge:.4f} ; {p14_tous + ic_v14_marge:.4f}]

  IC moyenne V2  t_{{67}}≈2,000 :
    marge = {ic_v2_marge:.4f}
    IC = [{xbar2 - ic_v2_marge:.4f} ; {xbar2 + ic_v2_marge:.4f}]

  ── Tests de conformité ────────────────────────────────────
  T1  z = {z_t1:.4f}   (seuil bilatéral : ±1,96)   -> {'REJET H0' if abs(z_t1) > 1.96 else 'NON-REJET'}
  T2  z = {z_t2:.4f}   (seuil unilatéral 5% : 1,645) -> {'REJET H0' if z_t2 > 1.645 else 'NON-REJET'}
  T3  t = {t_t3:.4f}   (seuil bilatéral T(67) : ≈2,000) -> {'REJET H0' if abs(t_t3) > 2.0 else 'NON-REJET'}

  ── Tests χ² ───────────────────────────────────────────────
  T4  χ²_obs = {chi2_t4:.4f}  k=3 ddl=2  seuil=5,991  -> {'REJET H0' if chi2_t4 > 5.991 else 'NON-REJET'}
  T5  χ²_obs = {chi2_t5:.4f}  (V2×V14)  ddl=1  seuil=3,841  -> {'REJET H0' if chi2_t5 > 3.841 else 'NON-REJET'}
  T6  χ²_obs = {chi2_t6:.4f}  (Perm×MoyS1 SC5/SC6)  ddl=1  seuil=3,841  -> {'REJET H0' if chi2_t6 > 3.841 else 'NON-REJET'}
""")

sep("DONE - figures générées dans rapport/figures/")
