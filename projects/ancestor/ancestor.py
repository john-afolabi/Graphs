class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    vertices = {}
    for x in ancestors:
        for val in x:
            if val not in vertices:
                vertices[val] = set()
        vertices[x[1]].add(x[0])

    s = Stack()
    s.push([starting_node])

    longest = 1
    earliest_ancestor = -1
    while s.size() > 0:
        path = s.pop()
        v = path[-1]
        if (len(path) == longest
                and v < earliest_ancestor) or (len(path) > longest):
            earliest_ancestor = v
            longest = len(path)
        for neighbor in vertices[v]:
            path_copy = path.copy()
            path_copy.append(neighbor)
            s.push(path_copy)
    return earliest_ancestor