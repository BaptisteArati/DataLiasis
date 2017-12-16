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

        rowNumber = 0

        Label(self, text="Standard").grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isMaxLoad = IntVar()
        Checkbutton(self, text="Max Load", variable=isMaxLoad).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isLoadingRate = IntVar()
        Checkbutton(self, text="Loading Rate", variable=isLoadingRate).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isPause = IntVar()
        Checkbutton(self, text="Pause", variable=isPause).grid(row=rowNumber, sticky=W)
        rowNumber += 1

        Label(self, text="").grid(row=rowNumber, sticky=W)
        rowNumber += 1

        Label(self, text="UNHT S/N").grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isFnContact = IntVar()
        Checkbutton(self, text="Fn Contact", variable=isFnContact).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isApproachSpeed = IntVar()
        Checkbutton(self, text="Approach Speed", variable=isApproachSpeed).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isX = IntVar()
        Checkbutton(self, text="X Position", variable=isX).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isY = IntVar()
        Checkbutton(self, text="Y Position", variable=isY).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isZ = IntVar()
        Checkbutton(self, text="Z Position", variable=isZ).grid(row=rowNumber, sticky=W)
        rowNumber += 1

        Label(self, text="").grid(row=rowNumber, sticky=W)
        rowNumber += 1

        Label(self, text="Main Results").grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isHit = IntVar()
        Checkbutton(self, text="Hit", variable=isHit).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isEit = IntVar()
        Checkbutton(self, text="Eit", variable=isEit).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isE = IntVar()
        Checkbutton(self, text="E*", variable=isE).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isPoissonRatio = IntVar()
        Checkbutton(self, text="Poisson's Ratio", variable=isPoissonRatio).grid(row=rowNumber, sticky=W)
        rowNumber += 1

        Label(self, text="").grid(row=rowNumber, sticky=W)
        rowNumber += 1

        Label(self, text="Additional Results").grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isHvit = IntVar()
        Checkbutton(self, text="Hvit", variable=isHvit).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isCIT = IntVar()
        Checkbutton(self, text="Cit", variable=isCIT).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isWTot = IntVar()
        Checkbutton(self, text="Wtot", variable=isWTot).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isWelast = IntVar()
        Checkbutton(self, text="Welast", variable=isWelast).grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isWplast = IntVar()
        Checkbutton(self, text="Wplast", variable=isWplast).grid(row=rowNumber, sticky=W)
        rowNumber += 1

        Label(self, text="").grid(row=rowNumber, sticky=W)
        rowNumber += 1

        Label(self, text="Measured Value").grid(row=rowNumber, sticky=W)
        rowNumber += 1
        isRaw = IntVar()
        Checkbutton(self, text="Raw Data", variable=isRaw).grid(row=rowNumber, sticky=W)
        rowNumber += 1

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