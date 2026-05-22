from fastapi import FastAPI
from routes.operations import router

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Welcome to FastAPI!"}

app.include_router(router)