# !/usr/bin/python
from Sudoku.Generator import *

# setting difficulties and their cutoffs for each solve method
difficulties = {
    'easy': (35, 0), 
    'medium': (81, 7), 
    'hard': (81, 12), 
    'extreme': (81, 17)
}

def create_board(diff = 'hard', base: str="base.txt"):
    # getting desired difficulty from command line
    difficulty = difficulties[diff]

    # constructing generator object from puzzle file (space delimited columns, line delimited rows)
    gen = Generator(base)

    # applying 100 random transformations to puzzle
    gen.randomize(100)

    # getting a copy before slots are removed
    initial = gen.board.copy()

    # applying logical reduction with corresponding difficulty cutoff
    gen.reduce_via_logical(difficulty[0])

    # catching zero case
    if difficulty[1] != 0:
        # applying random reduction with corresponding difficulty cutoff
        gen.reduce_via_random(difficulty[1])


    # getting copy after reductions are completed
    final = gen.board.copy()

    # printing out complete board (solution)
    print("The initial board before removals was: \r\n\r\n{0}".format(initial))

    # printing out board after reduction
    print("The generated board after removals was: \r\n\r\n{0}".format(final))

    return final

if __name__ == "__main__":
    create_board()