from enum import Enum
import random

class NumericalComparison(Enum):
    LessThan = 0
    Equal = 1
    GreaterThan = 2
    LessThanOrEqual = 3
    GreaterThanOrEqual = 4

    @classmethod
    def random_condition(cls):
        # cls here is the enumeration
        return random.choice(list(cls))


    def evaluate(self, side_a, side_b):
        if self.value == NumericalComparison.LessThan.value:
            return side_a < side_b
        elif self.value == NumericalComparison.Equal.value:
            return side_a == side_b
        elif self.value == NumericalComparison.GreaterThan.value:
            return side_a > side_b
        elif self.value == NumericalComparison.LessThanOrEqual.value:
            return side_a <= side_b
        elif self.value == NumericalComparison.GreaterThanOrEqual.value:
            return side_a >= side_b
        else:
            raise Exception("Unknown condition", self.value)
        
    def __str__(self):
        if self.value == NumericalComparison.LessThan.value:
            return "<"
        elif self.value == NumericalComparison.Equal.value:
            return "=="
        elif self.value == NumericalComparison.GreaterThan.value:
            return ">"
        elif self.value == NumericalComparison.LessThanOrEqual.value:
            return "<="
        elif self.value == NumericalComparison.GreaterThanOrEqual.value:
            return ">="
        else:
            raise Exception("Unknown condition", self.value)        