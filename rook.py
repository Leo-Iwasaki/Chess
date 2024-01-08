from globvar import *
from piece import *
from helper import *

class Rook(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, ROOK, tile)
        
    def visible_tiles(self, board):
        pair = visible_lines(board, self.get_tile(), self.get_colour(), [ROOK_LINE])
        tiles = pair[1]
        self.set_visible_tiles(tiles[0])
        self.set_checking_tiles(tiles[1])
        self.set_pinning_tiles(tiles[2])
        return pair[0]
    
    def valid_tiles(self, board, checking_pieces, pinner, enemy_visible):
        self.set_valid_moves(valid_lines(board, checking_pieces, pinner, self.get_tile(), self.get_colour(), [ROOK_LINE]))