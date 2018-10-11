import sys
from Node import Node
from UninformedSearch import UninformedSearch

if __name__ == "__main__":
    initial_puzzle = list(map(int, sys.argv[1].split()))
    initial = Node(initial_puzzle, None, "0", 0)
    depth_first_search = UninformedSearch(initial)
    depth_first_search.search("breadth_first")
    print("Printing states\n")
    for node in reversed(depth_first_search.path):
        node.print_state()


