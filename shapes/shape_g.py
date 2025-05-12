from shapes.base import AbstractShape

class ShapeG(AbstractShape):
    def get_matrix(self):
        return [[1], [1], [1]]

    def get_image(self):
        return "block-g.svg"

    def shape_type(self):
        return "G"