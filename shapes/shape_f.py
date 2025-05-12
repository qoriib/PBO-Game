from shapes.base import AbstractShape

class ShapeF(AbstractShape):
    def get_matrix(self):
        return [[1, 1, 1]]

    def get_image(self):
        return "block-f.svg"

    def shape_type(self):
        return "F"