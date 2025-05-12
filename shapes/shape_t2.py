from shapes.base import AbstractShape

class ShapeT2(AbstractShape):
    def get_matrix(self):
        return [
            [1, 1, 1],
            [0, 1, 0]
        ]

    def get_image(self):
        return "block-yellow.png"

    def shape_type(self):
        return "T2"