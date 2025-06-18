
import pytest
from codevariety import SmartSet

@pytest.mark.benchmark(group='Union')
def test_union_smartset(benchmark):
    a = SmartSet(range(1000))
    b = SmartSet(range(500, 1500))
    benchmark(lambda: a.union(b))

@pytest.mark.benchmark(group='Union')
def test_union_set(benchmark):
    a = set(range(1000))
    b = set(range(500, 1500))
    benchmark(lambda: a.union(b))

@pytest.mark.benchmark(group='Union')
def test_concat_list(benchmark):
    a = list(range(1000))
    b = list(range(500, 1500))
    benchmark(lambda: a + b)

@pytest.mark.benchmark(group='Sub')
def test_sub_smartset(benchmark):
    a = SmartSet(range(1000))
    b = SmartSet(range(500))
    benchmark(lambda: a - b)

@pytest.mark.benchmark(group='Sub')
def test_sub_set(benchmark):
    a = set(range(1000))
    b = set(range(500, 1500))
    benchmark(lambda: a - b)

@pytest.mark.benchmark(group='Add')
def test_add_smartset(benchmark):
    def setup_and_add():
        a = SmartSet()
        for x in range(1000):
            a.add(x)
    benchmark(setup_and_add)

@pytest.mark.benchmark(group='Add')
def test_add_set(benchmark):
    def setup_and_add():
        a = set()
        for x in range(1000):
            a.add(x)
    benchmark(setup_and_add)

@pytest.mark.benchmark(group='Add')
def test_add_list(benchmark):
    def setup_and_add():
        a = []
        for x in range(1000):
            a.append(x)
    benchmark(setup_and_add)

@pytest.mark.benchmark(group='Add')
def test_add_full_smartset(benchmark):
    import random
    a = SmartSet()
    for x in range(500):
        a.add(random.randint(0, 1000))
    def setup_and_add(a:SmartSet):
        for i in range(1000):
            a.add(i)
    benchmark(setup_and_add, a)

@pytest.mark.benchmark(group='Add')
def test_add_full_set(benchmark):
    import random
    a = set()
    for x in range(500):
        a.add(random.randint(0, 1000))
    def setup_and_add(a:set):
        for i in range(1000):
            a.add(i)
    benchmark(setup_and_add, a)

@pytest.mark.benchmark(group='remove')
def test_raw_remove_smartset(benchmark):
    def setup_and_remove():
        a = SmartSet([1, 2, 3])
        a.remove(1)
    benchmark(setup_and_remove)

@pytest.mark.benchmark(group='remove')
def test_raw_remove_set(benchmark):
    def setup_and_remove():
        a = {1, 2, 3}
        a.remove(1)
    benchmark(setup_and_remove)

@pytest.mark.benchmark(group='remove')
def test_remove_smartset(benchmark):
    def setup_and_remove():
        a = SmartSet(range(1000))
        for i in range(500):
            a.remove(i)
    benchmark(setup_and_remove)

@pytest.mark.benchmark(group='remove')
def test_remove_set(benchmark):
    def setup_and_remove():
        a = set(range(1000))
        for i in range(500):
            a.remove(i)
    benchmark(setup_and_remove)

@pytest.mark.benchmark(group='remove')
def test_raw_remove_list(benchmark):
    def setup_and_remove():
        a = [1, 2, 3]
        a.remove(1)
    benchmark(setup_and_remove)

@pytest.mark.benchmark(group='remove')
def test_remove_list(benchmark):
    def setup_and_remove():
        a = list(range(1000))
        for i in range(500):
            a.remove(i)
    benchmark(setup_and_remove)