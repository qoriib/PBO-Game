from shapes.base import AbstractShape

class ShapeT1(AbstractShape):
    def get_matrix(self):
        return [
            [0, 1, 0],
            [1, 1, 1]
        ]

    def get_image(self):
        return "block-yellow.png"

    def shape_type(self):
        return "T1"