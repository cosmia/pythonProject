#!/usr/bin/python
# -*- coding: utf-8 -*-

from myList import *

class NodeException(Exception):
    '''wyjatek dla klasy Node'''
    def __init__(self, value):
	'''konstruktor, argumentem tresc przy rzucaniu wyjatku'''
	self.napis = value
    def __str__(self):
	'''podaje powod wyjatku'''
	return repr(self.napis)
    __repr__ = __str__

class Node:
    '''klasa opisująca wezel/stan w automacie/drzewie Trie'''
    def __init__(self):
	'''konstruktor bezargumentowy
	   accept = MyList() - pusta lista,
	   fail = None
	   edges = {}'''
	self.accept = MyList()
	self.edges = {}
	self.fail = None
    def labelCorrect(self, label):
	'''sprawdza, czy label jest poprawna etykieta krawedzi
	   jesli nie, rzuca NodeException'''
	if not isinstance(label, (str, unicode)):
	    raise NodeException("label must be a character")
	if len(label) != 1:
	    raise NodeException("label must be exactly one character long")
    def nodeCorrect(self, node, n=1):
	'''sprawdza, czy node jest obiektem klasy Node
	   jesli nie, to rzuca NodeException
	   n to numer argumentu, ktorym jest node w jakiejs funkcji
	     sluzy uszczegolowieniu, ktory argument jest bledny'''
	if not isinstance(node, Node):
	    lan = "the "
	    if n != 1: lan += "second "
	    lan += "argument must be a node"
	    raise NodeException(lan)
    def getAccept(self):
	'''zwraca liste indeksow slow, ktore akceptuje ten wezel,
	   lista jest pusta, jesli ten wezel niczego nie akceptuje'''
	return self.accept
    def getLabels(self):
	'''zwraca liste etykiet dla krawedzi wychodzacych z tego wezla'''
	return self.edges.keys()
    def getAim(self, label):
	'''zwraca wezel, do ktorego prowadzi krawedz z etykieta label
	   jesli brak takiej krawedzi, zwraca None'''
	self.labelCorrect(label)
	if label not in self.edges:
	    if self.fail is None:
		return self
	    else:
		return None
	else:
	    return self.edges[label]
    def getFail(self):
	'''zwraca wezel odpowiadajacy najdluzszemu wlasciwemu sufiksowi
	   slowa, ktore do ktorego probowalismy znalezc dopasowanie'''
	return self.fail
    def setAccept(self, number):
	'''ustalamy, ze ten wezel akceptuje slowo o indeksie number lub slowa o
	   indeksach z MyList number
	   rzuca NodeException, jesli number nie jest calkowita liczba nieujemna
	   albo obiektem MyList calkowitych liczb nieujemnych'''
	if isinstance(number, MyList):
	    for i in number:
		if not isinstance(i, (long, int)) or i < 0:
		    mes = "argument should be a non-negative integer or long or a set of those"
		    raise NodeException(mes)
	    #print number
	    self.accept + number
	    return
	if not isinstance(number, (long, int)):
	    raise NodeException("argument should be an integer or long or a set of those")
	if number < 0:
	    raise NodeException("argument must be non-negative")
	self.accept.add(number)
    def setAim(self, label, node):
	'''ustalamy, ze z tego wezla bedzie wychodzic krawedz
	   etykietowana label i bedzie ona prowadzic do node
	   rzuca NodeException, jesli label niepoprawna lub node nie jest wezlem'''
	self.labelCorrect(label)
	self.nodeCorrect(node,2)
	self.edges[label] = node
    def setFail(self, node):
	'''ustalamy, ze najdluzszy sufiks slowa, do ktorego probowalismy
	  dopsowac w tym wezle odpowiada wezlowi node
	  rzuca wyjatkiem, jesli node nie jest wezlem'''
	self.nodeCorrect(node)
	self.fail = node
