import pygame
import os
from dino import Dinosaur

pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)
RUNNING = [
    pygame.image.load(os.path.join("Assets", "Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("Assets", "Dino", "DinoRun2.png")),
]
JUMPING = pygame.image.load(os.path.join("Assets", "Dino", "DinoJump.png"))
DUCKING = [
    pygame.image.load(os.path.join("Assets", "Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("Assets", "Dino", "DinoDuck2.png")),
]
SMALL_CACTUS = [
    pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus3.png")),
]
BIRD = [
    pygame.image.load(os.path.join("Assets", "Bird", "Bird1.png")),
    pygame.image.load(os.path.join("Assets", "Bird", "Bird2.png")),
]
CLOUD = pygame.image.load(os.path.join("Assets", "Other", "Cloud.png"))
BG = pygame.image.load(os.path.join("Assets", "Other", "Track.png"))


def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill(WHITE)
        user_input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(user_input)
        
        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    main()
