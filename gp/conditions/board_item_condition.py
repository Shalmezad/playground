from . import DeltaEvaluationCondition
from pommerman import constants
import random

class BoardItemCondition(DeltaEvaluationCondition):
    """Merely checks to see if an item exists at a given position"""

    @staticmethod
    def possible_items():
        return [
            constants.Item.Passage,
            constants.Item.Rigid,
            constants.Item.Wood,
            constants.Item.Bomb,
            constants.Item.Flames,
            constants.Item.Fog,
            constants.Item.ExtraBomb,
            constants.Item.IncrRange,
            constants.Item.Kick
        ]

    def evaluate_rc(self, extended_ops, r, c):
        return extended_ops['board'][r][c] == self.item.value

    def genesis(self):
        super(BoardItemCondition, self).genesis()
        self.item = random.choice(self.possible_items())
        return self

    def params_to_dict(self):
        adj_dict = super(BoardItemCondition, self).params_to_dict()
        adj_dict['item'] = self.item.value
        return adj_dict