from fastapi import FastAPI

from src.modules.sudoku.api import router as sudoku_router

app = FastAPI()

app.include_router(sudoku_router)

