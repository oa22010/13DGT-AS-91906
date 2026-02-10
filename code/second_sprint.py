# Import necessary modules
import tkinter as tk
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Choose your opponent")  # Set the window title

# Initialize a global variable to count button clicks
global button_num
button_num = 0

# Function to destroy the opponent choice widgets
def destroy_opponent_choice_widgets(widget_1, widget_2, widget_3):
    widget_1.destroy()  # Destroy the first widget
    widget_2.destroy()  # Destroy the second widget
    widget_3.destroy()  # Destroy the third widget

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

# Function to handle Restart Button clicks
def on_restart_button_click():
    print("Restart button clicked")# Print a message to the console when the Restart Button is clicked
    reset_game()  # Call the reset_game function to reset the game when the Restart Button is clicked

# Function to handle button clicks on the game board
def on_button_click(row, column):
    global button_num
    button_num += 1  # Increment the button click count
    print(f"Button clicked at row {row}, column {column}")  # Print the button click coordinates to the console
    if button_num % 2:
        turn = "X"  # Set turn to "X" for odd clicks
    else:
        turn = "O"  # Set turn to "O" for even clicks
    if opponent == "Player":  # Check if the button is not already marked and the opponent is Player
        buttons[row][column]["text"] = turn  # Mark the button when clicked
        win_check()  # Check for a win after the button is clicked

# Function to check for a win or a draw
def win_check():
    if buttons[0][0]["text"] == buttons[0][1]["text"] == buttons[0][2]["text"] != "":
        print(f"{buttons[0][0]['text']} wins!")  # Check for a win in the first row
        reset_game()  # Reset the game after a win
        # Change the background color of the winning buttons
        buttons[0][0]["bg"] = "lightgreen"
        buttons[0][1]["bg"] = "lightgreen"
        buttons[0][2]["bg"] = "lightgreen"
    elif buttons[1][0]["text"] == buttons[1][1]["text"] == buttons[1][2]["text"] != "":
        print(f"{buttons[1][0]['text']} wins!")  # Check for a win in the second row
        reset_game()  # Reset the game after a win
        # Change the background color of the winning buttons
        buttons[1][0]["bg"] = "lightgreen"
        buttons[1][1]["bg"] = "lightgreen"
        buttons[1][2]["bg"] = "lightgreen"
    elif buttons[2][0]["text"] == buttons[2][1]["text"] == buttons[2][2]["text"] != "":
        print(f"{buttons[2][0]['text']} wins!")  # Check for a win in the third row
        reset_game()  # Reset the game after a win
        # Change the background color of the winning buttons
        buttons[2][0]["bg"] = "lightgreen"
        buttons[2][1]["bg"] = "lightgreen"
        buttons[2][2]["bg"] = "lightgreen"
    elif buttons[0][0]["text"] == buttons[1][0]["text"] == buttons[2][0]["text"] != "":
        print(f"{buttons[0][0]['text']} wins!")  # Check for a win in the first column
        reset_game()  # Reset the game after a win
        # Change the background color of the winning buttons
        buttons[0][0]["bg"] = "lightgreen"
        buttons[1][0]["bg"] = "lightgreen"
        buttons[2][0]["bg"] = "lightgreen"
    elif buttons[0][1]["text"] == buttons[1][1]["text"] == buttons[2][1]["text"] != "":
        print(f"{buttons[0][1]['text']} wins!")  # Check for a win in the second column
        reset_game()  # Reset the game after a win
         # Change the background color of the winning buttons
        buttons[0][1]["bg"] = "lightgreen"
        buttons[1][1]["bg"] = "lightgreen"
        buttons[2][1]["bg"] = "lightgreen"
    elif buttons[0][2]["text"] == buttons[1][2]["text"] == buttons[2][2]["text"] != "":
        print(f"{buttons[0][2]['text']} wins!")  # Check for a win in the third column
        reset_game()  # Reset the game after a win
        # Change the background color of the winning buttons
        buttons[0][2]["bg"] = "lightgreen"
        buttons[1][2]["bg"] = "lightgreen"
        buttons[2][2]["bg"] = "lightgreen"
    elif buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        print(f"{buttons[0][0]['text']} wins!")  # Check for a win in the top-left to bottom-right diagonal
        reset_game()  # Reset the game after a win
        # Change the background color of the winning buttons
        buttons[0][0]["bg"] = "lightgreen"
        buttons[1][1]["bg"] = "lightgreen"
        buttons[2][2]["bg"] = "lightgreen"
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        print(f"{buttons[0][2]['text']} wins!")  # Check for a win in the top-right to bottom-left diagonal
        reset_game()  # Reset the game after a win
        # Change the background color of the winning buttons
        buttons[0][2]["bg"] = "lightgreen"
        buttons[1][1]["bg"] = "lightgreen"
        buttons[2][0]["bg"] = "lightgreen"
    
    if all(button["text"] != "" for row in buttons for button in row):
        print("It's a draw!")  # Check for a draw if all buttons are marked
        reset_game()  # Reset the game after a draw

def reset_game():
    global button_num
    button_num = 0  # Reset the button click count
    for row in buttons:
        for button in row:
            button["text"] = ""  # Clear the text on all buttons to reset the game
            root.after(1000, lambda b=button: b.config(bg="SystemButtonFace"))  # Reset the background color of the buttons after a short delay

# Function to handle opponent button clicks
def on_opponent_button_click(opponent_type, bot_button, player_button, warning_label):
    print(f"Selected opponent: {opponent_type}")  # Print the selected opponent type to the console
    
    if opponent_type == "Bot":
        global opponent
        opponent = "Bot"  # Set the opponent variable to "Bot"
    elif opponent_type == "Player":
        opponent = "Player"  # Set the opponent variable to "Player"

    root.title("Noughts and Crosses")  # Set the window title
    root.geometry("270x340") # Set the window size to dimensions needed for the game interface
    
    destroy_opponent_choice_widgets(bot_button, player_button, warning_label)  # Destroy the opponent choice buttons
    create_board()  # Create the game board

# Function to display the opponent choice interface
def opponent_choice():
    root.title("Choose opponent")  # Set the title

    warning_text = ttk.Label(root, text="Please choose your opponent before playing:")  # Create a label with instructions
    warning_text.pack(pady=5)  # Place the label in the window with some

    bot_button = ttk.Button(root, text="Player vs Bot", command=lambda: on_opponent_button_click("Bot", bot_button, player_button, warning_text))  # Create Bot Button
    bot_button.pack(pady=5)  # Place Bot Button in the window

    player_button = ttk.Button(root, text="Player vs Player", command=lambda: on_opponent_button_click("Player", bot_button, player_button, warning_text))  # Create Player Button
    player_button.pack(pady=5)  # Place Player Button in the window

opponent_choice()  # Call the function to display the opponent choice window

# Start the Tkinter main event loop to run the application
root.mainloop()