NUM_PLAYERS = 2
WHITE = True
BLACK = False
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

class Piece:
    def __init__(self, colour, name):
        self.__colour = colour
        self.__name = name

    def get_name(self):
        return self.__name

class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour, "p")

class Knight(Piece):
    def __init__(self, colour):
        super().__init__(colour, "n")

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__(colour, "b")

class Rook(Piece):
    def __init__(self, colour):
        super().__init__(colour, "r")

class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour, "q")
        self.__rook = Rook(colour)
        self.__bishop = Bishop(colour)

class King(Piece):
    def __init__(self, colour):
        super().__init__(colour, "k")

class Player:
    def __init__(self):
        self.__pieces = set()
        self.__rooks = set()
        self.__bishops = set()
        self.__queens = set()

    def add_piece(self, coord):
        self.__pieces.add(coord)

    def add_rook(self, coord):
        self.__rooks.add(coord)

    def add_bishop(self, coord):
        self.__bishops.add(coord)

    def add_queen(self, coord):
        self.__queens.add(coord)
        
    def remove_piece(self, coord):
        self.__pieces.remove(coord)

    def remove_rook(self, coord):
        self.__rooks.remove(coord)

    def remove_bishop(self, coord):
        self.__bishops.remove(coord)

    def remove_queen(self, coord):
        self.__queens.remove(coord)

class Board:
    def __init__(self):
        self.__white = Player()
        self.__black = Player()
        self.__turns = 1
        self.__test_pieces()

    def place_piece(self, colour):
        return

    def __test_pieces(self):
        column_end = BOARD_HEIGHT - 1
        row_end = BOARD_WIDTH - 1
        self.__pieces = []
        for y in range(BOARD_HEIGHT):
            row = []
            for x in range(BOARD_WIDTH):
                colour = y + 1 <= BOARD_HEIGHT / 2
                if y == 1 or y == column_end - 1:
                    row.append(Pawn(colour))
                elif y == 0 or y == column_end:
                    if x == 0 or x == row_end:
                        row.append(Rook(colour))
                    elif x == 1 or x == row_end - 1:
                        row.append(Knight(colour))
                    elif x == 2 or x == row_end - 2:
                        row.append(Bishop(colour))
                    elif (y == 0 and x == 3) or (y == column_end and x == row_end - 3):
                        row.append(Queen(colour))
                    else:
                        row.append(King(colour))
                else:
                    row.append(None)
                if row[x]:
                    if colour:
                        self.__white.add_piece((y,x))
                    else:
                        self.__black.add_piece((y,x))
            self.__pieces.append(row)

    def __valid_move(self, start, end):
        return

    def __move(self, start, end):
        return

    def __next_valid_moves(self):
        return

    def __find_check(self):
        return

    def make_move(self, start, end):
        if not self.__valid_move(start, end):
            return False
        self.__move(start, end)
        self.__next_valid_moves()
        self.__turns += 1
        return True

    def print_board(self):
        print ("-------------------")
        for y in range(BOARD_HEIGHT):
            row = "|"
            for x in range(BOARD_WIDTH):
                if self.__pieces[y][x]:
                    row = row + " " + self.__pieces[y][x].get_name()
                else:
                    row = row + "  "
            row = row + " |"
            print (row)
        print ("-------------------")

board = Board()
board.print_board()

