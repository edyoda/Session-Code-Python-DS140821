## Fixtures: They are used to have something pre run 
## before the test.

## __init__ from OOP?
## __init__.py file in Packages?
## Something which runs for the very first time.

import pytest

@pytest.fixture
def pre_data():
    data = {'python':3,'django':2}
    return data
    
@pytest.fixture
def pre_data2():
    x = ['apple','mango']
    return x

def test_case_1(pre_data2):
    assert pre_data2[0] == 'mango'
    
def test_case_2(pre_data):
    django = 1
    assert pre_data['django'] == django
    