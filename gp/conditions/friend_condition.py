from . import DeltaEvaluationCondition
import numpy as np

class FriendCondition(DeltaEvaluationCondition):

    def evaluate_rc(self, extended_ops, r, c):
        friend_id = extended_ops['teammate'].value
        friend_locations = np.where(extended_ops['board'] == friend_id)
        for f_r, f_c in zip(friend_locations[0], friend_locations[1]):
            if f_r == r and f_c == c:
                return True
        return False


    def genesis(self):
        super(FriendCondition, self).genesis()
        # We don't need to do anything for genesis. Either our friend's at the position or not...
        return self