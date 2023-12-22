class Piece:
    def __init__(self, colour, name, tile):
        self.__colour = colour
        self.__name = name
        self.__tile = tile
        self.__next_valid_moves = []
        
    def get_name(self):
        return self.__name
    
#functions below should be rewritten for each piece type
    def move(self, colour, end):
        if colour != self.__colour:
            return []
        if end in self.__next_valid_moves:
            #move
            return [] #return a list of moves as tuples (from, to)
        return []
    
    def valid_moves(self, pieces, checking_pieces, pinning):
        #set self.__next_valid_moves to a list of valid tiles to move to.
        return

class Pawn(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, "p", tile)

class Knight(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, "n", tile)

class Bishop(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, "b", tile)

class Rook(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, "r", tile)

class Queen(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, "q", tile)
        self.__rook = Rook(colour, tile)
        self.__bishop = Bishop(colour, tile)

class King(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, "k", tile)