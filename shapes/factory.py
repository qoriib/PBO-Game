import random
from config.options import GameOption
from shapes.shape_a import ShapeA
from shapes.shape_b import ShapeB
from shapes.shape_c import ShapeC
from shapes.shape_d import ShapeD
from shapes.shape_e import ShapeE
from shapes.shape_f import ShapeF
from shapes.shape_g import ShapeG

class ShapeFactory:
    SHAPE_CLASSES = [ShapeA, ShapeB, ShapeC, ShapeD, ShapeE, ShapeF, ShapeG]

    @staticmethod
    def generate():
        shapes = []
        center = GameOption.SCREEN_WIDTH // 2
        spacing = 200
        start_x = center - spacing
        for i in range(3):
            shape_class = random.choice(ShapeFactory.SHAPE_CLASSES)
            matrix = shape_class.get_matrix(shape_class)
            w = len(matrix[0]) * GameOption.CELL_SIZE
            h = len(matrix) * GameOption.CELL_SIZE
            x = start_x + i * spacing - w // 2
            y = GameOption.BOARD_OFFSET_Y + GameOption.GRID_SIZE * GameOption.CELL_SIZE + 80
            shapes.append(shape_class((x, y)))
        return shapes