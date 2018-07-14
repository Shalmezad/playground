from . import EvaluationCondition

import random

class DeltaEvaluationCondition(EvaluationCondition):
    """A condition based on an offset from the player"""

    # extended_ops is ops, plus a couple extra things so we aren't recalculating each evaluation
    def evaluate(self, extended_ops, angle=0, flip_x=False):
        # TODO: Convert my position, delta_r/delta_c, and the angle into a row/column
        # If the row/column is out of bounds, return false.
        position = extended_ops['position']
        # Get a new delta by rotating our current delta:
        r_c = (self.delta_r, self.delta_c)
        new_delta_r_c = DeltaEvaluationCondition.rotate_delta(r_c, angle)
        # Get a new position by adding the delta to our position:
        new_pos = (position[0] + new_delta_r_c[0], position[1] + new_delta_r_c[1])
        # See if we're out of bounds:
        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= 11 or new_pos[1] >= 11:
            return False
        # We're good:
        return self.evaluate_rc(extended_ops, new_pos[0], new_pos[1])

    def evaluate_rc(self, extended_ops, r, c):
        raise NotImplementedError()


    def genesis(self):
        self.delta_r = random.randint(-11,11)
        self.delta_c = random.randint(-11,11)

    def params_to_dict(self):
        return {
            "delta_r" : self.delta_r,
            "delta_c" : self.delta_c
        }

    @classmethod
    def rotate_delta(cls, r_c, angle):
        # TODO: Double check the math
        r = r_c[0]
        c = r_c[1]
        if angle == 0:
            return (r, c)
        elif angle == 90:
            # To the right (pointing down):
            # x becomes y
            # y becomes -x
            return (c, -r)
        elif angle == 180:
            # To the right twice (pointing left):
            # x becomes -x,
            # y becomes -y
            return (-r, -c)
        elif angle == 270:
            # To the left (pointing up):
            # x becomes -y,
            # y becomes -x
            return (-c, r)
