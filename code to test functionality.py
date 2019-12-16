import tkinter as tk
from tkinter import messagebox as mb
window = tk.Tk()
window.geometry('300x200')
window.resizable(False, False)
window.configure(bg='black')
font = ('arial', 14)


class Test:

    def __init__(self):
        self.label = tk.Label(window, text="let's get started", font=font)
        self.output = tk.Label(window, text='',  font=font)
        self.test = tk.Button(window, text='Add!', command=self.click)
        self.input1 = tk.Entry(window)
        self.input2 = tk.Entry(window)
        self.label.pack()
        self.input1.pack()
        self.input2.pack()
        self.test.pack()
        self.output.pack()

    def click(self):
        num1 = int(self.input1.get())
        num2 = int(self.input2.get())
        mb.showinfo('output',num1+num2)
        self.output.configure(text=(num1+num2))


obj=Test()
window.mainloop()
