import argparse
from Node import Node
from Search import Search


def print_results(title, search, file):
    print("\n" + title + ":\n")
    print("Nodes expanded = " + str(0) +
          ", Open list = " + str(len(search.open_list)) +
          ", Closed list = " + str(len(search.closed_list)) + "\n")
    print(search.trace_to_string())
    with open(file, "w") as file:
        file.write(search.trace_to_string())


# Usage: python3 solve_puzzle.py [-c columns] [-m max_depth] puzzle
parser = argparse.ArgumentParser(description='Solves puzzles based on the 8 puzzle.')

parser.add_argument("-c", "--columns", help="amount of columns in the puzzle", type=int, default=4)
parser.add_argument("-m", "--max-depth", help="max depth to stop depth-first-search", type=int, default=100)
parser.add_argument("puzzle", help="Puzzle to solve ex. \"1 0 3 7 5 2 6 4 9 10 11 8\"")

args = parser.parse_args()
initial_puzzle = list(map(int, args.puzzle.split()))

if len(initial_puzzle) % args.columns != 0:
    print("Incompatible puzzle and column value(" + str(args.columns) + ").")
    exit(1)

if len(set(initial_puzzle)) != len(initial_puzzle):
    print("Please do not have any duplicate values in puzzle.")
    exit(1)

initial_node = Node(initial_puzzle, args.columns, None, "0", 0)
breadth_first = Search(initial_node)
breadth_first.search("breadth_first")

initial_node = Node(initial_puzzle, args.columns, None, "0", 0)
depth_first = Search(initial_node)
depth_first.search("depth_first", args.max_depth)

initial_node = Node(initial_puzzle, args.columns, None, "0", 0, "linear_distance")
best_first_linear = Search(initial_node)
best_first_linear.search("best_first")

initial_node = Node(initial_puzzle, args.columns, None, "0", 0, "wrong_row_column")
best_first_wrong = Search(initial_node)
best_first_wrong.search("best_first")

initial_node = Node(initial_puzzle, args.columns, None, "0", 0, "linear_distance")
a_linear = Search(initial_node)
a_linear.search("a")

initial_node = Node(initial_puzzle, args.columns, None, "0", 0, "wrong_row_column")
a_wrong = Search(initial_node)
a_wrong.search("a")

print("\n----- Solutions -----\n")
print_results("Breadth First Search", breadth_first, "puzzleBreadth.txt")
print_results("Depth First Search", depth_first, "puzzleDFS.txt")
print_results("Best First Search (Linear Distance)", best_first_linear, "puzzleBFS-h1.txt")
print_results("Best First Search (Wrong Row Column)", best_first_wrong, "puzzleBFS-h2.txt")
print_results("A* Search (Linear Distance)", a_linear, "puzzleAs-h1.txt")
print_results("A* Search (Wrong Row Column)", a_wrong, "puzzleAs-h2.txt")


