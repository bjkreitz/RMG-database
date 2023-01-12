#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Monodentate_to_Bidentate/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.0,
        E0 = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""These values are made up, but based on the calculation of *CCH2 --> *C*CH2 which was found to be barrierless"""
)
