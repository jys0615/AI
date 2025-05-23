
# AI
=======
'''
ai_service/
├── main.py                      # FastAPI 진입점
├── router/
│   ├── style_transform.py       # 감성 문체 변환 API 라우터
│   └── merchant_qa.py           # Q&A 챗봇 API 라우터
├── service/
│   ├── style_converter.py       # GPT 문체 변환 기능 구현
│   └── qa_chatbot.py            # Q&A 유사 질문 매칭, 응답 생성
├── model/
│   ├── tfidf_model.pkl          # TF-IDF 벡터 저장 파일 (QA용)
│   └── merchant_qa_data.json    # 소상공인별 Q&A JSON DB
├── schema/
│   ├── style_schema.py          # Pydantic 모델 - 문체 변환
│   └── qa_schema.py             # Pydantic 모델 - Q&A 요청/응답
├── utils/
│   └── text_similarity.py       # 유사도 계산 함수 (TF-IDF, Cosine 등)
├── config/
│   └── openai_config.py         # GPT API 키 및 호출 설정
├── requirements.txt             # 의존성 패키지 목록
└── README.md                    # 설명서
'''
