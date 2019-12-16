import random as r
import tkinter as tk
import sys
from tkinter import messagebox

root = tk.Tk()
root.title('Random Number Game')
root.geometry('300x200')
root.resizable(False, False)
font = ('Arial', 15)
root.counter = 0


class Dain:
    def __init__(self):
        top = tk.Frame(root, width=300, height=200, bg="blue")
        top.pack(side='top', expand='yes', fill='both')
        bottom = tk.Frame(root, width=300, height=200, bg="green")
        bottom.pack(side='bottom', expand='yes', fill='both')
        self.generate_label = tk.Label(top, text='', bg="blue")
        self.generate_button = tk.Button(top, text='Generate', font=font,
                                         command=lambda: (self.random(), self.disable()))
        self.generate_button.pack(side='top')
        self.generate_label.pack()
        self.user_text = tk.Entry(bottom)
        self.user_button = tk.Button(bottom, text='Guess', bg="green",
                                     command=lambda: (self.guess(), self.count()))
        self.user_label = tk.Label(bottom, text='3 chances left ', bg="red")
        self.user_text.pack(side='top')
        self.user_label.pack(side='top')
        self.user_button.pack()

    def guess(self):
        num = int(self.user_text.get())
        if num == self.rand:
            messagebox.showinfo('Output', 'You win')
            sys.exit()
        else:
            messagebox.showinfo('Output', 'Try again')

    def count(self):
        root.counter += 1
        self.user_label.configure(text=3 - root.counter)
        if root.counter == 3:
            self.user_label.configure(text='Game Over ! You lost')
            self.show()

    def random(self):
        self.rand = r.randint(0, 10)
        self.generate_label.configure(text='Number is **', font=font)

    def show(self):
        self.generate_label.configure(text=self.rand, font=font)

    def disable(self):
        self.generate_button.configure(state='disable')


obj = Dain()
root.mainloop()
