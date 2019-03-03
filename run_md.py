import numpy as np
import matplotlib.pyplot as plt
import atomic

# set input variables
dt=0.001 #stepsize
n=10 #number of atoms in each direction
sig=1. #argon 3.4e-10
lat_const=1. #lattice constant + sig*2**(1/6)
steps=500 #nu,mber of runs/steps for integer
N=n*n
T=1.0 #temperature
m=1.  #for argon n=6.69e-26

#initial cond
r_x,r_y=atomic.init_positions(n,N,lat_const)

print('r_x[50]'+r_x[50])
print('r_y[50]'+r_y[50])

#create initial velocity
v_x,v_y=atomic.init_velocities(T,N)

#compute the acceleration due to the init config
a_x,a_y=atomic.compute_forces(r_x,r_y,N)

#run simulation
k=0
r50x=np.zeros(steps)
t=np.zeros(steps)
while k<steps:
    t[k]=k #for time 0.+dt*k
    v_x,v_y,r_x,r_y,a_x,a_y=vel_verlet(r_x,r_y,v_x,v_y,a_x,a_y,N,dt,m)
    r50x[k]=r50x[k]+r_x[50]
    k=k+1

plt.plot(t,r50x,'r',lw=1.5)
plt.show()


