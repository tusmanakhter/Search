import string


class Node:
    def __init__(self, state, parent, move, depth):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.columns = 4

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

    def expand_moves(self):
        for index, value in enumerate(self.state):
            if value == 0:
                empty = index
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
        child = Node(new_state, self, self.letters[switch_position], self.depth + 1)
        self.children.append(child)

    def print_state(self):
        print(self.move + " [" + ', '.join(str(x) for x in self.state) + "]")

    def is_same_state(self, other_state):
        is_same = False
        if self.state == other_state:
            is_same = True
        return is_same
