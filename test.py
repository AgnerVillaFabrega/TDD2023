import pytest

def test_helloFastApi():
    assert HelloFastApi() == "Hello Fast Api"


def test_isPrime():
    assert IsPrime(2) == True


def test_fibonacci():
    assert Fibonacci(2) == 2

