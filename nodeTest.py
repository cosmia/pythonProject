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
    def tearDown(self):
	pass

if __name__ == "__main__":
    unittest.main()