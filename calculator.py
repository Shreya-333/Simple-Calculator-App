# ✅ Importing tkinter module for GUI
import tkinter as tk

# ✅ Function to handle button clicks
def click(event):
    text = event.widget.cget("text")  # Get the label on the clicked button

    if text == "=":
        try:
            result = eval(screen.get())  # Calculate the result
            screen.set(result)          # Show it on screen
        except Exception:
            screen.set("Error")         # Handle errors like divide by zero

    elif text == "C":
        screen.set("")  # Clear the screen

    else:
        screen.set(screen.get() + text)  # Add clicked button's value to screen

# ✅ Create main window
root = tk.Tk()
root.geometry("320x440")
root.title("Simple Calculator")

# ✅ Create entry box (screen)
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# ✅ Create button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "+", "."],
    ["="] 
]

# ✅ Create buttons and place them on the screen
for row in buttons:
    frame = tk.Frame(root)
    frame.pack()

    for item in row:
        b = tk.Button(frame, text=item, font="Arial 18", width=5, height=2)
        b.pack(side=tk.LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)  # Link button to the click function

# ✅ Keep the window running
root.mainloop()
