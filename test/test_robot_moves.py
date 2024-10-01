import unittest

from src.robot_instructions import move_robot


class TestRobotMoves(unittest.TestCase):

    def test_can_move_north(self):
        initial_position = '0 0 N'
        instructions = 'F'
        output = move_robot(initial_position, instructions, '10 10', [])
        self.assertEqual(output, '0 1 N')

    def test_can_move_north_n_times(self):
        initial_position = '0 0 N'
        instructions = 'FFF'
        output = move_robot(initial_position, instructions, '10 10', [])
        self.assertEqual(output, '0 3 N')

    def test_can_move_east(self):
        initial_position = '0 0 E'
        instructions = 'F'
        output = move_robot(initial_position, instructions, '10 10', [])
        self.assertEqual(output, '1 0 E')

    def test_can_move_east_n_times(self):
        initial_position = '0 0 E'
        instructions = 'FF'
        output = move_robot(initial_position, instructions, '10 10', [])
        self.assertEqual(output, '2 0 E')

    def test_can_change_orientation(self):
        initial_position = '0 0 N'
        instructions = 'R'
        output = move_robot(initial_position, instructions, '10 10', [])
        self.assertEqual(output, '0 0 E')


if __name__ == '__main__':
    unittest.main()