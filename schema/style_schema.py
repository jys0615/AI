from pydantic import BaseModel

class StyleTransformRequest(BaseModel):
    original_text: str

class StyleTransformResponse(BaseModel):
    original: str
    transformed: str