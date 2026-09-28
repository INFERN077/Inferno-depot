"""Simulation du round 4 : investissement locatif à crédit contre ETF monde,
avec exactement les mêmes sorties d'argent pour les deux jumeaux.

Lancer : python3 scripts/immobilier-vs-bourse-simulation.py
"""


def simuler(prix=200_000, notaire=0.08, taux=0.033, annees=20, rendement_brut=0.037,
            indexation_loyer=0.015, part_charges=0.25, mois_vides=1, tmi=0.30,
            ps_foncier=0.172, hausse_prix=0.015, rendement_etf=0.07, ps_bourse=0.186):
    n = annees * 12
    t = taux / 12
    mensualite = prix * t / (1 - (1 + t) ** -n)  # la banque finance le bien, l'apport paie le notaire
    apport = prix * notaire
    capital_restant = prix
    deficit_reporte = 0.0
    loyer_mensuel = prix * rendement_brut / 12
    etf, verse_etf, effort_total = apport, apport, apport

    for annee in range(annees):
        interets = 0.0
        for _ in range(12):
            i = capital_restant * t
            interets += i
            capital_restant -= mensualite - i
        loyers = loyer_mensuel * (12 - mois_vides)
        charges = prix * rendement_brut * part_charges * 1.02 ** annee  # taxe foncière, copro, assurance, travaux
        imposable = loyers - charges - interets - deficit_reporte  # régime réel
        if imposable < 0:
            deficit_reporte, impot = -imposable, 0.0
        else:
            deficit_reporte, impot = 0.0, imposable * (tmi + ps_foncier)
        effort = mensualite * 12 + charges + impot - loyers  # ce qui sort de la poche du jumeau immobilier
        effort_total += effort
        for _ in range(12):  # le jumeau bourse investit le même effort, mois par mois
            etf = etf * (1 + rendement_etf) ** (1 / 12) + effort / 12
        verse_etf += effort
        loyer_mensuel *= 1 + indexation_loyer

    appartement = prix * (1 + hausse_prix) ** annees  # plus-value immobilière non taxée ici : avantage à la pierre
    etf_net = etf - max(0.0, etf - verse_etf) * ps_bourse
    effort_mensuel = (effort_total - apport) / n
    return appartement, etf_net, effort_mensuel


def point_egalite(**hypotheses):
    """Hausse annuelle du prix qui met les deux jumeaux à égalité."""
    bas, haut = -0.05, 0.08
    for _ in range(60):
        milieu = (bas + haut) / 2
        appartement, etf, _ = simuler(hausse_prix=milieu, **hypotheses)
        bas, haut = (milieu, haut) if appartement < etf else (bas, milieu)
    return milieu


if __name__ == "__main__":
    cas = {
        "200 000 €, loyer 3,7 % brut (type Paris)": dict(prix=200_000, rendement_brut=0.037),
        "120 000 €, loyer 7 % brut (ville moyenne)": dict(prix=120_000, rendement_brut=0.07),
    }
    for nom, hyp in cas.items():
        _, _, effort = simuler(**hyp)
        print(nom)
        print(f"  effort moyen : {effort:,.0f} €/mois".replace(",", " "))
        for etf in (0.07, 0.05):
            print(f"  point d'égalité si ETF à {etf:.0%}/an : +{point_egalite(rendement_etf=etf, **hyp):.2%}/an")
