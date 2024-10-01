def parse_initial_position(initial_position: str) -> [int, int, str]:

    x, y, orientation = initial_position.split()

    x = int(x)
    y = int(y)

    return x, y, orientation


def parse_grid(grid_size: str) -> [int, int]:
    max_x, max_y = grid_size.split()
    return int(max_x), int(max_y)
