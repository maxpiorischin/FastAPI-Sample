from fastapi import FastAPI
from app.services.sample import sample_function

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is the root of the app."}

@app.get("/sample")
async def sample():
    result = await sample_function()
    return {"message": result}
