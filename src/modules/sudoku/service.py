import re

from src.domain.errors.sudoku import SudokuErrors
from ...domain.sudoku import Sudoku 

class SudokuService:
    def _validate_sudoku(self, input: str) -> bool:
        if not re.fullmatch(r'\d+', input):
            raise ValueError(SudokuErrors.INVALID_SUDOKU_CHARS)

        if len(input) != 81:
            raise ValueError(SudokuErrors.INVALID_SUDOKU_LENGTH)

        return True
        
    def solve(self, input: str) -> Sudoku:
        self._validate_sudoku(input)
        
        sudoku = Sudoku(9, 9, 3, 3, list(map(int, list(input))), debug=False)
        sudoku.solve()
        
        return sudoku