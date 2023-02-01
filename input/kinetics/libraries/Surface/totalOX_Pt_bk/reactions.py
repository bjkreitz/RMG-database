#!/usr/bin/env python
# encoding: utf-8

name = "Pt111"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "CO + Pt <=> OCX",
    kinetics = StickingCoefficient(
        A = 8.0E-1,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
CO adsorption on Pt(111). From W. A. Brown, R. Kose, D. A. King, "Femtomole Adsorption Calorimetry on Single-Crystal Surfaces" Chem. Rev. 1998, 98, 797-831
"""
)

entry(
    index = 2,
    label = "OCX + OX <=> CO2X + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.133e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(92.15, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 3,
    label = "O2 + Pt + Pt <=> OX + OX",
    kinetics = StickingCoefficient(
        A=0.064,
        n =0,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""O2 adsorption on Pt(111). From W. A. Brown, R. Kose, D. A. King, "Femtomole Adsorption Calorimetry on Single-Crystal Surfaces" Chem. Rev. 1998, 98, 797-831"""
)

entry(
    index = 4,
    label = "C2H4 + Pt + Pt <=> h-C2H4X",
    kinetics = StickingCoefficient(
        A=0.67,
        n =0,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""O2 adsorption on Pt(111). From W. A. Brown, R. Kose, D. A. King, "Femtomole Adsorption Calorimetry on Single-Crystal Surfaces" Chem. Rev. 1998, 98, 797-831"""
)

entry(
    index = 5,
    label = "h-C2H4X + Pt <=> h-C2H3X + HX",
    kinetics = SurfaceArrhenius(
        A=(5.36e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(59.5, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 6,
    label = "h-C2H3X <=> CHX + CH2X",
    kinetics = SurfaceArrhenius(
        A=(2.94e13, '1/s'),
        n = 0,
        Ea=(140.09, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 7,
    label = "h-C2H4X <=> CH2X + CH2X",
    kinetics = SurfaceArrhenius(
        A=(3.09e15, '1/s'),
        n = 0,
        Ea=(228.00, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 8,
    label = "CHCH3X + Pt + Pt  <=>  h-C2H3X + HX",
    kinetics = SurfaceArrhenius(
        A=(2.32e30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea=(49.00, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 9,
    label = "CHCH3X + Pt  <=> CCH3X + HX",
    kinetics = SurfaceArrhenius(
        A=(5.481e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(27.61, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 10,
    label = "h-C2H3X + Pt <=> h-C2H2X + HX",
    kinetics = SurfaceArrhenius(
        A=(1.08e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(72.88, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 11,
    label = "h-C2H2X <=> CHX + CHX",
    kinetics = SurfaceArrhenius(
        A=(8.5e12, '1/s'),
        n = 0,
        Ea=(90.20, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 12,
    label = "h-CCH2X + HX <=> h-C2H3X + Pt",
    kinetics = SurfaceArrhenius(
        A=(2.399e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(65.3, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 13,
    label = "CH2CH3X + Pt + Pt <=> h-C2H4X + HX",
    kinetics = SurfaceArrhenius(
        A=(1.87e30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea=(46.13, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 14,
    label = "h-C2H2X + Pt <=> h-C2HX + HX",
    kinetics = SurfaceArrhenius(
        A=(2.033e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(151.29, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 15,
    label = "h-CCH2X + Pt <=>  h-C2HX + HX",
    kinetics = SurfaceArrhenius(
        A=(1.782e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(152.07, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 16,
    label = "h-C2HX <=> CHX + CX",
    kinetics = SurfaceArrhenius(
        A=(1.4e12, '1/s'),
        n = 0,
        Ea=(77.48, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 17,
    label = "CHCH3X + Pt <=> h-C2H4X",
    kinetics = SurfaceArrhenius(
        A=(6.717e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(158.12, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)


entry(
    index = 18,
    label = "CCH3X + Pt <=> h-C2H3X",
    kinetics = SurfaceArrhenius(
        A=(2.213E+21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(231.75, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 19,
    label = "h-CCH2X <=> h-C2H2X",
    kinetics = SurfaceArrhenius(
        A=(4.911e12, '1/s'),
        n = 0,
        Ea=(44.13, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 20,
    label = "OCX + Pt <=> CX + OX",
    kinetics = SurfaceArrhenius(
        A=(1.198e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(366.05, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 21,
    label = "CHX + OX <=> HCXO + Pt",
    kinetics = SurfaceArrhenius(
        A=(9.748e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(131.94, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 22,
    label = "OCX + HX <=> HCXO + Pt",
    kinetics = SurfaceArrhenius(
        A=(8.714e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(105.14, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 23,
    label = "OCX + HX <=> CXOH + Pt",
    kinetics = SurfaceArrhenius(
        A=(8.712e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(153.19, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 24,
    label = "CXOH + Pt <=> CX + HOX",
    kinetics = SurfaceArrhenius(
        A=(3.845e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(233.59, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 25,
    label = "CH3X + Pt <=> CH2X + HX",
    kinetics = SurfaceArrhenius(
        A=(1.337e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(87.97, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 26,
    label = "CH2X + Pt <=> CHX + HX",
    kinetics = SurfaceArrhenius(
        A=(5.510e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(32.43, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 27,
    label = "CHX + Pt <=> CX + HX",
    kinetics = SurfaceArrhenius(
        A=(1.157e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(138.67, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 28,
    label = "OCX + HOX <=> CXOOH + Pt",
    kinetics = SurfaceArrhenius(
        A=(2.225e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(36.36, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 29,
    label = "H2OX + Pt <=> HOX + HX",
    kinetics = SurfaceArrhenius(
        A=(8.144e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(91.65, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 30,
    label = "OX + HX <=> HOX + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.921e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(84.11, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 31,
    label = "CH2CH3X + Pt <=> CH2X + CH3X",
    kinetics = SurfaceArrhenius(
        A=(3.449e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(175.88, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 32,
    label = "CXOOH + OX <=> CO2X + HOX",
    kinetics = SurfaceArrhenius(
        A=(1.059e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(23.81, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 33,
    label = "CH4 + Pt + Pt <=> CH3X + HX",
    kinetics = StickingCoefficient(
        A = 6.04,
        n = 0,
        Ea=(58, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 34,
    label = "C2H6 + Pt + Pt <=> CH2CH3X + HX",
    kinetics = StickingCoefficient(
        A = 2.052,
        n = 0,
        Ea=(42.7, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)


entry(
    index = 35,
    label = "CCH3X + Pt + Pt <=> h-CCH2X + HX",
    kinetics = SurfaceArrhenius(
        A=(6.639E+28, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea=(126.70, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 36,
    label = "CCH3X + OX <=> CH3XCO + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.123E+22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(156.01, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 37,
    label = "CH3X + OCX <=> CH3XCO + Pt",
    kinetics = SurfaceArrhenius(
        A=(4.487E+21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(177.78, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)
