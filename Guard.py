from MasterPiece import MasterPiece

class Guard(MasterPiece):
    """
    Represents a guard piece. Inherits from MasterPiece. Will be instantiated in the Game class and contained
    in the Board class.
    """
    def __init__(self, color: str, name: str, type: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, type, location)
        