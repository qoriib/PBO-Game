from shapes.base import AbstractShape

class ShapeB(AbstractShape):
    def get_matrix(self):
        return [[1, 1]]

    def get_image(self):
        return "block-b.svg"

    def shape_type(self):
        return "B"