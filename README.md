<!DOCTYPE html>
<html>
  <body>
    <h1> galaxyCollision </h1>
      <p> This is a simulation of galaxy collisions! I have used Eulerian Integration to time step the N-bodies in the simulation and the Barnes-Hut Algorithm to optimize the time complexity of the N-body problem. A typical N-body problem is O(N^2), but with the Barnes-Hut Algorithm the complexity is O(Nlog(N)), allowing for many more bodies and a more realistic galactic collision </p>
    <br>
    <h3> Contents </h3>
    <ul>
      <li> Objects File - This file defines the Body and Cell Classes. A Body object is a mass in the N-body system. A Cell object represents a quadrant in 2 dimensional space. It has the ability to self divide into child quadrants and populate itself with Body objects. </li>
      <li> Tree File - This file defines the Tree object, which has an "advance" method that populates all of the cells with bodies, calculates the net forces on each body according to the Barnes-Hut Algorithm and steps each body through time.</li>
      <li> Initialize File - This file sets the initial conditions for the bodies in the system. Currently </li>
      <li> </li>
    </ul>
  </body>
</html>
  
