import pygame
import sys
import os
from config.options import GameOption
from core.board import Board
from shapes.factory import ShapeFactory

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(GameOption.MUSIC_PATH + "background.mp3")
        pygame.mixer.music.set_volume(0.5) 
        pygame.mixer.music.play(-1)

        # Membuat window game dengan ukuran sesuai konfigurasi
        self.screen = pygame.display.set_mode((GameOption.SCREEN_WIDTH, GameOption.SCREEN_HEIGHT))
        pygame.display.set_caption("Zen Block")
        self.clock = pygame.time.Clock()
        
        # Memuat font untuk menampilkan teks
        self.font = pygame.font.Font(os.path.join(GameOption.FONT_PATH, "Quicksand-Bold.ttf"), 28)
        
        # Mulai ulang game (setup ulang papan, shapes, dll)
        self.restart()

    # Fungsi untuk memulai ulang kondisi game
    def restart(self):
        self.board = Board()
        self.shapes = ShapeFactory.generate()
        self.dragging = None
        self.score = 0
        self.game_over = False

    # Fungsi utama untuk menjalankan game loop
    def run(self):
        running = True
        while running:

            # Membersihkan layar
            self.screen.fill(GameOption.BACKGROUND_COLOR)
            self.handle_events()

            # Gambarkan papan ke layar
            self.board.draw(self.screen)

            # Tampilkan bayangan shape saat di-drag
            if self.dragging:
                self.dragging.draw_preview(self.screen)
            
            # Gambarkan shape ke layar
            for shape in self.shapes:
                shape.draw(self.screen)

            # Gambarkan skor
            self.draw_score()
            if self.game_over:
                self.draw_game_over()

            # Update tampilan layar
            pygame.display.flip()

            # Batasi ke 60 frame per detik
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    # Menampilkan skor ke layar
    def draw_score(self):
        text = self.font.render(f"Score: {self.score}", True, GameOption.TEXT_COLOR)
        rect = text.get_rect(center=(GameOption.SCREEN_WIDTH // 2, 50))
        self.screen.blit(text, rect)

    # Menampilkan pesan Game Over
    def draw_game_over(self):
        overlay = pygame.Surface((GameOption.SCREEN_WIDTH, GameOption.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        text = self.font.render("Game Over! Press R to Restart", True, (255, 255, 255))
        rect = text.get_rect(center=(GameOption.SCREEN_WIDTH // 2, GameOption.SCREEN_HEIGHT // 2))
        self.screen.blit(text, rect)

    # Mengecek apakah semua shape tidak bisa diletakkan di board
    def is_game_over(self):
        return not any(self.board.can_place(shape) for shape in self.shapes)

    # Menangani semua input dari pengguna
    def handle_events(self):
        for event in pygame.event.get():

            # Tutup permainan jika pengguna menekan tombol close window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Menangani input keyboard
            elif event.type == pygame.KEYDOWN:
                # Restart game jika tombol R ditekan dan game sedang berakhir
                if self.game_over and event.key == pygame.K_r:
                    self.restart()

            # Menangani klik mouse saat game masih berjalan
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                for shape in self.shapes:
                    # Hitung ukuran shape berdasarkan matriksnya
                    w = len(shape.matrix[0]) * GameOption.CELL_SIZE
                    h = len(shape.matrix) * GameOption.CELL_SIZE

                    # Periksa apakah mouse mengklik area shape
                    if pygame.Rect(shape.x, shape.y, w, h).collidepoint(event.pos):
                        shape.held = True  # Aktifkan status drag
                        shape.offset = (event.pos[0] - shape.x, event.pos[1] - shape.y)  # Simpan offset posisi mouse dalam shape

                        # Simpan shape yang sedang di-drag
                        self.dragging = shape
                        break  # Hentikan pencarian shape lainnya

            # Menangani pergerakan mouse saat dragging shape
            elif event.type == pygame.MOUSEMOTION and self.dragging and not self.game_over:
                # Update posisi shape mengikuti posisi mouse (dengan memperhitungkan offset)
                ox, oy = self.dragging.offset
                self.dragging.x = event.pos[0] - ox
                self.dragging.y = event.pos[1] - oy

            # Menangani lepasnya mouse (drop shape)
            elif event.type == pygame.MOUSEBUTTONUP and self.dragging and not self.game_over:
                if self.board.place(self.dragging):  # Coba tempatkan shape ke papan
                    # Tambah skor jika ada garis yang dibersihkan
                    self.score += self.board.clear_lines() * 10  
                    
                    # Hapus shape dari daftar aktif
                    self.shapes.remove(self.dragging)  

                    # Jika semua shape sudah diletakkan, generate shape baru
                    if not self.shapes:
                        self.shapes = ShapeFactory.generate()

                    # Cek apakah kondisi game over terpenuhi setelah menempatkan shape baru
                    if self.is_game_over():
                        self.game_over = True
                else:
                    # Jika tidak bisa ditempatkan, kembalikan shape ke posisi awal
                    self.dragging.x, self.dragging.y = self.dragging.origin

                # Reset status drag
                self.dragging.held = False
                self.dragging = None