# Test cases for first sprint

**Test Type:** Expected  
**Input:**  
def opponent_choice():  
root.update_idletasks()  # Update the window to get accurate dimensions  
root_x = root.winfo_x()  
root_y = root.winfo_y()  
root_width = root.winfo_width()  

""Position the Toplevel to the right of the root window""  
toplevel_x = root_x + root_width  
toplevel_y = root_y # Align the top edges  
opponent_window.geometry(f"+{toplevel_x}+{toplevel_y}")  # Set the position of the Toplevel window

**Expected Outcome:** Popup window appears in front of main window  
**Actual Result:** Popup window appears behind main window  
**Pass or Fail:** Fail  
**Debugging:** Window now starts intially as popup design then transforms into main window.
  
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

**Test Type:** Expected  
**Input:**  
global button_num  
button_num = 0  # Initialize a global variable to count button clicks

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

""Function to handle opponent button clicks""  
def on_opponent_button_click(opponent_type, bot_button, player_button, warning_label):  
    print(f"Selected opponent: {opponent_type}")  # Print the selected opponent type to the console
    
if opponent_type == "Bot":  
        global opponent  
        opponent = "Bot"  # Set the opponent variable to "Bot"  
    elif opponent_type == "Player":  
        opponent = "Player"  # Set the opponent variable to "Player"

**Expected Outcome:** When a button is clicked, text turns into either X or O depending on whose turn it is  
**Actual Result:** When a button is clicked, text turns into either X or O depending on whose turn it is  
**Pass or Fail:** Pass  

**Test Type:** Expected  
**Input:**  
def on_restart_button_click():  
    print("Restart button clicked")  # Print a message to the console when the Restart Button is clicked  
    reset_game()  # Call the reset_game function to reset the game when the Restart Button is clicked

**Expected Outcome:** When button is clicked game resets  
**Actual Result:** When button is clicked game resets  
**Pass or Fail:** Pass  

**Test Type:** Boundary  
**Input:**  
if all(button["text"] != "" for row in buttons for button in row):
        print("It's a draw!")  # Check for a draw if all buttons are marked
        reset_game()  # Reset the game after a draw  

**Expected Outcome:** When board is full, a draw is announced and the game resets  
**Actual Outcome:** When board is full, a draw is announced and the game resets  
**Pass or Fail:** Pass