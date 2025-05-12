import pygame
import os
from abc import ABC, abstractmethod
from config.options import GameOption

class AbstractShape(ABC):
    def __init__(self, pos):
        self.matrix = self.get_matrix()
        image_path = os.path.join(GameOption.BLOCK_IMAGE_PATH, self.get_image())
        self.image = pygame.transform.scale(pygame.image.load(image_path), (GameOption.CELL_SIZE, GameOption.CELL_SIZE))
        self.x, self.y = pos
        self.origin = pos
        self.held = False
        self.offset = (0, 0)

    def draw(self, screen):
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val:
                    x = self.x + j * GameOption.CELL_SIZE
                    y = self.y + i * GameOption.CELL_SIZE
                    screen.blit(self.image, (x, y))
                    pygame.draw.rect(screen, GameOption.GRID_LINE_COLOR, (x, y, GameOption.CELL_SIZE, GameOption.CELL_SIZE), 1)

    def draw_preview(self, screen):
        gx, gy = self.get_grid_position()

        preview_image = self.image.copy().convert_alpha()
        preview_image.set_alpha(100)

        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val:
                    x = gx + j
                    y = gy + i
                    if 0 <= x < GameOption.GRID_SIZE and 0 <= y < GameOption.GRID_SIZE:
                        px = GameOption.BOARD_OFFSET_X + x * GameOption.CELL_SIZE
                        py = GameOption.BOARD_OFFSET_Y + y * GameOption.CELL_SIZE
                        screen.blit(preview_image, (px, py))
                        pygame.draw.rect(screen, GameOption.GRID_LINE_COLOR, (px, py, GameOption.CELL_SIZE, GameOption.CELL_SIZE), 1)

    def get_grid_position(self):
        gx = (self.x - GameOption.BOARD_OFFSET_X + GameOption.CELL_SIZE // 2) // GameOption.CELL_SIZE
        gy = (self.y - GameOption.BOARD_OFFSET_Y + GameOption.CELL_SIZE // 2) // GameOption.CELL_SIZE
        return gx, gy

    @abstractmethod
    def get_matrix(self):
        pass

    @abstractmethod
    def get_image(self):
        pass

    @abstractmethod
    def shape_type(self):
        pass