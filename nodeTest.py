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
	self.assertEqual(n.accept, set())
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
	self.assertRaises(NodeException, n.setAccept, 6.0)
	self.assertRaises(NodeException, n.setAccept, -7)
    def tearDown(self):
	pass

if __name__ == "__main__":
    unittest.main()