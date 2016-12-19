from models.rooms import Office, LivingSpace
from models.person import Staff, Fellow
import random
import sqlite3


class Amity(object):

    all_rooms = []
    livingspace = []
    office = []
    all_person = []
    office_allocations = {}
    livingspace_allocations = {}
    unallocated_office = []
    unallocated_livingspace = []
    person_data = {}
    staff = []
    fellow = []
    room_data = {}

    all_fellows = 0
    all_staff = 0

    """This method adds a new room given the room name and the type."""

    def create_room(self, room_type, rooms):
        for room_name in rooms:
            if room_name in Amity.all_rooms:
                print ('Room already exists')
            else:
                if room_type == 'LIVINGSPACE':
                    new_room = LivingSpace(room_name)
                    Amity.all_rooms.append(room_name)
                    Amity.livingspace.append(room_name)

                    Amity.room_data[room_name] = [
                        room_name, room_type, new_room.capacity]
                    Amity.livingspace_allocations[room_name] = []
                    print(room_name + ' ' + 'created successfully!')
                elif room_type == 'OFFICE':
                    new_room = Office(room_name)
                    Amity.all_rooms.append(room_name)
                    Amity.office.append(room_name)
                    Amity.room_data[room_name] = [
                        room_name, room_type, new_room.capacity]
                    Amity.office_allocations[room_name] = []
                    print(room_name + ' ' + 'created successfully!')

    @staticmethod
    def add_person(person_name, job_type, wants_accomodation):
        """This method adds a new person to the system. """
        if job_type == 'FELLOW':
            new_person = Fellow(person_name)
            person_id = 'F' + str(len(Amity.fellow) + 1)
            Amity.fellow.append(person_name)
            if wants_accomodation == 'YES':
                Amity.allocate_office(person_name)
                Amity.allocate_livingspace(person_name)

            elif wants_accomodation == 'NO':
                Amity.allocate_office(person_name)

        elif job_type == 'STAFF':
            new_person = Staff(person_name)
            person_id = 'S' + str(len(Amity.staff) + 1)
            Amity.allocate_office(person_name)
            Amity.staff.append(person_name)

        Amity.person_data[person_id] = [
            new_person.person_name, new_person.job_type, wants_accomodation]
        Amity.all_person.append(person_name)

    def allocate_office(person_name):
        vacant_offices = [room for room in Amity.office if len(
            Amity.office_allocations[room]) < Amity.room_data[room][2]]
        if vacant_offices:
            random_office = random.choice(vacant_offices)
            Amity.office_allocations[random_office].append(person_name)
        else:
            Amity.unallocated_office.append(person_name)

    def allocate_livingspace(person_name):
        vacant_livingspace = [room for room in Amity.livingspace if len(
            Amity.livingspace_allocations[room]) < Amity.room_data[room][2]]
        if vacant_livingspace:
            random_livingspace = random.choice(vacant_livingspace)
            Amity.livingspace_allocations[
                random_livingspace].append(person_name)
        else:
            Amity.unallocated_livingspace.append(person_name)

    @staticmethod
    def reallocate_person(person_id, room_name, room_type):

        if person_id not in Amity.person_data:
            print("person does not exist")
        else:
            person_name = Amity.person_data[person_id][0]
            room_capacity = Amity.room_data[room_name][2]
            if room_type == 'OFFICE':
                office_occupants = len(Amity.office_allocations[room_name])
                if office_occupants == room_capacity:
                    print (room_name + " " + "is currently full")
                else:
                    for room in Amity.office_allocations:
                        if person_name in Amity.office_allocations[room]:
                            Amity.office_allocations[
                                room].remove(person_name)
                    Amity.office_allocations[room_name].append(person_name)
            if room_type == 'LIVINGSPACE':
                living_occupants = len(
                    Amity.livingspace_allocations[room_name])
                if living_occupants == room_capacity:
                    print (room_name + " " + "is currently full")
                else:
                    for room in Amity.livingspace_allocations:
                        if person_name in Amity.livingspace_allocations[room]:
                            Amity.livingspace_allocations[
                                room].remove(person_name)
                    Amity.livingspace_allocations[
                        room_name].append(person_name)
        return ('Reallocation was Succesfull!')

    @staticmethod
    def load_people(filename):
        with open(filename, 'r') as people_file:
            people = people_file.readlines()
        for employee in people:
            employee_data = employee.split()
            person_name = employee_data[0] + " " + employee_data[1]
            job_type = employee_data[2]
            if job_type == 'STAFF':
                wants_accomodation = 'NO'
            elif job_type == 'FELLOW':
                accomodation = employee_data[3]
                if accomodation.upper() == 'Y':
                    wants_accomodation = 'YES'
                else:
                    wants_accomodation = 'NO'
            Amity.add_person(person_name, job_type, wants_accomodation)

        return ('People Loaded Succesfully!')

    @staticmethod
    def print_allocations(file_name):
        if file_name:
            file = open(file_name, 'w')
            file.write('%s\n' % 'LIVINGSPACE ALLOCATIONS')

            for room_name in Amity.livingspace_allocations:
                file.write("%s\n" % room_name)
                living_occupants = Amity.livingspace_allocations[room_name]
                for person in living_occupants:
                    file.write("%s\n" % person)

            file.write('%s\n' % 'OFFICE ALLOCATIONS')
            for room_name in Amity.office_allocations:
                file.write("%s\n" % room_name)
                office_occupants = Amity.office_allocations[room_name]
                for person in office_occupants:
                    file.write("%s\n" % person)
            file.close()

        else:
            for room_name in Amity.livingspace_allocations:
                print('LIVINGSPACE ALLOCATIONS')
                living_occupants = Amity.livingspace_allocations[room_name]
                print (room_name)
                print ('-' * 50)
                print (', '.join(living_occupants))

            for room_name in Amity.office_allocations:
                print('OFFICE ALLOCATIONS')
                office_occupants = Amity.office_allocations[room_name]
                print (room_name)
                print ('-' * 50)
                print (', '.join(office_occupants))

    @staticmethod
    def print_unallocated(file_name):
        if file_name:
            file = open(file_name, 'w')
            file.write('%s\n' % 'UNALLOCATED LIVINGSPACE')
            for person in Amity.unallocated_livingspace:
                file.write("%s\n" % person)

            file.write('%s\n' % 'UNALLOCATED OFFICE')
            for person in Amity.unallocated_office:
                file.write("%s\n" % person)
            file.close
        else:
            print('UNALLOCATED LIVINGSPACE')
            print (', '.join(Amity.unallocated_livingspace))
            print('UNALLOCATED OFFICE')
            print (', '.join(Amity.unallocated_office))

    @staticmethod
    def print_room(room_name):
        if room_name not in Amity.room_data:
            print('The room does not exist')
        elif room_name in Amity.room_data:
            if Amity.room_data[room_name][1].upper() == 'LIVINGSPACE':
                living_occupants = Amity.livingspace_allocations[room_name]
                print (room_name)
                print ('-' * 30)
                print (', '.join(living_occupants))

            else:
                office_occupants = Amity.office_allocations[room_name]
                print (room_name)
                print ('-' * 30)
                print (', '.join(office_occupants))
        return('Room printed Successfully!')

    @staticmethod
    def save_state(db_name):
        # if os.path.exists(db_name):

        conn = sqlite3.connect(db_name)
        with conn:
            cursor = conn.cursor()
            cursor.executescript('''
                DROP TABLE IF EXISTS ROOMS;
                DROP TABLE IF EXISTS PERSON;
                CREATE TABLE PERSON(ID TEXT,
                NAME TEXT, JOB_TYPE TEXT, ACCOMODATION TEXT);
                CREATE TABLE ROOMS(NAME TEXT,ROOM_TYPE TEXT,
                CAPACITY INTEGER, OCCUPANTS TEXT );
                ''')

            for person_id in Amity.person_data:
                emp_id = person_id
                name = Amity.person_data[person_id][0]
                job_type = Amity.person_data[person_id][1]
                accomodation = Amity.person_data[person_id][2]
                cursor.execute(
                    '''INSERT INTO PERSON (ID, NAME, JOB_TYPE, ACCOMODATION)
                    VALUES(?,?,?,?)''', (emp_id, name, job_type, accomodation))

            for room_name in Amity.room_data:
                r_name = Amity.room_data[room_name][0]
                room_type = Amity.room_data[room_name][1]
                capacity = Amity.room_data[room_name][2]
                occupants = " "
                if room_type.upper() == 'LIVINGSPACE':
                    occupants = ', '.join(
                        Amity.livingspace_allocations[room_name])

                elif room_type.upper() == 'OFFICE':
                    occupants = ', '.join(
                        Amity.office_allocations[room_name])
                cursor.execute(
                    '''INSERT INTO ROOMS (NAME, ROOM_TYPE, CAPACITY, OCCUPANTS)
                    VALUES(?,?,?,?)''', (r_name, room_type, capacity, occupants))
            return('Data saved successfully')

    @staticmethod
    def load_state(db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        for row in cursor.execute('SELECT * FROM ROOMS'):
            Amity.room_data[row[0]] = [row[0], row[1], row[2]]
            if row[1] == 'LIVINGSPACE':
                Amity.livingspace_allocations[row[0]] = row[3].split()
            elif row[1] == 'OFFICE':
                Amity.office_allocations[row[0]] = row[3].split()
        for row in cursor.execute('SELECT * FROM PERSON'):
            Amity.person_data[row[0]] = [row[1], row[2], row[3]]
        return('Data has been loaded into the system successfully')
