class BridgeState:
    def __init__(self, left, right, time, path):
        self.left = left  # people on left
        self.right = right  # people on right
        self.time = time
        self.path = path

    def is_goal(self):
        return len(self.left) == 0

    def moveGen(self):
        children = []
        if 'Umbrella' in self.left:
            # Two people go to right
            people = [p for p in self.left if p != 'Umbrella']
            for i in range(len(people)):
                for j in range(i + 1, len(people)):
                    p1, p2 = people[i], people[j]
                    new_left = self.left.copy()
                    new_right = self.right.copy()
                    for p in [p1, p2, 'Umbrella']:
                        new_left.remove(p)
                        new_right.append(p)
                    time_needed = max(p1[1], p2[1])
                    new_path = self.path + [f"{p1[0]} and {p2[0]} cross"]
                    children.append(BridgeState(new_left, new_right, self.time + time_needed, new_path))
        else:
            # One person comes back with umbrella
            people = [p for p in self.right if p != 'Umbrella']
            for p in people:
                new_left = self.left.copy()
                new_right = self.right.copy()
                for item in [p, 'Umbrella']:
                    new_right.remove(item)
                    new_left.append(item)
                time_needed = p[1]
                new_path = self.path + [f"{p[0]} returns"]
                children.append(BridgeState(new_left, new_right, self.time + time_needed, new_path))
        return children

    def dfs():
        people = [('Amogh', 5), ('Ameya', 10), ('Grandma', 20), ('Grandpa', 25)]
        start = BridgeState(people + ['Umbrella'], [], 0, [])
        stack = [start]

        while stack:
            state = stack.pop(0)
            if state.is_goal() and state.time <= 60:
                print("Path:", state.path)
                print("Total time:", state.time)
                return

            for child in state.moveGen():
                if child.time <= 60:
                    stack = [child] + stack  # LIFO stack behavior

        print("No valid path found within 60 minutes.")

BridgeState.dfs()
