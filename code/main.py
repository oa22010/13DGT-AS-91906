# Import necessary modules
import tkinter as tk
import random
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Choose your opponent")  # Set the window title
root.resizable(False, False)  # Disable window resizing

# Initialize variables
# Initialize the list to store winning combinations
win_combinations = [
        [(0, 0), (0, 1), (0, 2)],  # First row
        [(1, 0), (1, 1), (1, 2)],  # Second row
        [(2, 0), (2, 1), (2, 2)],  # Third row
        [(0, 0), (1, 0), (2, 0)],  # First column
        [(0, 1), (1, 1), (2, 1)],  # Second column
        [(0, 2), (1, 2), (2, 2)],  # Third column
        [(0, 0), (1, 1), (2, 2)],  # Top-left to bottom-right diagonal
        [(0, 2), (1, 1), (2, 0)]   # Top-right to bottom-left diagonal
        ]
x_score = 0  # Initialize Player X's score
o_score = 0  # Initialize Player O's score
draws_score = 0  # Initialize the draw score
button_num = 0  # Initialize a counter to track the number of button clicks

# Function to handle the bot's move
def bot_move():
    # Create a list of empty buttons on the board
    empty_buttons = [(r, c) for r in range(3)
                     for c in range(3)
                     if buttons[r][c]["text"] == ""]

    # Try to WIN first
    for combination in win_combinations:
        a, b, c = combination
        values = [buttons[a[0]][a[1]]["text"],
                  buttons[b[0]][b[1]]["text"],
                  buttons[c[0]][c[1]]["text"]]

        if values.count("O") == 2 and values.count("") == 1:
            move = combination[values.index("")]
            row, column = move
            buttons[row][column]["text"] = "O"
            buttons[row][column]["state"] = "disabled"
            global button_num
            button_num += 1
            win_check()
            return

    # BLOCK the player
    for combination in win_combinations:
        a, b, c = combination
        values = [buttons[a[0]][a[1]]["text"],
                  buttons[b[0]][b[1]]["text"],
                  buttons[c[0]][c[1]]["text"]]

        if values.count("X") == 2 and values.count("") == 1:
            move = combination[values.index("")]
            row, column = move
            buttons[row][column]["text"] = "O"
            buttons[row][column]["state"] = "disabled"
            button_num += 1
            win_check()
            return

    # If no winning or blocking move is available, pick middle if available
    if buttons[1][1]["text"] == "":
        buttons[1][1]["text"] = "O"
        buttons[1][1]["state"] = "disabled"
        button_num += 1
        win_check()
        return

    # Otherwise pick random
    if empty_buttons:
        row, column = random.choice(empty_buttons)
        buttons[row][column]["text"] = "O"
        buttons[row][column]["state"] = "disabled"
        button_num += 1
        win_check()


# Create the noughts and crosses board
def create_board():
    global buttons, restart_button, x_score, o_score, draws_score

    x_score = 0  # Reset Player X's score
    o_score = 0  # Reset Player O's score
    draws_score = 0  # Reset the draw score

    class Button(tk.Button):
        def __init__(self, row, column):
            super().__init__(
                root,
                text="",
                width=10,
                height=5,
                command=lambda r=row, c=column: on_button_click(r, c),
            )

            self.grid(row=row, column=column, padx=5, pady=5)

    buttons = [[Button(row, column) for column in range(3)] for row in range(3)]
    button_list = [button for row in buttons for button in row]

    restart_button = ttk.Button(root, text="Restart", command=on_restart_button_click)
    restart_button.grid(row=3, column=0, pady=10)

    how_to_play_button = ttk.Button(
        root,
        text="How to play",
        command=lambda: how_to_play(
            [restart_button, x_wins, o_wins, draws, restart_button, how_to_play_button, revert_button],
            button_list,
        ),
    )
    how_to_play_button.grid(row=3, column=1, pady=5)

    revert_button = ttk.Button(
        root,
        text="Back",
        command=lambda: revert_board(
            [restart_button, revert_button, x_wins, o_wins, draws, how_to_play_button], button_list
        ),
    )
    revert_button.grid(row=3, column=2, pady=5)

    global x_wins, o_wins, draws

    x_wins = tk.Label(root, text=f"X wins: {x_score}")
    x_wins.grid(row=4, column=0)

    o_wins = tk.Label(root, text=f"O wins: {o_score}")
    o_wins.grid(row=4, column=2)

    draws = tk.Label(root, text=f"Draws: {draws_score}")
    draws.grid(row=4, column=1)

    score_check("")

# Function to destroy the opponent choice widgets
def destroy_opponent_choice_widgets(widgets):
    for widget in widgets:
        widget.destroy()

def how_to_play(widgets, button_list):
    global button_num
    button_num = 0  # Reset the button click count
    root.geometry("500x150")
    root.title("How to play")

    destroy_opponent_choice_widgets(widgets)
    for button in button_list:
        button.destroy()

    instructions = tk.Label(
        root,
        text=(
            "Welcome to Noughts and Crosses!\n\n"
            "To play, simply click on an empty square to place your mark (X or O).\n"
            "The first player to get three in a row wins!\n"
            "You can choose to play against another player or against the bot.\n"
            "Good luck and have fun playing!"
        ),
    )
    instructions.pack(pady=10)

    back_button = ttk.Button(
        root,
        text="Back",
        command=lambda: on_opponent_button_click(opponent, [instructions, back_button]),
    )
    back_button.pack(pady=5)

