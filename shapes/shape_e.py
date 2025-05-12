from shapes.base import AbstractShape

class ShapeE(AbstractShape):
    def get_matrix(self):
        return [[1, 1], [1, 1]]

    def get_image(self):
        return "block-e.svg"

    def shape_type(self):
        return "E"