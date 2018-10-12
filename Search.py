# Parts of this implementation inspired by the following:
# https://www.youtube.com/watch?v=6edibwHBDFk
from operator import attrgetter


class Search:
    def __init__(self, initial):
        self.initial = initial
        self.path = []
        self.open_list = []
        self.closed_list = []

    def search(self, search_type, max_depth=None):
        self.open_list.append(self.initial)
        goal_found = False
        while len(self.open_list) > 0 and not goal_found:
            if search_type == "depth_first":
                current_node = self.open_list.pop()
            elif search_type == "breadth_first":
                current_node = self.open_list.pop(0)
            elif search_type == "best_first":
                current_node = min(self.open_list, key=attrgetter('heuristic'))
                self.open_list.remove(current_node)
            elif search_type == "a":
                current_node = min(self.open_list, key=attrgetter('f_value'))
                self.open_list.remove(current_node)
            else:
                print("Invalid search type")
                return
            self.closed_list.append(current_node)

            print("Searching depth: " + str(current_node.depth))  # For debugging
            print("Current state: " + current_node.state_to_string())  # For debugging

            if current_node.is_goal_state():
                goal_found = True
                self.trace_path(current_node)

            if search_type == "depth_first":
                if max_depth and current_node.depth >= max_depth:
                    continue
                current_node.expand_moves("depth_first")
            else:
                current_node.expand_moves()

            for child in current_node.children:
                if not self.node_in_list(child):
                    self.open_list.append(child)
        if search_type == "depth_first" and not goal_found and max_depth is not None:
            self.open_list = []
            self.closed_list = []
            self.search("depth_first", max_depth * 2)

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
        current = node
        self.path.append(current)

        while current.parent is not None:
            current = current.parent
            self.path.append(current)

    def trace_to_string(self):
        trace = ""
        for node in reversed(self.path):
            trace += node.state_to_string() + "\n"
        return trace

