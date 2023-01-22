# Write a script that prints out the steps required to solve the puzzle
# using the A* search algorithm and the Humming distance heuristic.
# Your output should be a list of lists, where each inner list is a state of the puzzle. 

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
    if zero[0] < 2:
        neighbors.append([zero[0] + 1, zero[1]])
    if zero[1] > 0:
        neighbors.append([zero[0], zero[1] - 1])
    if zero[1] < 2:
        neighbors.append([zero[0], zero[1] + 1])
    return neighbors

def move(puzzle, neighbor):
    new_puzzle = [row[:] for row in puzzle]
    zero = get_zero(new_puzzle)
    new_puzzle[zero[0]][zero[1]] = new_puzzle[neighbor[0]][neighbor[1]]
    new_puzzle[neighbor[0]][neighbor[1]] = 0
    return new_puzzle

def humming_distance(puzzle):
    distance = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != 0:
                if i != (puzzle[i][j] - 1) // 3 or j != (puzzle[i][j] - 1) % 3:
                    distance += 1
    return distance

def a_star_search(puzzle, goal):
    frontier = []
    frontier.append(puzzle)
    explored = []
    while len(frontier) > 0:
        frontier.sort(key = lambda x: humming_distance(x))
        current = frontier.pop(0)
        explored.append(current)
        if current == goal:
            return explored
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            new_puzzle = move(current, neighbor)
            if new_puzzle not in explored and new_puzzle not in frontier:
                frontier.append(new_puzzle)
    return []

def print_puzzle(puzzle, goal):
    puzzles = a_star_search(puzzle, goal)
    print("Humming distance:", humming_distance(puzzle))
    for puzzle in puzzles:
        print("Step:", puzzles.index(puzzle))
        for row in puzzle:
            print(row)
        print("_____")

puzzle =  [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

print_puzzle(puzzle, goal)