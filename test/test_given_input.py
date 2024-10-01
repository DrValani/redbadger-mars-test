import unittest

from src.robot_instructions import move


class TestSampleInput(unittest.TestCase):

    def test_ensure_sample_data_is_correct(self):
        robot_scent = []
        grid_size = '5 3'
        robot_position = '1 1 E'
        robot_instructions = 'RFRFRFRF'
        output = move(robot_position, robot_instructions, grid_size, robot_scent)
        self.assertEqual(output, '1 1 E')

        robot_position = '3 2 N'
        robot_instructions = 'FRRFLLFFRRFLL'
        output = move(robot_position, robot_instructions, grid_size, robot_scent)
        self.assertEqual(output, '3 3 N LOST')

        robot_position = '0 3 W'
        robot_instructions = 'LLFFFLFLFL'
        output = move(robot_position, robot_instructions, grid_size, robot_scent)
        self.assertEqual(output, '2 3 S')
