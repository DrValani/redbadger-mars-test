import unittest

from src.robot_instructions import move


class TestRobotMoves(unittest.TestCase):

    def test_can_move_north(self):
        initial_position = '0 0 N'
        instructions = 'F'
        output = move(initial_position, instructions)
        self.assertEqual(output, '0 1 N')

    def test_can_move_north_n_times(self):
        initial_position = '0 0 N'
        instructions = 'FFF'
        output = move(initial_position, instructions)
        self.assertEqual(output, '0 3 N')

    def test_can_move_east(self):
        initial_position = '0 0 E'
        instructions = 'F'
        output = move(initial_position, instructions)
        self.assertEqual(output, '1 0 E')

    def test_can_move_east_n_times(self):
        initial_position = '0 0 E'
        instructions = 'FF'
        output = move(initial_position, instructions)
        self.assertEqual(output, '2 0 E')

    def test_can_change_orientation(self):
        initial_position = '0 0 N'
        instructions = 'R'
        output = move(initial_position, instructions)
        self.assertEqual(output, '0 0 E')


if __name__ == '__main__':
    unittest.main()