import requests
from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from .models import QuestionAndAnswer
from .schemas import ResponseFromPublicAPI


def get_questions(questions_num: int, db: Session) -> dict:
    while True:
        url = f'https://jservice.io/api/random?count={questions_num}'
        response = requests.get(url)
        if response.status_code == 200:
            return {'public_api_error': f'Ответ стороннего API отличается от успешного.
                    Код ответа: {response.status_code}'}
        data = response.json()
        questions_received = ResponseFromPublicAPI(
            result=[
                {
                    'id': item['id'],
                    'question': item['question'],
                    'answer': item['answer'],
                    'created_at': item['created_at']
                    }
            for item in data]
        )
        question_ids = [item['id'] for item in questions_received.result]
        if check_questions_in_database(question_ids, db):
            continue
        latest_saved_question = fetch_latest_saved_question(db)
        save_new_questions_to_database(questions_received, db)
        return {
            'question': latest_saved_question
        } if latest_saved_question else {
            'question': 'Нет предыдущего сохранённого вопроса.'
        }
            
            
def check_questions_in_database(question_ids: list[int], db: Session) -> bool:
    for id in question_ids:
        query = select(QuestionAndAnswer).filter(id == id)
        result = db.execute(query)
        question = result.scalar_one_or_none()
        if question:
            return True
    return False


def fetch_latest_saved_question(db: Session) -> str | None:
    latest_record = db.query(QuestionAndAnswer).order_by(
        desc(QuestionAndAnswer.added_at)
    ).first()
    if latest_record:
        return latest_record.question
    return


def save_new_questions_to_database(questions: ResponseFromPublicAPI, db: Session) -> None:
    for item in questions.result:
        new_question = QuestionAndAnswer(
            id=item.id,
            question=item.question,
            answer=item.answer,
            created_at=item.created_at
        )
        db.add(new_question)
        db.commit()
