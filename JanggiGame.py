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

    def get_board(self) -> None:
        """
        Getter method for accessing board dict.
        """
        return self._board_spaces

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
        # clear board before updating
        self._visual_board = [['   ' for _ in range(9)] for _ in range(10)]
        for coord in self._board_spaces:
            if self._board_spaces[coord] is not None:
                self._visual_board[coord[0]][coord[1]] = self._board_spaces[coord].get_name()
    
    def set_piece(self, piece) -> None:
        """
        Sets the piece on the board. Will be used upon game initialization.
        param piece: piece object
        """
        self._board_spaces[piece.get_location()] = piece

    def remove_piece(self, coord: tuple) -> None:
        """
        Removes piece at the current location. Used when a piece is captured.
        """
        self._board_spaces[coord] = None

    def get_piece(self, coord: tuple):
        """
        Returns the piece residing at the passed in location.
        param coord: location to check
        return: piece at the location if it is occupied, else None
        """
        # check that given coordinate is a valid board location
        # when coord is valid, check that space is occupied
        if self._board_spaces[coord] is not None:
            return self._board_spaces[coord]


class MasterPiece:
    """
    Holds data common to all pieces of the game. Individual pieces will inherit from this class.
    Named after my code for this assignment.
    """
    def __init__(self, color: str, name: str, type: str, location: tuple):
        """
        Initializes the piece color, name, and location. Holds data member of the piece's current valid
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
        """
        return self._name

    def get_color(self) -> str:
        """
        Getter method for accessing the piece's color.
        """
        return self._color

    def get_type(self) -> str:
        """
        Getter method for accessing piece type.
        """
        return self._type

    def get_location(self) -> tuple:
        """
        Getter method for accessing a piece's location.
        """
        return self._location

    def set_location(self, location: tuple) -> None:
        """
        Sets the piece's location.
        """
        self._location = location
    
    def add_move(self, coord: tuple) -> None:
        """
        Adds destination coord to the piece's valid moves.
        """
        self._valid_moves.add(coord)
    
    def clear_moves(self) -> None:
        """
        Clears the piece's list of valid moves.
        """
        self._valid_moves.clear()
    
    def set_valid_moves(self, board) -> None:
        """
        Loops through each space on the board and checks if it is a valid destination for the piece.
        Adds all valid destinations to the piece's valid moves set. Set is wiped clean before looping.
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
            
            # handle vertical and horizontal moves
            if abs(next_loc[0] - cur_loc[0]) == 1 and next_loc[1] == cur_loc[1]:
                return True
            if abs(next_loc[1] - cur_loc[1]) == 1 and next_loc[0] == cur_loc[0]:
                return True
            
            # handle diagonal moves
            if (cur_loc == (9, 3) and next_loc == (8, 4)) or (cur_loc == (8, 4) and next_loc == (9, 3)):
                return True
            
            if (cur_loc == (9, 5) and next_loc == (8, 4)) or (cur_loc == (8, 4) and next_loc == (9, 5)):
                return True
            
            if (cur_loc == (7, 3) and next_loc == (8, 4)) or (cur_loc == (8, 4) and next_loc == (7, 3)):
                return True
            
            if (cur_loc == (7, 5) and next_loc == (8, 4)) or (cur_loc == (8, 4) and next_loc == (7, 5)):
                return True
            return False
        
        # handle red moves
        else:
            # cannot move out of the palace
            if (next_loc[0] > 2 or next_loc[0] < 0) or (next_loc[1] < 3 or next_loc[1] > 5):
                return False
            
            # handle vertical and horizontal moves
            if abs(next_loc[0] - cur_loc[0]) == 1 and next_loc[1] == cur_loc[1]:
                return True
            if abs(next_loc[1] - cur_loc[1]) == 1 and next_loc[0] == cur_loc[0]:
                return True

            # handle diagonal moves
            if (cur_loc == (0, 3) and next_loc == (1, 4)) or (cur_loc == (1, 4) and next_loc == (0, 3)):
                return True
            
            if (cur_loc == (0, 5) and next_loc == (1, 4)) or (cur_loc == (1, 4) and next_loc == (0, 5)):
                return True
            
            if (cur_loc == (2, 3) and next_loc == (1, 4)) or (cur_loc == (1, 4) and next_loc == (2, 3)):
                return True
            
            if (cur_loc == (2, 5) and next_loc == (1, 4)) or (cur_loc == (1, 4) and next_loc == (2, 5)):
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


class Soldier(MasterPiece):
    """
    Represents a soldier piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, type: str, location: tuple):
        """
        Uses MasterPiece init method to initialize the piece. Adds an in_palace data member to keep
        track of whether the piece is in the enemy palace.
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
        # handle off board spaces
        if next_loc[0] < 0 or next_loc[0] > 9 or next_loc[1] < 0 or next_loc[1] > 8:
            return False

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

           
class Cannon(MasterPiece):
    """
    Represents a cannon piece. Inherits from MasterPiece.
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
        # handle off board spaces
        if next_loc[0] < 0 or next_loc[0] > 9 or next_loc[1] < 0 or next_loc[1] > 8:
            return False
        
        cur_loc = self._location

        # any strictly horizontal or vertical moves are legal
        if (cur_loc[0] - next_loc[0] == 0 and abs(cur_loc[1] - next_loc[1]) > 1) \
        or (cur_loc[1] - next_loc[1] == 0 and abs(cur_loc[0] - next_loc[0]) > 1):
            return True

        blue_palace_x = [(7, 3), (7, 5), (9, 3), (9, 5)]
        red_palace_x = [(0, 3), (0, 5), (2, 3), (2, 5)]
        
        if (cur_loc in blue_palace_x and next_loc in blue_palace_x) or (cur_loc in red_palace_x \
        and next_loc in red_palace_x):
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
        if board.get_piece(next_loc) is not None and board.get_piece(next_loc).get_color() == self._color:
            return True
        
        # cannot capture another cannon
        elif board.get_piece(next_loc) is not None and board.get_piece(next_loc).get_type() == 'cannon':
            return True

        cur_loc = self._location

        # set up counter to count pieces between spaces
        counter = 0

        # loop through each space and check for occupation
        # if occupied by a cannon we can stop, the piece is blocked
        # otherwise increment the counter
        # when counter is 1 piece can be moved, otherwise False
        # check horizontal movements
        if cur_loc[0] == next_loc[0]:
                # increment or decrement value and check each space for occupation
            if cur_loc[1] < next_loc[1]:
                cur_loc = (cur_loc[0], cur_loc[1] + 1)
            else:
                cur_loc = (cur_loc[0], cur_loc[1] - 1)
            while cur_loc[1] != next_loc[1]:
                if board.get_piece(cur_loc) is not None and board.get_piece(cur_loc).get_type() == 'cannon':
                    return True
                elif board.get_piece(cur_loc) is not None:
                    counter += 1
                if cur_loc[1] < next_loc[1]:
                    cur_loc = (cur_loc[0], cur_loc[1] + 1)
                else:
                    cur_loc = (cur_loc[0], cur_loc[1] - 1)
            if counter == 1:
                return False
            return True

        # check vertical movements
        if cur_loc[1] == next_loc[1]:
            # increment or decrement value and check each space for occupation
            if cur_loc[0] < next_loc[0]:
                cur_loc = (cur_loc[0] + 1, cur_loc[1])
            else:
                cur_loc = (cur_loc[0] - 1, cur_loc[1])
            while cur_loc[0] != next_loc[0]:
                if board.get_piece(cur_loc) is not None and board.get_piece(cur_loc).get_type() == 'cannon':
                    return True
                elif board.get_piece(cur_loc) is not None:
                    counter += 1
                if cur_loc[0] < next_loc[0]:
                    cur_loc = (cur_loc[0] + 1, cur_loc[1])
                else:
                    cur_loc = (cur_loc[0] - 1, cur_loc[1])   
            if counter == 1:
                return False   
            return True

        blue_palace_x = [(7, 3), (7, 5), (9, 3), (9, 5)]
        red_palace_x = [(0, 3), (0, 5), (2, 3), (2, 5)]

        # handle traversing the palace diagonals
        # can jump over occupied center space so long as it isn't occupied by cannon
        if cur_loc in red_palace_x and next_loc in red_palace_x and board.get_piece((1, 4)) is not None \
        and board.get_piece((1, 4)).get_type() != 'cannon':
            return False
            
        if cur_loc in blue_palace_x and next_loc in blue_palace_x and board.get_piece((8, 4)) is not None \
        and board.get_piece((8, 4)).get_type() != 'cannon':
            return False
        return True       