# Function to handle Restart Button clicks
def on_restart_button_click():
    print("Restart button clicked")
    reset_game("")

    global x_score, o_score, draws_score
    x_score = 0
    o_score = 0
    draws_score = 0
    score_check("")

# Function to handle opponent button clicks
def on_opponent_button_click(opponent_type, widgets):
    print(f"Selected opponent: {opponent_type}")

    if opponent_type == "Bot":
        global opponent
        opponent = "Bot"
    elif opponent_type == "Player":
        opponent = "Player"

    root.title("Noughts and Crosses")
    root.geometry("270x370")

    destroy_opponent_choice_widgets(widgets)
    create_board()

# Function to display the opponent choice interface
def opponent_choice():
    global opponent_type

    root.geometry("250x100")
    root.title("Choose opponent")

    warning_text = ttk.Label(root, text="Please choose your opponent before playing:")
    warning_text.pack(pady=5)

    bot_button = ttk.Button(
        root,
        text="Player vs Bot",
        command=lambda: on_opponent_button_click("Bot", [bot_button, player_button, warning_text]),
    )
    bot_button.pack(pady=5)

    player_button = ttk.Button(
        root,
        text="Player vs Player",
        command=lambda: on_opponent_button_click("Player", [bot_button, player_button, warning_text]),
    )
    player_button.pack(pady=5)

# Function to handle button clicks on the game board
def on_button_click(row, column):
    global button_num
    button_num += 1  # Increment the button click count
    print(f"Button clicked at row {row}, column {column}")  # Print the button click coordinates to the console
    if opponent == "Bot" and button_num % 2 == 1:  # Check if the opponent is Bot and it's the player's turn
        if buttons[row][column]["text"] == "":  # Check if the button is empty
            buttons[row][column]["state"] = "disabled"  # Disable the button after it's marked
            buttons[row][column]["text"] = "X"  # Mark the button with "X"
            bot_move()  # Make the bot's move after the player's move
    elif opponent == "Player":  # Check if the button is not already marked and the opponent is Player:
        if buttons[row][column]["text"] == "" and button_num % 2 == 1:  # Check if the button is empty and it's Player X's turn
            buttons[row][column]["state"] = "disabled"  # Disable the button after it's marked
            buttons[row][column]["text"] = "X"  # Mark the button with "X"
        elif buttons[row][column]["text"] == "" and button_num % 2 == 0:  # Check if the button is empty and it's Player O's turn
            buttons[row][column]["state"] = "disabled"  # Disable the button after it's marked
            buttons[row][column]["text"] = "O"  # Mark the button with "O"
    if buttons[row][column]["text"] != "":  # Check if the button is not empty after the player's move
        buttons[row][column]["state"] = "disabled"  # Disable the button after it's marked
    win_check()  # Check for a win after the player's move

def reset_game(result):
    global button_num
    button_num = 0  # Reset the button click count
    if result == "Draw":
        score_check("Draw")  # Update the draw score
    for row in buttons:
        for button in row:
            button["text"] = ""  # Clear the text on all buttons to reset the game
            button["state"] = "normal"  # Enable all buttons to reset the game
            root.after(1000, lambda b=button: b.config(bg="SystemButtonFace"))

def revert_board(widgets, button_list):
    global button_num
    button_num = 0  # Reset the button click count
    for button in button_list:
        button.destroy()  # Destroy the game board buttons
    destroy_opponent_choice_widgets(widgets)  # Destroy the Restart and Revert buttons
    opponent_choice()  # Call the function to display the opponent choice window again

def score_check(result):
    global x_score, o_score, draws_score
    
    if result == "X":
        x_score += 1  # Increment Player X's score
        x_wins.config(text=f"X wins: {x_score}")  # Update the X wins label
    elif result == "O":
        o_score += 1  # Increment Player O's score
        o_wins.config(text=f"O wins: {o_score}")  # Update the O wins label
    elif result == "Draw":
        draws_score += 1  # Increment the draw score
        draws.config(text=f"Draws: {draws_score}")  # Update the Draws label
    else:
        print("Game reset")  # Print a message to the console when the game is reset without a win or draw

# Function to check for a win or a draw
def win_check():
    global win_combinations
    for combination in win_combinations:
        a, b, c = combination

        if (
            buttons[a[0]][a[1]]["text"]
            == buttons[b[0]][b[1]]["text"]
            == buttons[c[0]][c[1]]["text"]
            != ""
        ):
            winner = buttons[a[0]][a[1]]["text"]

            if winner == "X":
                color = "#ff9999"
            elif winner == "O":
                color = "lightblue"

            buttons[a[0]][a[1]].config(bg=color)
            buttons[b[0]][b[1]].config(bg=color)
            buttons[c[0]][c[1]].config(bg=color)

            score_check(winner)
            reset_game(winner)
            return

    if all(button["text"] != "" for row in buttons for button in row):
        reset_game("Draw")

opponent_choice()  # Call the function to display the opponent choice window

# Start the Tkinter main event loop to run the application
root.mainloop()