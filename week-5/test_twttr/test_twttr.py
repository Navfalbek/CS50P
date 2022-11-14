"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, 
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly,
each of whose names should begin with test_ so that you can execute your tests with: 

pytest test_twttr.py

"""


from twttr import shorten
import pytest


def test_shorten():
    assert shorten("dropdown") == "drpdwn"
    assert shorten("randomized") == "rndmzd"
    assert shorten("choosing") == "chsng"
    assert shorten("Generator") == "Gnrtr"
    assert shorten("ANOTHER") == "NTHR"
    assert shorten("MAKEIT4") == "MKT4"
    assert shorten("LET'SGO,") == "LT'SG,"
