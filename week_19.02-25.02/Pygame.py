import pygame
import sys
import random

# Definiere einige Konstanten für das Spiel
WIDTH = 400
HEIGHT = 400
ROWS = 4
COLS = 4
TILE_SIZE = WIDTH // COLS

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialisiere das Spiel
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle Game")
clock = pygame.time.Clock()

# Hilfsfunktion zum Mischen der Puzzle-Stücke
def shuffle_board():
    puzzle_pieces = [i for i in range(1, ROWS * COLS)]
    random.shuffle(puzzle_pieces)
    puzzle_pieces.append(0)  # 0 stellt das leere Feld dar
    return puzzle_pieces

# Überprüfe, ob das Puzzle gelöst wurde
def is_solved(board):
    return board == [i for i in range(1, ROWS * COLS)] + [0]

# Zeichne das Spielbrett
def draw_board(board):
    screen.fill(BLACK)
    for i in range(ROWS):
        for j in range(COLS):
            index = i * COLS + j
            if board[index] == 0:
                pygame.draw.rect(screen, WHITE, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            else:
                font = pygame.font.SysFont(None, 50)
                text = font.render(str(board[index]), True, BLACK)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                pygame.draw.rect(screen, WHITE, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                screen.blit(text, text_rect)

# Hauptspiel-Schleife
def main():
    puzzle_board = shuffle_board()
    empty_tile_index = puzzle_board.index(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and empty_tile_index > COLS - 1:
                    puzzle_board[empty_tile_index], puzzle_board[empty_tile_index - COLS] = \
                        puzzle_board[empty_tile_index - COLS], puzzle_board[empty_tile_index]
                    empty_tile_index -= COLS
                elif event.key == pygame.K_DOWN and empty_tile_index < ROWS * COLS - COLS:
                    puzzle_board[empty_tile_index], puzzle_board[empty_tile_index + COLS] = \
                        puzzle_board[empty_tile_index + COLS], puzzle_board[empty_tile_index]
                    empty_tile_index += COLS
                elif event.key == pygame.K_LEFT and empty_tile_index % COLS != 0:
                    puzzle_board[empty_tile_index], puzzle_board[empty_tile_index - 1] = \
                        puzzle_board[empty_tile_index - 1], puzzle_board[empty_tile_index]
                    empty_tile_index -= 1
                elif event.key == pygame.K_RIGHT and empty_tile_index % COLS != COLS - 1:
                    puzzle_board[empty_tile_index], puzzle_board[empty_tile_index + 1] = \
                        puzzle_board[empty_tile_index + 1], puzzle_board[empty_tile_index]
                    empty_tile_index += 1

        if is_solved(puzzle_board):
            print("Puzzle gelöst!")
            break

        draw_board(puzzle_board)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
