from availability import Availability
from user import User


def test_name_attribute_good():
    first = 'first'
    last = 'last'

    u = User(first, last, '', '')

    assert u.name == f'{first} {last}'


def test_to_string_good():
    first = 'first'
    last = 'last'
    email = 'email'
    phone = 'phone'

    u = User(first, last, email, phone)

    assert str(u) == f'Name: {first} {last},  Email: {email},  Phone Number: {phone}'


def test_availability_setter_good():
    u = User('', '', '', '')
    orig_avail = u.availability

    new_avail = Availability()
    u.availability = new_avail

    current_avail = u.availability

    assert orig_avail is not new_avail
    assert current_avail is not new_avail
