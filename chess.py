class Piece:
    def __init__(self):

class Pawn(piece):
    def __init__(self):
        super().__init__(piece)

    def valid_move(self, start_pos, end_pos, tiles):

class Knight(piece):
    def __init__(self):
        super().__init__(piece)

class Bishop(piece):
    def __init__(self):
        super().__init__(piece)

class Rook(piece):
    def __init__(self):
        super().__init__(piece)

class Queen(piece):
    def __init__(self):
        super().__init__(piece)
        self.__rook = Rook()
        self.__bishop = Bishop()

class King(piece):
    def __init__(self):
        super().__init__(piece)

class Player:
    def __init__(self):
        self.__pieces = []
        self.__rooks = []
        self.__bishops = []
        self.__queens = []

class Board:
    def __init__(self):
        self.__create_pieces()
        self.__white = Player()
        self.__black = Player()
        self.__turns = 1

    def __create_pieces(self):
        self.__tiles = [[],[]]

    def __valid_move(self, start, end):

    def __move(self, start, end):

    def __next_valid_moves(self):

    def __find_check(self):

    def make_move(self, start, end):
        if not self.__valid_move(start, end):
            return False
        self.__move(start, end)
        self.__next_valid_moves()
        self.__turns += 1


