#!/usr/bin/python
# -*- coding: utf-8 -*-

class NodeException(Exception):
    '''wyjatek dla klasy Node'''
    def __init__(self, value):
	'''konstruktor bezargumentowy'''
	self.napis = value
    def __str__(self):
	'''podaj powod wyjatku'''
	return repr(self.napis)
    __repr__ = __str__

class Node:
    def __init__(self):
	self.accept = None
	self.edges = {}
	self.fail = None
    def labelCorrect(self, label):
	if not isinstance(label, str):
	    raise NodeException("label must be a character")
	if len(label) != 1:
	    raise NodeException("label must be exactly one character long")
    def nodeCorrect(self, node, n=1):
	if not isinstance(node, Node):
	    lan = "the "
	    if n != 1: lan += "second "
	    lan += "argument must be a node"
	    raise NodeException(lan)
    def getAccept(self):
	return self.accept
    def getLabels(self):
	return edges.keys
    def getAim(self, label):
	self.labelCorrect(label)
	if label not in self.edges:
	    if self.fail is None:
		return self
	    else:
		return None
	else:
	    return self.edges[label]
    def getFail(self):
	return self.fail
    def setAccept(self, number):
	if not isinstance(number, (long, int)):
	    raise NodeException("argument should be an integer or long")
	self.accept = number
    def setAim(self, label, node):
	self.labelCorrect(label)
	self.nodeCorrect(node,2)
	self.edges[label] = node
    def setFail(self, node):
	self.nodeCorrect(node)
	self.fail = node