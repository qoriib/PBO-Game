from shapes.base import AbstractShape

class ShapeS2(AbstractShape):
    def get_matrix(self):
        return [
            [0, 1, 1],
            [1, 1, 0]
        ]

    def get_image(self):
        return "block-f.svg"

    def shape_type(self):
        return "F"