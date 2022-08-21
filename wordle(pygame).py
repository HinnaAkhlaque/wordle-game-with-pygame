# WORLDE GAME BUILT WITH PYGAME
import pygame
import random

pygame.init()

white = (255, 255,  255)
black = (0, 0, 0)
peach = (196, 142, 110)
yellow = (255,255,0)
green = (0, 255, 0)
red = (232, 16, 16)

width = 510
height = 570

turns = 0
board = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]

wordlist = ["first", "lunch", "eight", "bride", "fight", "great", "burst", "could", "might", "solid", "serve", "slice",
            "pizza", "adult", "nurse", "agent", "which", "beach", "award", "plane", "ghost", "china", "zebra", "power"]
word = random.choice(wordlist)

result = ["Superb!", "You did it!", "Amazing!", "Great!", "Splendid!"]
win = random.choice(result)

game_over = False
letter = 0
active_turn = True

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wordle!!")

title_font = pygame.font.SysFont("Helvetica", 40, "bold")
res_font = pygame.font.SysFont("Arial", 30)
res_font2 = pygame.font.SysFont("Arial", 40, "bold")
fps = 60
timer = pygame.time.Clock()


def draw_board():
    global turns
    global board


    for col in range(0, 4):
        for row in range(0, 4):
             pygame.draw.rect(window, red, [25, turns * 85 + 55, width - 40, 80], 3, 6)

    for col in range(0, 5):
        for row in range(0, 5):
            pygame.draw.rect(window, white, [col * 85 + 50, row * 85 + 60, 70, 70], 3, 5)
            text = title_font.render(board[row][col], True, white)
            window.blit(text, [col * 85 + 70, row * 85 + 68])

def check():
    global turns
    global board
    global word
    global score

    for col in range(0, 5):
        for row in range(0, 5):
            if word[col] == board[row][col] and turns > row:
                pygame.draw.rect(window, green, [col * 85 + 50, row * 85 + 60, 70, 70], 0, 5)
            elif board[row][col] in word and turns > row:
                pygame.draw.rect(window, yellow, [col * 85 + 50, row * 85 + 60, 70, 70], 0, 5)


running = True
while running:
    timer.tick(fps)
    window.fill(peach)
    check()
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.TEXTINPUT and active_turn and not game_over:
            entry = event.__getattribute__('text')
            if entry != " ":
                entry = entry.lower()
                board[turns][letter] = entry
                letter += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letter > 0:
                board[turns][letter - 1] = ' '
                letter = letter - 1

            if event.key == pygame.K_SPACE and not game_over:
                turns += 1
                letter = 0

            if event.key == pygame.K_SPACE and game_over:
                turns = 0
                letter = 0
                game_over = False
                word
                board = [[" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "]]

    if letter == 5:
        active_turn = False
    if letter < 5:
        active_turn = True

    for row in range(0, 5):
        guess = board[row][0] + board[row][1] + board[row][2] + board[row][3] + board[row][4]
        if guess == word and row < turns:
            game_over = True

    if turns == 5:
        game_over = True
        loser_text = res_font.render('Press space to play again', True, "red")
        window.blit(loser_text, (110, 500))

    if game_over and turns < 5:
        winner_text = res_font2.render(win, True, white)
        window.blit(winner_text, (170, 500))

    pygame.display.flip()
pygame.quit()


