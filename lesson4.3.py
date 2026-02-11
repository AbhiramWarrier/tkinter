from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfilename

window = Tk()
window.title("Codingal`s Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.rowconfigure(1, minisize=800, weigh=1)

def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(filetypes=[("Text files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return 
    txt_edit.delete(1.0 END)
    with open(filepath, "r") as input_files:
        text = input_files.read()