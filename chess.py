from pieces import *
from players import *

NUM_PLAYERS = 2
WHITE = True
BLACK = False
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

class Board:
    def __init__(self):
        self.__white = Player()
        self.__black = Player()
        self.__turns = 1
        self.__test_pieces()

    def place_piece(self, colour):
        return

    def __test_pieces(self):
        column_end = BOARD_HEIGHT - 1
        row_end = BOARD_WIDTH - 1
        self.__pieces = []
        for y in range(BOARD_HEIGHT):
            row = []
            for x in range(BOARD_WIDTH):
                colour = y + 1 <= BOARD_HEIGHT / 2
                if y == 1 or y == column_end - 1:
                    row.append(Pawn(colour, (y,x)))
                elif y == 0 or y == column_end:
                    if x == 1 or x == row_end - 1:
                        row.append(Knight(colour, (y,x)))
                    elif x == 2 or x == row_end - 2:
                        row.append(Bishop(colour, (y,x)))
                    elif x == 0 or x == row_end:
                        row.append(Rook(colour, (y,x)))
                    elif (y == 0 and x == 3) or (y == column_end and x == row_end - 3):
                        row.append(Queen(colour, (y,x)))
                    else:
                        row.append(King(colour, (y,x)))
                else:
                    row.append(None)
                if row[x]:
                    if colour:
                        self.__white.add_piece((y,x))
                    else:
                        self.__black.add_piece((y,x))
            self.__pieces.append(row)

#-------------------------------------------------------------------------------
#    def __move(self, colour, start, end):
#        mine = self.__white if colour else self.__black
#        mine.remove(start)
#        mine.add
#        piece = self.__pieces[start[0]][start[1]]
#        self.__pieces[start[0]][start[1]] = None
#        target = self.__pieces[end[0]][end[1]]
#        if target:
#            assert self.__tiles.colour != colour
#            opponent = self.__black if colour else self.__white
#            opponent.remove_piece(end)
#            if isinstance(target, Bishop):
#                opponent.remove_bishop(end)
#            elif isinstance(target, Rook):
#                opponent.remove_Rook(end)
#            elif isinstance(target, Queen):
#                opponent.remove_queen(end)
#        self.__pieces[end[0]][end[1]] = piece

    def __potential_check_bishop(self, end, piece):
#        for y in range(BOARD_HEIGHT):
#            x = [y - end[0] + end[1]]
#            if x >= 0:
#                target = self.__pieces[y][y - end]
#                if target and ()
#            if isinstance(self.__pieces[y][x], King):
#                return True
        return False

    def __potential_check_rook(self, end, piece):
        return False

    def __potential_check(self, colour, end):
        return
        
        #piece = self.__pieces[end[0]][end[1]]
        #player = self.__white if colour else self.__black
        #if not piece:
        #    return 
        #if isinstance(piece, Bishop) and self.__potential_check_bishop(self, end, piece):
        #    player.add_bishop(self, end)
        #elif isinstance(piece, Rook) and self.__potential_check_rook(self, end, piece):
        #    add_rook(self, end)
        #elif isinstance(piece, Queen) and (self.__potential_check_bishop(self, end, piece) or self.__potential_check_rook(self, end, piece)):
        #    add_queen(self, end)
        
#-------------------------------------------------------------------------------
    def __get_piece(self, tile):
        return self.__pieces[tile[0]][tile[1]]
        
    def __get_player(self, colour):
        return self.__white if colour else self.__black
    
    def __checking_pieces(self, colour, moves):
        return []
    
    def __pinning_and_pinned(self, colour, moves):
        return []

    def __next_valid_moves(self, colour, checking_pieces, pinning_and_pinned):
        player = self.__get_player(colour)
        for tile in player.get_pieces():
            piece = self.__get_piece(tile)
            pinning = None
            for pair in pinning_and_pinned:
                if pair[1] == tile:
                    pinning = pair[0]
            piece.valid_moves(self.__pieces, checking_pieces, pinning)

    def make_move(self, colour, start, end):
        piece = self.__get_piece(start)
        if not piece:
            return False
        moves = piece.move(colour, end)
        if moves == []:
            return False
        checking_pieces = self.__checking_pieces(colour, moves) #A list of our pieces that are checking the opponent.
        pinning_and_pinned = self.__pinning_and_pinned(colour, moves) #A list of tuples (pinning, pinned).
        self.__next_valid_moves(not colour, checking_pieces, pinning_and_pinned) #Calculates the next valid moves for opponent.
        self.__turns += 1
        return True

    def print_board(self):
        print ("-------------------")
        for y in range(BOARD_HEIGHT):
            row = "|"
            for x in range(BOARD_WIDTH):
                if self.__pieces[y][x]:
                    row = row + " " + self.__pieces[y][x].get_name()
                else:
                    row = row + "  "
            row = row + " |"
            print (row)
        print ("-------------------")

board = Board()
board.print_board()
board.make_move(WHITE, (1,0), (2,0))
board.print_board()