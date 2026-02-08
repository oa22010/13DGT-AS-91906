# Import necessary modules
import tkinter as tk
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Noughts and Crosses")  # Set the window title
root.geometry("270x340")    # Set the window size

class Button(tk.Button):
    def __init__(self, row, column):
        super().__init__(root, text="", width=10, height=5)  # Initialize the button
        self.grid(row=row, column=column, padx=5, pady=5)  # Place the button in the grid
    
buttons = [[Button(row, column) for column in range(3)] for row in range(3)]  # Create a 3x3 grid of buttons

restart_button = ttk.Button(root, text="Restart")  # Create Restart Button
restart_button.grid(row=3, column=0, columnspan=3, pady=10)  # Place Restart Button in the grid

# Start the Tkinter main event loop to run the application
root.mainloop()