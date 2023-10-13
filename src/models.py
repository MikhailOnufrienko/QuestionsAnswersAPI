from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import func, Column, DateTime, Integer, Text
from sqlalchemy.orm import DeclarativeBase


metadata = MetaData(schema='q_a')


class Base(DeclarativeBase):
    metadata = metadata


class QuestionAndAnswer(Base):
    __tablename__ = 'ques_and_ans'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime)
    added_at = Column(DateTime, nullable=False, default=func.now())

    def __init__(
        self, id: int, question: str,
        answer: str, created_at: datetime
    ) -> None:
        self.id = id
        self.question = question
        self.answer = answer
        self.created_at = created_at

    def __repr__(self) -> str:
        return self.question

