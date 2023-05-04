import pytest
from main import *
from starlette.testclient import TestClient

client = TestClient(app)

# def test_helloFastApi():
#     assert Hello() == "Hello FastApi"


def test_isPrime():
    response = client.get('/isPrime/59')
    assert response.status_code == 200
    assert response.json() == True


def test_fibonacci():
    response = client.get('/fibonacci/12')
    assert response.status_code == 200
    assert response.json() == {"Valor":233}

