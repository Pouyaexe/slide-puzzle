import hashlib

def get_zero(puzzle):
    """Get the position of the zero in the puzzle.
    Args:
        puzzle: the puzzle to be solved
    Returns:
        a list of lists
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
        # zero = [i,j] /// zero[0] = i , zero[1] = j
        neighbors.append([zero[0] - 1, zero[1]])
    if zero[0] < len(puzzle) - 1:
        neighbors.append([zero[0] + 1, zero[1]])
    if zero[1] > 0: # if zero is not in the first column because we can't move left
        neighbors.append([zero[0], zero[1] - 1])
    if zero[1] < len(puzzle[0]) - 1:
        neighbors.append([zero[0], zero[1] + 1])
    return neighbors

def get_neighbors_hash_table(puzzle):
    """Get the neighbors of the zero in the puzzle.
    Args:
    puzzle: the puzzle to be solved
    Returns:
    a list of lists of two integers, the row and column of the neighbors
    """
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


def move(puzzle, neighbor): # move the zero to the neighbor position and return the new puzzle (sliding the zero)
    new_puzzle = [row[:] for row in puzzle]
    zero = get_zero(new_puzzle)
    new_puzzle[zero[0]][zero[1]] = new_puzzle[neighbor[0]][neighbor[1]] 
    new_puzzle[neighbor[0]][neighbor[1]] = 0
    return new_puzzle

def manhattan_distance_hash_table(puzzle, goal):
    # create a hash table for the goal puzzle
    hash_table = {}
    for i in range(len(goal)):
        for j in range(len(goal[0])):
            hash_table[goal[i][j]] = [i, j] # goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] hash_table = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 0: [2, 2]} so i is the row and j is the column
    # calculate the manhattan distance
    ans = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != 0:
                ans += abs(hash_table[puzzle[i][j]][0] - i) + abs(hash_table[puzzle[i][j]][1] - j)
    return ans
 
def hash_puzzle(puzzle):
    # convert the puzzle to a string and hash it using sha256 
    return hashlib.sha256(str(puzzle).encode()).hexdigest() 

 
def a_star_search_hash_table(puzzle, goal):
    frontier = []
    frontier.append(puzzle)
    explored = {}
    while len(frontier) > 0:
        frontier.sort(key = lambda x: manhattan_distance_hash_table(x, goal))
        current = frontier.pop(0)
        puzzle_hash = hash_puzzle(current)
        if puzzle_hash in explored:
            continue
        print("Exploring:", puzzle_hash) 
        print("_____")
        print("Explored", explored)
        explored[puzzle_hash] = current
        if current == goal:
            return explored
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            new_puzzle = move(current, neighbor)
            if hash_puzzle(new_puzzle) not in explored and new_puzzle not in frontier:
                frontier.append(new_puzzle)
    return None

def print_puzzle(puzzle, goal):
    puzzles = a_star_search_hash_table(puzzle, goal)
    print("Manhattan Distance:", manhattan_distance_hash_table(puzzle, goal))
    # if size=len(puzzle)^2 > 9, we need to adjust the width of the output
    width = len(str(len(puzzle) ** 2))
    for puzzle_hash in puzzles:
        for row in puzzles[puzzle_hash]:
            for num in row:
                print(str(num).rjust(width), end = " ")
            print()
        print("-" * (width +1) * len(puzzle[0]))
        


puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print_puzzle(puzzle, goal)

# let's try a harder puzzle 
# puzzle = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
# goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 
# print_puzzle(puzzle, goal) 
# test 4*4 puzzle

# let's try a 4* 4easy puzzle(just one step)
puzzle = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

