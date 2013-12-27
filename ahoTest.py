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
	self.assertEqual(l.getAccept(), set())
	self.assertEqual(la.getAccept(), set())
	self.assertEqual(las.getAccept(), set())
	self.assertEqual(lase.getAccept(), set())
	zbior = set()
	zbior.add(1)
	self.assertEqual(laser.getAccept(), zbior)
	self.assertEqual(a.words[1], "laser")
	self.assertEqual(s.getFail(), r)
	self.assertEqual(se.getFail(), r)
	self.assertEqual(ser.getFail(), r)
	self.assertEqual(sern.getFail(), r)
	self.assertEqual(serni.getFail(), r)
	self.assertEqual(sernik.getFail(), r)
	self.assertEqual(s.getAccept(), set())
	self.assertEqual(se.getAccept(), set())
	self.assertEqual(ser.getAccept(), set())
	self.assertEqual(sern.getAccept(), set())
	self.assertEqual(serni.getAccept(), set())
	zbior = set()
	zbior.add(0)
	self.assertEqual(sernik.getAccept(), zbior)
	self.assertEqual(a.words[0], "sernik")
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
	self.assertEqual(s.getAccept(), set())
	self.assertEqual(sh.getFail(), h)
	self.assertEqual(sh.getAccept(), set())
	zbior = set(); zbior.add(0); zbior.add(1)
	self.assertEqual(she.getFail(), he)
	self.assertEqual(she.getAccept(), zbior)
	self.assertEqual(a.words[1], "she")
	self.assertEqual(a.words[0], "he")
	self.assertEqual(h.getFail(), r)
	self.assertEqual(h.getAccept(), set())
	self.assertEqual(he.getFail(), r)
	self.assertEqual(he.getAccept(), set([0]))
	self.assertEqual(her.getFail(), r)
	self.assertEqual(her.getAccept(), set())
	self.assertEqual(hers.getFail(), s)
	self.assertEqual(hers.getAccept(), set([3]))
	self.assertEqual(a.words[3], "hers")
	self.assertEqual(hi.getFail(), r)
	self.assertEqual(hi.getAccept(), set())
	self.assertEqual(his.getFail(), s)
	self.assertEqual(his.getAccept(), set([2]))
	self.assertEqual(a.words[2], "his")
    def test_clear(self):
	'''kod testujacy czyszczenie automatu'''
    def tearDown(self):
	pass

if __name__ == "__main__":
    unittest.main()
