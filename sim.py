import numpy as np
import atmosphere as atmos
from astropy import constants as const

class Sim:
    def __init__(self,earth_r = const.R_earth.value, earth_mass = const.M_earth.value):
        self.earth_r = earth_r
        self.rockets = []
        self.earth_mass = earth_mass

    def add_rocket(self,rocket):
        self.rockets.append(rocket)
        rocket.__addsim__(self)
    
    def gravity_step(self):
        for rocket in self.rockets:
            pass
    
    def step(self,dt=1):
        pass
    
class Rocket:
    def __init__(self,start_pos):
        self.start_pos = start_pos
        self.pos = start_pos
        self.sim = None
    
    def __addsim__(self,sim):
        self.sim = sim
    
    def r(self):
        return np.linalg.norm(self.pos)
    
    def h(self):
        return self.r() - self.sim.earth_r

start_height = 80000

sim = Sim()
rocket = Rocket(np.array([start_height + sim.earth_r,0,0]))
sim.add_rocket(rocket)

print(rocket.h())