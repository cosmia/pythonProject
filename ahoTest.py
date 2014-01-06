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
        self.assertEqual(a.n.getAccept(), MyList())
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
        self.assertRaises(AhoCorasickError, a.addWord, 7)
        self.assertRaises(AhoCorasickError, a.lookUp, 7)
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
        self.assertEqual(l.getAccept(), MyList())
        self.assertEqual(la.getAccept(), MyList())
        self.assertEqual(las.getAccept(), MyList())
        self.assertEqual(lase.getAccept(), MyList())
        zbior = MyList()
        zbior.add(1)
        self.assertEqual(laser.getAccept(), zbior)
        self.assertEqual(a.words[1], "laser")
        self.assertEqual(s.getFail(), r)
        self.assertEqual(se.getFail(), r)
        self.assertEqual(ser.getFail(), r)
        self.assertEqual(sern.getFail(), r)
        self.assertEqual(serni.getFail(), r)
        self.assertEqual(sernik.getFail(), r)
        self.assertEqual(s.getAccept(), MyList())
        self.assertEqual(se.getAccept(), MyList())
        self.assertEqual(ser.getAccept(), MyList())
        self.assertEqual(sern.getAccept(), MyList())
        self.assertEqual(serni.getAccept(), MyList())
        zbior = MyList()
        zbior.add(0)
        self.assertEqual(sernik.getAccept(), zbior)
        self.assertEqual(a.words[0], "sernik")
    def test_build2(self):
        '''kod testujacy metode AhoCorasick.build dla bardziej skomplikowanego
           automatu'''
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
        self.assertEqual(s.getAccept(), MyList())
        self.assertEqual(sh.getFail(), h)
        self.assertEqual(sh.getAccept(), MyList())
        zbior = MyList(); zbior.add(0); zbior.add(1)
        self.assertEqual(she.getFail(), he)
        self.assertEqual(set(she.getAccept()), set(zbior))
        self.assertEqual(a.words[1], "she")
        self.assertEqual(a.words[0], "he")
        self.assertEqual(h.getFail(), r)
        self.assertEqual(set(h.getAccept()), set())
        self.assertEqual(he.getFail(), r)
        self.assertEqual(set(he.getAccept()), set([0]))
        self.assertEqual(her.getFail(), r)
        self.assertEqual(set(her.getAccept()), set())
        self.assertEqual(hers.getFail(), s)
        self.assertEqual(set(hers.getAccept()), set([3]))
        self.assertEqual(a.words[3], "hers")
        self.assertEqual(hi.getFail(), r)
        self.assertEqual(set(hi.getAccept()), set())
        self.assertEqual(his.getFail(), s)
        self.assertEqual(set(his.getAccept()), set([2]))
        self.assertEqual(a.words[2], "his")
    def test_unicode(self):
        '''kod pokazujacy, ze dodawanie slow w postaci str jak i unicode
           dziala poprawnie'''
        a = AhoCorasick()
        a.addWord("ąćęłńóśźż")
        a.addWord(u"ąćęłńóśźż")
        self.assertTrue(a.lookUp("ąćęłńóśźż"))
        self.assertTrue(a.lookUp(u"ąćęłńóśźż"))
        self.assertEqual(len(a.words),1)
    def test_clear(self):
        '''kod testujacy czyszczenie automatu'''
        a = AhoCorasick()
        a.makeTree(["laser","sernik"])
        a.clear()
        self.assertEqual(a.words, [])
        self.assertEqual(set(a.n.getAccept()), set())
        self.assertEqual(a.n.getFail(), None)
        self.assertEqual(a.n.getLabels(), [])
    def test_search(self):
        '''test sprawdzajacy wyszukiwanie wzorcow w tekscie'''
        a = AhoCorasick()
        a.makeTree(["he","she","his","hers"])
        res = a.search("ushers")
        e = ("Found \"she\" in position 3\nFound \"he\" in position 3\n"
             "Found \"hers\" in position 5")
        self.assertEqual(res,e)
        res = a.search("")
        self.assertEqual(res, "Nothing found")
        res = a.search("w tym tekscie nic nie znajdzie")
        self.assertEqual(res, "Nothing found")
        res = a.search("ushers", True)
        #pierwsza czesc krotki - pozycja, druga - indeks slowa
        self.assertEqual(res,set([(3,0),(3,1),(5,3)]))
        res = a.search("w tym tekscie nic nie znajdzie",True)
        self.assertEqual(res,set())
        res = a.search("",True)
        self.assertEqual(res,set())
        self.assertRaises(AhoCorasickError, a.search, 7)
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
