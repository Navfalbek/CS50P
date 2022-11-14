"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, 
wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, 
but main is only called if the value of __name__ is "__main__"

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py

"""


import pytest
from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("N") == False
    assert is_valid("FI1.67") == False
    assert is_valid("thelongstring") == False
    assert is_valid("BNN22K") == False
    assert is_valid("CS05") == False
    assert is_valid("77OOD") == False
    assert is_valid("44") == False
