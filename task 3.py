def print_grid(grid):
    """Print the Sudoku grid in a readable format."""
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()


def is_valid(grid, row, col, num):
    """Check if placing num at grid[row][col] is valid."""
    # Check row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(grid):
    """Solve Sudoku using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try digits 1-9
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack
                return False
    return True


if __name__ == "__main__":
    # Example Sudoku puzzle (0 means empty cell)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("🔢 Unsolved Sudoku Puzzle:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\n✅ Solved Sudoku Puzzle:")
        print_grid(sudoku_grid)
    else:
        print("\n❌ No solution exists!")
