from fastapi import APIRouter, Depends, Path
from fastapi.responses import StreamingResponse
from src.modules.sudoku.service import SudokuService

router = APIRouter(prefix="/sudoku", tags=["sudoku"])


@router.get("/health")
def health():
    return {"health": True}


@router.get("/solution/{sudoku_str}/png")
def solve(
    sudoku_str: str = Path(
        ...,
        example="800000000003600000070090200050007000000045700000100030001000068008500010090000400",
    ),
    service: SudokuService = Depends(SudokuService),
):
    stream = service.solve(sudoku_str)
    return StreamingResponse(
        content=stream,
        media_type="application/octet-stream",
        headers={"Content-Disposition": 'attachment; filename="solved.png"'},
        status_code=200,
    )
