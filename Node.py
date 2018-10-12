# Parts of this implementation inspired by the following:
# https://www.youtube.com/watch?v=6edibwHBDFk
# https://gist.github.com/flatline/838202/ca0d35b0ce7e5d9ec86b77b0490baba4cda87980


import string
import math


class Node:
    def __init__(self, state, columns, parent, move, depth, heuristic_type=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.columns = columns
        self.heuristic_type = heuristic_type
        self.heuristic = self.heuristic(heuristic_type)
        self.f_value = self.f_value()

        # to get step
        self.letters = dict(enumerate(string.ascii_lowercase))

        # children
        self.children = []

    def is_goal_state(self):
        goal_state = True
        if self.state[len(self.state) - 1] != 0:
            return False
        for i in range(len(self.state)-2):
            if self.state[i] > self.state[i+1]:
                return False
        return goal_state

    def expand_moves(self, search_type=None):
        for index, value in enumerate(self.state):
            if value == 0:
                empty = index
                if search_type == "depth_first":
                    self.move_up_left(empty)
                    self.move_left(empty)
                    self.move_down_left(empty)
                    self.move_down(empty)
                    self.move_down_right(empty)
                    self.move_right(empty)
                    self.move_up_right(empty)
                    self.move_up(empty)
                else:
                    self.move_up(empty)
                    self.move_up_right(empty)
                    self.move_right(empty)
                    self.move_down_right(empty)
                    self.move_down(empty)
                    self.move_down_left(empty)
                    self.move_left(empty)
                    self.move_up_left(empty)

    def move_up(self, i):
        if i - self.columns > 0:
            switch_position = i-self.columns
            self.add_child_move(i, switch_position)

    def move_up_right(self, i):
        if i - self.columns > 0 and i % self.columns < self.columns - 1:
            switch_position = i+1-self.columns
            self.add_child_move(i, switch_position)

    def move_right(self, i):
        if i % self.columns < self.columns - 1:
            switch_position = i+1
            self.add_child_move(i, switch_position)

    def move_down_right(self, i):
        if i + self.columns < len(self.state) and i % self.columns < self.columns - 1:
            switch_position = i+1+self.columns
            self.add_child_move(i, switch_position)

    def move_down(self, i):
        if i + self.columns < len(self.state):
            switch_position = i+self.columns
            self.add_child_move(i, switch_position)

    def move_down_left(self, i):
        if i + self.columns < len(self.state) and i % self.columns > 0:
            switch_position = i-1+self.columns
            self.add_child_move(i, switch_position)

    def move_left(self, i):
        if i % self.columns > 0:
            switch_position = i-1
            self.add_child_move(i, switch_position)

    def move_up_left(self, i):
        if i - self.columns > 0 and i % self.columns > 0:
            switch_position = i-1-self.columns
            self.add_child_move(i, switch_position)

    def add_child_move(self, zero_index, switch_position):
        new_state = self.state.copy()
        new_state[zero_index], new_state[switch_position] = new_state[switch_position], new_state[zero_index]
        child = Node(new_state, self.columns, self, self.letters[switch_position], self.depth + 1, self.heuristic_type)
        self.children.append(child)

    def state_to_string(self):
        return self.move + " [" + ', '.join(str(x) for x in self.state) + "]"

    def is_same_state(self, other_state):
        is_same = False
        if self.state == other_state:
            is_same = True
        return is_same

    def f_value(self):
        if self.heuristic is not None:
            return self.heuristic + self.depth

    def heuristic(self, heuristic_type):
        if heuristic_type == "linear_distance":
            return self.heuristic_linear_distance()
        elif heuristic_type == "wrong_row_column":
            return self.heuristic_wrong_row_column()
        else:
            return None

    def heuristic_linear_distance(self):
        total = 0
        for index, element in enumerate(self.state):
            row = math.floor(index / self.columns)
            column = index % self.columns
            goal_row = math.floor((element - 1) / self.columns)
            goal_column = (element - 1) % self.columns

            # For 0 to go last
            if element == 0:
                goal_row = 2

            total += math.sqrt(math.sqrt((goal_row - row) ** 2 + (goal_column - column) ** 2))
        return total

    def heuristic_wrong_row_column(self):
        total = 0
        for index, element in enumerate(self.state):
            row = math.floor(index / self.columns)
            column = index % self.columns
            goal_row = math.floor((element - 1) / self.columns)
            goal_column = (element - 1) % self.columns

            # For 0 to go last
            if element == 0:
                goal_row = 2

            if (goal_row - row) != 0:
                total += 1
            if (goal_column - column) != 0:
                total += 1
        return total
