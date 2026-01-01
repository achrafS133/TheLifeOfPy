import pygame
import sys
from world import World

# Constants
WIDTH, HEIGHT = 1000, 800
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TheLifeOfPy - Artificial Life Simulation")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    world = World(WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        world.update()

        # Render
        screen.fill((0, 0, 0)) # Black background
        
        world.draw(screen)

        # UI Overlay
        stats = world.get_stats()
        y_offset = 10
        for key, value in stats.items():
            text = font.render(f"{key}: {value}", True, (255, 255, 255))
            screen.blit(text, (10, y_offset))
            y_offset += 25

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
