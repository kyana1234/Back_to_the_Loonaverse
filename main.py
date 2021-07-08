import pygame
from pygame import mixer
import spaceship
import alien
import bullet
import loonaverse_score as lvs
import os

# set the pygame screen spawn point
comp_screen_x = 100
comp_screen_y = 0

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (comp_screen_x, comp_screen_y)

# Initialize pygame
pygame.init()

# Title and Icon
pygame.display.set_caption('Back To the Loonaverse')
icon = pygame.image.load('graphics/orbit.png')
pygame.display.set_icon(icon)

# Create main menu screen
MENU_WINDOW_X = 800
MENU_WINDOW_Y = 340

# Create game screen
GAME_WINDOW_X = 540
GAME_WINDOW_Y = 960
# screen = pygame.display.set_mode((GAME_WINDOW_X, GAME_WINDOW_Y))
screen_dim = ""

# Background
main_menu_background = pygame.image.load('graphics/main_menu_horizontal_small.png')
main_game_background = pygame.image.load('graphics/background_small.jpg')

# font
font = pygame.font.Font('graphics/TingTong.ttf', 48)
menu_font = pygame.font.Font('graphics/Futura Book.ttf', 24)

# Player name
name = ""


def draw_player(player_obj, game_screen):
    """Draw player icon at default starting location
    :param player_obj: player object to draw
    """
    game_screen.blit(player_obj.get_img(), (player_obj.get_x(), player_obj.get_y()))


def draw_alien(alien_obj, game_screen):
    """Draw player icon at default starting location
    :param alien_obj: alien object to draw
    """
    game_screen.blit(alien_obj.get_img(), (alien_obj.get_x(), alien_obj.get_y()))


def draw_bullet(bullet_obj, game_screen):
    """Draw player icon at default starting location
    :param bullet_obj: alien object to draw
    """
    game_screen.blit(bullet_obj.get_img(), (bullet_obj.get_x(), bullet_obj.get_y()))


def display_score(score_name, score_value, x, y, game_screen):
    score = font.render(score_name + " :" + str(score_value), True, (255, 255, 255))
    game_screen.blit(score, (x, y))


def game_instructions(game_screen):
    instructions = menu_font.render("Move with the Arrow keys Press spacebar to fire Press spacebar to play",
                               True, (255, 255, 255))
    instructions_rect = instructions.get_rect()
    instructions_rect.midtop = (MENU_WINDOW_X / 2, MENU_WINDOW_Y / 2)
    game_screen.blit(instructions, instructions_rect)


def game_over_text(game_screen):
    game_over_string = menu_font.render("GAME OVER", True, (255, 255, 255))
    game_over_rect = game_over_string.get_rect()
    game_over_rect.midtop = (GAME_WINDOW_X / 2, GAME_WINDOW_Y / 4)
    game_screen.blit(game_over_string, game_over_rect)


def display_top_3(game_screen):
    top_3_dict = lvs.top_3_scores()
    # top_score_string = menu_font.render("", True, (255, 255, 255))
    # top_score_string = top_score_string.get_rect()
    # top_score_string.midtop = (GAME_WINDOW_X / 2, GAME_WINDOW_Y / 2)
    text_buffer = 0
    i = 0
    for i in range(0, 3):
        top_name = top_3_dict['name'][i]
        top_score = top_3_dict['score'][i]
        top_score_string = menu_font.render(top_name + " " + str(top_score), True, (255, 255, 255))
        top_score_string_rect = top_score_string.get_rect()
        top_score_string_rect.midtop = ((GAME_WINDOW_X / 2), (GAME_WINDOW_Y / 2) + text_buffer)
        text_buffer += 30  # number of pixels to go to next line
        game_screen.blit(top_score_string, top_score_string_rect)


def main_menu():
    # In-game background music
    mixer.music.load('assets/loona_intro_mixdown_16.wav')
    mixer.music.play(-1)  # play music in a loop
    valid_name = False
    while not valid_name:
        player_name = input("Please enter your player name: ")
        player_name_clean = player_name.strip()
        if not player_name_clean.isalpha():
            print('Please input a name that only contains alphabetical characters (A-Za-z)')
        else:
            valid_name = True

    screen = pygame.display.set_mode((MENU_WINDOW_X, MENU_WINDOW_Y))
    screen_dim = pygame.display.get_window_size()

    screen.fill((0, 0, 0))
    screen.blit(main_menu_background, (0, 0))
    game_instructions(screen)
    pygame.display.update()

    running = True
    while running:

        # Game instructions

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit game window
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # start game
                    running = False

    return player_name


# Main Game Loop
def main_game_loop(player_name):
    # open new screen
    screen = pygame.display.set_mode((GAME_WINDOW_X, GAME_WINDOW_Y))
    screen_dim = pygame.display.get_window_size()

    # In-game background music
    mixer.music.load('assets/& (&).wav')
    mixer.music.play(-1)  # play music in a loop

    # Create player object
    player = spaceship.Spaceship(screen_dim)

    # Spawned objects
    # Alien
    initial_alien = alien.Alien(screen_dim)
    spawned_aliens = [initial_alien]
    spawned_bullets = []

    # Manage random spawn rate for aliens
    counter = 1  # start from 1 to avoid double spawn at beginning

    # Score
    distance_score_counter = 0

    distance_score_text_x = 10
    distance_score_text_y = 10

    alien_score_counter = 0
    alien_score_text_x = 10
    alien_score_text_y = 50

    running = True
    while running:

        screen.fill((0, 0, 0))
        screen.blit(main_game_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit game window
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
                    spawned_bullets.append(
                        bullet.Bullet(screen_dim, player.get_x(), player.get_y(), player.get_img_dim()))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.set_vx(0)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player.set_vy(0)
        player.move()
        draw_player(player, screen)

        # Spawn alien
        # Require game to have at least 1 alien on the screen
        if counter % 1000 == 0 or len(spawned_aliens) == 0:
            spawned_aliens.append(alien.Alien(screen_dim))

        # Cross-check aliens and bullets for possible collisions or clear for movement
        for incoming_alien in spawned_aliens:
            remove_alien = False
            if player.hit_by_alien(incoming_alien):
                running = False
            for shot_bullet in spawned_bullets:
                if incoming_alien.hit_by_bullet(shot_bullet):
                    remove_alien = True
                    spawned_bullets.remove(shot_bullet)
                    alien_score_counter += 1
                    continue
                elif shot_bullet.reach_end():
                    spawned_bullets.remove(shot_bullet)
                    continue
                else:
                    shot_bullet.move()
                    draw_bullet(shot_bullet, screen)
            if remove_alien:
                spawned_aliens.remove(incoming_alien)
            elif incoming_alien.reach_end():
                spawned_aliens.remove(incoming_alien)
            else:
                incoming_alien.move()
                draw_alien(incoming_alien, screen)

        if counter % 1000 == 0:
            distance_score_counter += 10
        display_score("Distance score", distance_score_counter, distance_score_text_x, distance_score_text_y, screen)
        display_score("Aliens destroyed", alien_score_counter, alien_score_text_x, alien_score_text_y, screen)
        pygame.display.update()
        counter += 1

    # Display game over screen
    game_over(screen)
    pygame.display.update()
    # Calculate final score
    final_score = lvs.calculate_final_score(distance_score_counter, alien_score_counter)
    lvs.record_score(player_name, final_score)

    return screen


def game_over(screen):


    # Keep the game screen persistent so players can read scores until they exit
    running = True
    while running:
        game_over_text(screen)
        display_top_3(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit game window
                running = False


name = main_menu()
persistent_screen = main_game_loop(name)
game_over(persistent_screen)
