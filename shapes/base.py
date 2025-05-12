import pygame
import os
from abc import ABC, abstractmethod
from config.options import GameOption 

# Kelas abstrak dasar untuk semua bentuk (shape)
class AbstractShape(ABC):
    def __init__(self, pos):
        # Matrix bentuk shape, hasil dari implementasi subclass
        self.matrix = self.get_matrix()

        # Memuat gambar blok dan mengubah ukurannya sesuai ukuran cell
        image_path = os.path.join(GameOption.BLOCK_IMAGE_PATH, self.get_image())
        self.image = pygame.transform.scale(
            pygame.image.load(image_path),
            (GameOption.CELL_SIZE, GameOption.CELL_SIZE)
        )

        # Posisi koordinat pixel untuk menggambar shape
        self.x, self.y = pos

        # Posisi awal (digunakan untuk mengembalikan ke posisi asal jika tidak valid)
        self.origin = pos

        # Status apakah sedang di-drag oleh pemain
        self.held = False

        # Offset posisi mouse terhadap pojok kiri atas shape (untuk dragging)
        self.offset = (0, 0)

    # Fungsi untuk menggambar shape ke layar utama
    def draw(self, screen):
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                
                # Jika cell aktif (berisi bagian shape)
                if val:  
                    x = self.x + j * GameOption.CELL_SIZE
                    y = self.y + i * GameOption.CELL_SIZE
                    screen.blit(self.image, (x, y))
                    pygame.draw.rect(screen, GameOption.GRID_LINE_COLOR, (x, y, GameOption.CELL_SIZE, GameOption.CELL_SIZE), 1) 

    # Fungsi untuk menggambar bayangan (preview) ketika shape sedang di-drag
    def draw_preview(self, screen):
        gx, gy = self.get_grid_position()

        # Membuat salinan semi-transparan dari gambar blok
        preview_image = self.image.copy().convert_alpha()
        preview_image.set_alpha(100)  # Transparansi 100/255

        # Gambar setiap bagian dari matrix sebagai preview
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val:
                    x = gx + j
                    y = gy + i

                    # Pastikan posisi masih dalam batas grid
                    if 0 <= x < GameOption.GRID_SIZE and 0 <= y < GameOption.GRID_SIZE:
                        px = GameOption.BOARD_OFFSET_X + x * GameOption.CELL_SIZE
                        py = GameOption.BOARD_OFFSET_Y + y * GameOption.CELL_SIZE

                        # Gambar blok transparan
                        screen.blit(preview_image, (px, py))  
                        pygame.draw.rect(screen, GameOption.GRID_LINE_COLOR, (px, py, GameOption.CELL_SIZE, GameOption.CELL_SIZE), 1)

    # Mengubah posisi pixel (x, y) menjadi posisi grid (gx, gy)
    def get_grid_position(self):
        gx = (self.x - GameOption.BOARD_OFFSET_X + GameOption.CELL_SIZE // 2) // GameOption.CELL_SIZE
        gy = (self.y - GameOption.BOARD_OFFSET_Y + GameOption.CELL_SIZE // 2) // GameOption.CELL_SIZE
        return gx, gy

    # Method abstrak untuk mendapatkan matrix shape dari subclass (harus diimplementasikan)
    @abstractmethod
    def get_matrix(self):
        pass

    # Method abstrak untuk mendapatkan nama file gambar shape (harus diimplementasikan)
    @abstractmethod
    def get_image(self):
        pass

    # Method abstrak untuk mengetahui tipe shape (digunakan jika ingin membedakan jenis)
    @abstractmethod
    def shape_type(self):
        pass