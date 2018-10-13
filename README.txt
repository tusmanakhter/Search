Instructions

Usage: python3 solve_puzzle.py [-b] [-c columns] [-m max_depth] puzzle

To run this program specify the python3 interpreter and the solve_puzzle.py script name with arguments. The program
expects a string of integers, with no duplicates, as the puzzle.

Example:

python3 solve_puzzle.py "1 0 3 7 5 2 6 4 9 10 11 8"

The program will output the current depth and values of the state it is searching.

For depth first search, if the program is taking too long for a solution and you can see this, there is an option
to specify the max amount of depth to search. The program will then start an iterative deepening depth first search
instead of a vanilla depth first search. It will double the max depth after every iteration. This is specified with
the option "-m", Here is an example:

python3 solve_puzzle.py "1 0 3 7 5 2 6 4 9 10 11 8" -m 5

If you want to include breadth-first search in the program, specify the option -b. Example:

python3 solve_puzzle.py "1 0 3 7 5 2 6 4 9 10 11 8" -b

Also this program is meant to be able to run with a dynamic puzzle size, however a suitable column size must be
specified. This can be done with the option "-c". The default is 4 and expects a puzzle size to be a multiple of 4.
Here is an example to specify a different column size:

python3 solve_puzzle.py "1 0 3 7 5 2 6 4 9 10 11 8" -c 3