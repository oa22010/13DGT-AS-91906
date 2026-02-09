# Import necessary modules
import tkinter as tk
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Choose your opponent")  # Set the window title

def destroy_opponent_choice_widgets(bot_button, player_button, label):
    bot_button.destroy()  # Destroy the Bot Button
    player_button.destroy()  # Destroy the Player Button
    label.destroy()  # Destroy the instruction label

def create_board():
    #Create the noughts and crosses board
    global buttons, restart_button
    
    class Button(tk.Button):
        def __init__(self, row, column):
            super().__init__(root, text="", width=10, height=5)  # Initialize the button
            self.grid(row=row, column=column, padx=5, pady=5)  # Place the button in the grid
    
    buttons = [[Button(row, column) for column in range(3)] for row in range(3)]  # Create a 3x3 grid of buttons
    
    restart_button = ttk.Button(root, text="Restart")  # Create Restart Button
    restart_button.grid(row=3, column=0, columnspan=3, pady=10)  # Place Restart Button in the grid

def on_opponent_button_click(opponent_type, bot_button, player_button, warning_label):
    print(f"Selected opponent: {opponent_type}")  # Print the selected opponent type to the console
    
    root.title("Noughts and Crosses")  # Set the window title
    root.geometry("270x340") # Set the window size to dimensions needed for the game interface
    
    destroy_opponent_choice_widgets(bot_button, player_button, warning_label)  # Destroy the opponent choice buttons
    create_board()  # Create the game board

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