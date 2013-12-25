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
	pass
    def lookUp(self, word):
	'''sprawdza, czy dane slowo wystepuje w drzewie
	   zwraca True, jesli tak; False wpp
	   rzuca AhoCorasickException, jesli word nie jest strigiem'''
	pass