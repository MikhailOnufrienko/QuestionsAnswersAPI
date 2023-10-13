from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import Column, DateTime, Integer, String, Text
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
    added_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __init__(
        self, id: int, question: str,
        answer: str, created_at: datetime, added_at: datetime
    ) -> None:
        self.id = id
        self.question = question
        self.answer = answer
        self.created_at = created_at
        self.added_at = added_at

    def __repr__(self) -> str:
        return self.question

