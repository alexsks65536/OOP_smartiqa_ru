"""
class JustCounter:
    _secretCount = 0

    def count(self):
        self._secretCount += 1
        print(self._secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter._secretCount)
"""


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount)
