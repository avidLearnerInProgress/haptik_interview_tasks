import unittest
import os
import can_create_list

class TestCanCreateList(unittest.TestCase):


	def test_null(self): #test for no params
		result = can_create_list.can_create1()
		self.assertEqual(result, False)

	def test_input_list(self): #test for empty input
		result = can_create_list.can_create1(None, 'piechart')
		self.assertEqual(result, False)

	def test_input_string(self): #test for empty string
		result = can_create_list.can_create2(['front', 'end', 'back', 'tree'], None)
		self.assertEqual(result, False)

	def test_cancreate1function(self): #test function can_create1
		result = can_create_list.can_create1(['back', 'end', 'front', 'tree'], 'backend')
		self.assertEqual(result, True)

	def test_cancreate2function(self): #test function can_create2
		result = can_create_list.can_create2(['back', 'end', 'front', 'tree'], 'frontyard')
		self.assertEqual(result, False)