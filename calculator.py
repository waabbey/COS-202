"""
Mathematical Calculator (MC) - A GUI-based Calculator Application

This module implements a fully functional graphical calculator using Python's tkinter library.
The calculator supports basic arithmetic operations (addition, subtraction, multiplication, division),
exponentiation (^), integer division (\), and modulo (%). It features a user-friendly interface with
a display entry box and organized button layout.

Author: waabbey
"""

from tkinter import *

# Create window
root = Tk()
root.title("MATHEMATICAL CALCULATOR (MC)")
root.geometry("380x500")
root.resizable(False, False)
root.configure(bg="lightblue")

# Entry box
expression = ""  # Stores the mathematical expression as a string

entry = Entry(root, font=("Arial", 20), bd=10, relief=RIDGE,
              justify="right")
entry.pack(fill=BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def press(value):
    """
    Handle button press events and update the expression.
    
    Converts user-friendly operator symbols (^ for exponentiation, \ for integer division)
    into Python's equivalent operators (** and //) for internal calculation, while
    displaying the user-friendly symbols in the entry box.
    
    Args:
        value: The button value pressed by the user (digit, operator, or special character)
    """
    global expression

    if value == "^":
        # Convert ^ to ** for Python exponentiation, but display ^ to user
        expression += "**"
        entry.delete(0, END)
        entry.insert(END, expression.replace("**", "^"))

    elif value == "\\":
        # Convert \ to // for Python integer division, but display \ to user
        expression += "//"
        entry.delete(0, END)
        entry.insert(END, expression.replace("**", "^").replace("//", "\\"))

    else:
        # For all other values, add to expression and update display
        expression += str(value)
        entry.delete(0, END)
        entry.insert(END,
                     expression.replace("**", "^").replace("//", "\\"))


def equal():
    """
    Evaluate the mathematical expression and display the result.
    
    Uses Python's eval() function to calculate the expression stored in the global
    expression variable. If an error occurs (e.g., invalid syntax or division by zero),
    displays "Error" in the entry box.
    """
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = result
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
        expression = ""


def clear():
    """
    Clear the current expression and reset the display.
    
    Empties the global expression variable and clears all text from the entry box,
    returning the calculator to its initial state.
    """
    global expression
    expression = ""
    entry.delete(0, END)


def off():
    """
    Close the calculator application.
    
    Destroys the root window, terminating the calculator program.
    """
    root.destroy()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '+', '='],
    ['^', '%', '\\', 'C'],
    ['OFF']
]

frame = Frame(root, bg="lightblue")
frame.pack()

# Create and configure buttons dynamically
for row in buttons:
    r = Frame(frame)
    r.pack(expand=True, fill=BOTH)

    for btn in row:
        if btn == "=":
            # Equals button triggers the equal() function
            Button(r, text=btn, font=("Arial", 16),
                   command=equal, width=6, height=2).pack(side=LEFT, expand=True, fill=BOTH)

        elif btn == "C":
            # Clear button triggers the clear() function
            Button(r, text=btn, font=("Arial", 16),
                   command=clear, width=6, height=2).pack(side=LEFT, expand=True, fill=BOTH)

        elif btn == "OFF":
            # OFF button closes the application (styled in red)
            Button(r, text=btn, font=("Arial", 16),
                   command=off, bg="red", fg="white",
                   height=2).pack(side=LEFT, expand=True, fill=BOTH)

        else:
            # All other buttons trigger the press() function with their value
            Button(r, text=btn, font=("Arial", 16),
                   command=lambda b=btn: press(b),
                   width=6, height=2).pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()
