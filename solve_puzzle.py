import argparse
from Node import Node
from Search import Search
from time import perf_counter


def print_results(title, search, file, start_time, end_time):
    print("\n" + title + ":\n")
    print("Total = " + str(len(search.open_list)+len(search.closed_list)) +
          ", Open list = " + str(len(search.open_list)) +
          ", Closed list = " + str(len(search.closed_list)) +
          ", Path length = " + str(len(search.path)) +
          ", Exec time = " + str(end_time - start_time) + "s \n")
    print(search.trace_to_string())
    with open(file, "w") as file:
        file.write(search.trace_to_string())


# Usage: python3 solve_puzzle.py [-b] [-c columns] [-m max_depth] puzzle
parser = argparse.ArgumentParser(description='Solves puzzles based on the 8 puzzle.')

parser.add_argument('-b', help="Option to include breadth-first search", action='store_true')
parser.add_argument("-c", "--columns", help="amount of columns in the puzzle", type=int, default=4)
parser.add_argument("-m", "--max-depth", help="max depth to stop depth-first-search", type=int, default=None)
parser.add_argument('-i', help="Option to iterate in depth-first search", action='store_true')
parser.add_argument("puzzle", help="Puzzle to solve ex. \"1 0 3 7 5 2 6 4 9 10 11 8\"")

args = parser.parse_args()

if args.i and args.max_depth is None:
    parser.error("--max-depth is required with -i")

try:
    initial_puzzle = list(map(int, args.puzzle.split()))
except ValueError:
    parser.error("Please input a string of numbers as puzzle")

if len(initial_puzzle) % args.columns != 0:
    parser.error("Incompatible puzzle and columns value(" + str(args.columns) + ").")

if len(set(initial_puzzle)) != len(initial_puzzle):
    parser.error("Please do not have any duplicate values in puzzle.")

if args.b:
    start_breadth_first = perf_counter()
    initial_node = Node(initial_puzzle, args.columns, None, "0", 0)
    breadth_first = Search(initial_node)
    breadth_first.search("breadth_first")
    end_breadth_first = perf_counter()

start_depth_first = perf_counter()
initial_node = Node(initial_puzzle, args.columns, None, "0", 0)
depth_first = Search(initial_node)
depth_first.search("depth_first", args.max_depth, args.i)
end_depth_first = perf_counter()

start_best_first_linear = perf_counter()
initial_node = Node(initial_puzzle, args.columns, None, "0", 0, "linear_distance")
best_first_linear = Search(initial_node)
best_first_linear.search("best_first")
end_best_first_linear = perf_counter()

start_best_first_wrong = perf_counter()
initial_node = Node(initial_puzzle, args.columns, None, "0", 0, "wrong_row_column")
best_first_wrong = Search(initial_node)
best_first_wrong.search("best_first")
end_best_first_wrong = perf_counter()

start_a_linear = perf_counter()
initial_node = Node(initial_puzzle, args.columns, None, "0", 0, "linear_distance")
a_linear = Search(initial_node)
a_linear.search("a")
end_a_linear = perf_counter()

start_a_wrong = perf_counter()
initial_node = Node(initial_puzzle, args.columns, None, "0", 0, "wrong_row_column")
a_wrong = Search(initial_node)
a_wrong.search("a")
end_a_wrong = perf_counter()

print("\n----- Solutions -----\n")
if args.b:
    print_results("Breadth First Search", breadth_first, "puzzleBreadth.txt", start_breadth_first, end_breadth_first)
print_results("Depth First Search", depth_first, "puzzleDFS.txt", start_depth_first, end_depth_first)
print_results("Best First Search (Linear Distance)", best_first_linear, "puzzleBFS-h1.txt", start_best_first_linear, end_best_first_linear)
print_results("Best First Search (Wrong Row Column)", best_first_wrong, "puzzleBFS-h2.txt", start_best_first_wrong, end_best_first_wrong)
print_results("A* Search (Linear Distance)", a_linear, "puzzleAs-h1.txt", start_a_linear, end_a_linear)
print_results("A* Search (Wrong Row Column)", a_wrong, "puzzleAs-h2.txt", start_a_wrong, end_a_wrong)


