class Room(object):
    """This is the base room Class."""

    def __init__(self, room_name, room_type, capacity):
        self.room_name = room_name
        self.room_type = room_type
        self.capacity = capacity


class Office(Room):
    """This class LivingSpace inherits from Room class . It has a capacity of 6"""

    def __init__(self, room_name, room_type='OFFICE'):
        super(Office, self).__init__(room_name, 'OFFICE', 6)


class LivingSpace(Room):
    """This class LivingSpace inherits from Room class. It has a capacity of 4."""

    def __init__(self, room_name, room_type='	LIVINGSPACE', capacity=4):
        super(LivingSpace, self).__init__(room_name, 'LIVINGSPACE', 4)
