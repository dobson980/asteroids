# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    initialize_game()
    run_game_loop()
    
def initialize_game():
    """
    Initializes the game settings and screen.
    """
    pygame.init()
    global screen, clock, dt
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

def run_game_loop():
    """
    Runs the main game loop.
    """
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        screen.fill("black")

        player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # Game logic and rendering would go here
    


    pygame.quit()

if __name__ == "__main__":
    main()
