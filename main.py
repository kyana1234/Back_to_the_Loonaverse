import pygame

# Initialize pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("Back To the Loonaverse")
icon = pygame.image.load('graphics/orbit.png')
pygame.display.set_icon(icon)

# Create game screen
GAME_WINDOW_X = 800
GAME_WINDOW_Y = 600
screen = pygame.display.set_mode((GAME_WINDOW_X, GAME_WINDOW_Y))


def player(player_x: int, player_y: int):
    """Draw player icon at default starting location
    :param player_x: x-position on Surface grid
    :param player_y: y-position on Surface grid
    """
    screen.blit(playerImg, (player_x, player_y))


# Player
playerImg = pygame.image.load('graphics/spacecraft.png')
playerX = (GAME_WINDOW_X/2) - (playerImg.get_width()/2)  # icon is 64px
playerY = (GAME_WINDOW_Y/4) + (GAME_WINDOW_Y/2)

# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()
