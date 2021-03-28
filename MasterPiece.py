class MasterPiece:
    """
    Holds data common to all pieces of the game. Individual pieces will inherit from this class.
    Named after my code for this assignment (joke). Some of the methods will be called in the game class
    to get and set data, or to check for valid moves and whether a piece is blocked. It will also
    interact with Board class to check for valid moves of a piece.
    """
    def __init__(self, color: str, name: str, type: str, location: tuple):
        """
        Initializes the piece color, name, type, and location. Holds data member of the piece's current valid
        moves given the most recently updated board.
        """
        self._color = color
        self._name = name
        self._type = type
        self._location = location
        self._valid_moves = set()
    
    def get_name(self) -> str:
        """
        Getter method for accessing piece name.
        return: name of the piece
        """
        return self._name

    def get_color(self) -> str:
        """
        Getter method for accessing the piece's color.
        return: color of the piece
        """
        return self._color

    def get_type(self) -> str:
        """
        Getter method for accessing piece type.
        return: type of the piece
        """
        return self._type

    def get_location(self) -> tuple:
        """
        Getter method for accessing a piece's location.
        return: piece's coordinate location
        """
        return self._location
    
    def get_valid_moves(self) -> set:
        """
        Getter method for accessing a piece's valid moves.
        return: set of the pieces valid move-to coordinates
        """
        return self._valid_moves

    def set_location(self, location: tuple) -> None:
        """
        Sets the piece's location.
        return: None
        """
        self._location = location
    
    def add_move(self, coord: tuple) -> None:
        """
        Adds destination coord to the piece's valid moves.
        return: None
        """
        self._valid_moves.add(coord)
    
    def clear_moves(self) -> None:
        """
        Clears the piece's list of valid moves. Used before refilling so invalid moves do not persist.
        return: None
        """
        self._valid_moves.clear()
    
    def set_valid_moves(self, board) -> None:
        """
        Loops through each space on the board and checks if it is a valid destination for the piece.
        Adds all valid destinations to the piece's valid moves set. Set is wiped clean before looping.
        return: None
        """
        # clear set before adding spaces
        self.clear_moves()

        for space in board.get_board():
            if self.valid_move(space) and not self.is_blocked(space, board):
                self.add_move(space)

    def valid_move(self, next_loc: tuple):
        """
        Returns whether or not the piece can move from the current location to the next location. Only
        handles whether the space can be moved to by movement rules of the piece. Does not handle 
        whether the space is occupied, etc. Guard and general will inherit this method.
        param next_loc: space to move to
        return: True if space is within reach, else False
        """
        cur_loc = self._location

        # handle blue moves
        if self._color == 'blue':

            # cannot move out of the palace
            if (next_loc[0] < 7 or next_loc[0] > 9) or (next_loc[1] < 3 or next_loc[1] > 5):
                return False

            blue_palace_x = [(7, 3), (7, 5), (8, 4), (9, 3), (9, 5)]       

            # handle diagonal moves in palace
            if cur_loc in blue_palace_x and next_loc in blue_palace_x:
                if abs(cur_loc[0] - next_loc[0]) == 1 and abs(cur_loc[1] - next_loc[1]) == 1:
                    return True    

        else:
            # cannot move out of the palace
            if (next_loc[0] > 2 or next_loc[0] < 0) or (next_loc[1] < 3 or next_loc[1] > 5):
                return False

            red_palace_x = [(0, 3), (0, 5), (1, 4), (2, 3), (2, 5)]     

            # handle diagonal moves in palace
            if cur_loc in red_palace_x and next_loc in red_palace_x:
                if abs(cur_loc[0] - next_loc[0]) == 1 and abs(cur_loc[1] - next_loc[1]) == 1:
                    return True             
                  
        # handle vertical and horizontal moves
        if abs(next_loc[0] - cur_loc[0]) == 1 and next_loc[1] == cur_loc[1]:
            return True
        if abs(next_loc[1] - cur_loc[1]) == 1 and next_loc[0] == cur_loc[0]:
            return True
        return False
        
    def is_blocked(self, next_loc: tuple, board) -> bool:
        """
        Determines whether a piece is blocked from moving to it's desired location. Soldier, guard 
        and general will inherit this method. Does not take in to account if the space is a valid move 
        for the piece.
        param next_loc: desired move-to location of the piece
        param board: the current game board
        return: True if piece is blocked, else False
        """
        # for soldier, general, and guards, if space is occupied by same color piece it is blocked
        if board.get_piece(next_loc) is not None and board.get_piece(next_loc).get_color() == self._color:
            return True
        return False
        