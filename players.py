
class Player:
    def __init__(self):
        self.__pieces = set()
        self.__rooks = set()
        self.__bishops = set()
        self.__queens = set()
        
    def get_pieces(self):
        return self.__pieces
        
    def get_pinnable_pieces(self):
        return self.__rooks + self.__bishops + self.__queens

    def add_piece(self, coord):
        self.__pieces.add(coord)

    def add_bishop(self, coord):
        self.__bishops.add(coord)

    def add_rook(self, coord):
        self.__rooks.add(coord)

    def add_queen(self, coord):
        self.__queens.add(coord)
        
    def remove_piece(self, coord):
        self.__pieces.remove(coord)

    def remove_bishop(self, coord):
        if coord in self.__bishops:
            self.__bishops.remove(coord)

    def remove_rook(self, coord):
        if coord in self.__rooks:
            self.__rooks.remove(coord)

    def remove_queen(self, coord):
        if coord in self.__queens:
            self.__queens.remove(coord)