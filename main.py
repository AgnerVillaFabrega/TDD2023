from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def Hello():
    return "Hello FastApi"

@app.get('/isPrime/{numero}')
def IsPrime(numero: int):
    return True

@app.get('/fibonacci')
def Fibonacci(posicion: int):
    return 2