import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not client:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")