class Counter(object):
    isinstances = 0

    def __init__(self):
        Counter.isinstances += 1
        self.reset()

    def reset(self):
        self._value = 0

    def increment(self,amount = 1):
        self._value += amount

    def decremnet(self,amount = 1):
        self._value -= amount

    def getValue(self):
        return self._value

    def __str__(self):
        return str(self._value)

    def __eq__(self, other):
        if self is other:return True
        if type(self) != type(other): return False
        return self._value == other._value