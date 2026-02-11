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

**Test Type:** x  
**Input:**  
x

**Expected Outcome:** x  
**Actual Result:** x  
**Pass or Fail:** x  
**Debugging:**  