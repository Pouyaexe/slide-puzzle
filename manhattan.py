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

def manhattan_distance(puzzle): # calculate the manhattan distance: h(n)= sum of the distances of the tiles from their goal positions
    distance = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != 0:
                distance += abs(i - (puzzle[i][j] - 1) // len(puzzle[0])) + abs(j - (puzzle[i][j] - 1) % len(puzzle[0]))
    return distance



def a_star_search(puzzle, goal):
    "Using heapq to implement priority queue for A* search"
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(puzzle), puzzle)) # heapq.heappush(heap, item) pushes the value item onto the heap, maintaining the heap invariant. 
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)[1]
        # or we can  frontier.sort(key = lambda x: hammingDistance(x, goal)) which is the same as heapq but slower since it is O(nlogn) but heapq is O(logn)
        # to improve speed, we can use a set to store explored states
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
        print("_"*len(" ".join([str(x).rjust(width) for x in puzzles[i][j]])))
        print()
        

puzzle =  [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
print_puzzle(puzzle, goal)

# let's try a harder puzzle
# puzzle = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
# goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# print_puzzle(puzzle, goal)

# let's try a 4* 4easy puzzle(just one step)
puzzle = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

