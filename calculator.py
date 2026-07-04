from tkinter import *

# Create window
root = Tk()
root.title("MATHEMATICAL CALCULATOR (MC)")
root.geometry("380x500")
root.resizable(False, False)
root.configure(bg="lightblue")

# Entry box
expression = ""

entry = Entry(root, font=("Arial", 20), bd=10, relief=RIDGE,
              justify="right")
entry.pack(fill=BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def press(value):
    global expression

    if value == "^":
        expression += "**"
        entry.delete(0, END)
        entry.insert(END, expression.replace("**", "^"))

    elif value == "\\":
        expression += "//"
        entry.delete(0, END)
        entry.insert(END, expression.replace("**", "^").replace("//", "\\"))

    else:
        expression += str(value)
        entry.delete(0, END)
        entry.insert(END,
                     expression.replace("**", "^").replace("//", "\\"))


def equal():
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
    global expression
    expression = ""
    entry.delete(0, END)


def off():
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

for row in buttons:
    r = Frame(frame)
    r.pack(expand=True, fill=BOTH)

    for btn in row:
        if btn == "=":
            Button(r, text=btn, font=("Arial", 16),
                   command=equal, width=6, height=2).pack(side=LEFT, expand=True, fill=BOTH)

        elif btn == "C":
            Button(r, text=btn, font=("Arial", 16),
                   command=clear, width=6, height=2).pack(side=LEFT, expand=True, fill=BOTH)

        elif btn == "OFF":
            Button(r, text=btn, font=("Arial", 16),
                   command=off, bg="red", fg="white",
                   height=2).pack(side=LEFT, expand=True, fill=BOTH)

        else:
            Button(r, text=btn, font=("Arial", 16),
                   command=lambda b=btn: press(b),
                   width=6, height=2).pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()
