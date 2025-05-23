from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Question(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
def answer(question: Question):
    # Dummy response for now
    return {
        "answer": "This is a test answer. The real answer will come later.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/",
                "text": "Example link to Discourse"
            }
        ]
    }
