from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple

def get_most_similar(query: str, corpus: List[str]) -> Tuple[int, float]:
    """
    주어진 질문(query)과 corpus 내 질문들 간의 TF-IDF 코사인 유사도를 계산해
    가장 유사한 인덱스와 유사도를 반환
    """
    tfidf = TfidfVectorizer().fit(corpus + [query])
    vectors = tfidf.transform(corpus + [query])
    similarities = cosine_similarity(vectors[-1], vectors[:-1])[0]
    best_index = similarities.argmax()
    best_score = similarities[best_index]
    return best_index, float(best_score)