# Write a script that prints out the steps required to solve the puzzle
# using the A* search algorithm and the Manhattan distance heuristic.
# Your output should be a list of lists, where each inner list is a state of the puzzle.
# We will use hip in this example, but you can use any other heuristic function. 

import heapq # for priority queue implementation we use

def get_zero(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return [i, j]

def get_neighbors(puzzle):
    neighbors = []
    zero = get_zero(puzzle)
    if zero[0] > 0:
        neighbors.append([zero[0] - 1, zero[1]])
    if zero[0] < len(puzzle) - 1:
        neighbors.append([zero[0] + 1, zero[1]])
    if zero[1] > 0:
        neighbors.append([zero[0], zero[1] - 1])
    if zero[1] < len(puzzle[0]) - 1:
        neighbors.append([zero[0], zero[1] + 1])
    return neighbors

def move(puzzle, neighbor):
    new_puzzle = [row[:] for row in puzzle]
    zero = get_zero(new_puzzle)
    new_puzzle[zero[0]][zero[1]] = new_puzzle[neighbor[0]][neighbor[1]]
    new_puzzle[neighbor[0]][neighbor[1]] = 0
    return new_puzzle

def manhattan_distance(puzzle):
    distance = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != 0:
                distance += abs(i - (puzzle[i][j] - 1) // len(puzzle[0])) + abs(j - (puzzle[i][j] - 1) % len(puzzle[0]))
    return distance



def a_star_search(puzzle, goal):
    "Using heapq to implement priority queue for A* search"
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(puzzle), puzzle))
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)[1]
        # print("Expanding:", state)
        if state == goal:
            return explored + [state] # + state to include the goal state
        explored.append(state)
        for neighbor in get_neighbors(state):
            new_state = move(state, neighbor)
            if new_state not in explored and new_state not in [x[1] for x in frontier]:
                heapq.heappush(frontier, (manhattan_distance(new_state), new_state))
    return explored

def print_puzzle(puzzle, goal):
    puzzles = a_star_search(puzzle, goal)
    print("Manhattan distance:", manhattan_distance(puzzle))
    # if size=len(puzzle)^2 > 9, we need to adjust the width of the output
    width = len(str(len(puzzle) ** 2))
    for i in range(len(puzzles)):
        print("Step", i)
        for j in range(len(puzzles[i])):
            print(" ".join([str(x).rjust(width) for x in puzzles[i][j]]))
        print()
        

# puzzle =  [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
# goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
# print_puzzle(puzzle, goal)

# let's try a harder puzzle
# puzzle = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
# goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# print_puzzle(puzzle, goal)

# let's try a 11*11 easy puzzle(just one step)
puzzle = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]]
goal = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 0]]
print_puzzle(puzzle, goal)
