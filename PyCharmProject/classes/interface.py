from tkinter import *
from tkinter import filedialog

class Interface(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('CSM Instrument Text', '.txt'), ('All files', '')]
        dialog = filedialog.Open(self, filetypes = ftypes)
        filename = dialog.show()

        if filename != '':
            text = self.readFile(filename)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text