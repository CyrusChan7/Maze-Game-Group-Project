from controllers.game import GameController
from models.score import Score
from datetime import datetime
from models.persistence import Persistence
import tkinter  # This library is for the GUI where the user enters their username

# Player username in the global scope - this is where the GUI username entered will be saved
username = ""

# Using main() as a class
def main():
    """
    Runs the maze game
    """

    root = tkinter.Tk()
    root.title("Input name")        # Title of the tkinter GUI window
    root.geometry("250x100")        # Size/resolution of the GUI window

    player_username = tkinter.StringVar()

    def submit_username():
        """
        Controls the GUI where users enter there username 
        """
        global username     # Global is necessary as it is inconvenient to retrieve the return value
        username = player_username.get() # Assigns username var the value passed from GUI
        player_username.set("")
        root.destroy()      # Close the GUI window after the user submits their username

    # Creation of the items in the GUI
    username_label = tkinter.Label(root, text="Enter your username: ")
    username_entry = tkinter.Entry(root, textvariable=player_username )
    submit_button = tkinter.Button(root, text="Confirm username", command=submit_username)
    
    # Layout of the items in the GUI
    username_label.grid(row=0,column=0)
    username_entry.grid(row=0,column=1)
    submit_button.grid(row=2,column=1)

    root.mainloop()     # Keep the GUI open

    game_controller = GameController()  # Create an instance of GameController

    running = True
    while running:
        try:
            game_controller.get_user_input()
        except SystemExit:
            running = False
            continue

    player_backpack = game_controller.player_backpack

    # Check if user has all 4 items, otherwise do not write to CSV file
    if len(player_backpack) == 4:
        # If the user runs out of time, their score will also not be persisted
        if int(game_controller.player_time) != 0:
            score_value = game_controller.player_time * 25  # Score calculation algorithm
            print("The player score of", username, "is", int(score_value))

            player_score = Score()
            player_score.from_dict({
                "name": username,
                "score": score_value,
                "date": str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # .strftime() formats the date output
            })

            # Responsible for persisting the name, score, and date in a CSV file
            perc_file = Persistence(player_score)
            perc_file.to_csv()

main()
