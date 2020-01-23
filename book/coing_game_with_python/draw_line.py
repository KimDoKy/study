import sys, pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        for xpos in range(0, 400, 25):
            pygame.draw.line(SURFACE, 0xFFFFFF, (xpos, 0), (xpos, 300))

        for ypos in range(0, 300, 25):
            pygame.draw.line(SURFACE, 0xFFFFF, (0, ypos), (400, ypos))

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
