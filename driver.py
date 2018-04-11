from initialize import make_galaxies
import tree
import objects

duration = 3e10 #years
dt = 3e5 #years? is this small enough
time_steps = int(duration / dt)


#typical radius is 5e6 ly
box_size = 50 #Mega light years
theta = .5 #threshold for Barnes-Hut
N = 10 #number of bodies, not including Black Holes



#initialization initial conditions
bodies = make_galaxies(N)

#Creat the Quad Tree
sys = tree.Tree(bodies,box_size,dt,theta)



#for i in xrange(time_steps):
sys.advance()
bodies = sys.bodies
x = [b.rx for b in bodies]
y = [b.ry for b in bodies]

print(x)
