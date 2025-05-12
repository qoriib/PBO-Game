from shapes.base import AbstractShape

class ShapeD(AbstractShape):
    def get_matrix(self):
        return [[1, 1], [0, 1]]

    def get_image(self):
        return "block-d.svg"

    def shape_type(self):
        return "D"