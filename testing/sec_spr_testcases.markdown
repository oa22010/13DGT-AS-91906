

**Input:**  
""Function to handle button clicks on the game board""  
def on_button_click(row, column):  
    global button_num  
    button_num += 1  # Increment the button click count  
    print(f"Button clicked at row {row}, column {column}")  # Print the button click coordinates to the console     
    if button_num % 2:  
        turn = "X"  # Set turn to "X" for odd clicks  
    else:  
        turn = "O"  # Set turn to "O" for even clicks  

**Expected Outcome:** When button is clicked, it is marked and cannot b changed until game ends  
**Actual Result:** Button can be changed every click  
**Pass or Fail:** Fail  
**Debugging:** New condition added to check if button is already marked  
""Function to handle button clicks on the game board""  
def on_button_click(row, column):  
    global button_num  
    button_num += 1  # Increment the button click count  
    print(f"Button clicked at row {row}, column {column}")  # Print the button click coordinates to the console  
    if buttons[row][column]["text"] == "":  # Check if the button is not already marked     
        if button_num % 2:  
            turn = "X"  # Set turn to "X" for odd clicks  
        else:  
            turn = "O"  # Set turn to "O" for even clicks  
    else:  
        print("Button already marked.")  # Print a message to the console if the button is already marked
        return  # Exit the function if the button is already marked  