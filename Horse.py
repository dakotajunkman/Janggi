from MasterPiece import MasterPiece

class Horse(MasterPiece):
    """
    Represents a horse piece. Inherits from MasterPiece. Will be instantiated in the Game class and contained
    in the Board class.
    """
    def __init__(self, color: str, name: str, type, location: tuple):
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

        # horizontal move, then diagonal
        if abs(next_loc[0] - cur_loc[0]) == 1 and abs(next_loc[1] - cur_loc[1]) == 2:
            return True

        # vertical move, then diagonal
        elif abs(next_loc[0] - cur_loc[0]) == 2 and abs(next_loc[1] - cur_loc[1]) == 1:
            return True
        return False

    def is_blocked(self, next_loc: tuple, board) -> bool:
        """
        Determines whether a piece is blocked from moving to it's desired location. Does not take in to account if 
        the space is a valid move for the piece.
        param next_loc: desired move-to location of the piece
        param board: the current game board
        return: True if piece is blocked, else False
        """
        if board.get_piece(next_loc) is not None and board.get_piece(next_loc).get_color() == self._color:
            return True

        cur_loc = self._location

        # check horizontal then diagonal
        if abs(next_loc[0] - cur_loc[0]) == 1:
            if cur_loc[1] < next_loc[1]:
                cur_loc = (cur_loc[0], cur_loc[1] + 1)
            else:
                cur_loc = (cur_loc[0], cur_loc[1] - 1)
        
        # check vertical then diagonal
        else:
            if cur_loc[0] < next_loc[0]:
                cur_loc = (cur_loc[0] + 1, cur_loc[1])
            else:
                cur_loc = (cur_loc[0] - 1, cur_loc[1])        

        # do not need to check the destination since it was checked above
        # only need to check the orthogonal move
        if board.get_piece(cur_loc) is not None:
            return True
        return False   
