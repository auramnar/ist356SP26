# fastparams2.py

from fastapi import FastAPI, Header, Query, HTTPException

app = FastAPI() # initialize app with routes and endpoints

@app.get("/calculator/{operator}") # get end point with path parameter
def read_item(
    operator: str,
    a: float = Query(),   # query parameter
    b: float = Query(),   # 
    h: str = Header(default=None)  # safer default
):
    if operator == "add":
        result = a + b
    elif operator == "sub":
        result = a - b
    elif operator == "mul":
        result = a * b
    elif operator == "div":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a / b
    else:
        raise HTTPException(
            status_code=404,
            detail="Operator not found. should be: add, sub, mul, div"
        )

    return {
        "operator": operator,
        "a": a,
        "b": b,
        "result": result,
        "h": h
    }