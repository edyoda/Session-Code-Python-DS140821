# Way of Selecting or filtering test cases:
# 1) Running the test cases with substring matching approach.


def func(x):
    if x%2 == 0:
        return x+5
    else:
        return x-5
        
def test_krishna():
    assert func(3) == 8

def test_krishna2():
    assert func(2) == 7
    
def test_mohit():
    assert func(1) == -4
    

#cmd: py.test -k test_m

