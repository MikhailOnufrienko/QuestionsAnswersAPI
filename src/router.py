from typing import Annotated

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db_session
from .schemas import QuestionRequest, QuestionResponse
from .service import get_questions


router = APIRouter()


@router.post(
    '/questions',
    status_code=201,
    response_model=QuestionResponse,
    summary='Получить через публичный API новые вопросы.'
)
def questions(
    question_request: Annotated[
        QuestionRequest, Body(
            description='Количество вопросов, запрашиваемых из ресурса с вопросами.',
            example={'questions_num': 1}
        )
    ], db: Session = Depends(get_db_session)
) -> JSONResponse:
    """
    Запрашивает вопросы с ответами через публичный API, сохраняет в БД
    уникальные вопросы с ответами и возвращает предыдущий сохранённый в БД
    вопрос или None при его отсутствии или ошибку.
    Структура ответа:

    - **question**: предыдущий сохранённый в БД вопрос
    """
    result = get_questions(question_request.questions_num, db)
    if result.get('public_api_error'):
        return JSONResponse(content=result, status_code=200)
    if result.get('input_error'):
        return JSONResponse(content=result, status_code=422)
    return JSONResponse(content=result, status_code=201)
