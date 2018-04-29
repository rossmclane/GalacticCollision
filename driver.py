from initialize import make_galaxies
import tree
import objects

duration = 3e10 #years
dt = 100
#time_steps = int(duration / dt)
time_steps = 10

#typical radius is 5e6 ly
box_size = 50 #Mega light years
theta = .5 #threshold for Barnes-Hut
N = 0 #number of bodies, not including Black Holes



#initialization initial conditions
bodies = make_galaxies(N)

#Creat the Quad Tree
sys = tree.Tree(bodies,box_size,dt,theta)



for i in xrange(time_steps):
    print(sys.bodies)
    sys.advance()
