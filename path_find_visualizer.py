"""
Maze path finding algorithm visualization program in Python. Trying to learn more about curses module and
also got to use cProfile.

Heavily modified the code from: youtube.com/watch?v=txKBWtvV99Y
"""

import cProfile
import curses
import math
from queue import PriorityQueue
import time

# The problem maze with O as start, X as end, # as walls, and " " as path
problem_maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
start = "O"
end = "X"


# Function for printing maze
def print_maze(maze, stdscr, path=[]):
    # 2 colors
    blue = curses.color_pair(1)
    red = curses.color_pair(2)

    # Loops through every coordinate
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            # Red if on path
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", red)
            # Blue to print walls
            else:
                stdscr.addch(i, j * 2, value, blue)


# Function for finding a target in the maze
def find_target(maze, target):
    # Loops through every coordinate
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            # Returns the coordinates when found
            if value == target:
                return i, j
    # Returns none if target could not be found
    return None


# Function finding all possible neighbor moves
def find_neighbors(maze, y, x):
    # List for tracking
    neighbors = []
    # Checks each direction and adds if it is a possible path
    if y > 0:  # UP
        if maze[y - 1][x] != "#":
            neighbors.append((y - 1, x))
    if y + 1 < len(maze):  # DOWN
        if maze[y + 1][x] != "#":
            neighbors.append((y + 1, x))
    if x > 0:  # LEFT
        if maze[y][x - 1] != "#":
            neighbors.append((y, x - 1))
    if x + 1 < len(maze[0]):  # RIGHT
        if maze[y][x + 1] != "#":
            neighbors.append((y, x + 1))
    return neighbors


# Function for heuristic using manhattan distance
def manhattan_heuristic(current_coord, target_coord):
    cy, cx = current_coord
    ty, tx = target_coord
    return abs(tx - cx) + abs(ty - cy)


# Function for heuristic using euclidean distance (found that it is less efficient)
def euclidean_heuristic(current_coord, target_coord):
    cy, cx = current_coord
    ty, tx = target_coord
    return math.sqrt((tx - cx) ** 2 + (ty - cy) ** 2)


# Function for the actual a* search algorithm
def a_star(maze, stdscr):
    # Find start location and add start
    start_coord = find_target(maze, start)
    end_coord = find_target(maze, end)
    fringe = PriorityQueue()
    visited = [start_coord]
    fringe.put((0, 0, start_coord, [start_coord]))

    # Looping until there's no more possible paths
    while not fringe.empty():
        # Getting current state and coordinates
        _, backward_cost, current_coord, path = fringe.get()
        y, x = current_coord

        # Show updated maze path in console
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        # Goal check and returning path when over
        if current_coord == end_coord:
            return path

        # Adds neighboring moves if they have not been visited yet
        neighbors = find_neighbors(maze, y, x)
        backward_cost += 1  # increment backwards cost since one more move
        for neighbor in neighbors:
            if neighbor not in visited:
                # Calculates total predicted cost and total backward cost based on old backward cost
                total_cost = backward_cost + manhattan_heuristic(neighbor, end_coord)
                # total_cost = backward_cost + euclidean_heuristic(neighbor, end_coord)
                new_path = path + [neighbor]
                fringe.put((total_cost, backward_cost, neighbor, new_path))
                # Add to visited
                visited.append(neighbor)


# Main function
def main(stdscr):
    # Initialize color schemes
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # Run search algorithm
    a_star(problem_maze, stdscr)
    # stdscr.getch()


# Run everything using cProfile (to look at efficiency)
cProfile.run("curses.wrapper(main)")
