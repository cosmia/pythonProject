#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, BOTH
from ttk import Style


class Ramka(Frame):
    def __init__(self, parent):
	'''tworzy obiekt Example dziedziczacy po Frame, rodzicem ma byc parent'''
	#ramka znajduje sie w oknie...
	#wywolanie konstruktora rodzica - rodzicem jest parent
	Frame.__init__(self, parent)
	self.parent = parent
	#ustawiamy tytul okna
	self.parent.title("Angela Czubak, algorytm Aho-Corasick")
	#niech wypelnia w obu kierunkach, gdy okno rosnie - FILL=BOTH
	#expand = True - niech zmienia poszerza ramke, gdy okno rosnie
	self.pack(fill=BOTH, expand=True)
	#ustawiamy styl
	self.style = Style()
	self.style.theme_use("classic")

def main():
    root = Tk() #glowne okno aplikacji
    root.geometry("600x400+100+100")#wymiary=600x400, pozycja = (100,100)
    app = Ramka(root)
    root.mainloop()

if __name__ == '__main__':
    main()