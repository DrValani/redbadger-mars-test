import unittest

from src.parser import parse_initial_position
from src.robot_instructions import rotate


class TestRobotMoves(unittest.TestCase):

    def test_can_turn_north_to_east(self):
        orientation = 'N'
        instruction = 'R'
        output = rotate(orientation, instruction)
        self.assertEqual(output, 'E')

    def test_can_turn_from_east_to_south(self):
        orientation = 'E'
        instruction = 'R'
        output = rotate(orientation, instruction)
        self.assertEqual(output, 'S')

    def test_can_turn_east_to_north(self):
        orientation = 'E'
        instruction = 'L'
        output = rotate(orientation, instruction)
        self.assertEqual(output, 'N')

    def test_can_turn_from_south_to_east(self):
        orientation = 'S'
        instruction = 'L'
        output = rotate(orientation, instruction)
        self.assertEqual(output, 'E')


if __name__ == '__main__':
    unittest.main()