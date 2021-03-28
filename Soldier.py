from MasterPiece import MasterPiece

class Soldier(MasterPiece):
    """
    Represents a soldier piece. Inherits from MasterPiece. Will be instantiated by Game class, and contained
    in the Board class. 
    """
    def __init__(self, color: str, name: str, type: str, location: tuple):
        """
        Uses MasterPiece init method to initialize the piece. 
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
        
        # handle blue piece moves
        if self._color == 'blue':

            # one space forward is valid
            if cur_loc[0] - next_loc[0] == 1 and next_loc[1] == cur_loc[1]:
                return True
            
            # one space sideways is valid
            elif abs(next_loc[1] - cur_loc[1]) == 1 and next_loc[0] == cur_loc[0]:
                return True
            
            # handle palace movement rules
            elif next_loc == (1, 4) and (cur_loc == (2, 3) or cur_loc == (2, 5)):
                return True
            elif cur_loc == (1, 4) and (next_loc == (0, 3) or next_loc == (0, 5)):
                return True
            return False
        
        # handle red pieces
        else:
            if next_loc[0] - cur_loc[0] == 1 and next_loc[1] == cur_loc[1]:
                return True
            elif abs(next_loc[1] - cur_loc[1]) == 1 and next_loc[0] == cur_loc[0]:
                return True
            
            # palace movements
            elif next_loc == (8, 4) and (cur_loc == (7, 3) or cur_loc == (7, 5)):
                return True
            elif cur_loc == (8, 4) and (next_loc == (9, 3) or next_loc == (9, 5)):
                return True
            return False
            