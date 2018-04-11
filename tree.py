from objects import Body
from objects import Cell
import initialize

""" The tree class is used to drive the updating of the cells and the
recalculation of the forces across each time step """

#need to add in only interaction between BH and BH && BH and star

class Tree:
    def __init__(self, bodies, box_size, dt, theta):
        self.bodies = bodies #these are all the bodies to be added to the tree
        self.box_size = box_size
        self.dt = dt
        self.theta = theta

    def advance(self):

        #--------------This will repopulate the tree upon every step---------------#
        root = Cell(-self.box_size, self.box_size, -self.box_size, self.box_size)

        for body in self.bodies:
            root.add(body)
        self.bodies = root.get_bodies()


        #--------------For each body calculate the net force on it---------------#
        for body in self.bodies:
            body.resetForces() #reset the net force on the body
            cells = [root]
            while (cells): #while there are still cells in the list
                cell = cells.pop()
                if cell.far_enough(body, self.theta):
                    if (cell.n > 0):
                        body.addForce(cell)
                else:
                    cells.extend(cell.children)
            body.update(self.dt)
