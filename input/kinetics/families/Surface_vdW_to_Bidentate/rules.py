#!/usr/bin/env python
# encoding: utf-8

name = "Surface_vdW_to_Bidentate/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.838E+21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.0,
        E0 = (12.203, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""CH2CH2-vdw to bidentate calculated by Katrin Blondal."""
)
