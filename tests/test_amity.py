import unittest

from models.amity import Amity

class Amity_Test(unittest.TestCase):
	def setup_room():
		self.obj = room()
	def test_create_room(self):
		original_number_of_rooms = len(Amity.all_rooms)

		Amity.create_room("Oculus", "Office")

		new_nember_of_rooms = len(Amity.all_rooms)

		self.assertEqual(new_nember_of_rooms, original_number_of_rooms+1)  
	def test_add_person():
		pass