import numpy as np
import matplotlib.pyplot as plt

# initial positions
def init_positions(n,N,lat_const):
    r_x=np.zeros(N) #x coordinates
    r_y=np.zeros(N) #y coordinates
    count=0
    for i in range(0,n):
        for j in range(0,n):
            r_x[count]=(i+1)*lat_const
            r_y[count]=(j+1)*lat_const
            count=count+1
return r_x,r_y        

# initial velocities
def init_velocities(T,N):
    mean_vel=0 # mean velocity
    k_b=1. #1.3807e-23
    m=1. #for argon m=1.65e-21 kg
    st_dev=np.sqrt(k_b)*T/N)
    v_x=np.random.normal(mean_vel,st_dev,N)
    v_y=np.random.normal(mean_vel,st_dev,N)
    #centre of mass velocity
    v_x_cm=0.
    v_y_cm=0.
    for i in range(0,N):
        v_x_cm=v_x_cm+v_x[i]
        v_y_cm=v_y_cm+v_y[i]
    v_x_cm=v_x_cm/N
    v_y_cm=v_y_cm/N
    for i in range(0,N):
        v_x[i]=v_x[i]-v_x_cm
        v_y[i]=v_y[i]-v_y_cm
    return v_x,v_y

#compute forces from Lenord Jones potential
def compute_forces(r_x,r_y,N):
    eps=1. #Argon 1.65e-21
    sig=1.  # Argon 3.4e-10
    r_cut=2.5*sig  #cutof radius
    f_x=np.zeros(N) #x forcess
    f_y=np.zeros(N) #y forces
    for i in range(0,N-1):
        for j in range(i+1,N):
            dx=r_x[i]-r_x[j]
            dy=r_y[i]-r_y[j]
            r_ij=np.sqrt(dx*dx+dy*dy)
            if r_ij<rcut:
                f_x[i]=f_x[i]+48.*eps/r_ij*((sig/r_rij)**12-0.5*(sig/r_ij)**6)*dx
                f_x[j]=f_x[j]-48.*eps/r_ij*((sig/r_rij)**12-0.5*(sig/r_ij)**6)*dx
                f_x[i]=f_x[i]+48.*eps/r_ij*((sig/r_rij)**12-0.5*(sig/r_ij)**6)*dy
                f_x[j]=f_x[j]-48.*eps/r_ij*((sig/r_rij)**12-0.5*(sig/r_ij)**6)*dy
    return f_x,f_y

def vel_verlet(r_x,r_y,v_x,v_y,a_x,a_y,N,dt,m):
    for i in range(0,N):
        v_x[i]=v_x[i]+0.5*dt*a_x[i] #velocities at midstep
        v_y[j]=v_y[i]+0.5*dt*a_y[i]
        r_x[i]=r_x[i]+dt*v_x[i]
        r_y[i]=r_y[i]+dt*v_y[i]
    #compute forces at updated position
        a_x,a_y=compute_forces(r_x,r_y)
        for i in range(0,N):
        v_x[i]=v_x[i]+0.5*dt*a_x[i]
        v_y[j]=v_y[i]+0.5*dt*a_y[i]
return v_x,v_y,r_x,r_y,a_x,a_y


