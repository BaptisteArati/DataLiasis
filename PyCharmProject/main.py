from tkinter import *
from classes.interface import Interface

def main():

    root = Tk()
    ex = Interface(root)
    root.geometry("250x650+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()