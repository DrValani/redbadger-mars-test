from src.parser import parse

right_turn = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}
left_turn = {
    'E': 'N',
    'S': 'E',
    'W': 'S',
    'N': 'W',
}


def rotate(orientation: str, instruction: str) -> str:
    if instruction == 'R':
        return right_turn[orientation]
    return left_turn[orientation]  # Out of scope: Need to handle case when orientation is not L or R


def move(initial_position: str, instructions: str) -> str:
    x, y, orientation = parse(initial_position)
    for instruction in instructions:
        if instruction == 'F':
            if orientation == 'E':
                x += 1
            elif orientation == 'W':
                x -= 1
            elif orientation == 'N':
                y += 1
            elif orientation == 'S':
                y -= 1
        else:
            orientation = rotate(orientation, instruction)
    return f'{x} {y} {orientation}'
