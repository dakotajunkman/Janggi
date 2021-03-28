from JanggiGame import JanggiGame

def play_game():
    """
    Creates a game loop to play the game.
    """
    game = JanggiGame()
    game.get_board().update_visual_board()
    game.get_board().display_board()

    while game.get_game_state() == 'UNFINISHED':
        print(game.get_player_turn(), 'turn')
        move_from = input('Move from: ')
        move_to = input('Move to: ')
        game.make_move(move_from, move_to)
        game.get_board().update_visual_board()
        game.get_board().display_board()
        if game.is_in_check(game.get_player_turn()):
            print(game.get_player_turn(), 'is in check')
    print(game.get_game_state())

if __name__ == '__main__':
    play_game()