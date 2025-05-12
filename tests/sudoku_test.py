from src.sudoku import Sudoku

def test_solve():
    sudoku_input = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
    sudoku_output = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
    input = list(map(int, list(sudoku_input)))
        
    sudoku = Sudoku(9, 9, 3, 3, input)
    
    sudoku.solve()
        
    assert sudoku_output == sudoku.flatten_string()