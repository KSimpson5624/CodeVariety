
import pytest
from codevariety import SmartSet

def test_or_operator_union():
    a = SmartSet(['a', 'b'])
    b = SmartSet(['b', 'c'])
    result = a | b
    assert result == SmartSet(['a', 'b', 'c'])

def test_add_operator_union():
    a = SmartSet(['a', 'b'])
    b = SmartSet(['b', 'c'])
    result = a + b
    assert result == SmartSet(['a', 'b', 'c'])

def test_and_operator_intersection():
    a = SmartSet(['a', 'b', 'c'])
    b = SmartSet(['b', 'c', 'z'])
    result = a & b
    assert result == SmartSet(['b', 'c'])

def test_sub_operator_difference():
    a = SmartSet(['a', 'b', 'c'])
    b = SmartSet(['b', 'c', 'z'])
    result = a - b
    assert result == SmartSet(['a'])

def test_xor_operator_symmetric_difference():
    a = SmartSet(['a', 'b', 'c'])
    b = SmartSet(['b', 'c', 'z'])
    result = a ^ b
    assert result == SmartSet(['a', 'z'])

def test_ixor_operator_symmetric_difference():
    a = SmartSet(['a', 'b', 'c'])
    b = SmartSet(['b', 'c', 'z'])
    a ^= b
    assert a == SmartSet(['a', 'z'])

def test_iand_operator_intersection():
    a = SmartSet(['a', 'b', 'c'])
    b = SmartSet(['b', 'c', 'z'])
    a &= b
    assert a == SmartSet(['b', 'c'])

def test_ior_operator_union():
    a = SmartSet(['a', 'b', 'c'])
    b = SmartSet(['b', 'c', 'z'])
    a |= b
    assert a == SmartSet(['a', 'b', 'c', 'z'])

def test_isub_operator_difference():
    a = SmartSet(['a', 'b', 'c'])
    b = SmartSet(['b', 'c', 'z'])
    a -= b
    assert a == SmartSet(['a'])

def test_iadd_operator_union():
    a = SmartSet(['a', 'b', 'c'])
    b = SmartSet(['b', 'c', 'z'])
    a += b
    assert a == SmartSet(['a', 'b', 'c', 'z'])

@pytest.mark.parametrize('a, b, expected', [
    (['a', 'b', 'c'], ['b', 'c', 'z'], False),
    (['a', 'b', 'c'], ['c', 'b', 'a'], True),
])
def test_eq_operator(a, b, expected):
    assert (SmartSet(a) == SmartSet(b)) is expected

@pytest.mark.parametrize('a, b, expected', [
    (['a', 'b', 'c'], ['b', 'c', 'z'], True),
    (['a', 'b', 'c'], ['c', 'b', 'a'], False),
])
def test_ne_operator(a, b, expected):
    assert (SmartSet(a) != SmartSet(b)) is expected

def test_contains():
    a = SmartSet(['a', 'b', 'c'])
    assert 'a' in a

def test_not_contains():
    a = SmartSet(['a', 'b', 'c'])
    assert 'z' not in a

def test_len():
    a = SmartSet(['a', 'b', 'c'])
    assert len(a) == 3

def test_str():
    a = SmartSet(['a', 'b'])
    assert str(a) == "['a', 'b']" or str(a) == "['b', 'a']"


