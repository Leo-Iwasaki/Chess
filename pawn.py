from globvar import *
from piece import *

class Pawn(Piece):
    def __init__(self, colour, tile):
        super().__init__(colour, PAWN, tile)
        
    def visible_tiles(self, board):
        tile = self.get_tile()
        cur_y = tile[0]
        cur_x = tile[1]
        y_dif = 1
        if not self.get_colour():
            y_dif = -y_dif
        x_difs = [-1, 1]
        visible_tiles = []
        checking_tiles = []
        check = False
        
        for x_dif in x_difs:
            next_y = cur_y + y_dif
            next_x = cur_x + x_dif
            in_y_bound = next_y >= 0 and next_y < BOARD_HEIGHT
            in_x_bound = next_x >= 0 and next_x < BOARD_WIDTH
            
            if in_y_bound and in_x_bound:
                target = board[next_y][next_x]
                if target and target.get_colour() != self.get_colour() and target.get_name() == KING:
                    check = True
                    checking_tiles.append((cur_y, cur_x))
                visible_tiles.append((next_y, next_x))
                
        self.set_visible_tiles(visible_tiles)
        self.set_checking_tiles(checking_tiles)
        return (check, [])
    
    def valid_tiles(self, board, checking_pieces, pinner, enemy_visible): #need to do enpassent (input last move)
        valid_moves = []
        if len(checking_pieces) > 1:
            self.set_valid_moves(valid_moves)
            return
        tile = self.get_tile()
        colour = self.get_colour()
        y_dif = 1
        if not colour:
            y_dif = -y_dif
        cur_y = tile[0]
        cur_x = tile[1]
        next_y = cur_y + y_dif
        next_x = cur_x
        
        target = board[next_y][next_x]
        if not target:
            not_check = checking_pieces == [] or (next_y, next_x) in checking_pieces[0].get_checking_tiles()
            not_pin = not pinner or (next_y, next_x) in pinner.get_pinning_tiles()
            if not_check and not_pin:
                valid_moves.append((next_y, next_x))
            if (colour and cur_y == 1) or ((not colour) and cur_y == BOARD_HEIGHT - 2):
                next_y += y_dif
                target = board[next_y][next_x]
                if not target:
                    not_check = checking_pieces == [] or (next_y, next_x) in checking_pieces[0].get_checking_tiles()
                    not_pin = not pinner or (next_y, next_x) in pinner.get_pinning_tiles()
                    if not_check and not_pin:
                        valid_moves.append((next_y, next_x))
                        
        next_y = cur_y + y_dif
        x_difs = [-1, 1]
        for x_dif in x_difs:
            next_x = cur_x + x_dif
            in_x_bound = next_x >= 0 and next_x < BOARD_WIDTH
            if in_x_bound:
                target = board[next_y][next_x]
                if target and target.get_colour != colour:
                    not_check = checking_pieces == [] or (next_y, next_x) in checking_pieces[0].get_checking_tiles()
                    not_pin = not pinner or (next_y, next_x) in pinner.get_pinning_tiles()
                    if not_check and not_pin:
                        valid_moves.append((next_y, next_x))
                        
        self.set_valid_moves(valid_moves)