import unittest

from src.robot_instructions import move_robot


class TestRobotGetsLost(unittest.TestCase):

    def test_robot_gets_lost_going_north(self):
        grid_size = '1 1'
        initial_position = '0 0 N'
        instructions = 'FF'
        output = move_robot(initial_position, instructions, grid_size, [])
        self.assertEqual(output, '0 1 N LOST')

    def test_robot_gets_lost_out_going_south(self):
        grid_size = '1 1'
        initial_position = '0 0 S'
        instructions = 'F'
        output = move_robot(initial_position, instructions, grid_size, [])
        self.assertEqual(output, '0 0 S LOST')

    def test_robot_gets_lost_out_going_east(self):
        grid_size = '1 1'
        initial_position = '0 0 E'
        instructions = 'FF'
        output = move_robot(initial_position, instructions, grid_size, [])
        self.assertEqual(output, '1 0 E LOST')
