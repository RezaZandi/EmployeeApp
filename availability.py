
class Availability():
    _INDICIES = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6,
    }

    def __init__(self):
        self._schedule = [None] * 7

    @staticmethod
    def clone(old):
        new = Availability()
        for day in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:
            val = getattr(old, day)
            if val is not None:
                setattr(new, day, val)
        return new

    def _convert(self, day):
        assert day in self._INDICIES
        return self._INDICIES[day]

    def _get_day(self, day):
        return self._schedule[self._convert(day)]

    def _set_day(self, day, startend):
        start, end = startend
        assert start <= end
        self._schedule[self._convert(day)] = [start, end]

    def _check_day(self, day, time):
        entry = self._schedule[self._convert(day)]
        return entry is not None and entry[0] <= time <= entry[1]

    @property
    def mon(self):
        return self._get_day('monday')

    @mon.setter
    def mon(self, startend):
        self._set_day('monday', startend)

    @property
    def tue(self):
        return self._get_day('tuesday')

    @tue.setter
    def tue(self, startend):
        self._set_day('tuesday', startend)

    @property
    def wed(self):
        return self._get_day('wednesday')

    @wed.setter
    def wed(self, startend):
        self._set_day('wednesday', startend)

    @property
    def thu(self):
        return self._get_day('thursday')

    @thu.setter
    def thu(self, startend):
        self._set_day('thursday', startend)

    @property
    def fri(self):
        return self._get_day('friday')

    @fri.setter
    def fri(self, startend):
        self._set_day('friday', startend)

    @property
    def sat(self):
        return self._get_day('saturday')

    @sat.setter
    def sat(self, startend):
        self._set_day('saturday', startend)

    @property
    def sun(self):
        return self._get_day('sunday')

    @sun.setter
    def sun(self, startend):
        self._set_day('sunday', startend)

    def is_available(self, day, time):
        my_day = day.lower()
        rv = self._check_day(my_day, time)
        return rv
