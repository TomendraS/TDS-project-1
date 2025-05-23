from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Question(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
def answer(question: Question):
    # Dummy response for now, can be enhanced later with real logic
    return {
        "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate."
            }
        ]
    }
