from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/test")
async def test():
    return {"message": "It works good! version = 20260605_1051"}

@app.get("/get_key1")
async def get_key1():
    return {"message": os.getenv("test_key1")}

@app.get("/get_ar1729")
async def get_key():
    return {"message": os.getenv("ar1729")}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
