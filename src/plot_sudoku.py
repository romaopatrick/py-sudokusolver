import matplotlib.pyplot as plt
import numpy as np

def plot_sudoku(board: list[int], outputpath:str):
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
    plt.savefig(outputpath)