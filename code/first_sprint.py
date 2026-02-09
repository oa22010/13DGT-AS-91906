# Import necessary modules
import tkinter as tk
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Noughts and Crosses")  # Set the window title
root.geometry("270x340")    # Set the window size

def opponent_choice():
    root.update_idletasks()  # Update the window to get accurate dimensions
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()

    opponent_window = tk.Toplevel(root)  # Create a new window for the opponents name input
    opponent_window.title("Choose opponent")  # Set the title

    bot_button = ttk.Button(opponent_window, text="Player vs Bot")  # Create Bot Button
    bot_button.pack(pady=10)  # Place Bot Button in the window

    player_button = ttk.Button(opponent_window, text="Player vs Player")  # Create Player Button
    player_button.pack(pady=10)  # Place Player Button in the window

    # Position the Toplevel to the right of the root window
    toplevel_x = root_x + root_width
    toplevel_y = root_y # Align the top edges
    opponent_window.geometry(f"+{toplevel_x}+{toplevel_y}")  # Set the position of the Toplevel window

class Button(tk.Button):
    def __init__(self, row, column):
        super().__init__(root, text="", width=10, height=5)  # Initialize the button
        self.grid(row=row, column=column, padx=5, pady=5)  # Place the button in the grid
    
buttons = [[Button(row, column) for column in range(3)] for row in range(3)]  # Create a 3x3 grid of buttons

restart_button = ttk.Button(root, text="Restart")  # Create Restart Button
restart_button.grid(row=3, column=0, columnspan=3, pady=10)  # Place Restart Button in the grid

opponent_choice()  # Call the function to display the opponent choice window

# Start the Tkinter main event loop to run the application
root.mainloop()