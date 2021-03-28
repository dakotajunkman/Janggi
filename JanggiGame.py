from Board import Board
from Soldier import Soldier
from Cannon import Cannon          
from Chariot import Chariot
from Elephant import Elephant
from Horse import Horse
from Guard import Guard
from General import General
          
class JanggiGame:
    """
    Represents the actual game. Game state is updated and moves are made using the piece and board
    objects. Keeps track of whose turn it is to move, the state of the game, and whether or not a player is 
    in check. Instantiates a board and all pieces. Keeps track of current available pieces for each player. 
    """
    def __init__(self):
        """
        Initializes the board and pieces and places pieces on the board. Sets up the current state of
        the game and whose turn it is to move.
        """
        self._board = Board()
        self._pieces = {Chariot('red', 'rR1', 'chariot', (0, 0)), Elephant('red', 'rE1', 'elephant', (0, 1)),
        Horse('red', 'rH1', 'horse', (0, 2)), Guard('red', 'rA1', 'guard', (0, 3)), Guard('red', 'rA2', 'guard', (0, 5)),
        Elephant('red', 'rE2', 'elephant', (0, 6)), Horse('red', 'rH2', 'horse', (0, 7)), Chariot('red', 'rR2', 'chariot', (0, 8)),
        Cannon('red', 'rC1', 'cannon', (2, 1)), Cannon('red', 'rC2', 'cannon', (2, 7)), Soldier('red', 'rS1', 'soldier', (3, 0)),
        Soldier('red', 'rS2', 'soldier', (3, 2)), Soldier('red', 'rS3', 'soldier', (3, 4)),
        Soldier('red', 'rS4', 'soldier', (3, 6)), Soldier('red', 'rS5', 'soldier', (3, 8)),
        Soldier('blue', 'bS1', 'soldier', (6, 0)), Soldier('blue', 'bS2', 'soldier', (6, 2)), 
        Soldier('blue', 'bS3', 'soldier', (6, 4)), Soldier('blue', 'bS4', 'soldier', (6, 6)),
        Soldier('blue', 'bS5', 'soldier', (6, 8)), Cannon('blue', 'bC1', 'cannon', (7, 1)),
        Cannon('blue', 'bC2', 'cannon', (7, 7)), Chariot('blue', 'bR1', 'chariot', (9, 0)),
        Elephant('blue', 'bE1', 'elephant', (9, 1)), Horse('blue', 'bH1', 'horse', (9, 2)), 
        Guard('blue', 'bA1', 'guard', (9, 3)), Guard('blue', 'bA2', 'guard', (9, 5)),
        Elephant('blue', 'bE2', 'elephant', (9, 6)), Horse('blue', 'bH2', 'horse', (9, 7)), Chariot('blue', 'bR2', 'chariot', (9, 8)),
        General('blue', 'bG1', 'general', (8, 4)), General('red', 'rG1', 'general', (1, 4))}

        self._red_in_check = False
        self._blue_in_check = False
        self._player_swap = {'blue': 'red', 'red': 'blue'}
        self._player_turn = 'blue'
        self._game_state = 'UNFINISHED'

        for piece in self._pieces:
            self._board.set_piece(piece)

        # set initial valid moves
        self.update_valid_moves()
    
    def get_game_state(self) -> str:
        """
        Returns the current state of the game.
        """
        return self._game_state
    
    def get_board(self):
        """
        Returns the board object. Used for game loop.
        """
        return self._board

    def get_player_turn(self):
        """
        Returns whose turn it is to move. Used for game loop.
        """
        return self._player_turn

    def update_valid_moves(self) -> None:
        """
        Updates the valid moves for each piece on the board.
        return: None
        """
        for piece in self._pieces:
            piece.set_valid_moves(self._board)
    
    def is_in_check(self, color: str) -> bool:
        """
        Returns whether the given color general is in check.
        param color: color of the general to check
        return: True if general is in check, else False
        """
        if color == 'blue':
            return self._blue_in_check
        else:
            return self._red_in_check
    
    def alternate_turn(self) -> None:
        """
        Updates whose turn it is to move.
        return: None
        """
        self._player_turn = self._player_swap[self._player_turn]

    def is_valid_move(self, move_from: str, move_to: str):
        """
        Checks that the spaces fed to make_move are on the board, the game state allows for a move, and
        the correct player is moving. Also checks that the space has a piece to move.
        param move_from: space of the piece to move
        param move_to: space to move the piece to
        return: False if move is invalid, otherwise returns a tuple of the piece, current coordinate, and
        destination coordinate
        """
        # check that spaces are on the board
        if self._board.convert_coords(move_from) is None or self._board.convert_coords(move_to) is None:
            return False
        
        piece_loc = self._board.convert_coords(move_from)
        piece = self._board.get_piece(piece_loc)

        if self._board.get_piece(piece_loc) is None:
            return False

        # check that piece belongs to moving player and game is not over
        if piece.get_color() != self._player_turn or self._game_state != 'UNFINISHED':
            return False
        
        # send back necessary data to continue when move is valid
        return piece, piece_loc, self._board.convert_coords(move_to)
        
    def make_move(self, move_from: str, move_to: str) -> bool:
        """
        Handles basic piece movements in the game. Calls is_valid_move to check move validity and moves the piece
        and updates the board and game state when it is. After the move, it calls is_self_check to check if the move
        resulted in check for the moving player. It will then check if the move created check for the opposing player.
        When check is detected, it will check for a checkmate scenario and update the game status accordingly.
        Upon a valid move with no game state updates, the player turn will be swapped using alternate_turn.
        param move_from: space of the piece to move
        param move_to: space to move the piece to
        return: True when move is valid, otherwise False
        """
        # allow player to pass a turn when not in check
        if move_from == move_to and not self.is_in_check(self._player_turn):
            self.alternate_turn()
            return True
        
        # do not allow a pass when the player is in check
        if move_from == move_to and self.is_in_check(self._player_turn):
            return False

        # check that the spaces are valid and piece belongs to the correct player
        valid_move = self.is_valid_move(move_from, move_to)
        if not valid_move:
            return False
        
        # unpack tuple to get the piece, current coordinate, and destination coordinate
        piece = valid_move[0]
        cur_coord = valid_move[1]
        dest_coord = valid_move[2]

        # check that move is valid for the piece
        if dest_coord not in piece.get_valid_moves():
            return False        

        # save current board and piece state to revert when needed
        revert_pieces = self._pieces.copy()
        revert_board = self._board.get_board().copy()

        # remove captured piece from piece set when necessary
        capture_piece = self._board.get_piece(dest_coord)
        if capture_piece is not None:
            self._pieces.remove(capture_piece)
        
        # update board state and piece location
        piece.set_location(dest_coord)
        self._board.remove_piece(cur_coord)
        self._board.set_piece(piece)

        # ensure that self-check has not been created
        self.update_valid_moves()
        if self.is_check(self._player_turn):

            # when self-check occurs, revert board and pieces back to previous state
            # set piece location back to previous
            # re-calculate valid moves
            self._pieces = revert_pieces
            self._board.set_board(revert_board)
            piece.set_location(cur_coord)
            self.update_valid_moves()
            return False

        # detect if opponent has been placed in check
        if self.is_check(self._player_swap[self._player_turn]):
            if self._player_swap[self._player_turn] == 'blue':
                self._blue_in_check = True
            else:
                self._red_in_check = True
            
            if self.is_mate(self._player_swap[self._player_turn]):
                self._game_state = self._player_turn.upper() + '_WON'
                return True
        
        # once a player completes a valid move they are guaranteed to not be in check
        if self._player_turn == 'blue':
            self._blue_in_check = False
        else:
            self._red_in_check = False

        # update player turn and finish method
        self.alternate_turn()
        return True

    def is_check(self, color: str) -> bool:
        """
        Checks whether the most recent move of the player has created a check.
        Locates the player's general and checks if it's location is a valid move for the opposing player.
        This will serve dual-purpose, checking for self-check and opponent check based on the color passed. 
        param color: color of the player to check
        param board: current state of the board
        return: True if self-check created, otherwise False.
        """
        # locate the general and get its location coordinate
        for piece in self._pieces:
            if piece.get_type() == 'general' and piece.get_color() == color:
                general = piece
                break
        
        coord = general.get_location()

        # check if the general's location is a valid move for opposing players
        for piece in self._pieces:
            if piece.get_color() == self._player_swap[color] and coord in piece.get_valid_moves():
                return True
        return False

    def is_mate(self, color: str) -> bool:
        """
        Determines if a checkmate scenario has been created. Will only run if check was created on previous turn.
        Runs through the color's valid moves and determines if any will eliminate the check scenario.
        param color: color of player to check
        return: True if checkmate, else False
        """
        # iterate over player pieces and examine all moves to see if check can be eliminated
        for piece in self._pieces:
            if piece.get_color() == color:
                moves = piece.get_valid_moves().copy()

                # iterate over the piece's moves
                for move in moves:
                    revert_board = self._board.get_board().copy()
                    revert_pieces = self._pieces.copy()
                    old_coord = piece.get_location()

                    # make the move and see if it removed check
                    capture_piece = self._board.get_piece(move)
                    if capture_piece is not None:
                        self._pieces.remove(capture_piece)
                    piece.set_location(move)
                    self._board.remove_piece(old_coord)
                    self._board.set_piece(piece)
                    self.update_valid_moves()

                    # when check is removed, the game is not in checkmate
                    if not self.is_check(color):
                        self._pieces = revert_pieces
                        self._board.set_board(revert_board)
                        piece.set_location(old_coord)
                        self.update_valid_moves()
                        return False

                    # when check is not removed, reset the board and try again with next move
                    else:
                        self._pieces = revert_pieces
                        self._board.set_board(revert_board)
                        piece.set_location(old_coord)
                        self.update_valid_moves()

        # when no piece can remove check, the game is in checkmate
        return True
