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
def valid_chain():
    pass

def dna(chaine:str):
    pass

def proportion_dna(chain, sequence):
    pass

#PRACTICE TURTLE:
def draw_square():

    square = turtle.Turtle()

    square.forward(100)
    square.left(90)
    square.forward(100)
    square.left(90)
    square.forward(100)
    square.left(90)
    square.forward(100)
    
def draw_branch(size):

    shrink_factor = 0.8
    angle = 30
    branch.forward(size)
    branch.right(angle)
    branch.forward(size*shrink_factor)
    branch.backward(size*shrink_factor)
    branch.left(2*angle)
    branch.forward(size*shrink_factor)
    branch.backward(size*shrink_factor)
    branch.right(angle)
    branch.backward(size)

def draw_tree(size, depth):
    branch_count = 1
    shrink_factor = 0.8
    angle = 30
    depth = 0

    if depth >= branch_count:
        pass
    else:
        branch.forward(size)
        branch.right(angle)
        branch.forward(size*shrink_factor)
        branch.left(2*angle)
        branch.forward(size*shrink_factor)
        draw_tree(size*shrink_factor, depth+1)
    
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    #volume, masse = ellipse(10, 2, 4)
    #print("le volume est", volume, "et sa masse est", masse, ".")
    
    #print(draw_square())
    #branch = turtle.Turtle()
    #branch.setheading(90)
    #branch.color("green")
    #branch.width(4)
    #branch.speed(1)
#
    #draw_tree(100,3)
    #turtle.done()
    