class Chariot(MasterPiece):
    """
    Represents a chariot piece. Inherits from MasterPiece.
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
        # handle off board spaces
        if next_loc[0] < 0 or next_loc[0] > 9 or next_loc[1] < 0 or next_loc[1] > 8:
            return False

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
        Determines whether a piece is blocked from moving to it's desired location. Soldier, guard 
        and general will inherit this method. Does not take in to account if the space is a valid move 
        for the piece.
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


class Elephant(MasterPiece):
    """
    Represents an elephant piece. Inherits from MasterPiece.
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
        # handle off board spaces
        if next_loc[0] < 0 or next_loc[0] > 9 or next_loc[1] < 0 or next_loc[1] > 8:
            return False

        cur_loc = self._location

        # horizontal move, then diagonal
        if abs(next_loc[0] - cur_loc[0]) == 2 and abs(next_loc[1] - cur_loc[1]) == 3:
            return True

        # vertical move, then diagonal
        elif abs(next_loc[0] - cur_loc[0]) == 3 and abs(next_loc[1] - cur_loc[1]) == 2:
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
        if board.get_piece(next_loc) is not None and board.get_piece(next_loc).get_color() == self._color:
            return True

        cur_loc = self._location

        # check horizontal then diagonal
        if abs(next_loc[0] - cur_loc[0]) == 2:
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

        # check spot for occupation
        if board.get_piece(cur_loc) is not None:
            return True  

        # check diagonal spots
        if cur_loc[0] < next_loc[0] and cur_loc[1] < next_loc[1]:
            cur_loc = (cur_loc[0] + 1, cur_loc[1] + 1)
        elif cur_loc[0] < next_loc[0] and cur_loc[1] > next_loc[1]:
            cur_loc = (cur_loc[0] + 1, cur_loc[1] - 1)
        elif cur_loc[0] > next_loc[0] and cur_loc[1] > next_loc[1]:
            cur_loc = (cur_loc[0] - 1, cur_loc[1] - 1)            
        else:
            cur_loc = (cur_loc[0] - 1, cur_loc[1] + 1)      

        # check spot for occupation
        if board.get_piece(cur_loc) is not None:
            return True  
        return False            
                

