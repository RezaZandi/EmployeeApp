from demo import Demo
from availability import Availability
from user import User


def set_input_mock(ctx, responses):
    values = list(reversed(responses))
    def input_mock(*args, **kwargs):
        return values.pop()
    ctx.setattr('builtins.input', input_mock)


def create_user():
    u = User('First', 'Last', 'Email', 'Phone')
    u.create_availability(
        20, 22,
        22, 24,
        24, 26,
        26, 28,
        28, 30,
        30, 32,
        32, 34
    )
    return u


def test_create_user_good(monkeypatch):
    with monkeypatch.context() as m:
        set_input_mock(m, ['First', 'Last', 'Email', '1234567'])

        d = Demo()
        d.create_user()

        assert len(d.user_list) == 1
        assert d.user_list[0].first_name == 'First'
        assert d.user_list[0].last_name == 'Last'
        assert d.user_list[0].email == 'Email'
        assert d.user_list[0].phone_number == 1234567


def test_set_availability_not_found(monkeypatch):
    with monkeypatch.context() as m:
        set_input_mock(m, ['non-existent'])

        d = Demo()

        assert d.set_availability() is False


def test_set_availability_discard(monkeypatch):
    with monkeypatch.context() as m:
        set_input_mock(m, [
            'Email',
            '1', '2',
            '3', '4',
            '5', '6',
            '7', '8',
            '9', '10',
            '11', '12',
            '13', '14',
            'no'
        ])

        d = Demo()
        d.user_list.append(create_user())

        before_id = id(d.user_list[0].availability)
        assert d.set_availability() is False
        assert before_id == id(d.user_list[0].availability)


def test_set_availability_good(monkeypatch):
    with monkeypatch.context() as m:
        set_input_mock(m, [
            'Email',
            '1', '2',
            '3', '4',
            '5', '6',
            '7', '8',
            '9', '10',
            '11', '12',
            '13', '14',
            'yes'
        ])

        d = Demo()
        d.user_list.append(create_user())

        old_id = id(d.user_list[0].availability)
        assert d.set_availability() is True
        assert old_id != id(d.user_list[0].availability)
        assert d.user_list[0].availability.mon == [1, 2]
        assert d.user_list[0].availability.tue == [3, 4]
        assert d.user_list[0].availability.wed == [5, 6]
        assert d.user_list[0].availability.thu == [7, 8]
        assert d.user_list[0].availability.fri == [9, 10]
        assert d.user_list[0].availability.sat == [11, 12]
        assert d.user_list[0].availability.sun == [13, 14]


def test_view_availability_not_found(monkeypatch):
    with monkeypatch.context() as m:
        set_input_mock(m, ['non-existent'])

        d = Demo()

        assert d.view_availability() is False


def test_view_availability_good(monkeypatch):
    with monkeypatch.context() as m:
        set_input_mock(m, [
            'Email', 'MONDAY', '21', # good
            'Email', 'MONDAY', '30'  # bad
        ])

        d = Demo()
        d.user_list.append(create_user())

        assert d.view_availability() is True
        assert d.view_availability() is False


def test_delete_user_not_found(monkeypatch):
    with monkeypatch.context() as m:
        set_input_mock(m, ['non-existent'])

        d = Demo()

        assert d.delete_user() is False


def test_delete_user_good(monkeypatch):
    with monkeypatch.context() as m:
        set_input_mock(m, ['Email'])

        d = Demo()
        d.user_list.append(create_user())

        assert d.delete_user() is True
        assert len(d.user_list) == 0
