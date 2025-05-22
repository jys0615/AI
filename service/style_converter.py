from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def convert_style(original_text: str) -> str:
    prompt = (
        "다음 가게 소개글을 MZ세대에게 어필할 수 있도록 감성적인 문체로 자연스럽게 바꿔줘. "
        "과하지 않게, 200자 이내로 부탁해.\n\n"
        f"원문: {original_text}\n\n감성 문체:"
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # 필요 시 gpt-4로 교체 가능
        messages=[
            {"role": "system", "content": "당신은 감성적인 카피라이팅 전문가입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    
    transformed = response.choices[0].message.content.strip()
    return transformed