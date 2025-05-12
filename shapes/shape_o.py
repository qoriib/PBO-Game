from shapes.base import AbstractShape

class ShapeO(AbstractShape):
    def get_matrix(self):
        return [
            [1, 1],
            [1, 1]
        ]

    def get_image(self):
        return "block-yellow.png"

    def shape_type(self):
        return "O"