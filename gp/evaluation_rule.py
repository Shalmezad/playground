
# For actions:
from pommerman import constants
import random
import conditions

class EvaluationRule(object):
    @staticmethod
    def possible_conditions():
        return [
            conditions.AmmoCondition,
            conditions.BoardItemCondition,
            conditions.BombExistCondition,
            conditions.EnemyCondition,
            conditions.FriendCondition,
            conditions.KickCondition
        ]
    @staticmethod
    def possible_angles():
        return [
            0,
            90,
            180,
            270
        ]

    @staticmethod
    def random_condition():
        condition_class = random.choice(EvaluationRule.possible_conditions())
        condition = condition_class().genesis()
        return condition

    
    @staticmethod
    def rotate_action(action, angle):
        if angle == 0:
            # Don't rotate:
            return action
        elif angle == 90:
            # Rotate right:
            if action == constants.Action.Right:
                return constants.Action.Down
            elif action == constants.Action.Down:
                return constants.Action.Left
            elif action == constants.Action.Left:
                return constants.Action.Up
            elif action == constants.Action.Up:
                return constants.Action.Right
        elif angle == 180:
            # Rotate around:
            if action == constants.Action.Right:
                return constants.Action.Left
            elif action == constants.Action.Down:
                return constants.Action.Up
            elif action == constants.Action.Left:
                return constants.Action.Right
            elif action == constants.Action.Up:
                return constants.Action.Down
        elif angle == 270:
            # Rotate left:
            if action == constants.Action.Right:
                return constants.Action.Up
            elif action == constants.Action.Down:
                return constants.Action.Right
            elif action == constants.Action.Left:
                return constants.Action.Down
            elif action == constants.Action.Up:
                return constants.Action.Left
        raise Exception("Can't rotate, unknown angle/action", action, angle)

    def __init__(self, perform_genesis=True):
        # Set defaults:
        self.conditions = []
        self.action = constants.Action.Stop
        if perform_genesis:
            self.genesis()
    
    def genesis(self):
        self.action = random.choice(list(constants.Action))
        num_conditions = random.randint(1,20)
        self.conditions = []
        for i in range(num_conditions):
            condition = self.random_condition()
            # Safety catch:
            if condition == None:
                raise Exception("genesis() failed to return self", condition_class.__name__)
            self.conditions.append(condition)

    # Determines whether this rule fires:
    # True if it does,
    # False if it doesn't
    # Takes in an extended observable state
    # TODO: Need to return the angle this matches for
    def evaluate(self, extended_obs):
        for angle in self.possible_angles(): 
            # We have an angle:
            # Go through each of our rules:
            is_good = True
            for condition in self.conditions:
                is_good = is_good and condition.evaluate(extended_obs, angle)
                if not is_good:
                    break
            if is_good:
                return angle
        # If we've made it this far:
        return None

    def mutate(self):
        ADD_CHANCE = 0.2
        REMOVE_CHANCE = 0.2
        MUTATE_CHANCE = 0.1
        # 1) Add random conditions:
        if random.random() < ADD_CHANCE:
            num_to_add = random.randint(1,3)
            for i in range(num_to_add):
                condition = self.random_condition()
                self.conditions.append(condition)
        # 2) Remove random conditions:
        if random.random() < REMOVE_CHANCE:
            num_to_remove = random.randint(1,3)
            if len(self.conditions) > num_to_remove + 1:
                for i in range(num_to_remove):
                    j = random.randrange(0,len(self.conditions))
                    del self.conditions[j]
        for i in range(len(self.conditions)):
            if random.random() < MUTATE_CHANCE:
                self.conditions[i].genesis() # Genesis is essentially mutate

    # Returns the action for this rule
    # Note that you are responsible for calling .value
    # TODO: Need to rotate action based on given angle
    def get_action(self, angle):
        if self.action == constants.Action.Stop:
            return self.action
        elif self.action == constants.Action.Bomb:
            return self.action
        else:
            # Rotate:
            return self.rotate_action(self.action, angle)
    
    def to_dict(self):
        return {
            "conditions" : list(map(lambda x:x.to_dict(),self.conditions)),
            "action" : self.action.value
        }