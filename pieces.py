from chess import BOARD_WIDTH

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
    
    def valid_moves(self, pieces, checking_pieces, pinning):
        #set self.__next_valid_moves to a list of valid coords to move to.
        return

class Pawn(Piece):
    def __init__(self, colour, coord):
        super().__init__(colour, "p", coord)

class Knight(Piece):
    def __init__(self, colour, coord):
        super().__init__(colour, "n", coord)

class Bishop(Piece):
    def __init__(self, colour, coord):
        super().__init__(colour, "b", coord)

class Rook(Piece):
    def __init__(self, colour, coord):
        super().__init__(colour, "r", coord)

class Queen(Piece):
    def __init__(self, colour, coord):
        super().__init__(colour, "q", coord)
        self.__rook = Rook(colour, coord)
        self.__bishop = Bishop(colour, coord)

class King(Piece):
    def __init__(self, colour, coord):
        super().__init__(colour, "k", coord)
    
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