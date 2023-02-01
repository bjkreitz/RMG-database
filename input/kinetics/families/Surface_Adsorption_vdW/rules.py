#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/rules"
shortDesc = u""
longDesc = u"""
Surface adsorption of a closed-shell gas-phase species forming a van der Waals bond to the surface site
"""
entry(
    index = 1,
    label = "Adsorbate;VacantSite",
    kinetics = StickingCoefficientBEP(
        A = 0.1,
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)

entry(
    index = 2,
    label = "C2H4;VacantSite",
    kinetics = StickingCoefficientBEP(
        A = 0.01,
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
C2H4 adsorption on Pt(111). From W. A. Brown, R. Kose, D. A. King, "Femtomole Adsorption Calorimetry on Single-Crystal Surfaces" Chem. Rev. 1998, 98, 797-831
"""
)

entry(
    index = 3,
    label = "CH4;VacantSite",
    kinetics = StickingCoefficientBEP(
        A = 1e-14,
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
We only consider dissociative adsorption of CH4. This is easier than forbidding it. 
"""
)

entry(
    index = 4,
    label = "C2H6;VacantSite",
    kinetics = StickingCoefficientBEP(
        A = 1e-14,
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
We only consider dissociative adsorption of CH4. This is easier than forbidding it. 
"""
)

entry(
    index = 5,
    label = "C3H8;VacantSite",
    kinetics = StickingCoefficientBEP(
        A = 1e-14,
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
We only consider dissociative adsorption of CH4. This is easier than forbidding it. 
"""
)

