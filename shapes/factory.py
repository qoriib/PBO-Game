import random
from config.options import GameOption

# Mengimpor semua class bentuk (shape) yang merupakan turunan dari AbstractShape
from shapes.shape_a import ShapeA
from shapes.shape_b import ShapeB
from shapes.shape_c import ShapeC
from shapes.shape_d import ShapeD
from shapes.shape_e import ShapeE
from shapes.shape_f import ShapeF
from shapes.shape_g import ShapeG

# Kelas pembuat shape (factory) untuk menghasilkan shape secara acak
class ShapeFactory:
    # Daftar semua class shape yang tersedia
    SHAPE_CLASSES = [ShapeA, ShapeB, ShapeC, ShapeD, ShapeE, ShapeF, ShapeG]

    @staticmethod
    def generate():
        shapes = []  # List untuk menyimpan shape yang dihasilkan

        # Titik tengah layar untuk menyusun 3 shape di bawah papan
        center = GameOption.SCREEN_WIDTH // 2
        spacing = 200  # Jarak antar shape
        start_x = center - spacing  # Posisi x awal untuk shape pertama

        # Hasilkan 3 shape secara acak
        for i in range(3):
            
            # Pilih salah satu class shape secara acak dari daftar
            shape_class = random.choice(ShapeFactory.SHAPE_CLASSES)

            # Ambil matrix dari shape tersebut (ukuran dan bentuk blok)
            # Pemanggilan langsung class method/static method (tanpa instance)
            matrix = shape_class.get_matrix(shape_class)

            # Hitung ukuran pixel berdasarkan ukuran cell
            w = len(matrix[0]) * GameOption.CELL_SIZE  # Lebar shape
            h = len(matrix) * GameOption.CELL_SIZE     # Tinggi shape

            # Hitung posisi x dan y agar shape ditampilkan sejajar dan di bawah papan
            x = start_x + i * spacing - w // 2
            y = GameOption.BOARD_OFFSET_Y + GameOption.GRID_SIZE * GameOption.CELL_SIZE + 80

            # Buat instance shape dan tambahkan ke daftar
            shapes.append(shape_class((x, y)))

        # Kembalikan daftar 3 shape yang sudah dibuat
        return shapes