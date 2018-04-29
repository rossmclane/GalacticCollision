from numpy import pi,sqrt,sin,cos
import random
from objects import Body
#from tree import tree
import numpy.random as random
from math import floor

box_size = 50 #Mly
solar_mass = 2e30 #kg
BH_mass = 4e6 * solar_mass #kg
G = 6.673e-11 #Gravitational Constant

""" Function that returns a list of Body objects, including N stars and 2 Black Holes"""

#then write a driver file that runs the simulation and writes the data to a CSV file


def make_galaxies(N):
    bodies = []

    # random x & y positions of two Black Holes
    x1,y1 = random.uniform(-40,40,(1,2)).tolist()[0]
    x2,y2 = random.uniform(-40,40,(1,2)).tolist()[0]

    # appending the black holes Body objects the start of the list
    bodies.append(Body(x1,y1,0,0,BH_mass))
    bodies.append(Body(x2,y2,0,0,BH_mass))

    radii = [.1 * box_size, .2 * box_size] #radius of the galaxies


    for j in range(2):
        # for each galaxy, generate a random list of radii from 0
        # to the radius of that galaxy
        randList = random.uniform(0.,radii[j],(1, int(floor(N/2)))).tolist()[0]

        # for each radius, randomly generate an angle for that start
        # and generate inital velocity conditions
        for rand_r in randList:
            theta = random.uniform(0, 2*pi)

            # coordinate transformation, polar --> cart
            x_rel = rand_r * cos(theta) #relative to the Black Hole
            y_rel = rand_r * sin(theta) #relative to the Black Hole

            # create absolute x,y coordinates for the star
            x_abs = x_rel + bodies[j].rx #absolute in the box
            y_abs = y_rel + bodies[j].ry #aboslute in the box

            # magnitude of velocity assuming circular orbit
            v = sqrt(G * solar_mass / rand_r)

            # calculate the initial x,y velocities (assuming no inital galactic vel)
            phi = (pi / 2.) - theta
            vx = v * cos(phi)
            vy = v * sin(phi)

            bodies.append(Body(x_abs,y_abs,vx,vy,solar_mass))


    return(bodies)
