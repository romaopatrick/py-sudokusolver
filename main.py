from fastapi import FastAPI

from src.modules.shared.error_middleware import ErrorMiddleware
from src.modules.sudoku.api import router as sudoku_router

app = FastAPI()

app.add_middleware(ErrorMiddleware)
app.include_router(sudoku_router)

