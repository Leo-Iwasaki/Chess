class Player:
    def __init__(self):
        self.__pieces = set()
        
    def get_pieces(self):
        return self.__pieces

    def add_piece(self, coord):
        self.__pieces.add(coord)

    def remove_piece(self, coord):
        self.__pieces.remove(coord)