class Concatenate:
    def __init__(self, distance: float, radius: float):
        self.distance = distance
        self.radius = radius

    def __add__(self, other: float) -> float:
        result = self.distance + other

        if result > self.distance:
            return self.radius ** 2

        return result
