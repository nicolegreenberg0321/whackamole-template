import pygame
import random

def draw_grid(screen):
    grid_color = (0,0,0) #black for grid lines
    for x in range (0,640, 32):
        pygame.draw.line(screen, grid_color,(x, 0), (x, 512))
    for y in range (0, 512, 32):
        pygame.draw.line(screen, grid_color, (0, y), (640, y))

def random_mole_position():
    #grid is 20x20, so 20 cols, 16 rows
    x = random.randrange(0, 19)
    y = random.randrange(0, 15)
    return x * 32, y * 32


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        mole_image = pygame.image.load("mole.png")

        #initial position of mole
        x, y = 0, 0
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    #check if mole was clicked
                    if (mouse_x // 32) == (x //32) and (mouse_y // 32) == (y // 32):
                        #place mole randomly
                        x, y = random_mole_position()

            screen.fill("light green")
            draw_grid(screen)
            # You can draw the mole with this snippet:
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
