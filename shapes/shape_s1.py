from shapes.base import AbstractShape

class ShapeS1(AbstractShape):
    def get_matrix(self):
        return [
            [1, 1, 0],
            [0, 1, 1]
        ]

    def get_image(self):
        return "block-f.svg"

    def shape_type(self):
        return "F"