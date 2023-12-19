NUM_PLAYERS = 2
WHITE = True
BLACK = False
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

class Piece:
    def __init__(self, colour):
        self.__colour = colour
        self.__next_valid_moves = []

    # def __is_valid_colour(self, colour):
    #     if colour != self.colour:
    #         return False
    #     return True

    # def __is_valid_move(self, end):
    #     if end in __next_valid_moves:
    #         return False
    #     return True

    def valid_move(self, colour, end):
        if colour != self.colour:
            return False
        if end in __next_valid_moves:
            return False
        return True

class Pawn(Piece):
    def __init__(self):
        super().__init__(Piece)

class Knight(Piece):
    def __init__(self):
        super().__init__(Piece)

class Bishop(Piece):
    def __init__(self):
        super().__init__(Piece)

class Rook(Piece):
    def __init__(self):
        super().__init__(Piece)

class Queen(Piece):
    def __init__(self):
        super().__init__(Piece)
        self.__rook = Rook()
        self.__bishop = Bishop()

class King(Piece):
    def __init__(self):
        super().__init__(Piece)

class Player:
    def __init__(self):
        self.__pieces = {}
        self.__rooks = {}
        self.__bishops = {}
        self.__queens = {}

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
        self.__test_pieces()
        self.__white = Player()
        self.__black = Player()
        self.__turns = 1

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

    def __move(self, colour, start, end):
        mine = self.__white if colour else self.__while
        mine.remove(start)
        mine.add
        self.__tiles[start[0]][start[1]] = None
        target = self.__tiles[end[0]][end[1]]
        if target:
            assert self.__tiles.colour != colour
            opponent = self.__black if colour else self.__white
            opponent.remove_piece(end)

    def __next_valid_moves(self):
        return

    def make_move(self, colour, start, end):
        if not self.__tiles(start):
            return False
        if not self.__tiles[start[0]][start[1]].valid_move(self, end):
            return False
        self.__move(colour, start, end)
        self.__next_valid_moves()
        self.__turns += 1
        return True
