import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from calculator import add, sub, multiply, div

def test_add():
    assert add(5,3) == 8
    assert add(0,0) == 0
    assert add(-1,1) == 0
def test_sub():
    assert sub(5,3) == 2
    assert sub(-1,1) == -2
    assert sub(5,0) == 5
def test_multipy():
    assert multiply(5,2) == 10
    assert multiply(-1,5) == -5
    assert multiply(5,0) == 0
def test_div():
    assert div(10,2) == 5
    assert div(9,3) == 3
    assert div(0,6) == 0
    assert div(5,0) == 'Cannot divide by 0'             