class Person(object):
    """This is the base person class."""

    def __init__(self, person_name, job_type):
        self.person_name = person_name
        self.job_type = job_type


class Fellow(Person):
    def __init__(self, person_name):
        super(Fellow, self).__init__(person_name, 'FELLOW')


class Staff(Person):
    def __init__(self, person_name):
        super(Staff, self).__init__(person_name, 'STAFF')
