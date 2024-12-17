from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/")
async def receive_json(request: Request, x_auth_user_id: str = Header(None)):
    print(f"All headers: {request.headers}")
    if not x_auth_user_id:
        raise HTTPException(status_code=400, detail="X-Auth-User-Id header missing")

    print(f"Received X-Auth-User-Id: {x_auth_user_id}")
    return JSONResponse(content={"message": "Data received", "auth_user_id": x_auth_user_id})
