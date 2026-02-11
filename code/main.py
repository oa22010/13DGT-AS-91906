# Import necessary modules
import tkinter as tk
import random
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Choose your opponent")  # Set the window title

# Initialize a global variable to count button clicks
global button_num
global x_score, o_score, draws_score
global win_combinations
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
button_num = 0

def bot_move():
    empty_buttons = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]["text"] == ""]  # Get a list of empty buttons
    if empty_buttons:  # Check if there are any empty buttons left
        global win_combinations
        if empty_buttons == win_combinations:  # Check if the bot can win in the next move/basic blocking strategy
            row, column = random.choice(empty_buttons)  # Randomly select an empty button
            buttons[row][column]["text"] = "O"  # Mark the selected button with "O"
            global button_num
            button_num += 1  # Increment the button click count after the bot's move
        else:
            row, column = random.choice(empty_buttons)  # Randomly select an empty button
            buttons[row][column]["text"] = "O"  # Mark the selected button with "O"
            button_num += 1  # Increment the button click count after the bot's move
        win_check()  # Check for a win after the bot's move

# Create the noughts and crosses board
def create_board():
    global buttons, restart_button
    
    class Button(tk.Button):
        def __init__(self, row, column):
            super().__init__(root, text="", width=10, height=5, command=lambda r=row, c=column: on_button_click(r, c))  # Initialize the button
            self.grid(row=row, column=column, padx=5, pady=5)  # Place the button in the grid
    
    buttons = [[Button(row, column) for column in range(3)] for row in range(3)]  # Create a 3x3 grid of buttons
    
    restart_button = ttk.Button(root, text="Restart", command=on_restart_button_click)  # Create Restart Button
    restart_button.grid(row=3, column=0, columnspan=3, pady=10)  # Place Restart Button in the grid

    score_check("")  # Initialize the score display

# Function to destroy the opponent choice widgets
def destroy_opponent_choice_widgets(widgets):
    for widget in widgets:
        widget.destroy()  # Destroy each widget in the list

# Function to handle Restart Button clicks
def on_restart_button_click():
    print("Restart button clicked")# Print a message to the console when the Restart Button is clicked
    reset_game("")  # Call the reset_game function to reset the game when the Restart Button is clicked
    
    # Reset the scores when the Restart Button is clicked
    global x_score, o_score, draws_score
    x_score = 0
    o_score = 0
    draws_score = 0
    score_check("")  # Update the score display after resetting the scores

# Function to handle opponent button clicks
def on_opponent_button_click(opponent_type, widgets):
    print(f"Selected opponent: {opponent_type}")  # Print the selected opponent type to the console
    
    if opponent_type == "Bot":
        global opponent
        opponent = "Bot"  # Set the opponent variable to "Bot"
    elif opponent_type == "Player":
        opponent = "Player"  # Set the opponent variable to "Player"

    root.title("Noughts and Crosses")  # Set the window title
    root.geometry("270x370") # Set the window size to dimensions needed for the game interface
    
    destroy_opponent_choice_widgets(widgets)  # Destroy the opponent choice buttons
    create_board()  # Create the game board

# Function to display the opponent choice interface
def opponent_choice():
    root.title("Choose opponent")  # Set the title

    warning_text = ttk.Label(root, text="Please choose your opponent before playing:")  # Create a label with instructions
    warning_text.pack(pady=5)  # Place the label in the window with some

    bot_button = ttk.Button(root, text="Player vs Bot", command=lambda: on_opponent_button_click("Bot", [bot_button, player_button, warning_text]))  # Create Bot Button
    bot_button.pack(pady=5)  # Place Bot Button in the window

    player_button = ttk.Button(root, text="Player vs Player", command=lambda: on_opponent_button_click("Player", [bot_button, player_button, warning_text]))  # Create Player Button
    player_button.pack(pady=5)  # Place Player Button in the window

# Function to handle button clicks on the game board
def on_button_click(row, column):
    global button_num
    button_num += 1  # Increment the button click count
    print(f"Button clicked at row {row}, column {column}")  # Print the button click coordinates to the console
    if opponent == "Bot" and button_num % 2 == 1:  # Check if the opponent is Bot and it's the player's turn
        if buttons[row][column]["text"] == "":  # Check if the button is empty
            buttons[row][column]["text"] = "X"  # Mark the button with "X"
            bot_move()  # Make the bot's move after the player's move
    elif opponent == "Player":  # Check if the button is not already marked and the opponent is Player:
        if buttons[row][column]["text"] == "" and button_num % 2 == 1:  # Check if the button is empty and it's Player X's turn
            buttons[row][column]["text"] = "X"  # Mark the button with "X"
        elif buttons[row][column]["text"] == "" and button_num % 2 == 0:  # Check if the button is empty and it's Player O's turn
            buttons[row][column]["text"] = "O"  # Mark the button with "O"
    win_check()  # Check for a win after the player's move

def reset_game(result):
    global button_num
    button_num = 0  # Reset the button click count
    for row in buttons:
        for button in row:
            button["text"] = ""  # Clear the text on all buttons to reset the game
            root.after(1000, lambda b=button: b.config(bg="SystemButtonFace"))  # Reset the background color of the buttons after a short delay

def score_check(result):
    global x_score, o_score, draws_score

    x_wins = tk.Label(root, text=f"X wins: {x_score}")  # Create a label to display Player X's wins
    x_wins.grid(row=4, column=0)  # Place the label in the grid

    o_wins = tk.Label(root, text=f"O wins: {o_score}")  # Create a label to display Player O's wins
    o_wins.grid(row=4, column=1)  # Place the label in the grid

    draws = tk.Label(root, text=f"Draws: {draws_score}")  # Create a label to display the number of draws
    draws.grid(row=4, column=2)  # Place the label in the grid
    
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
        if buttons[combination[0][0]][combination[0][1]]["text"] == buttons[combination[1][0]][combination[1][1]]["text"] == buttons[combination[2][0]][combination[2][1]]["text"] != "":
            winner = buttons[combination[0][0]][combination[0][1]]["text"]  # Get the winner's symbol
            buttons[combination[0][0]][combination[0][1]].config(bg="lightgreen")  # Highlight the winning combination
            buttons[combination[1][0]][combination[1][1]].config(bg="lightgreen")  # Highlight the winning combination
            buttons[combination[2][0]][combination[2][1]].config(bg="lightgreen")  # Highlight the winning combination
            score_check(winner)  # Update the scores based on the winner
            reset_game(winner)  # Reset the game after a win
            return  # Exit the function after a win is detected
        elif all(button["text"] != "" for row in buttons for button in row):
            reset_game("Draw")  # Reset the game after a draw
        else:
            pass

opponent_choice()  # Call the function to display the opponent choice window

# Start the Tkinter main event loop to run the application
root.mainloop()