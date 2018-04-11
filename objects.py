import math
import numpy

""" The Body and Cell objects are defined here. A Body can step itself through time, with
Euler Integration. A Cell can self divide, and populate itself with Bodies """

G = 6.673e-11 #Gravitational Constant

# Body Class
class Body:
    def __init__(self, rx, ry, vx, vy, mass):
        self.rx, self.ry = rx, ry
        self.vx, self.vy = vx, vy
        self.fx, self.fy = 0, 0
        self.mass = mass

    # Euler integration time step
    def update(self, dt):
        self.vx += dt * (self.fx / self.mass)
        self.vy += dt * (self.fy / self.mass)
        self.rx += dt * self.vx
        self.ry += dt * self.vy

    # distance between a body and a cell
    def distance_To(self,cell):
        dx = cell.xcen - self.rx
        dy = cell.ycen - self.ry
        return(math.sqrt(dx**2 + dy**2),dx,dy)

    def resetForces(self):
        self.fx = 0
        self.fy = 0

    # calcualte the force between self and a cell, and update fx & fy
    def addForce(self, cell):
        dist,dx,dy = self.distance_To(cell)
        F = (G * self.mass * cell.totm) / (dist * dist)
        self.fx += F * (dx / dist) #cosine
        self.fy += F * (dy / dist) # sine

# A cell can have no body, one body, OR refer to 4 child nodes
class Cell:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin, self.xmax = xmin, xmax
        self.ymin, self.ymax = ymin, ymax

        #start with no bodies
        self.n = 0
        self.xcen, self.ycen = 0, 0
        self.totm = 0
        self.children = []
        self.body = None

    # test if an (x,y) coordinate is in this cell's bounds
    def incell(self, x, y):
        if (x > self.xmin and x<= self.xmax and y > self.ymin and y <= self.ymax):
            return(True)
        else:
            return(False)

    # this is a method to add a body to a cell
    def add(self, body):
        # if body is not in the bounds of the cell, don't do anything
        if not self.incell(body.rx, body.ry):
            return()

        # if this cell already has some bodies
        if self.n > 0:
            # if there is only one body currently, make children
            if self.n == 1:
                self.make_children()
                for child in self.children:
                    child.add(self.body)
                self.body = None
            # either way try to add the body to all the children
            for child in self.children:
                child.add(body) #now add the incoming body to one of these children
        else:
            self.body = body

        # change center of mass. Update total mass, then update CoM
        self.totm += body.mass #update total mass
        self.xcen = (self.n * self.xcen + body.rx) / float(self.n + 1)
        self.ycen = (self.n * self.ycen + body.ry) / float(self.n + 1)
        self.n += 1

    def make_children(self):
        xhalf = (self.xmin + self.xmax) / 2.
        yhalf = (self.ymin + self.ymax) / 2.
        child1 = Cell(self.xmin, xhalf, self.ymin, yhalf)
        child2 = Cell(xhalf, self.xmax, self.ymin, yhalf)
        child3 = Cell(self.xmin, xhalf, yhalf, self.ymax)
        child4 = Cell(xhalf, self.xmax, yhalf, self.ymax)
        self.children = [child1, child2, child3, child4]


    # traverse the tree to get a list of bodies in this cell and below
    def get_bodies(self):
    # if this cell has one body (external cell), return that body
        if self.body:
            return([self.body])
    # if this cell has children, accumulate their bodies
        elif self.children:
            body_list = []
            for child in self.children:
                body_list.extend(child.get_bodies()) #this recurses down until their is either 1 or 0 bodies
            return(body_list)
    # if this is an external node, with no body, return nothing
        else:
            return([])

     # test if this cell is far enough from the specified body
    def far_enough(self, body, theta):
     # if this cell is internal, cell center of mass
     # must be farther from body than size of cell
        if (self.children):
            s = self.xmax - self.xmin # width of the cell
            dx = self.xcen - body.rx
            dy = self.ycen - body.ry
            d  = (dx*dx + dy*dy)**0.5
            return((d/s) > theta)
    # else if the cell is external, just check to make sure
    # the body doesn't interact with itself.
        else:
            return(self.body != body)
