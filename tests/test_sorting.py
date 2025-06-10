
from smartset import SmartSet

def test_sort():
    a = SmartSet([6, 3, 5, 4, 7, 1])
    a.sort()
    assert str(a) == "[1, 3, 4, 5, 6, 7]"

def test_unsort():
    # Using 10 items to lower the possibility of a failure. With 10 there is a 0.000028% chance of it randomly landing in sorted order.
    a = SmartSet(['b', 'a', 'z', 'e', 'n', 'k', 'o', 'r', 'l', 'p'])
    a.sort()
    assert str(a) == "['a', 'b', 'e', 'k', 'l', 'n', 'o', 'p', 'r', 'z']"
    a.unsort()
    assert str(a) != "['a', 'b', 'e', 'k', 'l', 'n', 'o', 'p', 'r', 'z']"