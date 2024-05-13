import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height, screen_height):  # Add screen_height as an argument
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [4, 4]
        self.rect = self.image.get_rect()
        self.screen_height = screen_height  # Store the screen_height

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.y > self.screen_height - self.rect.height or self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]
