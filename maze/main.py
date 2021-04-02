from controllers.game import GameController
from models.score import Score
from datetime import datetime
import tkinter  # This library is for the GUI where the user enters their name


def main():

    root = tkinter.Tk()
    root.geometry("250x100")

    player_username = tkinter.StringVar()

    def submit_username():
        name = player_username.get()
        print(f"Your username is: {name}")
        player_username.set("")
        root.destroy()      # Close the GUI window after the user submits their username

        return name

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
        "name": "Rye Ang lamao",
        "score": game_controller.player_time,
        "date": str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
     })
    
    print(player_score.player_name)
    print(player_score.date)
    print(player_score.score)

main()
