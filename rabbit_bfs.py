class State:
    def __init__(self, positions, path=[]):
        self.positions = positions
        self.path = path

    def goal_test(self):
        return self.positions == ['E', 'E', 'E', '_', 'W', 'W', 'W']

    def moveGen(self):
        children = []
        pos = self.positions
        empty = pos.index('_')

        # Move rules
        for i in range(len(pos)):
            if pos[i] == 'W':
                if i + 1 == empty:
                    new_pos = pos.copy()
                    new_pos[i], new_pos[empty] = new_pos[empty], new_pos[i]
                    children.append(State(new_pos, self.path + [new_pos]))
                elif i + 2 == empty:
                    if pos[i + 1] in ['E', 'W']:
                        new_pos = pos.copy()
                        new_pos[i], new_pos[empty] = new_pos[empty], new_pos[i]
                        children.append(State(new_pos, self.path + [new_pos]))
            elif pos[i] == 'E':
                if i - 1 == empty:
                    new_pos = pos.copy()
                    new_pos[i], new_pos[empty] = new_pos[empty], new_pos[i]
                    children.append(State(new_pos, self.path + [new_pos]))
                elif i - 2 == empty:
                    if pos[i - 1] in ['E', 'W']:
                        new_pos = pos.copy()
                        new_pos[i], new_pos[empty] = new_pos[empty], new_pos[i]
                        children.append(State(new_pos, self.path + [new_pos]))
        return children

    def bfs():
        start = State(['W', 'W', 'W', '_', 'E', 'E', 'E'], [])
        open_list = [start]
        closed = []

        while open_list:
            node = open_list.pop(0)
            if node.goal_test():
                return node.path

            closed.append(node.positions)
            children = node.moveGen()

            for child in children:
                if child.positions not in closed and child not in open_list:
                    open_list.append(child)

        return []

State.bfs()
    
