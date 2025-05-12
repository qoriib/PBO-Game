from shapes.base import AbstractShape

class ShapeI1(AbstractShape):
    def get_matrix(self):
        return [[1], [1]]

    def get_image(self):
        return "block-c.svg"

    def shape_type(self):
        return "C"