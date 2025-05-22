from pydantic import BaseModel
from typing import List, Optional

class QAEntry(BaseModel):
    question: str
    answer: str

class QAResponse(BaseModel):
    matched_question: str
    answer: str
    score: float

class QARequest(BaseModel):
    merchant_id: str
    question: str