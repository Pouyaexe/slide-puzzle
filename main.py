import heapq

# Function to calculate the Manhattan distance
def manhattan_distance(puzzle, goal):
    distance = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != 0:
                x, y = divmod(puzzle[i][j] - 1, len(puzzle[0]))
                distance += abs(i - x) + abs(j - y)
    return distance

# Function to generate the possible next states
def next_states(puzzle, blank, goal):
    i, j = blank
    states = []
    if i > 0:
        new_puzzle = [row[:] for row in puzzle]
        blank_num = new_puzzle[i-1][j]
        new_puzzle[i][j], new_puzzle[i-1][j] = new_puzzle[i-1][j], new_puzzle[i][j]
        states.append((new_puzzle, 'up', blank_num))
    if i < len(puzzle) - 1:
        new_puzzle = [row[:] for row in puzzle]
        blank_num = new_puzzle[i+1][j]
        new_puzzle[i][j], new_puzzle[i+1][j] = new_puzzle[i+1][j], new_puzzle[i][j]
        states.append((new_puzzle, 'down', blank_num))
    if j > 0:
        new_puzzle = [row[:] for row in puzzle]
        blank_num = new_puzzle[i][j-1]
        new_puzzle[i][j], new_puzzle[i][j-1] = new_puzzle[i][j-1], new_puzzle[i][j]
        states.append((new_puzzle, 'left', blank_num))
    if j < len(puzzle[0]) - 1:
        new_puzzle = [row[:] for row in puzzle]
        blank_num = new_puzzle[i][j+1]
        new_puzzle[i][j], new_puzzle[i][j+1] = new_puzzle[i][j+1], new_puzzle[i][j]
        states.append((new_puzzle, 'right', blank_num))
    # Find the tile that is going to be moved
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != goal[i][j]:
                move_num = puzzle[i][j]
                break
    return states, move_num

# A* search function
def a_star(puzzle, goal):
    # Initialize the heap with the starting state
    heap = [(manhattan_distance(puzzle, goal), puzzle, [])]
    # Create a set to keep track of the visited states
    visited = set()
    while heap:
        # Pop the state with the lowest f(n) from the heap
        _

# Example usage
puzzle = [[1, 2, 3],
          [4, 0, 6],
          [7, 5, 8]]
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]
print(a_star(puzzle, goal))
        