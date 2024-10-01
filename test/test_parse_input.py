import unittest

from src.parser import parse_initial_position, parse_grid


# Assume that all input data is in the correct format


class TestParseInitialPositionString(unittest.TestCase):

    def test_parse_initial_position(self):
        initial_position = '1 2 N'
        x, y, orientation = parse_initial_position(initial_position)
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)
        self.assertEqual(orientation, 'N')

    def test_parse_grid_size(self):
        grid_size = '5 3'
        max_x, max_y = parse_grid(grid_size)
        self.assertEqual(max_x, 5)
        self.assertEqual(max_y, 3)


if __name__ == '__main__':
    unittest.main()
