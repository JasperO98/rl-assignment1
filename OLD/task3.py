from game import HexBoard
import re
import numpy as np

if __name__ == '__main__':
    colour = HexBoard.RED
    board = HexBoard(3)
    print('Red Starts')
    board.print()
    board.render()

    while True:
        if colour == HexBoard.BLUE:
            match = re.match(r'^([0-9]+)([a-z])$', input('Coordinates: ').lower())

            if not match:
                print('Invalid Move')
                continue

            row = int(match.groups()[0])
            column = ord(match.groups()[1]) - ord('a')

            if not board.exists((column, row)) or not board.is_empty((column, row)):
                print('Invalid Move')
                continue
        else:
            column, row = board.alphabeta(0, -np.inf, np.inf, {}, 3, {})

        board.place((column, row), colour)
        colour = board.get_opposite_color(colour)
        board.print()
        board.render()

        if board.check_win(HexBoard.RED):
            print('Red Won')
            print(board.update_rating("dijk_3", "user"))
            print(board.get_leadboard())
            break
        if board.check_win(HexBoard.BLUE):
            print('Blue Won')
            print(board.update_rating("user", "dijk_3"))
            print(board.get_leadboard())
            break