class Board:
    """
    Represents the board of the game. Includes a visual representation of the
    board, a dictionary to represent each space on the board, and a method for
    updating the visual board. Keeps track of where pieces are on the board. 
    Moves pieces on the board and removes captured pieces from the board.
    Instantiated by the Game class to be the board of the game. When in the Game class,
    the board will contain at least one of each of the piece class objects as a way of 
    keeping track of piece locations.
    """
    def __init__(self):
        """
        Initializes a visual board (for game loop), the board spaces which will hold pieces when the game
        starts, a coordinate map to convert Janggi algebraic notation in to tuple coordinates.
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

    def get_board(self) -> dict:
        """
        Getter method for accessing board dict.
        return: board spaces dictionary
        """
        return self._board_spaces
    
    def set_board(self, board: dict) -> None:
        """
        Sets the board to a new board. Used for reverting the board to a previous state.
        return: None
        """
        self._board_spaces = board

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
        Prints the board to output. Used in game loop.
        return: None
        """
        print('      A      B      C      D      E      F      G      H      I')
        print('   ---------------------------------------------------------------')
        for index in range(10):
            if index < 9:
                print(str(index + 1) + ' ', self._visual_board[index], index + 1)
            else:
                print(index + 1, self._visual_board[index], index + 1)
            print('   ---------------------------------------------------------------')
        print('      A      B      C      D      E      F      G      H      I')

    def update_visual_board(self) -> None:
        """
        Iterates over dictionary of board spaces and places pieces on the visual
        board in their corresponding position. Used in game loop.
        return: None
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
        return: None
        """
        self._board_spaces[piece.get_location()] = piece

    def remove_piece(self, coord: tuple) -> None:
        """
        Removes piece at the current location. Used when a piece is captured.
        return: None
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
            