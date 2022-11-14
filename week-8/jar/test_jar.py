"""
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:

__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. 
If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

__str__ should return a str with  🍪, where  is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.

withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.

capacity should return the cookie jar’s capacity.

size should return the number of cookies actually in the cookie jar.


Either before or after you implement jar.py, additionally implement, in a file called test_jar.py, four or more functions that collectively test your implementation of Jar thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_jar.py

"""


from jar import Jar
import pytest


def test_init():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.__init__(-3)
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar._size == 3
    jar.deposit(2)
    assert jar._size == 5
    with pytest.raises(ValueError):
        jar.deposit(9)


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(2)
    assert jar._size == 9
    jar.withdraw(5)
    assert jar._size == 4
    jar.withdraw(3)
    assert jar._size == 1
    with pytest.raises(ValueError):
        jar.withdraw(5)
