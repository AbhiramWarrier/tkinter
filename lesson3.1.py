from tkinter import *

window = Tk()

def handle_keypress(event):
    """Print the characther associated to the key pressed"""
    print(event.char)

window.bind("<Key>", handle_keypress)

window.mainloop()