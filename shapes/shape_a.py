from shapes.base import AbstractShape

class ShapeA(AbstractShape):
    def get_matrix(self):
        return [[1]]

    def get_image(self):
        return "block-a.svg"

    def shape_type(self):
        return "A"