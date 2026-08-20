import pygame
import random


class Game:
    def __init__(self, visual=False, clock=False):
        self.visual = visual
        self.clock = clock
        pygame.init()
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dino = pygame.FRect((0, 0), (30, 50))
        self.obsticals = [pygame.FRect((0, 0), (20, 55)), pygame.FRect((0, 0), (15, 30)), pygame.FRect((0, 0), (30, 30)), pygame.FRect((0,0), (45, 30)), pygame.FRect((0, 0), (60, 30)), pygame.FRect((0, 0), 60, 50)]

    def get_inputs(self, input):
        if input == 0:
            self.jump()

    def jump(self):
        pass

    def update_screen(self):
        for x in self.renders:
            self.window.blit(x[0], x[1])
        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            if self.visual:
                self.update_screen()

            if self.clock:
                self.clock.tick(60)

        pygame.quit()

        