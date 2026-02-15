# Test cases for second sprint

**Test Type:** Boundary  
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

**Expected Outcome:** When button is clicked, it is marked and cannot be changed until game ends  
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

**Test Type:** Expected  
**Input:**  
    
    # Change the background color of the winning buttons
    buttons[0][0]["bg"] = "lightgreen"
    buttons[0][1]["bg"] = "lightgreen"
    buttons[0][2]["bg"] = "lightgreen"

**Expected Outcome:** Winning buttons background turns green  
**Actual Result:** Winning buttons background turns green  
**Pass or Fail:** Pass  

**Test Type:** Expected  
**Input:**  

    x_wins = tk.Label(root, text=f"X wins: {x_score}")  # Create a label to display Player X's wins
    x_wins.grid(row=4, column=0)  # Place the label in the grid

    o_wins = tk.Label(root, text=f"O wins: {o_score}")  # Create a label to display Player O's wins
    o_wins.grid(row=4, column=1)  # Place the label in the grid

    draws = tk.Label(root, text=f"Draws: {draws_score}")  # Create a label to display the number of draws
    draws.grid(row=4, column=2)  # Place the label in the grid

**Expected Outcome:** Score labels update every time a player wins or draws  
**Actual Result:** Score variables update but not labels  
**Pass or Fail:** Fail  
**Debugging:** Added updating code  

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

**Test Type:** Expected  
**Input:**  
    
    # Function to destroy the opponent choice widgets
    def destroy_opponent_choice_widgets(widget_1, widget_2, widget_3):
        widget_1.destroy()  # Destroy the first widget
        widget_2.destroy()  # Destroy the second widget
        widget_3.destroy()  # Destroy the third widget

**Expected Outcome:** Widgets are destroyed  
**Actual Result:** Widgets are destroyed  
**Pass or Fail:** Pass  
**Debugging:** Even though it was a pass, code was refined to allow variable amount of widgets and be more concise  
    
    # Function to destroy the opponent choice widgets
        def destroy_opponent_choice_widgets(widgets):
            for widget in widgets:
                widget.destroy()  # Destroy each widget in the list