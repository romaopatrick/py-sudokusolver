import io
import math
import matplotlib.pyplot as plt
import numpy as np


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

    def plot(self, force = False):
        if self.debug or force:
            plot_sudoku(self.current, self.plot_path)

    def flatten_string(self) -> str:
        return "".join(map(str, self.current))

    def solve(self):
        self.plot()
        if not self._iterate():
            self.plot()
            raise ValueError("SOLVER BROKEN")

        if self.debug:
            print(f"{sum(1 for n in self.current if n == 0)} to go! :)")
            print(f"TOTAL ITERATIONS TO SOLVE: {self.iters_to_solve}")
            self.plot()

    def _is_safe_col(self, idx: int, num: int) -> bool:
        idx = idx if idx < self.width else idx % self.width

        for i in range(self.height):
            if self.current[idx + (i * self.width)] == num:
                return False

        return True

    def _is_safe_row(self, idx: int, num: int) -> bool:
        diff = idx / self.width
        idx = math.floor((diff)) * self.width

        for i in range(self.width):
            if self.current[idx + i] == num:
                return False

        return True

    def _is_safe_square(self, idx: int, num: int) -> bool:
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

    def _is_safe(self, idx: int, num: int) -> bool:
        return (
            self._is_safe_row(idx, num)
            and self._is_safe_col(idx, num)
            and self._is_safe_square(idx, num)
        )
        
    def as_stream(self, solve = True) -> io.BytesIO:
        if solve:
            self.solve()
            
        img_stream = io.BytesIO()
        plot_sudoku(self.current, img_stream)
        img_stream.seek(0)
        
        return img_stream

    def _iterate(self) -> bool:
        for i, _ in enumerate(self.current):
            if self.current[i] == 0:
                for num in range(1, self.height + 1):
                    if self._is_safe(i, num):
                        
                        self.current[i] = num
                        
                        if self._iterate():
                            return True
                        
                        self.current[i] = 0

                return False
                
            if self.debug:
                self.plot()
                self.iters_to_solve += 1

        return True

def plot_sudoku(board: list[int], output):
    if len(board) != 81:
        raise ValueError("Input must be a list of 81 integers.")

    grid = np.array(board).reshape((9, 9))

    _, ax = plt.subplots(figsize=(5, 5))
    ax.matshow(np.ones_like(grid), cmap='gray', vmin=0, vmax=1)  # light background

    # Draw numbers
    for i in range(9):
        for j in range(9):
            num = grid[i, j]
            if num != 0:
                ax.text(j, i, str(num), va='center', ha='center', fontsize=14)

    # Draw thicker lines every 3 blocks
    for i in range(10):
        lw = 2 if i % 3 == 0 else 0.5
        ax.axhline(i - 0.5, color='black', lw=lw)
        ax.axvline(i - 0.5, color='black', lw=lw)

    ax.set_xticks([])
    ax.set_yticks([])
    plt.savefig(output, format='png')