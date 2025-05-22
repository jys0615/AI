from fastapi import APIRouter, HTTPException
from schema.style_schema import StyleTransformRequest, StyleTransformResponse
from service.style_converter import convert_style

router = APIRouter()

@router.post("/style-transform", response_model=StyleTransformResponse)
def transform_style(request: StyleTransformRequest):
    try:
        transformed = convert_style(request.original_text)
        return StyleTransformResponse(original=request.original_text, transformed=transformed)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))