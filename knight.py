from globvar import *
from piece import *

class Knight(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, KNIGHT, tile)
        
    def visible_tiles(self, board):
        tile = self.get_tile()
        cur_y = tile[0]
        cur_x = tile[1]
        check = False
        visible_tiles = []
        checking_tiles = []
        for y in range(max(0, cur_y - 2), min(BOARD_HEIGHT - 1, cur_y + 2)):
            for x in range(max(0, cur_x - 2), min(BOARD_WIDTH - 1, cur_x + 2)):
                if abs(y - cur_y) + abs(x - cur_x) == 3:
                    target = board[y][x]
                    if target and target.get_colour() != self.get_colour() and target.get_name() == KING:
                        check = True
                        checking_tiles.append((cur_y, cur_x))
                    visible_tiles.append((y, x))
        
        self.set_visible_tiles(visible_tiles)
        self.set_checking_tiles(checking_tiles)
        return (check, [])

    def valid_tiles(self, board, checking_pieces, pinner, enemy_visible):
        valid_moves = []
        if len(checking_pieces) > 1:
            self.set_valid_moves(valid_moves)
            return
        tile = self.get_tile()
        cur_y = tile[0]
        cur_x = tile[1]
    
        for y in range(max(0, cur_y - 2), min(BOARD_HEIGHT, cur_y + 3)):
            for x in range(max(0, cur_x - 2), min(BOARD_WIDTH, cur_x + 3)):
                if abs(y - cur_y) + abs(x - cur_x) == 3:
                    target = board[y][x]
                    if not (target and target.get_colour() == self.get_colour()):
                        not_check = checking_pieces == [] or (y, x) in checking_pieces[0].get_checking_tiles()
                        not_pin = not pinner or (y,x) in pinner.get_pinning_tiles()
                        if not_check and not_pin:
                            valid_moves.append((y, x))
                        
        self.set_valid_moves(valid_moves)