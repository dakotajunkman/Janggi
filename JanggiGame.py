# Author: Dakota Junkman 
# Date: 02/20/2021
# Description: A backend implementation of the abstract board game, Janggi
# (also known as Korean Chess).

class Board:
    """
    Represents the board of the game. Includes a visual representation of the
    board, a dictionary to represent each space on the board, and a method for
    updating the visual board. Keeps track of where pieces are on the board. 
    """
    def __init__(self):
        """
        Initializes the board and necessary data members.
        """
        self._visual_board = [
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ]
        self._board_spaces = {
            (0, 0): None, (0, 1): None, (0, 2): None, (0, 3): None, (0, 4): None,
            (0, 5): None, (0, 6): None, (0, 7): None, (0, 8): None,
            (1, 0): None, (1, 1): None, (1, 2): None, (1, 3): None, (1, 4): None,
            (1, 5): None, (1, 6): None, (1, 7): None, (1, 8): None,
            (2, 0): None, (2, 1): None, (2, 2): None, (2, 3): None, (2, 4): None,
            (2, 5): None, (2, 6): None, (2, 7): None, (2, 8): None,
            (3, 0): None, (3, 1): None, (3, 2): None, (3, 3): None, (3, 4): None,
            (3, 5): None, (3, 6): None, (3, 7): None, (3, 8): None,
            (4, 0): None, (4, 1): None, (4, 2): None, (4, 3): None, (4, 4): None,
            (4, 5): None, (4, 6): None, (4, 7): None, (4, 8): None,
            (5, 0): None, (5, 1): None, (5, 2): None, (5, 3): None, (5, 4): None,
            (5, 5): None, (5, 6): None, (5, 7): None, (5, 8): None,
            (6, 0): None, (6, 1): None, (6, 2): None, (6, 3): None, (6, 4): None,
            (6, 5): None, (6, 6): None, (6, 7): None, (6, 8): None,
            (7, 0): None, (7, 1): None, (7, 2): None, (7, 3): None, (7, 4): None,
            (7, 5): None, (7, 6): None, (7, 7): None, (7, 8): None,
            (8, 0): None, (8, 1): None, (8, 2): None, (8, 3): None, (8, 4): None,
            (8, 5): None, (8, 6): None, (8, 7): None, (8, 8): None,
            (9, 0): None, (9, 1): None, (9, 2): None, (9, 3): None, (9, 4): None,
            (9, 5): None, (9, 6): None, (9, 7): None, (9, 8): None
        }

        self._coord_map = {
            '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9,
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8
        }
    
    def convert_coords(self, coord: str):
        """
        Converts Janggi algebraic notation in to coordinates.
        param coord: Janggi algebraic board location
        return: tuple of coordinates when location is on the board, else None
        """
        # handles rows 1 - 9
        if len(coord) == 2:
            if 'a' <= coord[0].lower() <= 'i' and '0' <= coord[1] <= '9':
                row_coord = self._coord_map[coord[1]]
                col_coord = self._coord_map[coord[0]]
                return row_coord, col_coord
        
        # handles row 10
        elif len(coord) == 3:
            if 'a' <= coord[0].lower() <= 'i' and coord[1] == '1' and coord[2] == '0':
                row_coord = self._coord_map[coord[1:]]
                col_coord = self._coord_map[coord[0]]
                return row_coord, col_coord

    def display_board(self) -> None:
        """
        Prints the board to output. Used for debugging only.
        """
        for row in self._visual_board:
            print(row)
    
    def update_visual_board(self) -> None:
        """
        Iterates over dictionary of board spaces and places pieces on the visual
        board in their corresponding position. Used for debugging only.
        """
        for coord in self._board_spaces:
            if self._board_spaces[coord] is not None:
                self._visual_board[coord[0]][coord[1]] = self._board_spaces[coord].get_name()
    
    def move_piece(self, piece) -> None:
        """
        Finds piece on the board and moves it to its new location.
        param piece: piece object
        """
        for coord in self._board_spaces:
            if self._board_spaces[coord] == piece:
                self._board_spaces[coord] = None
        self._board_spaces[piece.get_location()] = piece
    
    def set_piece(self, piece) -> None:
        """
        Sets the piece on the board. Will be used upon game initialization.
        param piece: piece object
        """
        self._board_spaces[piece.get_location()] = piece

    def get_piece(self, coord: str):
        """
        Returns the piece residing at the passed in location.
        param coord: location to check
        return: piece at the location if it is occupied, else None
        """
        # check that given coordinate is a valid board location
        # when coord is valid, check that space is occupied
        if self.convert_coords(coord) and self._board_spaces[self.convert_coords(coord)] is not None:
            return self._board_spaces[self.convert_coords(coord)]

class MasterPiece:
    """
    Holds data common to all pieces of the game. Individual pieces will inherit from this class.
    """
    def __init__(self, color: str, name: str, location: tuple):
        """
        Initializes the piece. Sets the color and initial location on the board. Calls the board move
        piece method to set the piece on the board.
        """
        self._color = color
        self._name = name
        self._location = location
    
    def get_name(self) -> str:
        """
        Getter method for accessing piece name.
        """
        return self._name

    def get_location(self) -> tuple:
        """
        Getter method for accessing the piece's location.
        """
        return self._location
    
    def set_location(self, coord: tuple) -> None:
        """
        Updates the piece's location.
        """
        self._location = coord


