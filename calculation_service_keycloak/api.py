from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from calculations.calculate import calculate
from calculations.expression import get_random_expression
from auth import decode_token


app = FastAPI()


class ExpressionRequest(BaseModel):
    expression: str


@app.post("/api/calculate/")
def calculate_api_view(expression_request: ExpressionRequest, payload=Depends(decode_token)):
    print(payload)
    try:
        result = calculate(expression_request.expression)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/random-expression/")
def random_expression_api_view(payload=Depends(decode_token)):
    print(payload)
    expression = get_random_expression()
    return {"expression": expression}
