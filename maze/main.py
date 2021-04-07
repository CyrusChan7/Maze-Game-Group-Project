from controllers.game import GameController
from models.score import Score
from datetime import datetime
from models.persistence import Persistence
import tkinter  # This library is for the GUI where the user enters their name


def main():

    root = tkinter.Tk()
    root.geometry("250x100")

    player_username = tkinter.StringVar()
    
    #player username
    username = ""

    def submit_username():
        global username
        username = player_username.get()
        print(f"Your username is: {username}")
        player_username.set("")
        root.destroy()      # Close the GUI window after the user submits their username

    username_label = tkinter.Label(root, text="Enter your username: ")
    username_entry = tkinter.Entry(root, textvariable=player_username )
    submit_button = tkinter.Button(root, text="Confirm username", command=submit_username)
    
    username_label.grid(row=0,column=0)
    username_entry.grid(row=0,column=1)
    submit_button.grid(row=2,column=1)

    root.mainloop()

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

    player_score = Score()
    player_score.from_dict({
        "name": "Player",
        "score": game_controller.player_time*25,
        "date": str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
     })

    perc_file = Persistence(player_score)
    perc_file.to_csv()

main()
