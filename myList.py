#!/usr/bin/python
# -*- coding: utf-8 -*-

class MyListError(Exception):
    '''Wyjatek dla klasy MyList.'''
    def __init__(self, mes):
        '''Konstruktor, argumentem tresc przy rzucaniu wyjatku.'''
        self.value = mes
    def __str__(self):
        '''Podaje tresc wyjatku.'''
        return self.value

class Element:
    '''Klasa opisujaca element MyList.'''
    def __init__(self, arg=None, follow=None):
        '''Konstruktor; arg - element znajdujacy sie w liscie,
             follow - nastepny element na liscie.'''
        if follow is not None and not isinstance(follow, Element):
            raise MyListError("argument is not an Element")
        self.arg = arg
        self.follow = follow
    def setData(self, arg):
        '''Ustawia zawartosc elementu listy na arg.'''
        self.arg = arg
    def setNext(self, follow):
        '''Ustawia nastepny element listy na follow.'''
        if not isinstance(follow, Element):
            raise MyListError("argument is not an Element")
        self.follow = follow
    def getData(self):
        '''Zwraca zawartosc elementu listy.'''
        return self.arg
    def getNext(self):
        '''Zwraca nastepny element na liscie.'''
        return self.follow

class MyList:
    '''Lista, ktora bedzie mozna laczyc z druga w czasie stalym
         jest to uproszczona lista, nie zawiera np. usuwania elementow,
         gdyz nie wydaje sie to potrzebne.'''
    def __init__(self):
        '''Konstruktor, tworzy pusta liste.'''
        self.first = None
        self.last = None
        self.current = None
        self.length = 0
    def add(self, argument):
        '''Metoda dodajaca argument do listy na ostatnia pozycje.'''
        if self.first is None:
            self.first = Element(argument, None)
            self.last = self.first
        else:
            tmp = Element(argument, None)
            self.last.setNext(tmp)
            self.last = tmp
        self.length += 1
    def __iadd__(self, other):
        '''Metoda dodajaca do siebie dwa obiekty MyList
           zmienia pierwszy obiekt, zwraca wskaznik na pierwszy obiekt.'''
        if other is None or other.first is None:
            return self
        if not isinstance(other, MyList):
            raise MyListError("the other argument is not a MyList")
        if self.first is None:
            self.first = other.first
            self.length = other.length
            self.last = other.last
            return self
        #print other.first
        self.last.setNext(other.first)
        self.length += other.length
        return self
    def __iter__(self):
        '''Metoda zwracajaca iterator.'''
        self.current = self.first
        return self
    def next(self):
        '''Metoda zwracajaca nastepny element na liscie.'''
        if self.current is None:
            raise StopIteration
        else:
            tmp = self.current.getData()
            self.current = self.current.getNext()
            return tmp
    def __len__(self):
        '''Metoda zwracajaca dlugosc listy.'''
        return self.length
    def __eq__(self, other):
        '''Metoda porownujaca listy
           zwraca True, jesli listy rowne, False wpp.'''
        if not isinstance(other, MyList):
            return False
        dl = len(other)
        if dl != len(self):
            return False
        iter1 = iter(self)
        iter2 = iter(other)
        for i in range(dl):
            e1 = iter1.next()
            e2 = iter2.next()
            if e2 != e1:
                return False
        return True
    def __ne__(self, other):
        '''Metoda sprawdzajaca, czy listy sa rozne
           zwraca True, jesli tak; False wpp.'''
        return not self == other
    def __contains__(self, other):
        '''Metoda sprawdzajaca, czy lista zawiera other
           zwraca True, jesli tak; False wpp.'''
        for i in self:
            if other == i:
                return True
        return False