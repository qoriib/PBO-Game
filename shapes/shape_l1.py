from shapes.base import AbstractShape

class ShapeL1(AbstractShape):
    def get_matrix(self):
        return [
            [1, 0],
            [1, 1]
        ]

    def get_image(self):
        return "block-red.png"

    def shape_type(self):
        return "L1"