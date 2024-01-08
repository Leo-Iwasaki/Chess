from globvar import *
from piece import *
        
class King(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, KING, tile)

    def get_moves(self, colour, end):
        ret = []
        if colour == self.__colour and end in self.__next_valid_moves:
            ret.append((self.__coord, end))
            if end[1] == self.__coord[1] - 2:
                ret.append(((end[0], 0), (end[0], end[1] + 1)))
            elif end[1] == self.__coord[1] + 2:
                ret.append(((end[0], BOARD_WIDTH - 1), (end[0], end[1] - 1)))
        return ret
    
    def visible_tiles(self, board):
        tile = self.get_tile()
        cur_y = tile[0]
        cur_x = tile[1]
        visible_tiles = []
        checking_tiles = []
        for y in range(max(0, cur_y - 1), min(BOARD_HEIGHT - 1, cur_y + 1)):
            for x in range(max(0, cur_x - 1), min(BOARD_WIDTH - 1, cur_x + 1)):
                if y != cur_y or x != cur_x:
                    visible_tiles.append((y,x))
        
        self.set_visible_tiles(visible_tiles)
        self.set_checking_tiles(checking_tiles)
        return (False, [])
    
    def valid_tiles(self, board, checking_pieces, pinner, enemy_visible):
        valid_moves = []
        tile = self.get_tile()
        cur_y = tile[0]
        cur_x = tile[1]
        
        for y in range(max(0, cur_y - 1), min(BOARD_HEIGHT - 1, cur_y + 1)):
            for x in range(max(0, cur_x - 1), min(BOARD_WIDTH - 1, cur_x + 1)):
                if y != cur_y or x != cur_x:
                    if (y, x) not in enemy_visible:
                        valid_moves.append((y, x))
                        
        self.set_valid_moves(valid_moves)