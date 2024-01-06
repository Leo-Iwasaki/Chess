from chess import BOARD_WIDTH

PAWN = "p"
KNIGHT = "k"
BISHOP = "b"
ROOK = "r"
QUEEN = "q"
KING = "k"

class Piece:
    def __init__(self, colour, name, coord):
        self.__colour = colour
        self.__name = name
        self.__coord = coord
        self.__next_valid_moves = []

    def get_colour(self):
        return self.__colour

    def get_name(self):
        return self.__name
    
    # Return a list of moves as tuples (from, to)
    def move(self, colour, end):
        ret = []
        if colour == self.__colour and end in self.__next_valid_moves:
            ret.append((self.__coord, end))
        return ret

    def set_coord(self, coord):
        self.__coord = coord
        if colour != self.__colour:
            return []
        if end in self.__next_valid_moves:
            return [] #return a list of moves as tuples (from, to)
        return []
    
    def valid_moves(self, pieces, checking_pieces, pinning):
        #set self.__next_valid_moves to a list of valid coords to move to.
        return
    
    def get_valid_moves(self):
        return self.__next_valid_moves

class Pawn(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, PAWN, tile)

class Knight(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, KNIGHT, tile)

class Bishop(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, BISHOP, tile)

class Rook(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, ROOK, tile)

class Queen(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, QUEEN, tile)
        self.__rook = Rook(colour, tile)
        self.__bishop = Bishop(colour, tile)

class King(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, KING, tile)

    # Return a list of moves as tuples (from, to)
    # Override for castle
    def move(self, colour, end):
        ret = []
        if colour == self.__colour and end in self.__next_valid_moves:
            ret.append((self.__coord, end))
            if end[1] == self.__coord[1] - 2:
                ret.append(((end[0], 0), (end[0], end[1] + 1)))
            elif end[1] == self.__coord[1] + 2:
                ret.append(((end[0], BOARD_WIDTH - 1), (end[0], end[1] - 1)))
        return ret
