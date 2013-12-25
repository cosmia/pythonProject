#!/usr/bin/python
# -*- coding: utf-8 -*-

from node import *

class AhoCorasickException(Exception):
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
    def addWord(self, word):
	'''dodaje slowo word do automatu/drzewa
	   rzuca AhoCorasickException, jesli word nie jest stringiem'''
	if not isinstance(word, str):
	    raise AhoCorasickException("argument nie jest stringiem")
	dl = len(word)
	if dl == 0: return #nie dodajemy pustego slowa
	wezel = self.n
	i = 0
	#idziemy dopoki mozemy po istniejacych wezlach
	while i < dl:
	    labels = wezel.getLabels()
	    if s[i] in labels:
		wezel = wezel.getAim(s[i])
	    else:
		break
	    i += 1
	#a teraz tworzymy nowe, jesli taka potrzeba
	while i < dl:
	    wezel.setAim(s[i], Node())
	    wezel = wezel.getAim(s[i])
	    i += 1
	#jesli jeszcze nie dodalismy tego slowa
	if wezel.getAccept() == set():
	    ktore = len(self.words)
	    wezel.setAccept(ktore)
	    self.words.append(word)
    def lookUp(self, word):
	'''sprawdza, czy dane slowo wystepuje w drzewie
	   zwraca True, jesli tak; False wpp
	   rzuca AhoCorasickException, jesli word nie jest strigiem'''
	pass