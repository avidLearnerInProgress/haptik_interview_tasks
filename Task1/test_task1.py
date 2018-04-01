import unittest
import os
import most_active_users

class TestActiveUsers(unittest.TestCase):

	def test_file(self): #test if file exists
		result = os.path.isfile('./chats.txt')  
		self.assertEqual(result, True)

	def test_data_in_file(self): #test if file is not empty
		result = (os.stat('./chats.txt').st_size != 0)
		self.assertEqual(result, True)

	def test_readfunction(self): #test read function
		result = most_active_users.read('./chats.txt')
		self.assertNotEqual(result, None)

	def test_computeusersfunction(self):
		result = most_active_users.compute_active_users(most_active_users.read('./chats.txt'))
		for ele in result: 
			self.assertNotEqual(ele, None) #test individual elements of result
		self.assertNotEqual(result, None) #test if result is not none
		self.assertEqual(len(result), 3) #test if length of result is 3