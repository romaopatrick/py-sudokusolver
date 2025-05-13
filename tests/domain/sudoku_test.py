from src.domain.sudoku import Sudoku
import pytest


@pytest.mark.parametrize(
    "input, output",
    [
        pytest.param(
            "004300209005009001070060043006002087190007400050083000600000105003508690042910300",
            "864371259325849761971265843436192587198657432257483916689734125713528694542916378",
            id="easy",
        ),
        pytest.param(
            "090050800803060002040300000000005004608700500900000000030000000507600400000020010",
            "796152843813467952245389176371895264628743591954216738132974685587631429469528317",
            id="expert",
        ),
        pytest.param(
            "800000000003600000070090200050007000000045700000100030001000068008500010090000400",
            "812753649943682175675491283154237896369845721287169534521974368438526917796318452",
            id="arto ikala's hardest sudoku in the world",
        ),
    ],
)
def test_solve_success(input: str, output: str):
    input = list(map(int, list(input)))

    sudoku = Sudoku(9, 9, 3, 3, input, debug=False)

    sudoku.solve()
    sudoku.plot(force=True)

    assert output == sudoku.flatten_string()
