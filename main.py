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

# Function to find the coordinates of the blank space
def find_blank(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i, j)

# Function to generate the possible next states
def next_states(puzzle, blank):
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
    return states

# A* search function
def a_star(puzzle, goal):
    # Initialize the heap with the starting state
    heap = [(manhattan_distance(puzzle, goal), puzzle, [])]
    # Create a set to keep track of the visited states
    visited = set()
    while heap:
        # Pop the state with the lowest f(n) from the heap
        _, current_puzzle, moves = heapq.heappop(heap)
        # If the current state is the goal state, return the moves
        if current_puzzle == goal:
            return moves
        # If the current state has already been visited, skip it
        if str(current_puzzle) in visited:
            continue
        # Mark the current state as visited
        visited.add(str(current_puzzle))
        # Print the current state of the puzzle
        for row in current_puzzle:
            print(row)
        # Find the coordinates of the blank space
        blank = find_blank(current_puzzle)
        # Generate the possible next states
        for next_puzzle, move, blank_num in next_states(current_puzzle, blank):
            # Append the move to the list of moves
            next_moves = moves + [move]
            # Print the tile number and arrow for the next move
            print(f"{blank_num}-{move}")
            if move == 'up':
                print("↑")
            elif move == 'down':
                print("↓")
            elif move == 'left':
                print("←")
            elif move == 'right':
                print("→")
            # Calculate the heuristic value
            h = manhattan_distance(next_puzzle, goal)
            # Add the next state to the heap with f(n) = g(n) + h(n)
            heapq.heappush(heap, (len(next_moves) + h, next_puzzle, next_moves))

# Example usage
puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print(a_star(puzzle, goal))
        