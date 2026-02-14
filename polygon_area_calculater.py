
import math

class Rectangle:
    def __init__(self, width, height):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.        """
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ""
        for _ in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        """
        Calculates how many times a given shape fits inside the rectangle.

        Args:
            shape (Rectangle): The shape to check.

        Returns:
            int: The number of times the shape fits inside the rectangle.
        """
        if isinstance(shape, Rectangle):
            return (self.width // shape.width) * (self.height // shape.height)
        return 0

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        """
        Initializes a Square object.

        Args:
            side (int): The length of the square's sides.
        """
        self.side = side

    def set_side(self, side):
        self.width = side
        self.height = side
    def set_width(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


# Usage example:
rect = Rectangle(10, 5)
print(rect.get_area())  # 50
rect.set_height(3)
print(rect.get_perimeter())  # 26
print(rect)  # Rectangle(width=10, height=3)
print(rect.get_picture())  # a picture of the rectangle

sq = Square(9)
print(sq.get_area())  # 81
sq.set_side(4)
print(sq.get_diagonal())  # 5.656854249492381
print(sq)  # Square(side=4)
print(sq.get_picture())  # a picture of the square

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 6