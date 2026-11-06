from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self.width= width
        self.height= height
    
   
    def set_width(self, new_width):
        self.width = new_width
    

    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = sqrt(self.width **2 +  self.height ** 2)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        return "\n".join("*" * self.width for _ in range(self.height)) + "\n"
    
    def get_amount_inside(self, shape):
        return (self.get_area()) // (shape.get_area())
    
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width= side
        self.height= side

    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)
    
    def __repr__(self):
        return f'Square(side={self.width})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))