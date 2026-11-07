def interception_identifier(
    area: list[list[float]]
) -> list[list[int]]:

    size = len(area)

    return [
        [1 if i == j else 0 for j in range(size)]
        for i in range(size)
    ]
