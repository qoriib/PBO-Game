from shapes.base import AbstractShape

class ShapeI3(AbstractShape):
    def get_matrix(self):
        return [
            [1, 1, 1]
        ]

    def get_image(self):
        return "block-blue.png"

    def shape_type(self):
        return "I3"