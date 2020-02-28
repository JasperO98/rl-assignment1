from game import HexBoard
import re

if __name__ == '__main__':
    colour = HexBoard.RED
    board = HexBoard(9)
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
            column, row = board.iterarive_deepening()

        board.place((column, row), colour)
        colour = board.get_opposite_color(colour)
        board.print()
        board.render()

        if board.check_win(HexBoard.RED):
            print('Red Won')
            break
        if board.check_win(HexBoard.BLUE):
            print('Blue Won')
            break