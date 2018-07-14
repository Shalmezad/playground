from . import EvaluationCondition
from . import NumericalComparison
import random

class AmmoCondition(EvaluationCondition):
    """Determines whether the player has a certain ammount of ammo"""
    def genesis(self):
        self.condition = NumericalComparison.random_condition()
        self.ammount = random.randint(0,4)
        return self
    
    def evaluate(self, extended_ops, angle=0, flip_x=False):
        # So < 3 means "is my ammo < 3"
        return self.condition.evaluate(extended_ops['ammo'], self.ammount)
    
    def __str__(self):
        return "mybombs {} {}".format(self.condition, self.ammount)

    def params_to_dict(self):
        return {
            "condition" : self.condition.value,
            "ammount" : self.ammount
        }