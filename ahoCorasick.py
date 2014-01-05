#!/usr/bin/python
# -*- coding: utf-8 -*-

from node import *
from Queue import *

class AhoCorasickError(Exception):
    '''wyjatek dla klasy Node'''
    def __init__(self, value):
        '''konstruktor, argumentem tresc przy rzucaniu wyjatku'''
        self.napis = value
    def __str__(self):
        '''podaj powod wyjatku'''
        return repr(self.napis)

class AhoCorasick:
    '''klasa opisujaca drzewo Trie / automat, sluzacy wyszukiwaniu wzorcow'''
    def __init__(self):
        '''konstruktor bezargumentowy
           n - korzen drzewa, pusty
           words - pusta liczba slow zakodowanych w drzewie'''
        self.n = Node()
        self.words = []
        self.built = False
    def addWord(self, word):
        '''dodaje slowo word do automatu/drzewa
           rzuca AhoCorasickError, jesli word nie jest stringiem
             lub zbudowano juz automat'''
        if self.built:
            raise AhoCorasickError("automaton has been built already")
        if not isinstance(word, (str, unicode)):
            raise AhoCorasickError("argument is not a string")
        dl = len(word)
        if dl == 0: return #nie dodajemy pustego slowa
        wezel = self.n
        i = 0
        #idziemy dopoki mozemy po istniejacych wezlach
        while i < dl:
            litera = word[i]
            labels = wezel.getLabels()
            if litera in labels:
                wezel = wezel.getAim(litera)
            else:
                break
            i += 1
        #a teraz tworzymy nowe, jesli taka potrzeba
        while i < dl:
            litera = word[i]
            wezel.setAim(litera, Node())
            wezel = wezel.getAim(litera)
            #wezel.setFail(self.n)
            #na poczatku najdluzszy wlasciwy sufiks to slowo puste
            #mozna to w sumie robic przy budowaniu automatu...
            i += 1
        #jesli jeszcze nie dodalismy tego slowa
        if wezel.getAccept() == MyList():
            ktore = len(self.words)
            wezel.setAccept(ktore)
            self.words.append(word)
    def lookUp(self, word):
        '''sprawdza, czy dane slowo wystepuje w drzewie
           zwraca True, jesli tak; False wpp
           rzuca AhoCorasickError, jesli word nie jest strigiem'''
        if not isinstance(word, str):
            raise AhoCorasickError("argument is not a string")
        if word == "": return False
        i = 0
        dl = len(word)
        wezel = self.n
        while i < dl:
            litera = word[i]
            labels = wezel.getLabels()
            if litera not in labels:
                return False
            wezel = wezel.getAim(litera)
            i += 1
        if wezel.getAccept() != MyList():
            return True
        return False
    def build(self):
        '''konstruuje automat skonczony na podstawie drzewa, ktore
           powstaje podczas dodawania slow metoda addWord'''
        q = Queue()
        for i in self.n.getLabels():
            s = self.n.getAim(i)
            s.setFail(self.n)
            q.put(s)
        while not q.empty():
            r = q.get()
            for a in r.getLabels():
                u = r.getAim(a)
                q.put(u)
                v = r.getFail()
                while v.getAim(a) is None: #jesli stad nie ma tego przejscia
                    v = v.getFail()        #to szukaj krotszego dopasowania
                u.setFail(v.getAim(a))
                #dodaj nowe akceptowane slow
                u.setAccept(u.getFail().getAccept())
        self.built = True
    def makeTree(self, wordList):
        '''konstruuje drzewo i automat na podstawie listy slow wordList
           takze dodaje do istniejacego automatu wzorce z wordList
           rzuca AhoCorasickError, jesli wordList nie jest lista stringow
             lub zbudowano juz automat'''
        if self.built:
            raise AhoCorasickError("automaton has been built already")
        if not isinstance(wordList, list):
            raise AhoCorasickError("argument is not a list")
        for i in wordList:
            if not isinstance(i, (str, unicode)):
                raise AhoCorasickError("element of the list is not a string")
        for i in wordList:
            self.addWord(i)
        self.build()
    def clear(self):
        '''czysci automat i drzewo'''
        self.words = []
        self.n = Node()
        self.built = False
    def search(self, tekst, returnSet=False):
        '''wyszukuje wzorce w zmiennej tekst, zwraca string z wiadomoscia o
             wynikach
           domyslny argument returnSet mowi o formacie zwracanej wartosci
           jesli returnSet jest False, to zwracamy string z informacjami
           jesli returnSet jest True, to zwracamy zbior krotek o dlugosci dwa,
              krotka zawiera pozycje, na ktorej znalazla slowo, oraz indeks slowa
           jesli tekst nie jest zmienna string, to rzuca AhoCorasickError'''
        if not isinstance(tekst, (str, unicode)):
            raise AhoCorasickError("argument is not a string")
        node = self.n
        if not returnSet: message = ""
        else: message = set()
        dl = len(tekst)
        for i in range(dl):
            while not node.getAim(tekst[i]):
                node = node.getFail()
            node = node.getAim(tekst[i])
            if node.getAccept() != set():
                zbior = node.getAccept()
                for j in zbior:
                    if returnSet:
                        message.add((i,j))
                    else:
                        message += ("Found \""+self.words[j]+"\" in position "+
                                    str(i)+"\n")
        if not returnSet and message == "":
            message = "Nothing found\n"
        if not returnSet: message = message[:len(message)-1]
        return message
