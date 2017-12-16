from tkinter import *
from classes.interface import Interface

def main():

    root = Tk()
    ex = Interface(root)
    root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()