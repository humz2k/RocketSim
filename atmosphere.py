from astropy import units as u

layers = {"troposphere": 11000 * u.m, "tropopause": 20000 * u.m, "stratosphere": 30000 * u.m}
class Temperature:
    def __init__(self,T0 = 288.15 * u.K, L = .0065 * u.K,layers=layers):
        self.T0 = T0
        self.L = L
        self.layers = layers
    
    def __call__(self,h):
        if type(h) == type(int):
            h = h * u.m
        print(h)
        #if h.value < self.layers["troposphere"].value:
         #   return self.T0 - self.L * h

T = Temperature()
print(T(10))