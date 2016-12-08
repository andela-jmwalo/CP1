import unittest
import os.path
from models.amity import Amity

class Amity_Test(unittest.TestCase):
	
	def setUp(self):
		self.amity= Amity()
	
	def test_create_room(self):
		original_number_of_rooms = len(Amity.all_rooms)

		self.amity.create_room("Oculus", "Office")

		new_number_of_rooms = len(Amity.all_rooms)

		self.assertEqual(new_number_of_rooms, original_number_of_rooms+1)  
	
	def test_add_person(self):
		current_number_of_people = len(Amity.all_people)
		self.amity.add_person('Judith','F','Y')
		new_number_of_people =len(Amity.all_people)
		self.assertEqual(new_number_of_people,current_number_of_people+1)

	def test_reallocate_person(self):
		
		message = self.amity.reallocate_person('F001','Ruby')
		
		self.assertEqual(message, "Successful Reallocation")

	def test_load_people(self):
		result = self.amity.load_people('test.txt')
		self.assertEqual(result, 'People Loaded Succesfully')

	def test_print_allocations(self):
		result = self.amity.print_allocations('test.txt')
		self.assertTrue(os.path.isfile('test.txt'))
		
	def test_print_unallocated(self):
		result = self.amity.print_unallocated('test.txt')
		self.assertTrue(os.path.isfile('test.txt'))

	def test_print_room(self):
		message = self.amity.print_room('Emerald')
		self.assertEqual(message, 'Room printed Successfully!')

	def test_save_state(self):
		self.assertEqual(self.amity.load_state('amity.db'), 'Data Saved Successfully')

	def test_load_state(self):
		self.assertEqual(self.amity.save_state('amity.db'), 'Data saved successfully')



