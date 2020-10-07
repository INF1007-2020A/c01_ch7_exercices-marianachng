#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle 
from math import pi

# TODO: Importez vos modules ici
def ellipse(masse_volumique: float, a: float=1, b: float=2, cF float=3) -> tuple:
    volume = 4/3 * pi * a * b * c
    mass = volume * masse_volumique

    return volume, mass


# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    volume, masse = ellipse(10, 2, 4)
    print("le volume est", volume, "et sa masse est", masse, ".")
