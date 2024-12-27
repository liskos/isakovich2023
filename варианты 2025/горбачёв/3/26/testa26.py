import a26

def test1():
    assert a26.f('test1.txt') == (4, 1)

def test2():
    assert a26.f('test2.txt') == (11, 0)

def test3():
    assert a26.f('test3.txt') == (12, 2)

def test4():
    assert a26.f('test4.txt') == (11, 2)