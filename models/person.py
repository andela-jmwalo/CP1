class Person(object):
    """This is the base person class."""

    def __init__(self):
        pass


class Fellow(Person):
    """This class Fellow inherits from Person class ."""

    def __init__(self, person_name):
        self.person_name = person_name
        self.job_type = 'STAFF'


class Staff(Person):
    """This class Fellow inherits from Person class ."""

    def __init__(self, person_name):
        self.person_name = person_name
        self.job_type = 'FELLOW'
