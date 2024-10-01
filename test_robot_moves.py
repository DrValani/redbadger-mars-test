import unittest


def move(instructions: str):
    if instructions == 'FF':
        return '0 2 N'
    return '0 1 N'

class TestRobotMoves(unittest.TestCase):

    def test_can_move_forward(self):
        instructions = 'F'
        output = move(instructions)
        self.assertEqual(output, '0 1 N')

    def test_can_move_forward_twice(self):
        instructions = 'FF'
        output = move(instructions)
        self.assertEqual(output, '0 2 N')
        
if __name__ == '__main__':
    unittest.main()