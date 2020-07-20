from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text='Ola mundo')
        self.msg.pack()
        self.pack()
app = Application()
mainloop()