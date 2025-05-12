from shapes.base import AbstractShape

class ShapeU(AbstractShape):
    def get_matrix(self):
        return [
            [1, 0, 1],
            [1, 1, 1]
        ]

    def get_image(self):
        return "block-purple.png"

    def shape_type(self):
        return "U"