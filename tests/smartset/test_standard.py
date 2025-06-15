
from src.codevariety import SmartSet

def test_union():
    a = SmartSet([1, 2, 3])
    b = SmartSet([4, 5, 6])
    result = a | b
    assert result == SmartSet([1, 2, 3, 4, 5, 6])

def test_copy():
    a = SmartSet([1, 2, 3])
    b = a.copy()
    assert a == b

def test_add():
    a = SmartSet([1, 2, 3])
    a.add(4)
    assert a == SmartSet([1, 2, 3, 4])

def test_remove():
    a = SmartSet([1, 2, 3])
    a.remove(1)
    assert a == SmartSet([2, 3])

def test_discard():
    a = SmartSet([1, 2, 3])
    a.discard(1)
    assert a == SmartSet([2, 3])

def test_update():
    a = SmartSet([1, 2, 3])
    a.update([4, 5, 6])
    assert a == SmartSet([1, 2, 3, 4, 5, 6])

def test_difference():
    a = SmartSet([1, 2, 3])
    b = SmartSet([1, 5, 6])
    result = a.difference(b)
    assert result == SmartSet([2, 3])

def test_symmetric_difference():
    a = SmartSet([1, 2, 3])
    b = SmartSet([1, 5, 6])
    result = a.symmetric_difference(b)
    assert result == SmartSet([2, 3, 5, 6])

def test_intersection():
    a = SmartSet([1, 2, 3])
    b = SmartSet([1, 5, 3])
    result = a.intersection(b)
    assert result == SmartSet([1, 3])

def test_issubset():
    a = SmartSet([1, 2, 3])
    b = SmartSet([1, 2])
    assert b.issubset(a) == True

def test_issuperset():
    a = SmartSet([1, 2, 3])
    b = SmartSet([1, 2])
    assert a.issuperset(b) == True

def test_isdisjoint():
    a = SmartSet([1, 2, 3])
    b = SmartSet([1, 2])
    assert a.isdisjoint(b) == False

def test_includes():
    a = SmartSet([1, 2, 3])
    b = SmartSet([1, 2])
    assert a.includes(b) == True

def test_clear():
    a = SmartSet([1, 2, 3])
    assert len(a) == 3
    a.clear()
    assert len(a) == 0

def test_pop_unsorted():
    a = SmartSet(['a', 'b', 'c'])
    value = a.pop()
    assert value == 'a' or value == 'b' or value == 'c'
    assert len(a) == 2

def test_pop_sorted():
    a = SmartSet(['b', 'a', 'c'])
    a.sort()
    value = a.pop()
    assert a == SmartSet(['b', 'c']), 'Incorrect value was removed from SmartSet after pop() on sorted data.'
    assert value == 'a', f'Top value was not correct in pop() with sorted SmartSet. Expected: "a". Got: "{value}"'




