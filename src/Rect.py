class Rectangle:
    def __init__(self, base: float, height: float):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")

        self.base = base
        self.height = height

    def area(self) -> float:
        return self.base * self.height

    def __repr__(self):
        return f"Rectangle(base={self.base}, height={self.height})"

    def rect_vector(self):
        return (self.base, self.height)
