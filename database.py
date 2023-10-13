from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker

from config import settings


DATABASE_DSN: str = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'.format(
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    name=settings.DB_NAME
)

engine: Engine = create_engine(DATABASE_DSN, echo=True)

session: Session = sessionmaker(engine)


async def get_db_session() -> Session:
    with session() as session:
        yield session 
