from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse, StreamingResponse
from src.modules.sudoku.service import SudokuService

router = APIRouter(prefix="/sudoku", tags=["sudoku"])


@router.get("/health")
def health():
    return {"health": True}


@router.get("/solution/{sudoku_str}/png")
def solve_png(
    sudoku_str: str = Path(
        ...,
        example="800000000003600000070090200050007000000045700000100030001000068008500010090000400",
    ),
    service: SudokuService = Depends(SudokuService),
):
    sudoku = service.solve(sudoku_str)
    return StreamingResponse(
        content=sudoku.as_stream(),
        media_type="application/octet-stream",
        headers={"Content-Disposition": 'attachment; filename="solved.png"'},
        status_code=200,
    )


@router.get("/solution/{sudoku_str}")
def solve_flatten(
    sudoku_str: str = Path(
        ...,
        example="800000000003600000070090200050007000000045700000100030001000068008500010090000400",
    ),
    service: SudokuService = Depends(SudokuService),
):
    sudoku = service.solve(sudoku_str)
    return JSONResponse(
        content={
            "solution": sudoku.flatten_string(),
            'iterations': sudoku.iters_to_solve,
        },
        status_code=200,
    )
