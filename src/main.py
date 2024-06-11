import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import possibleCombinations

app = FastAPI()

class Score(BaseModel):
    score: str

@app.post("/verify/")
async def verify(score: Score):
    combinations = possibleCombinations.countPossibleCombinations(score.score)
    return {"combinations": combinations}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")