#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, Text, BOTH, W, N, E, S
from ttk import Style, Button


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
	self.initUI()
    def initUI(self):
	'''zajmuje sie rozkladem poszczegolnych elementow'''
	self.columnconfigure(2, weight=1)
	self.rowconfigure(2, weight=1)
	tekst = Text(self, bg="white")
	tekst.grid(row=0, column=0, columnspan=3, rowspan=4, padx=4, sticky=E+W+N+S)
	saveAsButton = Button(self, text="zapisz jako...")
	saveAsButton.grid(row=4, column=0)
	openButton = Button(self, text="otworz...")
	openButton.grid(row=4, column=1)

def main():
    root = Tk() #glowne okno aplikacji
    root.geometry("600x400+100+100")#wymiary=600x400, pozycja = (100,100)
    app = Ramka(root)
    root.mainloop()

if __name__ == '__main__':
    main()