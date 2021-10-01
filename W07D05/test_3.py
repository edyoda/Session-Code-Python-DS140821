## Way of selecting or filtering test cases:
# 2) Marking the test cases.

import pytest

def func(x):
    if x%2 == 0:
        return x+5
    else:
        return x-5
       
@pytest.mark.mohit
def test_1():
    assert func(3) == 8

@pytest.mark.krishna 
def test_2():
    assert func(2) == 7
    
@pytest.mark.krishna 
def test_3():
    assert func(1) == -4
   
# cmd: py.test -m krishna
    
    