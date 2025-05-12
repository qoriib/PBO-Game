from shapes.base import AbstractShape

class ShapeL2(AbstractShape):
    def get_matrix(self):
        return [
            [1, 1, 1],
            [1, 0, 0]
        ]

    def get_image(self):
        return "block-d.svg"

    def shape_type(self):
        return "D"