#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TODO: Importez vos modules ici

import turtle 
from math import pi

# TODO: Définissez vos fonction ici

def ellipse(masse_volumique: float, a: float=1, b: float=2, c: float=3) -> tuple:
    volume = 4/3 * pi * a * b * c
    mass = volume * masse_volumique

    return volume, mass

def sort_letters():
    pass

def draw_tree():
    pass

def valid_chain():
    pass

def dna(chaine:str):
    pass

def proportion_dna(chain, sequence):
    pass

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    volume, masse = ellipse(10, 2, 4)
    print("le volume est", volume, "et sa masse est", masse, ".")
