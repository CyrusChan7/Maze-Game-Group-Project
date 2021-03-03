from controllers.game import GameController

def main():
    """
    Runs the maze game
    """
    game_controller = GameController()

    running = True
    while running:
        try:
            game_controller.get_user_input()
        except SystemExit:
            running = False
            continue

main()
