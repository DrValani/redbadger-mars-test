import unittest


def move(instructions: str):
    y = 0
    for instruction in instructions:
        if instruction == 'F':
            y += 1
    return f'0 {y} N'

class TestRobotMoves(unittest.TestCase):

    def test_can_move_forward(self):
        instructions = 'F'
        output = move(instructions)
        self.assertEqual(output, '0 1 N')

    def test_can_move_forward_n_times(self):
        instructions = 'FFF'
        output = move(instructions)
        self.assertEqual(output, '0 3 N')

        
if __name__ == '__main__':
    unittest.main()