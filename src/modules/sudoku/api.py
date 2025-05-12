from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from src.modules.sudoku.service import SudokuService

router = APIRouter(prefix="/sudoku", tags=["sudoku"])


@router.get("/health")
def health():
    return {"health": True}


@router.get("/solution/{sudoku_str}/png")
def solve(sudoku_str: str, service: SudokuService = Depends(SudokuService)):
    stream = service.solve(sudoku_str)
    return StreamingResponse(
        content=stream,
        media_type="application/octet-stream",
        headers={"Content-Disposition": 'attachment; filename="solved.png"'},
        status_code=200,
    )
