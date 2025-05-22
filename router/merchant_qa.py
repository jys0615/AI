from fastapi import APIRouter, HTTPException
from schema.qa_schema import QARequest, QAResponse
from service.qa_chatbot import get_best_answer

router = APIRouter()

@router.post("/merchant", response_model=QAResponse)
def answer_customer_question(request: QARequest):
    try:
        return get_best_answer(request.merchant_id, request.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))