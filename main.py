import tkinter as tk

expression = ""

def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        result = eval(expression)
        expression = str(result)
        display_var.set(expression)
    except:
        expression = ""
        display_var.set("Error")

root = tk.Tk()
root.title("My Calculator")
root.geometry("360x600")
root.resizable(False, False)

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 28),
    justify="right"
)
display.pack(
    padx=15,
    pady=20,
    ipady=15,
    fill="x"
)

buttons = [
    ["AC", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:
        if button == "":
            continue

        if button == "AC":
            command = clear
        elif button == "⌫":
            command = backspace
        elif button == "=":
            command = calculate
        else:
            command = lambda x=button: press(x)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 20),
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=3,
            pady=3
        )

root.mainloop()
