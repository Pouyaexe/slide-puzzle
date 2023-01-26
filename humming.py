# App for solving the 8-puzzle problem using A* search and humming distance heuristic.

def get_zero(puzzle):
    """Get the position of the zero in the puzzle.

    Args:
        puzzle: the puzzle to be solved

    Returns:
        a list of two integers, the row and column of the zero
    """
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return [i, j]

# get the neighbors of the zero (up, down, left, right)
def get_neighbors(puzzle):
    """Get the neighbors of the zero in the puzzle.
    Args:
        puzzle: the puzzle to be solved
        
    Returns:
        a list of lists of two integers, the row and column of the neighbors
    """
    neighbors = []
    zero = get_zero(puzzle)
    if zero[0] > 0: # if zero is not in the first row because we can't move up
        neighbors.append([zero[0] - 1, zero[1]])
    if zero[0] < len(puzzle) - 1:
        neighbors.append([zero[0] + 1, zero[1]])
    if zero[1] > 0: # if zero is not in the first column because we can't move left
        neighbors.append([zero[0], zero[1] - 1])
    if zero[1] < len(puzzle[0]) - 1:
        neighbors.append([zero[0], zero[1] + 1])
    return neighbors


def move(puzzle, neighbor): # move the zero to the neighbor position and return the new puzzle (sliding the zero)
    new_puzzle = [row[:] for row in puzzle]
    zero = get_zero(new_puzzle)
    new_puzzle[zero[0]][zero[1]] = new_puzzle[neighbor[0]][neighbor[1]]
    new_puzzle[neighbor[0]][neighbor[1]] = 0
    return new_puzzle

def hammingDistance( puzle, goal): # calculate the number of tiles that are not in the right position (hamming distance): h(n)= number of misplaced tiles
    ans = 0
    for i in range(len(puzle)):
        for j in range(len(puzle[0])):
            if puzle[i][j] != goal[i][j]: # if the tile is not in the right position (not equal to the goal)
                ans += 1
    return ans           

def a_star_search(puzzle, goal):
    frontier = []
    frontier.append(puzzle)
    explored = []
    while len(frontier) > 0:
        frontier.sort(key = lambda x: hammingDistance(x, goal)) # sort the frontier by the hamming distance. The puzzle with the lowest hamming distance will be the first in the frontier
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
    print("hamming distance:", hammingDistance(puzzle, goal))
    # if size=len(puzzle)^2 > 9, we need to adjust the width of the output
    width = len(str(len(puzzle) ** 2))
    for i in range(len(puzzles)):
        print("Step", i)
        for j in range(len(puzzles[i])):
            print(" ".join([str(x).rjust(width) for x in puzzles[i][j]]))
        print("_"*len(" ".join([str(x).rjust(width) for x in puzzles[i][j]])))
        print()



puzzle =  [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# 4 * 4 puzzle
puzzle = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]]
goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

print_puzzle(puzzle, goal)