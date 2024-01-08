from globvar import *
from players import *

from pawn import *
from knight import *
from bishop import *
from rook import *
from queen import *
from king import *

class Board:
    def __init__(self):
        self.__white = Player()
        self.__black = Player()
        self.__turns = 1
        self.__test_pieces()
        self.__next_valid_moves(BLACK)
        
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
                    elif (y == 0 and x == 3) or (y == column_end and x == 3):
                        row.append(Queen(colour, (y,x)))
                    else:
                        row.append(King(colour, (y,x)))
                else:
                    row.append(None)
                if row[x]:
                    if colour:
                        self.__white.add_piece((y, x))
                    else:
                        self.__black.add_piece((y, x))
            self.__pieces.append(row)

    def __get_piece(self, tile):
        return self.__pieces[tile[0]][tile[1]]
    
    def __set_tile(self, tile, piece):
        self.__pieces[tile[0]][tile[1]] = piece
        
    def __get_player(self, colour):
        return self.__white if colour else self.__black
    
    def __move(self, colour, moves):
        cur_player = self.__get_player(colour)
        next_player = self.__get_player(not colour)
        for pair in moves:
            move_from = pair[0]
            move_to = pair[1]
            piece = self.__get_piece(move_from)
            target = self.__get_piece(move_to)
            self.__set_tile(move_from, None)
            self.__set_tile(move_to, piece)
            piece.set_tile(move_to)
            cur_player.remove_piece(move_from)
            cur_player.add_piece(move_to)
            if target:
                next_player.remove_piece(move_to)
            
    def __next_valid_moves(self, colour):
        cur_player = self.__get_player(colour)
        checking_pieces = []
        pinned_pieces = []
        for tile in cur_player.get_pieces():
            piece = self.__get_piece(tile)
            tuple = piece.visible_tiles(self.__pieces)
            if tuple[0]:
                checking_pieces.append(piece)
            pinned_pieces += tuple[1]
            piece.set_valid_moves([])
            
        next_player = self.__get_player(not colour)
        for tile in next_player.get_pieces():
            piece = self.__get_piece(tile)
            pinner = None
            for tuple in pinned_pieces:
                if tuple[1] == piece:
                    pinner = self.__get_piece(tuple[0])
            piece.valid_tiles(self.__pieces, checking_pieces, pinner, cur_player.get_pieces())

    def make_move(self, start, end):
        piece = self.__get_piece(start)
        if not piece:
            return False
        moves = piece.get_moves(end)
        if moves == []:
            print("invalid move\n")
            return False
        colour = piece.get_colour()
        self.__move(colour, moves)
        self.__next_valid_moves(colour)
        self.__turns += 1
        
        board.print_board()
        return True

    def print_board(self):
        print("\nTurn " + str(self.__turns - 1))
        print (("+" + ("-" * 3)) * BOARD_WIDTH + "+")
        for y in range(BOARD_HEIGHT):
            row = "|"
            for x in range(BOARD_WIDTH):
                if self.__pieces[BOARD_HEIGHT - y - 1][x]:
                    row = row  + " " + self.__pieces[BOARD_HEIGHT - y - 1][x].get_name() + " |"
                else:
                    row = row + "   |"
            print (row)
            print (("+" + ("-" * 3)) * BOARD_WIDTH + "+")
        

board = Board()

board.make_move((1,3), (3,3)) #  d4
board.make_move((6,4), (5,4)) #  e6

board.make_move((1,2), (3,2)) #  c4
board.make_move((6,5), (4,5)) #  f5

board.make_move((0,1), (2,2)) #  Nc3
board.make_move((7,6), (5,5)) #  Nf6

board.make_move((0,6), (2,5)) #  Nf3
board.make_move((6,1), (5,1)) #  b6

board.make_move((1,4), (2,4)) #  e3
board.make_move((7,2), (6,1)) #  Bb7

board.make_move((0,5), (2,3)) #  Bd3
board.make_move((7,5), (3,1)) #  Bb4