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
        new_puzzle[i][j], new_puzzle[i][j-1] = new_puzzle[i][j-1], new_puzzle[i]

# Example usage
puzzle = [[1, 2, 3],
          [4, 0, 6],
          [7, 5, 8]]
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]
print(a_star(puzzle, goal))
        