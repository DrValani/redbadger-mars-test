import unittest


def move(instruction: str):
    return '0 1 N'

class TestRobotMoves(unittest.TestCase):

    def test_can_move_forward(self):
        instruction = 'F'
        output = move(instruction)
        self.assertEqual(output, '0 1 N')

    def test_can_move_forward_twice(self):
        instruction = 'FF'
        output = move(instruction)
        self.assertEqual(output, '0 2 N')
        
if __name__ == '__main__':
    unittest.main()