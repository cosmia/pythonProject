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
	#testowanie wyjatkow
	self.assertRaises(AhoCorasickException, a.addWord, 7)
	self.assertRaises(AhoCorasickException, a.lookUp, 7)
    def test_build(self):
	'''kod testujacy metode AhoCorasick.build'''
	a = AhoCorasick()
	a.addWord("sernik")
	a.addWord("laser")
	a.build()
	r = a.n
	l = r.getAim("l")
	la = l.getAim("a")
	las = la.getAim("s")
	lase = las.getAim("e")
	laser = lase.getAim("r")
	s = r.getAim("s")
	se = s.getAim("e")
	ser = se.getAim("r")
	sern = ser.getAim("n")
	serni = sern.getAim("i")
	sernik = serni.getAim("k")
	self.assertEqual(l.getFail(), r)
	self.assertEqual(la.getFail(), r)
	self.assertEqual(las.getFail(), s)
	self.assertEqual(lase.getFail(), se)
	self.assertEqual(laser.getFail(), ser)
	self.assertEqual(s.getFail(), r)
	self.assertEqual(se.getFail(), r)
	self.assertEqual(ser.getFail(), r)
	self.assertEqual(sern.getFail(), r)
	self.assertEqual(serni.getFail(), r)
	self.assertEqual(sernik.getFail(), r)
    def test_build2(self):
	'''kod testujacy metode AhoCorasick.build dla bardziej skomplikowanego automatu'''
	a = AhoCorasick()
	a.addWord("he")
	a.addWord("she")
	a.addWord("his")
	a.addWord("hers")
	a.build()
	r = a.n
	h = r.getAim("h")
	hi = h.getAim("i")
	his = hi.getAim("s")
	he = h.getAim("e")
	her = he.getAim("r")
	hers = her.getAim("s")
	s = r.getAim("s")
	sh = s.getAim("h")
	she = sh.getAim("e")
	self.assertEqual(s.getFail(), r)
	self.assertEqual(sh.getFail(), h)
	self.assertEqual(she.getFail(), he)
	self.assertEqual(h.getFail(), r)
	self.assertEqual(he.getFail(), r)
	self.assertEqual(her.getFail(), r)
	self.assertEqual(hers.getFail(), s)
	self.assertEqual(hi.getFail(), r)
	self.assertEqual(his.getFail(), s)
    def tearDown(self):
	pass

if __name__ == "__main__":
    unittest.main()
