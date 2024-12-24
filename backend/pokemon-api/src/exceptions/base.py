from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

def add_global_exception_handlers(app: FastAPI):

    logger = logging.getLogger("uvicorn.error")

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.error(f"Validation Error: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors(), "body": exc.body},
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.warning(f"HTTP Exception: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    @app.exception_handler(StarletteHTTPException)
    async def starlette_http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.warning(f"Starlette HTTP Exception: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
        logger.error(f"Database Error: {exc}")
        return JSONResponse(
            status_code=500,
            content={"detail": "A database error occurred."},
        )

    @app.exception_handler(KeyError)
    async def key_error_handler(request: Request, exc: KeyError):
        logger.error(f"KeyError: {str(exc)}")
        return JSONResponse(
            status_code=400,
            content={"detail": f"Missing key: {str(exc)}"},
        )

    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        logger.error(f"ValueError: {str(exc)}")
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)},
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled Exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "An internal server error occurred."},
        )
