import unittest
import os.path
from models.amity import Amity


class Amity_Test(unittest.TestCase):

    def setUp(self):
        self.Amity = Amity()

    def test_create_livingspace(self):
        original_number_of_living = len(Amity.livingspace)

        self.Amity.create_room('LIVINGSPACE', ['SCALA', 'RUBY'])

        new_number_of_living = len(Amity.livingspace)

        self.assertEqual(new_number_of_living, original_number_of_living + 2)

    def test_create_office(self):
        original_number_of_office = len(Amity.office)

        self.Amity.create_room('OFFICE', ['PURPLE', 'ORANGE'])

        new_number_of_office = len(Amity.office)

        self.assertEqual(new_number_of_office, original_number_of_office + 2)

    def test_add_person(self):
        current_number_of_people = len(Amity.all_person)
        self.Amity.add_person('Judith Mwalo', 'FELLOW', 'YES')
        new_number_of_people = len(Amity.all_person)
        self.assertEqual(new_number_of_people, current_number_of_people + 1)

    def test_reallocate_person(self):

        message = self.Amity.reallocate_person('F1', 'RUBY', 'LIVINGSPACE')
        print(Amity.livingspace_allocations['RUBY'])
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
            'fix.db'), 'Data saved successfully')

    def test_load_state(self):
        self.assertEqual(self.Amity.load_state(
            'amity.db'), 'Data has been loaded into the system successfully')
