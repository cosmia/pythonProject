#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, Text, BOTH, W, N, E, S, DISABLED
from ttk import Style, Button, Label


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
	self.rowconfigure(5, weight=1)
	label0 = Label(self, text="tekst do przeszukania:") #pierwsza etykieta
	label0.grid(row=0,column=0, padx=4)
	tekst = Text(self, bg="white") #glowne pole tekstowe
	tekst.grid(row=1, column=0, columnspan=3, rowspan=5, padx=4, sticky=E+W+N+S)
	saveAsButton = Button(self, text="zapisz jako...") #klawisz zapisywania
	saveAsButton.grid(row=6, column=0, sticky=W)
	openButton = Button(self, text="otwórz...") #klawisz otwierania
	openButton.grid(row=6, column=1, sticky=W)
	label1 = Label(self, text="Aktualne slowa:") #etykieta z boku
	label1.grid(column=3, row=0, padx=2, sticky=N+W)
	pole = Text(self, bg="white", height=10, width=35) #pole ze slowami, wysokosc
	pole.grid(column=3, row=1, padx=2, columnspan=2)		   #w liczbie znakow
	pole.config(state=DISABLED)
	clear = Button(self, text="wyczyść listę słów")
	clear.grid(column=4, row=2, sticky=W)
	search = Button(self, text="wyszukaj")
	search.grid(column=3, row=2, sticky=W)

def main():
    root = Tk() #glowne okno aplikacji
    root.geometry("600x400+100+100")#wymiary=600x400, pozycja = (100,100)
    app = Ramka(root)
    root.mainloop()

if __name__ == '__main__':
    main()