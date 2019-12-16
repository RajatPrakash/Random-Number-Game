import random as r
import tkinter as tk
from tkinter import messagebox as mb

guess = 0
window = tk.Tk()
window.geometry('200x300')


class Guess:
    def __init__(self, master):
        top_frame = tk.Frame(master)
        top_frame.pack()
        bottom_frame = tk.Frame(master)
        bottom_frame.pack()
        self.num = tk.Entry(top_frame)
        self.num.configure(state='disabled', bg='white')
        self.start_button = tk.Button(top_frame, text='start  ', bg='green', command=self.show)
        self.guess_button = tk.Button(top_frame, text='Guess', bg='red', command=lambda: (self.rand(), self.dis()))
        self.guess_button.grid(row=0, column=3)
        self.label = tk.Label(top_frame
                              , text='Random number is:')
        self.label.grid(row=0, column=7)
        self.start_button.grid(row=2, column=3)
        self.num.grid(row=7, column=15)

    def show(self):
        self.num.configure(state='normal', bg='green')

    def dis(self):
        self.guess_button.configure(state='disabled', bg='silver')

    def rand(self):
        self.guess = r.randint(0, 10)
        self.label.config(text=self.guess)


rand_object = Guess(window)

window.mainloop()
