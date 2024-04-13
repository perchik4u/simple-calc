from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from calculate import calculate_expression


app = FastAPI()

app.mount("/", StaticFiles(directory=".", html=True), name="static")



@app.post("calculate.py")
async def calculate(expression: str):
    result = calculate_expression(expression)  
    return result
