from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def Hello():
    return "Hello FastApi"

@app.get('/isPrime/{numero}')
def IsPrime(numero: int):
    if numero <= 0 :
        return False
    elif numero == 1:
        return True
    else: 
        for i in range(2, numero+1):
            if numero%i == 0 and i<numero:
                return False
            elif i == numero:
                return True

@app.get('/fibonacci')
def Fibonacci(posicion: int):
    return 2