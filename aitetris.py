import os
import random
import time
import sys

if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

WIDTH = 10
HEIGHT = 20
TETROMINOS = {
    'I': [['#', '#', '#', '#']],
    'O': [['#', '#'], ['#', '#']],
    'T': [['#', '#', '#'], [' ', '#', ' ']],
    'J': [['#', '#', '#'], [' ', ' ', '#']],
    'L': [['#', '#', '#'], ['#', ' ', ' ']],
    'S': [[' ', '#', '#'], ['#', '#', ' ']],
    'Z': [['#', '#', ' '], [' ', '#', '#']],
}

def get_key():
    if os.name == 'nt':
        if msvcrt.kbhit():
            return msvcrt.getch().decode()
        return None
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ch: return ch
        return None

def rotate(tetromino):
    return list(zip(*tetromino[::-1]))

def check_collision(field, tetromino, x, y):
    for i, row in enumerate(tetromino):
        for j, cell in enumerate(row):
            if cell == '#':
                if x + j < 0 or x + j >= WIDTH or y + i >= HEIGHT or (y + i >= 0 and field[y + i][x + j] != ' '):
                    return True
    return False

def clear_lines(field):
    lines_cleared = 0
    for i in range(HEIGHT):
        if all(cell == '#' for cell in field[i]):
            del field[i]
            field.insert(0, [' ' for _ in range(WIDTH)])
            lines_cleared += 1
    return lines_cleared

def print_field(field, score):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in field:
        print('|' + ''.join(row) + '|')
    print('-' * (WIDTH + 2))
    print("Score:", score)

def main():
    field = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    score = 0
    current_tetromino = random.choice(list(TETROMINOS.values()))
    x = WIDTH // 2 - len(current_tetromino[0]) // 2
    y = 0
    drop_timer = 0
    drop_interval = 1
    game_over = False

    while not game_over:
        print_field(field, score)
        key = get_key()

        if key == 'a' and not check_collision(field, current_tetromino, x - 1, y):
            x -= 1
        elif key == 'd' and not check_collision(field, current_tetromino, x + 1, y):
            x += 1
        elif key == 'w': # 回転
            rotated_tetromino = rotate(current_tetromino)
            if not check_collision(field, rotated_tetromino, x, y):
                current_tetromino = rotated_tetromino

        if drop_timer >= drop_interval:
            if check_collision(field, current_tetromino, x, y + 1):
                for i, row in enumerate(current_tetromino):
                    for j, cell in enumerate(row):
                        if cell == '#':
                            if y + i >= 0 and x+j < WIDTH:
                                field[y + i][x + j] = '#'
                lines_cleared = clear_lines(field)
                score += lines_cleared ** 2 * 100
                current_tetromino = random.choice(list(TETROMINOS.values()))
                x = WIDTH // 2 - len(current_tetromino[0]) // 2
                y = 0
                if check_collision(field,current_tetromino,x,y): #新しいミノがおけない＝ゲームオーバー
                    game_over = True

            else:
                y += 1
            drop_timer = 0

        time.sleep(0.1) # 速度調整
        drop_timer += 0.1
    print("Game Over!")


if __name__ == "__main__":
    main()