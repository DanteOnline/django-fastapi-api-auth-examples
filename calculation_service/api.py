from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from calculations.calculate import calculate
from calculations.expression import get_random_expression
from auth import get_current_user


app = FastAPI()


class ExpressionRequest(BaseModel):
    expression: str


@app.post("/api/calculate/")
def calculate_api_view(payload: ExpressionRequest, current_user: str = Depends(get_current_user)):
    print(current_user)
    try:
        result = calculate(payload.expression)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/random-expression/")
def random_expression_api_view(current_user: str = Depends(get_current_user)):
    print(current_user)
    expression = get_random_expression()
    return {"expression": expression}
