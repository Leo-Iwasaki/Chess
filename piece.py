from globvar import *

class Piece:
    def __init__(self, colour, name, tile):
        self.__colour = colour
        self.__name = name
        self.__tile = tile
        self.__next_valid_moves = []
        self.__visible_tiles = []
        self.__checking_tiles = []
        self.__pinning_tiles = []

    def get_colour(self):
        return self.__colour

    def get_name(self):
        return self.__name

    def get_tile(self):
        return self.__tile

    def set_tile(self, tile):
        self.__tile = tile    
        
    def get_valid_moves(self):
        return self.__next_valid_moves

    def set_valid_moves(self, moves):
        self.__next_valid_moves = moves
         
    def get_visible_tiles(self):
        return self.__visible_tiles

    def set_visible_tiles(self, tiles):
        self.__visible_tiles = tiles
         
    def get_checking_tiles(self):
        return self.__checking_tiles

    def set_checking_tiles(self, tiles):
        self.__checking_tiles = tiles
    
    def get_pinning_tiles(self):
        return self.__pinning_tiles

    def set_pinning_tiles(self, tiles):
        self.__pinning_tiles = tiles
    
    def get_moves(self, end):
        ret = []
        if end in self.__next_valid_moves:
            ret.append((self.__tile, end))
        return ret