"""
In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which isn’t actually a valid IPv4 (or IPv6) address.

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or more functions that collectively test your implementation of validate thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_numb3rs.py

"""


import pytest
from numb3rs import validate

def test_validate():
    assert validate("4.5.6.5") == True
    assert validate("277.0.5.6") == False
    assert validate("-4.150.15.654") == False
    assert validate("1555.223.235.2") == False
    assert validate("00.05.055.051") == True
    assert validate("20.555.1.2") == False
    assert validate("2.2.655.2") == False
    assert validate("2.2.2.655") == False
