import pygame
from config.options import GameOption

class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(GameOption.GRID_SIZE)] for _ in range(GameOption.GRID_SIZE)]

    def draw(self, screen):
        for row in range(GameOption.GRID_SIZE):
            for col in range(GameOption.GRID_SIZE):
                x = GameOption.BOARD_OFFSET_X + col * GameOption.CELL_SIZE
                y = GameOption.BOARD_OFFSET_Y + row * GameOption.CELL_SIZE
                cell = self.grid[row][col]
                if cell:
                    screen.blit(cell, (x, y))
                else:
                    pygame.draw.rect(screen, GameOption.EMPTY_COLOR, (x, y, GameOption.CELL_SIZE, GameOption.CELL_SIZE))
                pygame.draw.rect(screen, GameOption.GRID_LINE_COLOR, (x, y, GameOption.CELL_SIZE, GameOption.CELL_SIZE), 1)
        for i in range(0, GameOption.GRID_SIZE + 1, 3):
            pygame.draw.line(screen, GameOption.BIG_GRID_COLOR, (GameOption.BOARD_OFFSET_X, GameOption.BOARD_OFFSET_Y + i * GameOption.CELL_SIZE), (GameOption.BOARD_OFFSET_X + GameOption.GRID_SIZE * GameOption.CELL_SIZE, GameOption.BOARD_OFFSET_Y + i * GameOption.CELL_SIZE), 3)
            pygame.draw.line(screen, GameOption.BIG_GRID_COLOR, (GameOption.BOARD_OFFSET_X + i * GameOption.CELL_SIZE, GameOption.BOARD_OFFSET_Y), (GameOption.BOARD_OFFSET_X + i * GameOption.CELL_SIZE, GameOption.BOARD_OFFSET_Y + GameOption.GRID_SIZE * GameOption.CELL_SIZE), 3)

    def can_place(self, shape):
        for gy in range(GameOption.GRID_SIZE):
            for gx in range(GameOption.GRID_SIZE):
                if self._can_place_at(shape, gx, gy):
                    return True
        return False

    def _can_place_at(self, shape, gx, gy):
        for i, row in enumerate(shape.matrix):
            for j, val in enumerate(row):
                if val:
                    x = gx + j
                    y = gy + i
                    if not (0 <= x < GameOption.GRID_SIZE and 0 <= y < GameOption.GRID_SIZE):
                        return False
                    if self.grid[y][x]:
                        return False
        return True

    def place(self, shape):
        gx, gy = shape.get_grid_position()
        if not self._can_place_at(shape, gx, gy):
            return False  # penempatan tidak valid

        for i, row in enumerate(shape.matrix):
            for j, val in enumerate(row):
                if val:
                    self.grid[gy + i][gx + j] = shape.image
        return True

    def clear_lines(self):
        cleared = 0
        for y in range(GameOption.GRID_SIZE):
            if all(self.grid[y][x] for x in range(GameOption.GRID_SIZE)):
                for x in range(GameOption.GRID_SIZE):
                    self.grid[y][x] = 0
                cleared += 1
        for x in range(GameOption.GRID_SIZE):
            if all(self.grid[y][x] for y in range(GameOption.GRID_SIZE)):
                for y in range(GameOption.GRID_SIZE):
                    self.grid[y][x] = 0
                cleared += 1
        for i in range(0, GameOption.GRID_SIZE, 3):
            for j in range(0, GameOption.GRID_SIZE, 3):
                if all(self.grid[i + y][j + x] for y in range(3) for x in range(3)):
                    for y in range(3):
                        for x in range(3):
                            self.grid[i + y][j + x] = 0
                    cleared += 1
        return cleared