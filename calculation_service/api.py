from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculations.calculate import calculate
from calculations.expression import get_random_expression

app = FastAPI()


class ExpressionRequest(BaseModel):
    expression: str


@app.post("/api/calculate/")
def calculate_api_view(payload: ExpressionRequest):
    try:
        result = calculate(payload.expression)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/random-expression/")
def random_expression_api_view():
    expression = get_random_expression()
    return {"expression": expression}
