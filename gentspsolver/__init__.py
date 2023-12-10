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

# This function performs a mutation operation on a route by swapping two cities with a certain mutation rate
def mutate(route, mutation_rate):
    for swapped in range(len(route)):
        if(random.random() < mutation_rate):
            swap_with = int(random.random() * len(route))

            city1 = route[swapped]
            city2 = route[swap_with]

            route[swapped] = city2
            route[swap_with] = city1
    return route

# This function runs the Genetic Algorithm for the Traveling Salesman Problem
def genetic_algorithm(cities, pop_size, mutation_rate, generations):
    population = [random.sample(cities, len(cities)) for _ in range(pop_size)]
    for _ in range(generations):
        scores = [(total_distance(individual), individual) for individual in population]
        scores.sort()
        selected = [individual for _, individual in scores[:pop_size//2]]
        population = selected
        for _ in range(len(population), pop_size):
            individual1 = population[int(random.random() * len(population))]
            individual2 = population[int(random.random() * len(population))]
            child = crossover(individual1, individual2)
            child = mutate(child, mutation_rate)
            population.append(child)
    return min(population, key=total_distance)

# This function plots the best route
def plot_route(route):
    # Unpack the first and second city coordinates to x and y respectively
    x, y = zip(*route)

    # Add the first city at the end of the route to close the loop
    x = list(x) + [x[0]]
    y = list(y) + [y[0]]

    plt.figure(figsize=(10, 10))
    plt.plot(x, y, 'xb-', markersize=10)
    plt.title(f'Best Route - Total Distance: {total_distance(route):.2f}')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()
