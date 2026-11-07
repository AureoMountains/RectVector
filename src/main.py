from geometry import Rectangle
from operations import Concatenate
from matrices import interception_identifier
from objects import Final
from visualizer import run_visualizer


def main():
    rectangle = Rectangle(10, 20)

    print(rectangle)
    print("Area:", rectangle.area())

    operation = Concatenate(distance=5, radius=3)
    print("Operation:", operation + 2)

    matrix = interception_identifier([
        [1, 2],
        [3, 4]
    ])

    print("Identity matrix:", matrix)

    object_a = Final(10, 2)
    object_b = Final(5, 3)

    print(object_a + object_b)

    run_visualizer(rectangle)


if __name__ == "__main__":
    main()
