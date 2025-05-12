from shapes.base import AbstractShape

class ShapeS2(AbstractShape):
    def get_matrix(self):
        return [
            [0, 1, 1],
            [1, 1, 0]
        ]

    def get_image(self):
        return "block-purple.png"

    def shape_type(self):
        return "S2"