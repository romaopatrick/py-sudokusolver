import io
import pytest
from src.domain.errors.sudoku import SudokuErrors
from src.modules.sudoku.service import SudokuService


@pytest.mark.parametrize(
    "success, input_str, output",
    [
        pytest.param(
            False,
            "test_false",
            SudokuErrors.INVALID_SUDOKU_CHARS,
            id="invalid_chars_str",
        ),
        pytest.param(
            False, "000-1", SudokuErrors.INVALID_SUDOKU_CHARS, id="invalid_chars_negative"
        ),
        pytest.param(
            False, "0.300", SudokuErrors.INVALID_SUDOKU_CHARS, id="invalid_chars_decimal"
        ),
        pytest.param(False, "0808", SudokuErrors.INVALID_SUDOKU_LENGTH, id="invalid_length"),
        pytest.param(
            True,
            "800000000003600000070090200050007000000045700000100030001000068008500010090000400",
            True,
            id="valid_board",
        ),
    ],
)
def test_validate(
    success: bool, input_str: str, output, service: SudokuService = SudokuService()
):
    if not success:
        with pytest.raises(ValueError, match=str(output)):
            service._validate_sudoku(input_str)
        return

    assert service._validate_sudoku(input_str) == output
    

@pytest.mark.parametrize(
    "success, input_str, output",
    [
        pytest.param(
            False,
            "test_false",
            SudokuErrors.INVALID_SUDOKU_CHARS,
            id="invalid_chars_str",
        ),
        pytest.param(
            False, "000-1", SudokuErrors.INVALID_SUDOKU_CHARS, id="invalid_chars_negative"
        ),
        pytest.param(
            False, "0.300", SudokuErrors.INVALID_SUDOKU_CHARS, id="invalid_chars_decimal"
        ),
        pytest.param(False, "0808", SudokuErrors.INVALID_SUDOKU_LENGTH, id="invalid_length"),
        pytest.param(
            True,
            "004300209005009001070060043006002087190007400050083000600000105003508690042910300",
            True,
            id="valid_board",
        ),
    ],
)
def test_solve(success, input_str, output, service: SudokuService = SudokuService()):
    if not success:
        with pytest.raises(ValueError, match=str(output)):
            service._validate_sudoku(input_str)
    else:
        result = service.solve(input_str).as_stream()
        
        assert isinstance(result, io.BytesIO), "The result should be a file-like object"
        
        result.seek(0)
        content = str(result.read())
        assert len(content) > 0
