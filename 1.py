import os
import sys
import pygame

pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображениями '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Game(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        x_pos = 0
        self.image = load_image('gameover.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def moveG(self):
        self.rect = self.rect.move(x_pos, height)
        x_pos += 1


if __name__ == '__main__':
    fps = 200
    clock = pygame.time.Clock()
    game = Game(all_sprites)
    for i in range(width):
        game.moveG()
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 255))
        pygame.display.flip()
        game.update()
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
    pygame.quit()
