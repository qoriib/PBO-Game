import pygame
from config.options import GameOption

class Board:
    # Membuat grid 2D berukuran GRID_SIZE x GRID_SIZE, berisi 0 (kosong)
    def __init__(self):
        self.grid = [[0 for _ in range(GameOption.GRID_SIZE)] for _ in range(GameOption.GRID_SIZE)]

    # Fungsi untuk menggambar seluruh grid ke layar
    def draw(self, screen):
        for row in range(GameOption.GRID_SIZE):
            for col in range(GameOption.GRID_SIZE):

                # Hitung posisi x dan y di layar
                x = GameOption.BOARD_OFFSET_X + col * GameOption.CELL_SIZE
                y = GameOption.BOARD_OFFSET_Y + row * GameOption.CELL_SIZE
                cell = self.grid[row][col]
                
                # Jika sel berisi gambar (blok), tampilkan gambar tersebut
                if cell:
                    screen.blit(cell, (x, y))
                
                # Jika kosong, gambar kotak dengan warna kosong
                else:
                    pygame.draw.rect(screen, GameOption.EMPTY_COLOR, (x, y, GameOption.CELL_SIZE, GameOption.CELL_SIZE))

                # Gambar garis batas sel
                pygame.draw.rect(screen, GameOption.GRID_LINE_COLOR, (x, y, GameOption.CELL_SIZE, GameOption.CELL_SIZE), 1)

        # Gambar garis tebal setiap 3 baris/kolom untuk menandai sub-grid 3x3
        for i in range(0, GameOption.GRID_SIZE + 1, 3):
            # Garis horizontal tebal
            pygame.draw.line(screen, GameOption.BIG_GRID_COLOR,
                             (GameOption.BOARD_OFFSET_X, GameOption.BOARD_OFFSET_Y + i * GameOption.CELL_SIZE),
                             (GameOption.BOARD_OFFSET_X + GameOption.GRID_SIZE * GameOption.CELL_SIZE,
                              GameOption.BOARD_OFFSET_Y + i * GameOption.CELL_SIZE), 3)
            # Garis vertikal tebal
            pygame.draw.line(screen, GameOption.BIG_GRID_COLOR,
                             (GameOption.BOARD_OFFSET_X + i * GameOption.CELL_SIZE, GameOption.BOARD_OFFSET_Y),
                             (GameOption.BOARD_OFFSET_X + i * GameOption.CELL_SIZE,
                              GameOption.BOARD_OFFSET_Y + GameOption.GRID_SIZE * GameOption.CELL_SIZE), 3)

    # Fungsi untuk mengecek apakah shape bisa ditempatkan di posisi manapun dalam grid
    def can_place(self, shape):
        for gy in range(GameOption.GRID_SIZE):
            for gx in range(GameOption.GRID_SIZE):
                if self._can_place_at(shape, gx, gy):
                    return True
        return False

    # Fungsi untuk mengecek apakah shape bisa diletakkan di grid posisi (gx, gy)
    def _can_place_at(self, shape, gx, gy):
        for i, row in enumerate(shape.matrix):
            for j, val in enumerate(row):
                if val:
                    x = gx + j
                    y = gy + i

                    # Cek jika posisi berada di luar batas grid
                    if not (0 <= x < GameOption.GRID_SIZE and 0 <= y < GameOption.GRID_SIZE):
                        return False

                    # Cek jika posisi sudah terisi
                    if self.grid[y][x]:
                        return False
        return True

    # Tempatkan shape ke grid jika valid
    def place(self, shape):

        # Ambil posisi grid berdasarkan koordinat pixel shape
        gx, gy = shape.get_grid_position() 
        if not self._can_place_at(shape, gx, gy):
            # Penempatan tidak sah
            return False 

        for i, row in enumerate(shape.matrix):
            for j, val in enumerate(row):
                if val:
                    # Tempatkan gambar shape ke dalam grid
                    self.grid[gy + i][gx + j] = shape.image
        return True

    # Fungsi untuk menghapus baris, kolom, atau blok 3x3 yang penuh
    def clear_lines(self):
        cleared = 0

        # Hapus baris penuh
        for y in range(GameOption.GRID_SIZE):
            if all(self.grid[y][x] for x in range(GameOption.GRID_SIZE)):
                for x in range(GameOption.GRID_SIZE):
                    self.grid[y][x] = 0
                cleared += 1

        # Hapus kolom penuh
        for x in range(GameOption.GRID_SIZE):
            if all(self.grid[y][x] for y in range(GameOption.GRID_SIZE)):
                for y in range(GameOption.GRID_SIZE):
                    self.grid[y][x] = 0
                cleared += 1

        # Hapus blok 3x3 penuh
        for i in range(0, GameOption.GRID_SIZE, 3):
            for j in range(0, GameOption.GRID_SIZE, 3):
                if all(self.grid[i + y][j + x] for y in range(3) for x in range(3)):
                    for y in range(3):
                        for x in range(3):
                            self.grid[i + y][j + x] = 0
                    cleared += 1

        return cleared