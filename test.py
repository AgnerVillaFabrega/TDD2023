import pytest
from main import Hello
from main import IsPrime
from main import Fibonacci



def test_helloFastApi():
    assert Hello() == "Hello FastApi"


def test_isPrime():
    assert IsPrime(3) == False


def test_fibonacci():
    assert Fibonacci(2) == 2

