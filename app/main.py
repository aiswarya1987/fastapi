from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Sample Python Service", version="1.0.0")

# simple "readiness" toggle to simulate startup/teardown phases
is_ready = {"ready": True}

class SumRequest(BaseModel):
    a: float
    b: float

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    return {"ready": bool(is_ready["ready"])}

@app.get("/version")
def version():
    return {"service": app.title, "version": app.version}

@app.post("/sum")
def sum_numbers(payload: SumRequest):
    return {"result": payload.a + payload.b}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="item_id must be >= 0")
    # pretend this came from storage
    return {"id": item_id, "name": f"item-{item_id}"}
