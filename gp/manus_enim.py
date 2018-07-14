from genome import Genome

class ManusEnim(object):
    @staticmethod
    def get_genome():
        genome = Genome(False)

        genome.rules.append(ManusEnim.rule_first_move())

        return genome

    
    @staticmethod
    def rule_first_move():
        """
        First move: If we're in the corner of an L shape,
        Move RIGHT
        """
        