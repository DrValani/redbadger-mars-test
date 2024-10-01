import unittest

from src.parser import parse

## Assume that all input data is in the correct format

class TestParseInitialPositionString(unittest.TestCase):

    def test_can_move_north(self):
        initial_position = '1 2 N'
        x, y, orientation = parse(initial_position)
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)
        self.assertEqual(orientation, 'N')


if __name__ == '__main__':
    unittest.main()
