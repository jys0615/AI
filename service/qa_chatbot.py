import json
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from schema.qa_schema import QAResponse

# 간단한 TF-IDF 기반 Q&A 응답
def get_best_answer(merchant_id: str, customer_question: str) -> QAResponse:
    with open("model/merchant_qa_data.json", "r", encoding="utf-8") as f:
        qa_data = json.load(f)

    merchant_qas = qa_data.get(merchant_id, [])
    if not merchant_qas:
        return QAResponse(matched_question="", answer="죄송합니다. 등록된 답변이 없습니다.", score=0.0)

    questions = [item["question"] for item in merchant_qas]
    answers = [item["answer"] for item in merchant_qas]

    tfidf = TfidfVectorizer().fit(questions + [customer_question])
    vectors = tfidf.transform(questions + [customer_question])

    similarities = cosine_similarity(vectors[-1], vectors[:-1])[0]
    best_idx = similarities.argmax()
    best_score = similarities[best_idx]

    return QAResponse(
        matched_question=questions[best_idx],
        answer=answers[best_idx],
        score=float(best_score)
    )