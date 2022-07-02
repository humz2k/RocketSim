import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("atmosphere.csv")
geometric_height = data.loc[:,"Geometric"].to_numpy()
temp_k = data.loc[:,"temp k"].to_numpy()
density = data.loc[:,"density kg/m**3"].to_numpy()
pressure = data.loc[:,"pressure N/m**2"].to_numpy()

def T(h):
    comp = geometric_height > h
    if np.sum(comp) == 0:
        return -347.66
    big_t = temp_k[comp][0]
    small_t = temp_k[np.logical_not(comp)][-1]
    big_h = geometric_height[comp][0]
    small_h = geometric_height[np.logical_not(comp)][-1]
    h_change = big_h - small_h
    t_change = big_t - small_t
    mul = (h-small_h)/h_change
    return mul * t_change + small_t

Temp = np.vectorize(T)

def rho(h):
    comp = geometric_height > h
    if np.sum(comp) == 0:
        return -347.66
    big_t = density[comp][0]
    small_t = density[np.logical_not(comp)][-1]
    big_h = geometric_height[comp][0]
    small_h = geometric_height[np.logical_not(comp)][-1]
    h_change = big_h - small_h
    t_change = big_t - small_t
    mul = (h-small_h)/h_change
    return mul * t_change + small_t

Density = np.vectorize(rho)

def P(h):
    comp = geometric_height > h
    if np.sum(comp) == 0:
        return -347.66
    big_t = pressure[comp][0]
    small_t = pressure[np.logical_not(comp)][-1]
    big_h = geometric_height[comp][0]
    small_h = geometric_height[np.logical_not(comp)][-1]
    h_change = big_h - small_h
    t_change = big_t - small_t
    mul = (h-small_h)/h_change
    return mul * t_change + small_t

Pressure = np.vectorize(P)