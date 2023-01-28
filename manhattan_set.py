

def a_star_search(puzzle, goal):
    "Using set to implement priority queue for A* search"
    frontier = set()
    frontier.add(puzzle)
    explored = set()
    while len(frontier) > 0:
        state = frontier.pop()
        if state == goal:
            return explored.union(state)
        explored.add(state)
        for neighbor in get_neighbors(state):
            new_state = move(state, neighbor)
            if new_state not in explored and new_state not in frontier:
                frontier.add(new_state)
    return explored