class Soldier(MasterPiece):
    """
    Represents a soldier piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, location: tuple):
        """
        Uses MasterPiece init method to initialize the piece.
        """
        super().__init__(color, name, location)
    

class Cannon(MasterPiece):
    """
    Represents a cannon piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, location)


class Chariot(MasterPiece):
    """
    Represents a chariot piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, location)


class Elephant(MasterPiece):
    """
    Represents an elephant piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, location)


class Horse(MasterPiece):
    """
    Represents a horse piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, location)


class Guard(MasterPiece):
    """
    Represents a guard piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, location)


class General(MasterPiece):
    """
    Represents a general piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, location)


class JanggiGame:
    """
    Represents the actual game. Game state is updated and moves are made using the piece and board
    objects.
    """
    def __init__(self):
        """
        Initializes the board and pieces and places pieces on the board. Sets up the current state of
        the game and whose turn it is to move.
        """
        # initialize the playing board
        self._board = Board()

        # initialize the red pieces and place them on the board
        # chariots will be denoted by R, for their western chess counterpart Rook
        self._rR1 = Chariot('red', 'rR1', (0, 0))
        self._board.set_piece(self._rR1)
        self._rE1 = Elephant('red', 'rE1', (0, 1))
        self._board.set_piece(self._rE1)
        self._rH1 = Horse('red', 'rH1', (0, 2))
        self._board.set_piece(self._rH1)
        # guards will be denoted by A, for their xiangqi counterpart Advisor
        self._rA1 = Guard('red', 'rA1', (0, 3))
        self._board.set_piece(self._rA1)
        self._rA2 = Guard('red', 'rA2', (0, 5))
        self._board.set_piece(self._rA2)
        self._rE2 = Elephant('red', 'rE2', (0, 6))
        self._board.set_piece(self._rE2)
        self._rH2 = Horse('red', 'rH2', (0, 7))
        self._board.set_piece(self._rH2)
        self._rR2 = Chariot('red', 'rR2', (0, 8))
        self._board.set_piece(self._rR2)
        self._rG1 = General('red', 'rG1', (1, 4))
        self._board.set_piece(self._rG1)
        self._rC1 = Cannon('red', 'rC1', (2, 1))
        self._board.set_piece(self._rC1)
        self._rC2 = Cannon('red', 'rC2', (2, 7))
        self._board.set_piece(self._rC2)
        self._rS1 = Soldier('red', 'rS1', (3, 0))
        self._board.set_piece(self._rS1)
        self._rS2 = Soldier('red', 'rS2', (3, 2))
        self._board.set_piece(self._rS2)
        self._rS3 = Soldier('red', 'rS3', (3, 4))
        self._board.set_piece(self._rS3)
        self._rS4 = Soldier('red', 'rS4', (3, 6))
        self._board.set_piece(self._rS4)
        self._rS5 = Soldier('red', 'rS5', (3, 8))
        self._board.set_piece(self._rS5)

        # initialize blue pieces and place on the board
        self._bR1 = Chariot('blue', 'bR1', (9, 0))
        self._board.set_piece(self._bR1)
        self._bE1 = Elephant('blue', 'bE1', (9, 1))
        self._board.set_piece(self._bE1)
        self._bH1 = Horse('blue', 'bH1', (9, 2))
        self._board.set_piece(self._bH1)
        self._bA1 = Guard('blue', 'bA1', (9, 3))
        self._board.set_piece(self._bA1)
        self._bA2 = Guard('blue', 'bA2', (9, 5))
        self._board.set_piece(self._bA2)
        self._bE2 = Elephant('blue', 'bE2', (9, 6))
        self._board.set_piece(self._bE2)
        self._bH2 = Horse('blue', 'bH2', (9, 7))
        self._board.set_piece(self._bH2)
        self._bR2 = Chariot('blue', 'bR2', (9, 8))
        self._board.set_piece(self._bR2)
        self._bG1 = General('blue', 'bG1', (8, 4))
        self._board.set_piece(self._bG1)
        self._bC1 = Cannon('blue', 'bC1', (7, 1))
        self._board.set_piece(self._bC1)
        self._bC2 = Cannon('blue', 'bC2', (7, 7))
        self._board.set_piece(self._bC2)
        self._bS1 = Soldier('blue', 'bS1', (6, 0))
        self._board.set_piece(self._bS1)
        self._bS2 = Soldier('blue', 'bS2', (6, 2))
        self._board.set_piece(self._bS2)
        self._bS3 = Soldier('blue', 'bS3', (6, 4))
        self._board.set_piece(self._bS3)
        self._bS4 = Soldier('blue', 'bS4', (6, 6))
        self._board.set_piece(self._bS4)
        self._bS5 = Soldier('blue', 'bS5', (6, 8))
        self._board.set_piece(self._bS5)
