def incr(x):
    return x + 1

def test_incr():
    assert incr(3) == 4

def test_incr_err():
    assert incr(3) == 5