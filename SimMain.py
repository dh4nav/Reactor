#!/usr/bin/env python

import numpy as np
import numba as nb
import os, sys

concentration_co2  = [0.0] * 10
concentration_MeCo24 = [0.0] * 10

k = [0.25] * 10
t = 1.0

filename = "out.txt"

def Inject(concentrations, index, amount):
    new_concentrations = [0.0] * len(concentrations)
    new_concentrations[index] = amount
    return concentrations + np.array(new_concentrations)

def CalculateReaction(concentrations, reaction_constants, timestep):
    log_concentrations = np.log(concentrations)
    new_log_concentrations = log_concentrations - (reaction_constants * timestep)
    return np.exp(new_log_concentrations1)

def MoveSubstance(concentrations, move_constants):
    new_concentrations = [0.0] * len(concentrations)
    for n, c in enumerate(concentrations):
        for m in move_constants[n]:
            new_concentrations[m[0]] += c * m[1]
    return np.array(new_concentrations)

def WriteOut(concentrations, out_file):
    opf = open(out_file, "a")
    concentrations.tofile(opf, " ")
    opf.close()

def Initialize():
