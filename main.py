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

@app.get('/fibonacci/{position}')
def Fibonacci(position: int):
    current_position = 1
    future_position  = 1
    count = 1
    if position <= 0:
        return {"Numero":0}
    
    while count <= position:
        value_position = current_position + future_position
        current_position = future_position
        future_position = value_position
        count+= 1
    
    return{"Valor": current_position}
    