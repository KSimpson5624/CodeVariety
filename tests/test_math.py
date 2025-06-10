import pytest

from smartset import SmartSet

def test_check_numeric_invalid_number():
    a = SmartSet([1, 2, 3])
    with pytest.raises(ValueError, match='Scalar must be an integer or float.'):
        a._check_numeric('a')

def test_check_numeric_invalid_smartset():
    a = SmartSet(['a', 'b', 'c'])
    with pytest.raises(ValueError, match='SmartSet must contain only numbers for this operation.'):
        a._check_numeric(2)

def test_scale():
    nums = SmartSet([1, 2, 3])
    nums.scale(2)
    assert nums == SmartSet([2, 4, 6])

def test_scaled():
    nums = SmartSet([1, 2, 3])
    new_nums = nums.scaled(3)
    assert new_nums == SmartSet([3, 6, 9])

def test_mean():
    nums = SmartSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert nums.mean() == 5.5

def test_sum():
    nums = SmartSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert nums.sum() == 55

def test_min():
    nums = SmartSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert nums.min() == 1

def test_max():
    nums = SmartSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert nums.max() == 10

def test_normalize():
    nums = SmartSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    new_nums = nums.normalize()
    assert new_nums == SmartSet([
        0.10192943828752511,
        0.15289415743128767,
        0.2548235957188128,
        0.20385887657505022,
        0.30578831486257535,
        0.3567530340063379,
        0.40771775315010045,
        0.458682472293863,
        0.5096471914376256,
        0.050964719143762556
    ])

