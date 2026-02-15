# Test cases for third sprint

**Test Type:** Boundary  
**Input:** 

    root = tk.Tk()
    root.title("Choose your opponent")  # Set the window title

**Expected Outcome:** Window only changes size when transforming  
**Actual Result:** User can alter window size at will  
**Pass or Fail:** Fail  
**Debugging:** Added  

    root.resizable(False, False)  # Disable window resizing

**Test Type:** Expected  
**Input:**  

    if buttons[row][column]["text"] == "":  # Check if the button is empty
            buttons[row][column]["state"] = "disabled"  # Disable the button after it's marked
            buttons[row][column]["text"] = "X"  # Mark the button with "X"

**Expected Outcome:** When button is filled it cannot be clicked, and when unfilled can be  
**Actual Result:** When button is filled it is permanently filled  
**Pass or Fail:** Fail  
**Debugging:** Added  

    for button in row:
            button["text"] = ""  # Clear the text on all buttons to reset the game
            button["state"] = "normal"  # Enable all buttons to reset the game

**Test Type:** Expected  
**Input:**  

    revert_button = ttk.Button(root, text="Back", 
    command=lambda: revert_board([
    restart_button, revert_button, x_wins, o_wins, draws], button_list))  # Create Revert Button

**Expected Outcome:** Removes all widgets and reverts window  
**Actual Result:** Creates error, with how to play button not removed  
**Pass or Fail:** Fail  
**Debugging:** Added 'how_to_play_button' to list  

**Test Type:** Expected  
**Input:**  

    buttons = [[Button(row, column) for column in range(3)] for row in range(3)]  # Create a 3x3 grid of buttons  
    revert_button = ttk.Button(root, text="Back", 
    command=lambda: revert_board([
    restart_button, revert_button, x_wins, o_wins, draws, how_to_play_button], buttons))

**Expected Outcome:** Buttons are deleted when revert button is clicked  
**Actual Result:** Error  
**Pass or Fail:** Fail  
**Debugging:** Flattened list so it can be read  

    buttons = [[Button(row, column) for column in range(3)] for row in range(3)]  # Create a 3x3 grid of buttons
    button_list = [button for row in buttons for button in row]    
    revert_button = ttk.Button(root, text="Back", 
    command=lambda: revert_board([
    restart_button, revert_button, x_wins, o_wins, draws, how_to_play_button], button_list))

**Test Type:** Boundary  
**Input:**  

    def bot_move():
    empty_buttons = [(r, c) for r in range(3) 
                     for c in range(3) if buttons[r][c]["text"] == ""]  # Get a list of empty buttons
    empty_buttons_dict = {(r, c): buttons[r][c]["text"] for r in range(3) 
                          for c in range(3) if buttons[r][c]["text"] == ""}  # Create a dictionary of empty buttons with their coordinates as keys and their text as values
    row = random.randint(0, 2)  # Generate a random row index
    column = random.randint(0, 2)  # Generate a random column index
    if empty_buttons:  # Check if there are any empty buttons left
        if empty_buttons_dict.get((0, column)) == "X" and empty_buttons_dict.get((1, column)) == "X" and empty_buttons_dict.get((2, column)) == "":
            row, column = (2, column)  

**Expected Outcome:** Bot blocks player and wins when possible  
**Actual Result:** Bot fails to block and always acts randomly  
**Pass or Fail:** Fail  
**Debugging:** Changed method in which code checks for winner  
    
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

**Test Type:** x  
**Input:**  
x

**Expected Outcome:** x  
**Actual Result:** x  
**Pass or Fail:** x  
**Debugging:**  