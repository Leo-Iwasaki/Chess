from globvar import *
                        
def visible_lines(board, tile, colour, lines):
    cur_y = tile[0]
    cur_x = tile[1]
    check = False
    pinned = []
    visible_tiles = []
    checking_tiles = []
    pinning_tiles = []
    
    for y in range(-1, 2): # [-1, 0, 1]
        for x in range(-1, 2):
            if abs(y) + abs(x) in lines:
                next_y = cur_y
                next_x = cur_x
                our_piece = False
                stop_search = False
                last_enemy = None
                check_in_line = False
                checking_line = [(next_y, next_x)]
                pinning_line = [(next_y, next_x)]
                while not (stop_search):
                    if next_y != cur_y or next_x != cur_x:
                        if not last_enemy:
                            visible_tiles.append((next_y, next_x))
                        if target:
                            if target.get_name() == KING:
                                check_in_line = True
                                if last_enemy:
                                    pinned.append((tile, last_enemy))
                                    pinning_tiles += pinning_line
                                    
                                else:
                                    check = True
                                    checking_tiles += checking_line
                            else:
                                last_enemy = target
                    checking_line.append((next_y, next_x))
                    pinning_line.append((next_y, next_x))
                    
                    next_y += y
                    next_x += x
                    in_y_bound = next_y >= 0 and next_y < BOARD_HEIGHT
                    in_x_bound = next_x >= 0 and next_x < BOARD_WIDTH
                    stop_search = True
                    if in_y_bound and in_x_bound:
                        target = board[next_y][next_x]
                        our_piece = target != None and target.get_colour() == colour
                        searched_pin = target != None and last_enemy != None
                        stop_search = our_piece or searched_pin or check_in_line
                        if stop_search and our_piece:
                            visible_tiles.append((next_y, next_x))
                    
    return ((check, pinned), [visible_tiles, checking_tiles, pinning_tiles])

def valid_lines(board, checking_pieces, pinner, tile, colour, lines): #this broken
        valid_moves = []
        if len(checking_pieces) > 1:
            return valid_moves
        cur_y = tile[0]
        cur_x = tile[1]
        
        for y in range(-1, 2):
            for x in range(-1, 2):
                if (abs(y) + abs(x)) in lines:
                    next_y = cur_y
                    next_x = cur_x
                    our_piece = False
                    stop_search = False
                    
                    while not (stop_search):
                        if next_y != cur_y or next_x != cur_x:
                            not_check = checking_pieces == [] or (next_y, next_x) in checking_pieces[0].get_checking_tiles()
                            not_pin = not pinner or (next_y, next_x) in pinner.get_pinning_tiles()
                            if not_check and not_pin:
                                valid_moves.append((next_y, next_x))

                        next_y += y
                        next_x += x
                        in_y_bound = next_y >= 0 and next_y < BOARD_HEIGHT
                        in_x_bound = next_x >= 0 and next_x < BOARD_WIDTH
                        stop_search = True
                        if in_y_bound and in_x_bound:
                            target = board[next_y][next_x]
                            stop_search = target != None
                            if stop_search:
                                if target.get_colour() != colour:
                                    not_check = checking_pieces == [] or (next_y, next_x) in checking_pieces[0].get_checking_tiles()
                                    not_pin = not pinner or (next_y, next_x) in pinner.get_pinning_tiles()
                                    if not_check and not_pin:
                                        valid_moves.append((next_y, next_x))
                        
        return valid_moves