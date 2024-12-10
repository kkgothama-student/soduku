def read_puzzle(file_path):
    with open(file_path, 'r') as file:
        puzzle = []
        for line in file:
            puzzle.append([int(num) for num in line.split()])
    return puzzle

def solve_sudoku(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # An empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def write_puzzle(puzzle, file_path): 
    with open(file_path, 'w') as file: 
        for row in puzzle: 
            file.write(' '.join(map(str, row)) + '\n')

puzzle = read_puzzle("path/to/puzzle.txt") 
print("Solving puzzle from", "path/to/puzzle.txt") 

    
if solve_sudoku(puzzle): 
    write_puzzle(puzzle, "path/to/solved_puzzle.txt") 
    print("Solved puzzle written to", "path/to/solved_puzzle.txt") 
else: 
    print("No solution exists for the given puzzle")