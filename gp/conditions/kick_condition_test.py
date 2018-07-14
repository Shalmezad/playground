from conditions import KickCondition
import unittest

class KickConditionTest(unittest.TestCase):
    """
    Test that evaluate functions properly
    """
    def test_evaluates_able_to_kick(self):
        kick_condition = KickCondition()
        kick_condition.should_have_kick = True
        ops = {'can_kick': True}
        result = kick_condition.evaluate(ops)
        self.assertEqual(result, True)


    def test_evaluates_able_to_kick_looking_for_not(self):
        kick_condition = KickCondition()
        kick_condition.should_have_kick = False
        ops = {'can_kick': True}
        result = kick_condition.evaluate(ops)
        self.assertEqual(result, False)

    def test_evaluates_not_able_to_kick(self):
        kick_condition = KickCondition()
        kick_condition.should_have_kick = False
        ops = {'can_kick': False}
        result = kick_condition.evaluate(ops)
        self.assertEqual(result, True)

    def test_evaluates_not_able_to_kick_looking_for_able(self):
        kick_condition = KickCondition()
        kick_condition.should_have_kick = True
        ops = {'can_kick': False}
        result = kick_condition.evaluate(ops)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()