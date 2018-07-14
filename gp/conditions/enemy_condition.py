from . import DeltaEvaluationCondition
import numpy as np

class EnemyCondition(DeltaEvaluationCondition):

    def evaluate_rc(self, extended_ops, r, c):
        # 'enemies': [<Item.Agent1: 11>, <Item.Agent3: 13>, <Item.AgentDummy: 9>]
        enemy_ids = list(map(lambda x:x.value,extended_ops['enemies']))
        #friend_id = extended_ops['teammate'].value
        #print(extended_ops)
        #print('EnemyCondition#evaluate_rc')
        #print(enemy_ids)
        #print(friend_id)
        #enemy_ids.remove(friend_id)
        for enemy_id in enemy_ids:
            enemy_locations = np.where(extended_ops['board'] == enemy_id)
            for e_r, e_c in zip(enemy_locations[0], enemy_locations[1]):
                if e_r == r and e_c == c:
                    return True
        return False


    def genesis(self):
        super(EnemyCondition, self).genesis()
        # We don't need to do anything for genesis. Either our friend's at the position or not...
        return self