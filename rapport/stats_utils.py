"""
stats_utils.py - Fonctions statistiques du cours SM403
"""

import math
from typing import List, Tuple


# Statistiques descriptives - variables quantitatives

def moyenne(vals: List[float]) -> float:
    """Déf. 1.4 : x_barre = (1/n) * somme(xi)"""
    return sum(vals) / len(vals)


def mediane(vals_sorted: List[float], n: int) -> float:
    """Déf. 1.5 + Point méthode 1.1
    n impair : rang (n+1)/2
    n pair   : moyenne des rangs n/2 et n/2+1
    """
    if n % 2 == 1:
        return vals_sorted[(n + 1) // 2 - 1]
    return (vals_sorted[n // 2 - 1] + vals_sorted[n // 2]) / 2


def quartiles(vals_sorted: List[float], n: int) -> Tuple[float, float]:
    """Déf. 1.6 + Point méthode 1.2 - retourne (Q1, Q3)
    n multiple de 4 : moyenne des rangs n/4 et n/4+1 (Q1), 3n/4 et 3n/4+1 (Q3)
    sinon : rang E(n/4)+1 (Q1), E(3n/4)+1 (Q3)
    """
    if n % 4 == 0:
        q1 = (vals_sorted[n // 4 - 1] + vals_sorted[n // 4]) / 2
        q3 = (vals_sorted[3 * n // 4 - 1] + vals_sorted[3 * n // 4]) / 2
    else:
        q1 = vals_sorted[int(n / 4)]
        q3 = vals_sorted[int(3 * n / 4)]
    return q1, q3


def variance_obs(vals: List[float], xbar: float) -> float:
    """Déf. 1.9 : sigma2 = (1/n) * somme(xi - x_barre)^2 = moyenne(x^2) - x_barre^2"""
    n = len(vals)
    s2 = sum(x ** 2 for x in vals) / n - xbar ** 2
    return max(s2, 0.0)  # évite les erreurs d'arrondi numérique


def variance_estimee(sigma2_obs: float, n: int) -> float:
    """§2.3.1 : Se2 = n / (n-1) * sigma2_obs"""
    return (n / (n - 1)) * sigma2_obs


# Corrélation linéaire

def covariance(xs: List[float], ys: List[float], xbar: float, ybar: float) -> float:
    """Déf. 1.15 : Cov(X,Y) = (1/n) * somme((xi - x_barre)(yi - y_barre))"""
    n = len(xs)
    return sum((xs[i] - xbar) * (ys[i] - ybar) for i in range(n)) / n


def correlation(xs: List[float], ys: List[float]) -> float:
    """Déf. 1.16 : r = Cov(X,Y) / (sigmaX * sigmaY)"""
    xbar = moyenne(xs)
    ybar = moyenne(ys)
    cov = covariance(xs, ys, xbar, ybar)
    sx = math.sqrt(variance_obs(xs, xbar))
    sy = math.sqrt(variance_obs(ys, ybar))
    if sx == 0 or sy == 0:
        return float("nan")
    return cov / (sx * sy)
