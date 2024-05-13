import sys
import pygame
import random
from Paddle import Paddle
from Ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.paddles = pygame.sprite.Group()
        self.ball = Ball(BLACK, 20, 20, SCREEN_HEIGHT)  # Pass SCREEN_HEIGHT as an argument
        self.paddle1 = Paddle(BLACK, 10, 100)
        self.paddle2 = Paddle(BLACK, 10, 100)
        self.paddle1.rect.x = 20
        self.paddle1.rect.y = (SCREEN_HEIGHT - self.paddle1.rect.height) // 2
        self.paddle2.rect.x = SCREEN_WIDTH - 30
        self.paddle2.rect.y = (SCREEN_HEIGHT - self.paddle2.rect.height) // 2
        self.paddles.add(self.paddle1, self.paddle2)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.paddle1.move(event.pos[1])

            # AI control for the opponent's paddle
            target_y = self.ball.rect.centery
            if self.paddle2.rect.centery < target_y:
                self.paddle2.move(self.paddle2.rect.y + 5)
            elif self.paddle2.rect.centery > target_y:
                self.paddle2.move(self.paddle2.rect.y - 5)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.paddle2.move(self.paddle2.rect.y - 5)
            if keys[pygame.K_DOWN]:
                self.paddle2.move(self.paddle2.rect.y + 5)

            # Check for collision with paddles
            if pygame.sprite.spritecollide(self.ball, self.paddles, False):
                self.ball.velocity[0] *= -1  # Flip X-coordinate trajectory



            self.screen.fill(WHITE)
            self.paddles.draw(self.screen)
            self.ball.update()
            pygame.draw.rect(self.screen, BLACK, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT], 2)
            self.screen.blit(self.ball.image, self.ball.rect)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
