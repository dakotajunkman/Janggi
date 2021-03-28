from MasterPiece import MasterPiece

class Chariot(MasterPiece):
    """
    Represents a chariot piece. Inherits from MasterPiece. Will be instantiated in the Game class and contained
    in the Board class.
    """
    def __init__(self, color: str, name: str, type: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, type, location)

    def valid_move(self, next_loc: tuple) -> bool:
        """
        Returns whether or not the piece can move from the current location to the next location. Only
        handles whether the space can be moved to by movement rules of the piece. Does not handle 
        whether the space is occupied, etc.
        param next_loc: space to move to
        return: True if space is within reach, else False
        """     
        cur_loc = self._location

        # any strictly horizontal or vertical moves are legal
        if cur_loc[0] - next_loc[0] == 0 or cur_loc[1] - next_loc[1] == 0:
            return True

        blue_palace_x = [(7, 3), (7, 5), (8, 4), (9, 3), (9, 5)]
        red_palace_x = [(0, 3), (0, 5), (1, 4), (2, 3), (2, 5)]
        
        if (cur_loc in blue_palace_x and next_loc in blue_palace_x) or (cur_loc in red_palace_x \
        and next_loc in red_palace_x):
            return True
        return False

    def is_blocked(self, next_loc: tuple, board) -> bool:
        """
        Determines whether a piece is blocked from moving to it's desired location. Does not take in to account 
        if the space is a valid move for the piece.
        param next_loc: desired move-to location of the piece
        param board: the current game board
        return: True if piece is blocked, else False
        """
        if board.get_piece(next_loc) is not None and board.get_piece(next_loc).get_color() == self._color:
            return True

        cur_loc = self._location

        # check horizontal movements
        if cur_loc[0] == next_loc[0]:
                # increment or decrement value and check each space for occupation
            if cur_loc[1] < next_loc[1]:
                cur_loc = (cur_loc[0], cur_loc[1] + 1)
            else:
                cur_loc = (cur_loc[0], cur_loc[1] - 1)
            while cur_loc[1] != next_loc[1]:
                if board.get_piece(cur_loc) is not None:
                    return True
                if cur_loc[1] < next_loc[1]:
                    cur_loc = (cur_loc[0], cur_loc[1] + 1)
                else:
                    cur_loc = (cur_loc[0], cur_loc[1] - 1)
            return False

        # check vertical movements
        if cur_loc[1] == next_loc[1]:
                # increment or decrement value and check each space for occupation
            if cur_loc[0] < next_loc[0]:
                cur_loc = (cur_loc[0] + 1, cur_loc[1])
            else:
                cur_loc = (cur_loc[0] - 1, cur_loc[1])
            while cur_loc[0] != next_loc[0]:
                if board.get_piece(cur_loc) is not None:
                    return True
                if cur_loc[0] < next_loc[0]:
                    cur_loc = (cur_loc[0] + 1, cur_loc[1])
                else:
                    cur_loc = (cur_loc[0] - 1, cur_loc[1])   
            return False   

        blue_palace_x = [(7, 3), (7, 5), (9, 3), (9, 5)]
        red_palace_x = [(0, 3), (0, 5), (2, 3), (2, 5)]

        # handle traversing the palace diagonals
        if cur_loc in red_palace_x and next_loc in red_palace_x and board.get_piece((1, 4)) is not None:
            return True
            
        if cur_loc in blue_palace_x and next_loc in blue_palace_x and board.get_piece((8, 4)) is not None:
            return True
        return False
