import pygame
import random

width = 550
background_color = (255,255,255)
buffer = 5
grid = [[0 for _ in range(9)] for _ in range(9)]

def play(win,position):
    font = pygame.font.Font(None,36)
    i,j = position[1], position[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid[i-1][j-1] != 0 :
                    return
                if event.key == 48:
                    grid[i-1][j-1] = event.key = 48
                    pygame.draw.rect(win, background_color, (position[0]*50 +buffer, position[1]*50+ buffer, 50-buffer,50 - buffer))
                    pygame.display.update()
                if 1 < event.key - 48 < 10:
                    pygame.draw.rect(win, background_color, (position[0]*50 +buffer, position[1]*50+ buffer, 50-buffer,50 - buffer))
                    value = font.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 +15, position[1]*50 ))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                return
            return

def is_valid_move(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_random_sudoku():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(grid)
    num_to_remove = random.randint(35, 55)  
    for _ in range(num_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        grid[row][col] = 0
    
    return grid

def main():
    pygame.init()
    win = pygame.display.set_mode((width, width))
    win.fill(background_color)
    pygame.display.set_caption('Sudoku')
    sudoku_grid = generate_random_sudoku()

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, width - 50), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (width - 50, 50 + 50 * i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, width - 50), 1)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (width - 50, 50 + 50 * i), 1)

    for i in range(9):
        for j in range(9):
            if sudoku_grid[i][j] != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(sudoku_grid[i][j]), True, (0, 0, 0))
                win.blit(text, (64 + j * 50, 64 + i * 50))

    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                play(win,(pos//50,pos))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()