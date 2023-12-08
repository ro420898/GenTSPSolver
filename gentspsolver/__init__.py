import numpy as np
import matplotlib.pyplot as plt
import random

# This function calculates the Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

# This function calculates the total distance of a route
def total_distance(cities):
    return sum([distance(cities[i-1], cities[i]) for i in range(len(cities))])

# This function performs a crossover operation on two parent routes to generate a child route
def crossover(parent1, parent2):
    child = parent1[:len(parent1)//2]
    child += [item for item in parent2 if item not in child]
    return child
