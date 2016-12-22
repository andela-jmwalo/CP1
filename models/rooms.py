class Room(object):
    """This is the base room Class."""
    def __init__(self):
        pass


class Office(Room):
    """This class LivingSpace inherits from Room class .
    It has a capacity of 6"""
    def __init__(self, room_name):
        self.room_name = room_name
        self.room_type = 'OFFICE'
        self.capacity = 6


class LivingSpace(Room):
    """This class LivingSpace inherits from Room class.
    It has a capacity of 4."""

    def __init__(self, room_name):

        self.room_name = room_name
        self.room_type = 'LIVINGSPACE'
        self.capacity = 4
