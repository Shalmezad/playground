from . import DeltaEvaluationCondition

class BombExistCondition(DeltaEvaluationCondition):
    """Merely checks to see if a bomb exists at a given position"""

    def evaluate_rc(self, extended_ops, r, c):
        return extended_ops['bomb_blast_strength'][r][c] > 0

    def genesis(self):
        super(BombExistCondition, self).genesis()
        return self