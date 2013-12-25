#!/usr/bin/python
#-*- coding: utf-8 -*-

from ahoCorasick import *
import unittest

class TestAho(unittest.TestCase):
    '''kod testujacy klase AhoCorasick'''
    def setUp(self):
	pass
    def test_init(self):
	'''sprawdzam dzialanie konstruktora'''
	a = AhoCorasick()
	#porownianie korzenia z domyslnym wezlem + czy lista slow pusta
	self.assertEqual(a.n.getAccept(), set())
	self.assertEqual(a.n.getFail(), None)
	self.assertEqual(a.n.getLabels(), [])
	self.assertEqual(a.words, [])
    def test_tree(self):
	'''sprawdzam dodawanie i wyszukiwanie slow w drzewie'''
	a = AhoCorasick()
	self.assertFalse(a.lookUp("nie ma"))
	self.assertFalse(a.lookUp("tak"))
	self.assertFalse(a.lookUp("ta"))
	a.addWord("tak")
	self.assertFalse(a.lookUp("nie ma"))
	self.assertTrue(a.lookUp("tak"))
	self.assertFalse(a.lookUp("ta"))
	a.addWord("ta")
	self.assertFalse(a.lookUp("nie ma"))
	self.assertTrue(a.lookUp("tak"))
	self.assertTrue(a.lookUp("ta"))
    def tearDown(self):
	pass

if __name__ == "__main__":
    unittest.main()
