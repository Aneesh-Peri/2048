import pygame
import sys

pygame.init()


# Below are some variables which need to be initialized and also some starter things needed 
PEACH = (185,173,161)
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (128,128,128)
WIDTH,HEIGHT = 400,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")
font = pygame.font.Font('freesansbold.ttf', 24)
score = 0
high_score = 0
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0




colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}


# This function will help draw the board 
def draw_board():
    pygame.draw.rect(WIN,PEACH,[0,0,500,400],0,10)
    score_text = font.render(f'Score: {score}', True, 'black')
    high_score_text = font.render(f'High Score: {high_score}', True, 'black')
    WIN.blit(score_text, (10, 410))
    WIN.blit(high_score_text, (10, 450))


# This will draw the tiles for 2048
def draw_tiles(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(WIN,color,[j*95+20,i*95+20,75,75])

            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf',48 - (5 * value_len))


# This is the main loop for the game 
def main():
    # Below will be the button which creates the main menu button
    while True:
        WIN.fill(GRAY)
        draw_board()   
        draw_tiles(board_values) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()