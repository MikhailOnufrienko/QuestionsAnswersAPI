import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from config import settings
from database import get_db_session
from src.router import router


app = FastAPI(
    title=settings.SERVICE_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    error_messages = [error["msg"] for error in exc.errors()]
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": ", ".join(error_messages)},
    )


app.include_router(router, prefix='/api/v1', tags=['questions'])


@app.on_event('startup')
def startup() -> None:
    global postgres
    for session in get_db_session():
        postgres = session


@app.on_event('shutdown')
def shutdown() -> None:
    postgres.close()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8001, 
        reload=True
    )
