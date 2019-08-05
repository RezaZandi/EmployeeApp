import datetime
from availability import Availability

class User():

    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.dob = None
        self._availability = Availability()

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, new_avail):
        self._availability = Availability.clone(new_avail)

    def get_availability(self, day, time):
        return self._availability.is_available(day, time)

    def create_availability(self, m_s, m_e, t_s, t_e, w_s, w_e, r_s, r_e, f_s, f_e, s_s, s_e, n_s, n_e):
        self._availability = Availability()
        self._availability.mon = (m_s, m_e)
        self._availability.tue = (t_s, t_e)
        self._availability.wed = (w_s, w_e)
        self._availability.thu = (r_s, r_e)
        self._availability.fri = (f_s, f_e)
        self._availability.sat = (s_s, s_e)
        self._availability.sun = (n_s, n_e)

    def __str__(self):
        return f'Name: {self.name},  Email: {self.email},  Phone Number: {self.phone_number}'


#TODO: Add Manager and Employee class that INHERIRITS from User class
#Employee should inherit from User.
#Manager should inherit from Employee.


class Employee(User):
    def __init__(self, first_name, last_name, email, phone_number, store, emp_type):
        super().__init__(first_name, last_name, email, phone_number)
        self.store = store
        self.type = emp_type
