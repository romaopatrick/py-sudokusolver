import math
from src.plot_sudoku import plot_sudoku


class Sudoku:
    def __init__(
        self,
        h: int,
        w: int,
        sh: int,
        sw: int,
        input: list[int],
        debug=True,
        plot_path="sudoku.png",
    ):
        self.height = h
        self.width = w
        self.square_height = sh
        self.square_width = sw
        self.input = input
        self.current = input
        self.debug = debug
        self.plot_path = plot_path
        self.iters_to_solve = 0

    def plot(self):
        plot_sudoku(self.current, self.plot_path)

    def flatten_string(self) -> str:
        return "".join(map(str, self.current))

    def solve(self):
        if not self._iterate_():
            if self.debug:
                self.plot()
            raise ValueError("SOLVER BROKEN")

        if self.debug:
            print(f"{sum(1 for n in self.current if n == 0)} to go! :)")
            print(f"TOTAL ITERATIONS TO SOLVE: {self.iters_to_solve}")
            self.plot()

    def _is_safe_col_(self, idx: int, num: int) -> bool:
        idx = idx if idx < self.width else idx % self.width

        for i in range(self.height):
            if self.current[idx + (i * self.width)] == num:
                return False

        return True

    def _is_safe_row_(self, idx: int, num: int) -> bool:
        diff = idx / self.width
        idx = math.floor((diff)) * self.width

        for i in range(self.width):
            if self.current[idx + i] == num:
                return False

        return True

    def _is_safe_square_(self, idx: int, num: int) -> bool:
        idx_col = idx % self.width
        idx_row = idx // self.height

        sq_idx = (idx_col // self.square_width) + (idx_row // self.square_height) * (
            self.width // self.square_width
        ) * self.square_height
        
        sq_idx *= self.square_width

        for line in range(self.square_height):
            for col in range(self.square_width):
                i = sq_idx + col + (line * self.width)
                elem = self.current[i]
                if elem == num:
                    return False

        return True

    def _is_safe_(self, idx: int, num: int) -> bool:
        return (
            self._is_safe_row_(idx, num)
            and self._is_safe_col_(idx, num)
            and self._is_safe_square_(idx, num)
        )

    def _iterate_(self) -> bool:
        for i, _ in enumerate(self.current):
            if self.current[i] != 0:
                continue
        
            for num in range(1, self.height + 1):
                if self._is_safe_(i, num):
                    self.current[i] = num
                    if self._iterate_():
                        return True
                    self.current[i] = 0

            return False

        if self.debug:
            self.plot()
            self.iters_to_solve += 1

        return True
