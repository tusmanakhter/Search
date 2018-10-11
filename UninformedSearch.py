class UninformedSearch:
    def __init__(self, initial):
        self.initial = initial
        self.path = []
        self.open_list = []
        self.closed_list = []

    def search(self, type):
        self.open_list.append(self.initial)
        goal_found = False
        while len(self.open_list) > 0 and not goal_found:
            if type == "depth_first":
                current_node = self.open_list.pop()
            elif type == "breadth_first":
                current_node = self.open_list.pop(0)
            else:
                print("Invalid search type")
                return
            self.closed_list.append(current_node)

            current_node.print_state()  # For debugging
            print(current_node.depth)  # For debugging

            current_node.expand_moves()
            for child in current_node.children:
                if child.is_goal_state():
                    print("Found goal.")
                    goal_found = True
                    self.trace_path(child)
                if not self.node_in_list(child):
                    self.open_list.append(child)

    def node_in_list(self, new_node):
        contains = False
        for node in self.open_list:
            if node.is_same_state(new_node.state):
                contains = True
        for node in self.closed_list:
            if node.is_same_state(new_node.state):
                contains = True
        return contains

    def trace_path(self, node):
        print("Tracing path\n")
        current = node
        self.path.append(current)

        while current.parent is not None:
            current = current.parent
            self.path.append(current)
