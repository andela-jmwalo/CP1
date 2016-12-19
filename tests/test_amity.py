import unittest
import os.path
from models.amity import Amity


class Amity_Test(unittest.TestCase):

    def setUp(self):
        self.Amity = Amity()

    def test_create_room(self):
        original_number_of_rooms = len(Amity.all_rooms)

        self.Amity.create_room('LIVINGSPACE', ['SCALA', 'RUBY'])

        new_number_of_rooms = len(Amity.all_rooms)

        self.assertEqual(new_number_of_rooms, original_number_of_rooms + 2)

    def test_add_person(self):
        current_number_of_people = len(Amity.all_person)
        self.Amity.add_person('Judith Mwalo', 'FELLOW', 'YES')
        new_number_of_people = len(Amity.all_person)
        self.assertEqual(new_number_of_people, current_number_of_people + 1)

    def test_reallocate_person(self):

        message = self.Amity.reallocate_person('F1', 'RUBY', 'LIVINGSPACE')

        self.assertEqual(message, 'Reallocation was Succesfull!')

    def test_load_people(self):
        filename = 'amity.txt'
        result = self.Amity.load_people(filename)
        self.assertEqual(result, 'People Loaded Succesfully!')

    def test_print_allocations(self):
        self.Amity.print_allocations('test.txt')
        self.assertTrue(os.path.isfile('test.txt'))

    def test_print_unallocated(self):
        self.Amity.print_unallocated('tests.txt')
        self.assertTrue(os.path.isfile('tests.txt'))

    def test_print_room(self):
        message = self.Amity.print_room('SCALA')
        self.assertEqual(message, 'Room printed Successfully!')

    def test_save_state(self):
        self.assertEqual(self.Amity.save_state(
            'test.db'), 'Data saved successfully')

    def test_load_state(self):
        self.assertEqual(self.Amity.load_state(
            'test.db'), 'Data has been loaded into the system successfully')
