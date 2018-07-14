class EvaluationCondition(object):

    """Base evaluation condition. Returns true/false based on observable state and what it's looking for"""

    # extended_ops is ops, plus a couple extra things so we aren't recalculating each evaluation
    def evaluate(self, extended_ops, angle=0, flip_x=False):
        raise NotImplementedError()

    def genesis(self):
        raise NotImplementedError()

    def to_dict(self):
        return {
            "conditionType": self.__class__.__name__,
            "params": self.params_to_dict()
        }

    def params_to_dict(self):
        raise NotImplementedError()