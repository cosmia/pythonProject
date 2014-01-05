#!/usr/bin/python
#-*- coding: utf-8 -*-

from node import *

import unittest

class TestNode(unittest.TestCase):
    '''kod testujacy klase Node'''
    def setUp(self):
        pass
    def test_init(self):
        '''sprawdzam dzialanie konstruktora'''
        n = Node()
        self.assertEqual(n.accept, MyList())
        self.assertEqual(n.fail, None)
        self.assertEqual(n.edges, {})
    def test_accept(self):
        '''kod testujacy metody setAccept i getAccept'''
        n = Node()
        n.setAccept(4)
        n.setAccept(8)
        s = n.getAccept()
        self.assertTrue(4 in s)
        self.assertTrue(8 in s)
        self.assertFalse(7 in s)
        self.assertRaises(NodeError, n.setAccept, 6.0)
        self.assertRaises(NodeError, n.setAccept, -7)
        mySet = MyList()
        mySet.add(5)
        n.setAccept(mySet)
        secondSet = MyList()
        secondSet.add(4)
        secondSet.add(8)
        secondSet.add(5)
        result = n.getAccept()
        self.assertEqual(result, secondSet)
        mySet = MyList()
        mySet.add(5)
        mySet.add(8.0)
        self.assertRaises(NodeError, n.setAccept, mySet)
        mySet = MyList()
        mySet.add(5)
        mySet.add(-8)
        self.assertRaises(NodeError, n.setAccept, mySet)
    def test_aim(self):
        '''kod testujacy dzialanie metod getAim i setAim'''
        n = Node()
        self.assertRaises(NodeError, n.getAim, 7)
        self.assertRaises(NodeError, n.getAim, "")
        self.assertRaises(NodeError, n.getAim, "df")
        #domyslnie kazdy wezel jest korzeniem jakiegos drzewa
        #powinien dla kazdej 'litery' zwracac lacze na siebie,
        #o ile nie ustanowiono inaczej
        self.assertEqual(n.getAim("a"), n)
        self.assertEqual(n.getAim("e"), n)
        n2 = Node()
        n.setAim("e", n2)
        self.assertEqual(n.getAim("a"), n)
        self.assertEqual(n.getAim("e"), n2)
        #n2 nie jest korzeniem - dlatego ustawiam jego fail na
        #inny wezel, np. n
        n2.fail = n
        self.assertEqual(n2.getAim("a"), None)
        self.assertRaises(NodeError, n.setAim, 7, n2)
        self.assertRaises(NodeError, n.setAim, "", n2)
        self.assertRaises(NodeError, n.setAim, "df", n2)
        self.assertRaises(NodeError, n.setAim, "a", "gfg")
    def test_fail(self):
        '''kod testujacy dzialanie metod getFail i setFail'''
        n1 = Node()
        n2 = Node()
        self.assertEqual(n1.getFail(), None)
        self.assertEqual(n2.getFail(), None)
        n2.setFail(n1)
        self.assertEqual(n2.getFail(), n1)
        self.assertRaises(NodeError, n1.setFail, "gfgf")
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()