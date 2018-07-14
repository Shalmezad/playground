from . import EvaluationCondition
import random

class KickCondition(EvaluationCondition):
    """Determines whether the player is able to kick or not"""
    def genesis(self):
        self.should_have_kick = random.random() < .5
        return self
    
    def evaluate(self, extended_ops, angle=0, flip_x=False):
        return extended_ops['can_kick'] == self.should_have_kick

    def params_to_dict(self):
        return {
            "shouldHaveKick" : self.should_have_kick
        }