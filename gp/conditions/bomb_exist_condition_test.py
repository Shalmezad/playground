from conditions import BombExistCondition
import unittest

class BombExistConditionTest(unittest.TestCase):
    def setUp(self):
        self.ops = {}
        w, h = 11, 11;
        self.ops['bomb_blast_strength'] = [[0 for x in range(w)] for y in range(h)]
        self.ops['position'] = (4,4)


    """
    Test that evaluate functions properly
    """
    def test_evaluates_bomb_delta_no_angle_no_flip(self):
        bomb_exist_condition = BombExistCondition()
        # Player at 4,4, bomb at 6,5
        # Delta     2,1
        # Checking  6,5
        bomb_exist_condition.delta_r = 2
        bomb_exist_condition.delta_c = 1
        self.ops['bomb_blast_strength'][6][5] = 3
        result = bomb_exist_condition.evaluate(self.ops)
        self.assertEqual(result, True)

    def test_evaluates_bomb_delta_no_angle_no_flip(self):
        bomb_exist_condition = BombExistCondition()
        # Player at 4,4
        # Delta     2,1
        # Checking  6,5
        bomb_exist_condition.delta_r = 2
        bomb_exist_condition.delta_c = 1
        result = bomb_exist_condition.evaluate(self.ops)
        self.assertEqual(result, False)
