# the function which we are unit testing.
def func(x):
    if x%2 == 0:
        return x+5
    else:
        return x-5

def test_method():
    assert func(3) == 8
    
def test_method_2():
    assert func(2) == 7
    
# cmd: py.test test.py