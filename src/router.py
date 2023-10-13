from fastapi import APIRouter
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
    question_request: QuestionRequest, db: Session = Depends(get_db_session)
) -> JSONResponse:
    """
    Запрашивает вопросы с ответами через публичный API, сохраняет в БД
    уникальные вопросы с ответами и возвращает предыдущий сохранённый в БД
    вопрос или None при его отсутствии.
    """
    result = get_questions(question_request.questions_num, db)
    if result.get('public_api_error'):
        return JSONResponse(content=result, status_code=200)
    return JSONResponse(content=result, status_code=201)
