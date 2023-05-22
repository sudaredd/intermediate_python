try:
    a = 5/1
    b = a + 10
except ZeroDivisionError as ex:
    print(ex)
except TypeError as ex:
    print(ex)
else:
    print("all good")
finally:
    print("finally block")

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_val(val):
    if val > 50:
        raise ValueTooHighError('Value is too high')
    if val < 10:
        raise ValueTooSmallError("value is too small", val)

try:
    test_val(9)
except ValueTooHighError as ex:
    print(ex)
except ValueTooSmallError as ex:
    print(ex.message, ex.value)