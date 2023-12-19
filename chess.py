class Piece:
    def __init__(self):
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

class Pawn(piece):
    def __init__(self):
        super().__init__(piece)

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

    def make_move(self, colour, start, end):
        if not self.__tiles(start):
            return False
        if not self.__tiles[start[0]][start[1]].valid_move(self, end):
            return False
        self.__move(colour, start, end)
        self.__next_valid_moves()
        self.__turns += 1
