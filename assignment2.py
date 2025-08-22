#     1.​ Implementation of Best First Search and A* Search.



class State:
    def __init__(self, position, goal):
        self.position = position    
        self.goal = goal            

    def goalTest(self):
        return self.position == self.goal


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def h(state):
    return manhattan(state.position, state.goal)

def MoveGen(state, grid):
    rows, cols = len(grid), len(grid[0])
    x, y = state.position
    g = state.goal
    children = []
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            children.append(State((nx, ny), g))
    return children

def format_path(path):
    return "[" + ", ".join(f"({r},{c})" for r, c in path) + "]"



def BestFirstSearch(grid):
    n, m = len(grid), len(grid[0])
    start_pos, goal_pos = (0, 0), (n-1, m-1)
    if grid[start_pos[0]][start_pos[1]] == 1 or grid[goal_pos[0]][goal_pos[1]] == 1:
        return []

    S = State(start_pos, goal_pos)
    OPEN = [(S, h(S))]
    parent = {}
    visited = set()

    while OPEN:
        OPEN.sort(key=lambda t: t[1])
        N, _ = OPEN.pop(0)
        visited.add(N.position)

        if N.goalTest():
            path = []
            cur = N.position
            while cur in parent:
                path.append(cur)
                cur = parent[cur]
            path.append(start_pos)
            path.reverse()
            return path

        for M in MoveGen(N, grid):
            if M.position not in visited and all(M.position != node.position for node, _ in OPEN):
                parent[M.position] = N.position
                OPEN.append((M, h(M)))

    return []



def AStarSearch(grid):
    n, m = len(grid), len(grid[0])
    start_pos, goal_pos = (0, 0), (n-1, m-1)
    if grid[start_pos[0]][start_pos[1]] == 1 or grid[goal_pos[0]][goal_pos[1]] == 1:
        return []

    S = State(start_pos, goal_pos)
    g = {(i, j): float('inf') for i in range(n) for j in range(m)}
    parent = {}
    g[S.position] = 0
    f = {S.position: g[S.position] + h(S)}

    OPEN = [S]
    CLOSED = set()

    while OPEN:
        OPEN.sort(key=lambda node: f.get(node.position, float('inf')))
        N = OPEN.pop(0)
        CLOSED.add(N.position)

        if N.goalTest():
            path = []
            cur = N.position
            while cur in parent:
                path.append(cur)
                cur = parent[cur]
            path.append(start_pos)
            path.reverse()
            return path

        for M in MoveGen(N, grid):
            tentative = g[N.position] + 1
            if tentative < g[M.position]:
                parent[M.position] = N.position
                g[M.position] = tentative
                f[M.position] = g[M.position] + manhattan(M.position, goal_pos)

                if M.position not in CLOSED and all(M.position != node.position for node in OPEN):
                    OPEN.append(M)

    return []



def show_results(title, grid):
    print(title)
    print("Input:")
    for i, row in enumerate(grid):
        if i == 0:
            print("grid = [", row, ",")
        elif i == len(grid) - 1:
            print("        ", row, "]")
        else:
            print("        ", row, ",")

    bfs_path = BestFirstSearch(grid)
    astar_path = AStarSearch(grid)

    header = "Output (example format):" if title.strip().startswith("Example 1") else "Output:"
    print(header)

    if bfs_path:
        print(f"Best First Search → Path length: {len(bfs_path)}, Path: {format_path(bfs_path)}")
    else:
        print("Best First Search → Path length: -1")

    if astar_path:
        print(f"A* Search→ Path length: {len(astar_path)}, Path: {format_path(astar_path)}")
    else:
        print("A* Search→ Path length: -1")
    print()



def test_example1():
    grid = [[0, 1],
            [1, 0]]
    assert BestFirstSearch(grid) == [(0,0),(1,1)]
    assert AStarSearch(grid) == [(0,0),(1,1)]

def test_example2():
    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]
    assert BestFirstSearch(grid) == [(0,0),(0,1),(0,2),(1,2),(2,2)] or BestFirstSearch(grid) == [(0,0),(0,1),(1,2),(2,2)]
    assert AStarSearch(grid) == [(0,0),(0,1),(0,2),(1,2),(2,2)] or AStarSearch(grid) == [(0,0),(0,1),(1,2),(2,2)]

def test_example3():
    grid = [[1, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]
    assert BestFirstSearch(grid) == []
    assert AStarSearch(grid) == []



if __name__ == "__main__":
    show_results("Example 1:", [[0, 1],
                                [1, 0]])

    show_results("Example 2:", [[0, 0, 0],
                                [1, 1, 0],
                                [1, 1, 0]])

    show_results("Example 3:", [[1, 0, 0],
                                [1, 1, 0],
                                [1, 1, 0]])


#      2.​ Output for given test cases



"""   outputs:
            1.  grid = [ [0, 1] ,[1, 0] ]
                Best First Search → Path length: 2, Path: [(0,0), (1,1)]
                A* Search→ Path length: 2, Path: [(0,0), (1,1)]

            2.  grid = [ [0, 0, 0] ,[1, 1, 0] ,[1, 1, 0] ]
                Best First Search → Path length: 4, Path: [(0,0), (0,1), (1,2), (2,2)]
                A* Search→ Path length: 4, Path: [(0,0), (0,1), (1,2), (2,2)]
                
            3.  grid = [ [1, 0, 0] ,[1, 1, 0] ,[1, 1, 0] ]
                Best First Search → Path length: -1
                A* Search→ Path length: -1
"""


#       A short comparison (1–2 paragraphs) discussing differences in results and performance.​  


""" 
                Best First Search and A* both manage to find paths in the examples, but they work a bit differently.
            Best First Search only looks at the estimated distance to the goal, so it tends to head straight 
            toward it as quickly as possible. This can make it faster in some cases, but it doesn’t always 
            guarantee the shortest path and can get stuck if the greedy choice leads into a dead end. A*, on the
            other hand, combines the actual distance traveled with the estimated distance left. Because of this, 
            it explores more carefully and always finds the shortest path when one exists.

                In terms of performance, Best First Search can feel quicker since it expands fewer nodes when the path is obvious, 
            but it’s less reliable. A* takes a little more work since it keeps track of both the cost so far and the cost ahead, 
            but this extra effort pays off with guaranteed optimal results. For problems like grid navigation, A* is usually 
            the safer and more dependable choice.



""""
