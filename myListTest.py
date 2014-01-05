#!/usr/bin/python
#-*- coding: utf-8 -*-

from myList import *

import unittest

class TestMyList(unittest.TestCase):
    '''kod testujacy klase MyList'''
    def setUp(self):
        pass
    def test_init(self):
        '''sprawdzam dzialanie konstruktora'''
        l = MyList()
        self.assertEqual(l.first, None)
        self.assertEqual(l.last, None)
        self.assertEqual(l.current, None)
        self.assertEqual(len(l), 0)
    def test_Element(self):
        '''kod testujacy tworzenie Elementu'''
        n = Element()
        n2 = Element(3)
        n3 = Element(4, n2)
        self.assertEqual(n2.getData(), 3)
        self.assertEqual(n3.getNext(), n2)
        self.assertRaises(MyListError, Element, 3, 4)
        self.assertRaises(MyListError, n2.setNext, "3")
        n.setData(5)
        self.assertEqual(n.getData(), 5)
        n.setNext(n3)
        self.assertEqual(n.getNext(), n3)
    def test_add(self):
        '''kod testujacy dodawanie elementu do listy'''
        l = MyList()
        l.add(4)
        self.assertEqual(l.first.getData(), 4)
        self.assertEqual(l.last.getData(), 4)
        l.add(8)
        self.assertEqual(l.last.getData(), 8)
        l.add(7)
        self.assertEqual(l.last.getData(), 7)
    def test_contains(self):
        '''kod testujacy sprawdzanie, czy element nalezy do listy'''
        l = MyList()
        self.assertFalse(4 in l)
        self.assertFalse(8 in l)
        self.assertFalse(7 in l)
        self.assertFalse(13 in l)
        l.add(4)
        l.add(8)
        l.add(7)
        self.assertTrue(4 in l)
        self.assertTrue(8 in l)
        self.assertTrue(7 in l)
        self.assertFalse(13 in l)
    def test_equal(self):
        '''kod testujacy porownywanie list'''
        l1 = MyList()
        l2 = MyList()
        self.assertEqual(l1, l2)
        l1.add(3)
        self.assertNotEqual(l1, l2)
        l1.add(4)
        l1.add(9)
        l2.add(3)
        l2.add(4)
        l2.add(9)
        self.assertEqual(l1, l2)
        l2.add(7)
        self.assertNotEqual(l1, l2)
    def test_join(self):
        '''kod testujacy laczenie list'''
        l1 = MyList()
        l2 = MyList()
        l3 = MyList()
        l1.add(2)
        l2.add(5)
        l2.add(4)
        l3.add(2)
        l3.add(5)
        l3.add(4)
        self.assertEqual(l1+l2, l3)
        l4 = MyList()
        l4+l3
        self.assertEqual(l4, l3)
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()