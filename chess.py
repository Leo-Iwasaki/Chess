from pieces import *
from players import *

import copy

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

    # Place pieces
    def place_piece(self, colour):
        return

    # Normal chess placing
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
                        self.__white.add_piece(row[x])
                    else:
                        self.__black.add_piece(row[x])
            self.__pieces.append(row)

#-------------------------------------------------------------------------------
#    def __potential_check_bishop(self, end, piece):
#        for y in range(BOARD_HEIGHT):
#            x = [y - end[0] + end[1]]
#            if x >= 0:
#                target = self.__pieces[y][y - end]
#                if target and ()
#            if isinstance(self.__pieces[y][x], King):
#                return True
#         return False

#     def __potential_check_rook(self, end, piece):
#         return False

#     def __potential_check(self, colour, end):
#         piece = self.__pieces[end[0]][end[1]]
#         player = self.__white if colour else self.__black
#         if not piece:
#             return 
#         if isinstance(piece, Bishop) and self.__potential_check_bishop(self, end, piece):
#             player.add_bishop(self, end)
#         elif isinstance(piece, Rook) and self.__potential_check_rook(self, end, piece):
#             add_rook(self, end)
#         elif isinstance(piece, Queen) and (self.__potential_check_bishop(self, end, piece) or self.__potential_check_rook(self, end, piece)):
#             add_queen(self, end)

#-------------------------------------------------------------------------------
    def __get_piece(self, tile, pieces):
        return pieces[tile[0]][tile[1]]
    
    def __set_tile(self, tile, pieces, piece):
        pieces[tile[0]][tile[1]] = piece
        return pieces
        
    def __get_player(self, colour):
        return self.__white if colour else self.__black
    
    def __move(self, colour, moves):
       for pair in moves:
           piece = self.__get_piece(pair[0])
           assert colour == piece.get_colour()
           self.__pieces[pair[0][0]][pair[0][1]] = None
           target = self.__get_piece(pair[1])
           self.__pieces[pair[1][0]][pair[1][1]] = piece
           piece.set_coord(pair[1])
           self.__get_player(colour).remove_piece(pair[0])
           self.__get_player(colour).add_piece(pair[1])
           if target:
                assert colour != target.get_colour()
                self.__get_player(not colour).remove_piece(pair[1])

    # A list of our pieces that are checking the opponent.
    def __checking_pieces(self, colour):
        return []

    # A list of tuples (pinning, pinned).
    def __pinning_and_pinned(self, colour):
        return []

    def __checking_pieces(self, colour):
        pieces = self.__pieces
        checking_pieces = []
        for tile in self.__get_player(colour).get_pinnable_pieces():
            piece = self.__get_piece(tile, pieces)
            for target_tile in piece.get_valid_moves():
                target_piece = self.__get_piece(target_tile, pieces)
                if target_piece and target_piece.get_name() == KING:
                    checking_pieces.append(piece)
        return checking_pieces
    
    def __pinning_and_pinned(self, colour):
        checking_pieces = []
        for tile in self.__get_player(colour).get_pinnable_pieces():
            pieces = self.__pieces.copy()
            piece = self.__get_piece(tile, pieces)
            for target_tile in piece.get_valid_moves():
                target_piece = self.__get_piece(target_tile, pieces)
                if target_piece and target_piece.get_name() != KING:  
                    pieces = self.__set_tile(tile, pieces, None)
                    
            piece_clone = copy.deepcopy(piece)
            piece_clone.valid_moves(pieces, [], [])
            for target_tile in piece_clone.get_valid_moves():
                target_piece = self.__get_piece(target_tile, pieces)
                if target_piece and target_piece.get_name() == KING:
                    checking_pieces.append(piece)
        return checking_pieces

    # Calculates the next valid moves for opponent.
    def __next_valid_moves(self, colour, checking_pieces, pinning_and_pinned):
        player = self.__get_player(colour)
        for piece in player.get_pieces():
            pinning = None
            for pair in pinning_and_pinned:
                if pair[1] == piece:
                    pinning = pair[0]
                    break
            piece.valid_moves(self.__pieces, checking_pieces, pinning)

# [ make_move ]
# get piece at start
#   if no piece, return False
# piece.move
#   if the piece is opponent's, return [] (return False)
#   if end is not a valid move, return [] (return False)
#   else, return moves as a list
# self.__move
#   replace each piece in Board.__pieces
#   change Piece.__tile of each piece
#   replace coords in Player.__pieces
# self.__checking_pieces
#   return all the pieces that are checking (piece that just moved, bishop, rook or queen)
# self.__pinning_and_pinned
#   return all the pieces that can check if one opponent piece moves
# self.__next_valid_moves
#   update next valid moves of the opponent

    def make_move(self, colour, start, end):
        piece = self.__get_piece(start, self.__pieces)
        if not piece:
            return False
        moves = piece.move(colour, end)
        if moves == []:
            return False
        self.__move(colour, moves)
        checking_pieces = self.__checking_pieces(colour)
        pinning_and_pinned = self.__pinning_and_pinned(colour)
        self.__next_valid_moves(not colour, checking_pieces, pinning_and_pinned)
        self.__turns += 1
        return True

    def print_board(self):
        print ("-" * (BOARD_WIDTH * 4 + 1))
        for y in range(BOARD_HEIGHT):
            row = "|"
            for x in range(BOARD_WIDTH):
                if self.__pieces[y][x]:
                    row = row  + " " + self.__pieces[y][x].get_name() + " |"
                else:
                    row = row + "   |"
            print (row)
            print ("-" * (BOARD_WIDTH * 4 + 1))
        print("Turn " + str(self.__turns), "\n")

board = Board()
board.print_board()
board.make_move(WHITE, (1,0), (2,0))
board.print_board()