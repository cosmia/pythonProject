#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, Text, BOTH, W, N, E, S, DISABLED, NORMAL
from ttk import Style, Button, Label, Entry, Scrollbar
from ScrolledText import ScrolledText
from Tkconstants import END, FIRST
import tkMessageBox as MesBox

class Ramka(Frame):
    def __init__(self, parent):
	'''tworzy obiekt Example dziedziczacy po Frame, rodzicem ma byc parent'''
	self.listaSlow = [] #lista slow do wyszukania
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
	#co robic przy zamykaniu okna
	self.parent.protocol("WM_DELETE_WINDOW", self.question)
	self.initUI()
    def initUI(self):
	'''zajmuje sie rozkladem poszczegolnych elementow'''
	self.columnconfigure(3, weight=1)
	self.rowconfigure(6, weight=1)
	self.drawMain()
	self.drawList()
	self.drawInput()
    def drawMain(self):
	'''rysuje glowne pole tekstowe, etykiete tego pola, klawisze zapisz i otworz'''
	self.label0 = Label(self, text="Tekst do przeszukania:") #pierwsza etykieta
	self.label0.grid(row=0,column=0, padx=4, columnspan=2, sticky=W)
	self.tekst = ScrolledText(self, bg="white") #glowne pole tekstowe
	self.tekst.grid(row=1, column=0, columnspan=4, rowspan=6, padx=4, sticky=E+W+N+S)
	self.saveAsButton = Button(self, text="zapisz jako...") #klawisz zapisywania
	self.saveAsButton.grid(row=7, column=0, sticky=W)
	self.openButton = Button(self, text="otwórz...") #klawisz otwierania
	self.openButton.grid(row=7, column=1, sticky=W)
	self.clearText = Button(self, text="wyczyść tekst")
	self.clearText.grid(row=7, column=2, sticky=W)
    def drawList(self):
	'''rysuje etykiete, liste slow do wyszukania oraz klawisz wyszukania i czyszczenia listy'''
	self.label1 = Label(self, text="Aktualne slowa:") #etykieta z boku
	self.label1.grid(column=4, row=0, padx=2, sticky=N+W)
	self.pole = ScrolledText(self, bg="white", height=10, width=35) 
	#pole ze slowami, wysokosc w liczbie znakow
	self.pole.grid(column=4, row=1, padx=2, columnspan=2)
	self.pole.config(state=DISABLED)
	#self.pole.insert(END,"sdfdfsdfsdfg dfgfdgfd fgsdg")
	self.clear = Button(self, text="wyczyść listę słów", command=self.clearList)
	self.clear.grid(column=5, row=2, sticky=W)
	self.clear.bind('<Return>', self.clearList)
	self.search = Button(self, text="wyszukaj")
	self.search.grid(column=4, row=2, sticky=W)
    def drawInput(self):
	'''rysuje etykiete, pole wprowadzania i klawisz dodawania slowa'''
	self.label2 = Label(self, text="Słowo:")
	self.label2.grid(column=4, row=3, pady=5, padx=2, sticky=W)
	self.wejscie = Entry(self, width=32)
	self.wejscie.bind('<Return>', self.addWord)
	self.wejscie.grid(column=4, row=4, padx=5, columnspan=3, sticky=W)
	self.add = Button(self, text="dodaj", command=self.addWord)
	self.add.grid(column=4, row=5, padx=2, sticky=W)
	self.add.bind('<Return>', self.addWord)
    def addWord(self, event=None):
	'''metoda wywolywana po kliknieciu klawisza <dodaj>'''
	wartosc = self.wejscie.get()
	if wartosc != "" and wartosc not in self.listaSlow:
	    maxLen = self.pole["width"]
	    improved = wartosc +", "
	    self.pole.config(state=NORMAL)
	    lenNow = len(self.pole.get(1.0, END))-1
	    linesBefore = lenNow/maxLen
	    linesAfter = (lenNow + len(improved))/maxLen
	    if linesAfter > linesBefore and len(improved) <= maxLen and linesAfter%maxLen > 0:
		for i in range(maxLen - lenNow%maxLen):
		    self.pole.insert(END, " ")
	    self.pole.insert(END, improved)
	    self.pole.config(state=DISABLED)
	    self.listaSlow.append(wartosc)
	self.wejscie.delete(0, END)
    def clearList(self, event=None):
	'''metoda czyszczaca liste slow'''
	if self.listaSlow != []:
	    self.pole.config(state=NORMAL)
	    self.pole.delete(1.0, END)
	    self.pole.config(state=DISABLED)
	    self.listaSlow = []
    def question(self):
	'''metoda rysujaca okienko "czy na pewno chcesz zakonczyc"'''
	if MesBox.askokcancel("Koniec","Czy na pewno chcesz wyjść z aplikacji?"):
	    self.quit()

def main():
    root = Tk() #glowne okno aplikacji
    root.geometry("650x400+100+100")#wymiary=650x400, pozycja = (100,100)
    app = Ramka(root)
    root.mainloop()

if __name__ == '__main__':
    main()