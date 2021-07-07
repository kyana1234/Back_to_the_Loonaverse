import pygame
import spaceship
import alien
import bullet

# Initialize pygame
pygame.init()

# Title and Icon
pygame.display.set_caption('Back To the Loonaverse')
icon = pygame.image.load('graphics/orbit.png')
pygame.display.set_icon(icon)

# Create game screen
GAME_WINDOW_X = 540
GAME_WINDOW_Y = 960
screen = pygame.display.set_mode((GAME_WINDOW_X, GAME_WINDOW_Y))
screen_dim = pygame.display.get_window_size()

# Background
background = pygame.image.load('graphics/background_small.jpg')

# Create player object
player = spaceship.Spaceship(screen_dim)


def draw_player(player_obj):
    """Draw player icon at default starting location
    :param player_obj: player object to draw
    """
    screen.blit(player_obj.get_img(), (player_obj.get_x(), player_obj.get_y()))


def draw_alien(alien_obj):
    """Draw player icon at default starting location
    :param alien_obj: alien object to draw
    """
    screen.blit(alien_obj.get_img(), (alien_obj.get_x(), alien_obj.get_y()))


def draw_bullet(bullet_obj):
    """Draw player icon at default starting location
    :param bullet_obj: alien object to draw
    """
    screen.blit(bullet_obj.get_img(), (bullet_obj.get_x(), bullet_obj.get_y()))


# Player
# playerImg = pygame.image.load('graphics/spacecraft.png')
# playerX = (GAME_WINDOW_X/2) - (playerImg.get_width()/2)  # icon is 64px
# playerY = (GAME_WINDOW_Y/4) + (GAME_WINDOW_Y/2)
# playerX_velocity = 0

# Alien

initial_alien = alien.Alien(screen_dim)
# shot_bullet = bullet.Bullet(screen_dim, player.get_x(), player.get_y(), player.get_img_dim())

# Spawned objects
spawned_aliens = [initial_alien]
spawned_bullets = []

# manage random spawn rate for aliens
counter = 1  # start from 1 to avoid double spawn at beginning

# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # exit game windo
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.set_vx(-1.5)
            elif event.key == pygame.K_RIGHT:
                player.set_vx(1.5)
            elif event.key == pygame.K_UP:
                player.set_vy(-1.5)
            elif event.key == pygame.K_DOWN:
                player.set_vy(1.5)
            elif event.key == pygame.K_SPACE:
                spawned_bullets.append(bullet.Bullet(screen_dim, player.get_x(), player.get_y(), player.get_img_dim()))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.set_vx(0)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.set_vy(0)

    player.move()
    draw_player(player)

    # Spawn alien
    if counter % 10000 == 0:
        spawned_aliens.append(alien.Alien(screen_dim))

    # Cross-check aliens and bullets for possible collisions or clear for movement
    for incoming_alien in spawned_aliens:
        remove_alien = False
        for shot_bullet in spawned_bullets:
            if incoming_alien.hit_by_bullet(shot_bullet):
                remove_alien = True
                spawned_bullets.remove(shot_bullet)
                continue
            elif shot_bullet.reach_end():
                spawned_bullets.remove(shot_bullet)
                continue
            else:
                shot_bullet.move()
                draw_bullet(shot_bullet)
        if remove_alien:
            spawned_aliens.remove(incoming_alien)
        elif incoming_alien.reach_end():
            spawned_aliens.remove(incoming_alien)
        else:
            incoming_alien.move()
            draw_alien(incoming_alien)


    pygame.display.update()
    counter += 1
