from datetime import datetime

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    questions_num: int


class ResponseFromPublicAPISingle(BaseModel):
    id: int
    question: str
    answer: str
    created_at: str


class ResponseFromPublicAPI(BaseModel):
    result: list[ResponseFromPublicAPISingle]


class QuestionResponseSingle(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    questions: list[QuestionResponseSingle]
