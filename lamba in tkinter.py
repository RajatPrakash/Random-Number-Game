import sys
import tkinter as tk
from tkinter import messagebox as mg

window = tk.Tk()
window.geometry('200x100')
design = ('Arial', 14)

window.counter = 0


# this function is for counting number of times the button is clicked


def clicked():
    window.counter += 1
    if window.counter == 4:
        sys.exit()
    else:
        print(window.counter)


class Test:
    def __init__(self):
        self.frame = tk.Frame(window, bg='black')
        self.frame.grid()
        self.user = tk.Entry(self.frame)
        self.user.focus()
        self.result_label = tk.Label(self.frame, text='')
        self.result_label.grid(row=10, column=12)
        self.user.grid(row=10, column=10)
        #  self.text = input('enter the text')
        self.button = tk.Button(self.frame, text='click me', bg='red', font=design,
                                command=lambda: self.message())
        self.button.grid(row=2, column=2)

    #  this method is for printing what is in text box

    def message(self):
        result = self.user.get()
        self.result_label.configure(text=result)


obj = Test()
window.mainloop()
