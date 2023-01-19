"""
Basic genetic algorithm in python. Trying to evolve a solution to get the best fit function.

A bit of guidance from: https://www.youtube.com/watch?v=4XZoVQOt-0I
"""

import random

# Constants
POP_SIZE = 1000  # population size
MAX_GEN = 10000  # max number of generations to run through
TOP_KEEP = 0.005  # amount of the best to be kept for next gen
TOP_BREED = 0.1  # amount of the best to be used for breeding
GOAL_FITNESS = 9999999  # goal for fitness of function
MUTATION_VARIATION = 0.25  # amount to mutate by
VARS = 3  # total number of variables in the function

# Get bounds for mutation
mut_s = 1 - MUTATION_VARIATION
mut_l = 1 + MUTATION_VARIATION


# Variables
target = 25  # target amount we are trying to reach
def func(x, y, z):  # function that we are fitting
    return 5 * x ** 3 + 3 * y ** 5 + 75 * z


# Determining fitness of solution (how close it is to the answer)
def fitness(x, y, z):
    diff = func(x, y, z) - target

    # if answer is perfect
    if diff == 0:
        return 9999999
    # give fitness based on how far it is
    else:
        # smaller the larger the difference, larger the closer it is
        return abs(1 / diff)


# Generate random starting solutions
sol = []
for i in range(POP_SIZE):
    sol.append((random.uniform(0, 10000),
                random.uniform(0, 10000),
                random.uniform(0, 10000)))

# Running through generations
for gen in range(MAX_GEN):
    # Get fitness and rank solutions (best to worst)
    ranked_sol = []
    for s in sol:
        # print(s)
        ranked_sol.append((fitness(s[0], s[1], s[2]), s))
    ranked_sol.sort(reverse=True)

    # Print to see the best solution and fitness for each gen
    print(f"------------------------- Generation {gen} Best Solutions -------------------------")
    print(ranked_sol[0])

    # Stop if it is past the goal
    if ranked_sol[0][0] > GOAL_FITNESS:
        break

    # New population for next generation
    kept = int(POP_SIZE * TOP_KEEP)  # amount to keep
    # keeping some of the best from the gen
    sol = []
    for i in range(kept):
        sol.append(ranked_sol[i][1])

    # make matrix to track vars separately in best solutions
    inds = []
    for v in range(VARS):
        inds.append([])
    for i in range(int(POP_SIZE * TOP_BREED)):
        inds[0].append(ranked_sol[i][1][0])
        inds[1].append(ranked_sol[i][1][1])
        inds[2].append(ranked_sol[i][1][2])

    # creating new population with crossover and mutation
    for i in range(kept, POP_SIZE):
        sol.append((random.choice(inds[0]) * random.uniform(mut_s, mut_l),
                    random.choice(inds[1]) * random.uniform(mut_s, mut_l),
                    random.choice(inds[2]) * random.uniform(mut_s, mut_l)))

print(f"\n\n\nBest Solution: {ranked_sol[0][1]}" +
      f"\nAnswer: {func(ranked_sol[0][1][0], ranked_sol[0][1][1], ranked_sol[0][1][2])}")
