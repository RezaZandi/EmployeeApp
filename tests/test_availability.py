import pytest
from random import randint
from availability import Availability


def _attr_check_good(attr_name):
    a = Availability()
    assert getattr(a, attr_name) is None

    start = randint(0, 50)
    end = randint(51, 100)
    setattr(a, attr_name, (start, end))

    assert getattr(a, attr_name) == [start, end]


def _attr_check_bad(attr_name):
    a = Availability()
    with pytest.raises(AssertionError):
        setattr(a, attr_name, (2, 1))


def test_mon_attr():
    _attr_check_good('mon')
    _attr_check_bad('mon')


def test_tue_attr():
    _attr_check_good('tue')
    _attr_check_bad('tue')


def test_wed_attr():
    _attr_check_good('wed')
    _attr_check_bad('wed')


def test_thu_attr():
    _attr_check_good('thu')
    _attr_check_bad('thu')


def test_fri_attr():
    _attr_check_good('fri')
    _attr_check_bad('fri')


def test_sat_attr():
    _attr_check_good('sat')
    _attr_check_bad('sat')


def test_sun_attr():
    _attr_check_good('sun')
    _attr_check_bad('sun')


def _is_available_check(attr_name, day):
    start = randint(0, 25)
    end = randint(26, 50)
    good = randint(start, end)
    bad = randint(51, 100)

    a = Availability()
    assert a.is_available(day, good) is False
    assert a.is_available(day, bad) is False

    setattr(a, attr_name, (start, end))
    assert a.is_available(day, good) is True
    assert a.is_available(day, bad) is False


def test_mon_available():
    _is_available_check('mon', 'MONDAY')


def test_tue_available():
    _is_available_check('tue', 'TUESDAY')


def test_wed_available():
    _is_available_check('wed', 'WEDNESDAY')


def test_thu_available():
    _is_available_check('thu', 'THURSDAY')


def test_fri_available():
    _is_available_check('fri', 'FRIDAY')


def test_sat_available():
    _is_available_check('sat', 'SATURDAY')


def test_sun_available():
    _is_available_check('sun', 'SUNDAY')
