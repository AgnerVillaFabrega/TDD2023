import pytest
from main import *
from starlette.testclient import TestClient

client = TestClient(app)

# def test_helloFastApi():
#     assert Hello() == "Hello FastApi"

def test_isPrime():
    assert isPrime(59) == True


def test_fibonacci():
    assert fibonacci(12) == {"Valor":233}

#EndPoints
def test_endpoint_isPrime():
    response = client.get('/isPrime/59')
    assert response.status_code == 200
    assert response.json() == True


def test_endpoint_fibonacci():
    response = client.get('/fibonacci/12')
    assert response.status_code == 200
    assert response.json() == {"Valor":233}

