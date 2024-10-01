import unittest

from src.robot_instructions import move


class TestRobotGetsLost(unittest.TestCase):

    def test_robot_gets_lost_going_north_leaves_a_scent(self):
        robot_scent = []
        grid_size = '1 1'
        lost_robot_initial_position = '0 0 N'
        lost_robot_instructions = 'F'
        lost_robot_output = move(lost_robot_initial_position, lost_robot_instructions, grid_size, robot_scent)

        next_robot_initial_position = '0 0 N'
        next_robot_instructions = 'F'
        next_robot_output = move(next_robot_initial_position, next_robot_instructions, grid_size, robot_scent)

        self.assertEqual(lost_robot_output, '0 1 N LOST')
        self.assertEqual(next_robot_output, '0 0 N')
