from pydantic import BaseModel, Field, PositiveInt


class QuestionRequest(BaseModel):
    questions_num: PositiveInt = Field(strict=True, gt=0, le=100)


class ResponseFromPublicAPISingle(BaseModel):
    id: int
    question: str
    answer: str
    created_at: str


class ResponseFromPublicAPI(BaseModel):
    result: list[ResponseFromPublicAPISingle]


class QuestionResponse(BaseModel):
    question: str