class Horse(MasterPiece):
    """
    Represents a horse piece. Inherits from MasterPiece.
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
        # handle off board spaces
        if next_loc[0] < 0 or next_loc[0] > 9 or next_loc[1] < 0 or next_loc[1] > 8:
            return False
        
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
        Determines whether a piece is blocked from moving to it's desired location. Soldier, guard 
        and general will inherit this method. Does not take in to account if the space is a valid move 
        for the piece.
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


class Guard(MasterPiece):
    """
    Represents a guard piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, type: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, type, location)


class General(MasterPiece):
    """
    Represents a general piece. Inherits from MasterPiece.
    """
    def __init__(self, color: str, name: str, type: str, location: tuple):
        """
        Uses MasterPiece method to initialize the piece.
        """
        super().__init__(color, name, type, location)
    

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
        self._board = Board()
        self._pieces = {Chariot('red', 'rR1', 'chariot', (0, 0)), Elephant('red', 'rE1', 'elephant', (0, 1)),
        Horse('red', 'rH1', 'horse', (0, 2)), Guard('red', 'rA1', 'guard', (0, 3)), Guard('red', 'rA2', 'guard', (0, 5)),
        Elephant('red', 'rE2', 'elephant', (0, 6)), Horse('red', 'rH2', 'horse', (0, 7)), Chariot('red', 'rR1', 'chariot', (0, 8)),
        Cannon('red', 'rC1', 'cannon', (2, 1)), Cannon('red', 'rC2', 'cannon', (2, 7)), Soldier('red', 'rS1', 'soldier', (3, 0)),
        Soldier('red', 'rS2', 'soldier', (3, 2)), Soldier('red', 'rS3', 'soldier', (3, 4)),
        Soldier('red', 'rS4', 'soldier', (3, 6)), Soldier('red', 'rS5', 'soldier', (3, 8)),
        Soldier('blue', 'bS1', 'soldier', (6, 0)), Soldier('blue', 'bS2', 'soldier', (6, 2)), 
        Soldier('blue', 'bS3', 'soldier', (6, 4)), Soldier('blue', 'bS4', 'soldier', (6, 6)),
        Soldier('blue', 'bS5', 'soldier', (6, 8)), Cannon('blue', 'bC1', 'cannon', (7, 1)),
        Cannon('blue', 'bC2', 'cannon', (7, 7)), Chariot('blue', 'bR1', 'chariot', (9, 0)),
        Elephant('blue', 'bE1', 'elephant', (9, 1)), Horse('blue', 'bH1', 'horse', (9, 2)), 
        Guard('blue', 'bA1', 'guard', (9, 3)), Guard('blue', 'bA2', 'guard', (9, 5)),
        Elephant('blue', 'bE2', 'elephant', (9, 6)), Horse('blue', 'bH2', 'horse', (9, 7)), Chariot('blue', 'bR1', 'chariot', (9, 8)),
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
    
    def update_valid_moves(self) -> None:
        """
        Updates the valid moves for each piece on the board.
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
        """
        self._player_turn = self._player_swap[self._player_turn]

    def is_valid_move(self, move_from: str, move_to: str):
        """
        Checks that the spaces fed to make_move are on the board, the game state allows for a move, and
        the correct player is moving.
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

        # check that piece belongs to moving player and game is not over
        if piece.get_color() != self._player_turn or self._game_state != 'UNFINISHED':
            return False
        
        # send back necessary data to continue when move is valid
        return piece, piece_loc, self._board.convert_coords(move_to)
        
    def make_move(self, move_from: str, move_to: str) -> bool:
        """
        Handles basic piece movements in the game. Checks that the move is valid and moves the piece
        and updates the board and game state when it is.
        param move_from: space of the piece to move
        param move_to: space to move the piece to
        return: True when move is valid, otherwise False
        """
        # check that the spaces are valid and piece belongs to the correct player
        valid_move = self.is_valid_move(move_from, move_to)
        if not valid_move:
            return False
        
        # unpack tuple to get the piece, current coordinate, and destination coordinate
        piece = valid_move[0]
        cur_coord = valid_move[1]
        dest_coord = valid_move[2]

        # check that move is valid for the piece
        if not piece.valid_move(dest_coord) or piece.is_blocked(dest_coord, self._board):
            return False
        
        


        
