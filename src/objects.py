class Final:
    def __init__(self, function, floor):
        self.function = function
        self.floor = floor

    def __add__(self, other):
        if not isinstance(other, Final):
            return NotImplemented

        return Final(
            function=self.function + other.function,
            floor=self.floor + other.floor
        )

    def __repr__(self):
        return (
            f"Final(function={self.function}, "
            f"floor={self.floor})"
        )
