def parse(initial_position: str) -> [int, int, str]:

    x, y, orientation = initial_position.split()

    x = int(x)
    y = int(y)

    return x, y, orientation
