
# For actions:
from pommerman import constants
import random
from evaluation_rule import EvaluationRule
import json
import copy

class Genome(object):
    @staticmethod
    def crossover(genome_a, genome_b):
        # TODO: Code me
        # Make 2 child genomes:
        child_a = Genome(False)
        child_b = Genome(False)
        # Figure out crossover points in parent_a and parent_b
        cross_point_a = random.randrange(0,len(genome_a.rules))
        cross_point_b = random.randrange(0,len(genome_b.rules))
        # First part of a + last part of b:
        child_a.rules = copy.deepcopy(genome_a.rules[:cross_point_a] + genome_b.rules[cross_point_b:])
        # First part of b + last part of a:
        child_b.rules = copy.deepcopy(genome_b.rules[:cross_point_b]+genome_a.rules[cross_point_a:])
        return [child_a, child_b]

    def __init__(self, perform_genesis=True):
        # Ensure we have suitable defaults:
        self.rules = []
        self.default_action = constants.Action.Stop
        # Perform genesis in most cases (new instance):
        if perform_genesis:
            self.genesis()


    def genesis(self):
        num_rules = random.randint(1,20)
        self.rules = []
        for i in range(num_rules):
            rule = EvaluationRule()
            self.rules.append(rule)
        # Random action for the default:
        self.default_action = random.choice(list(constants.Action))

    # Returns the default action for this genome
    # Note that you are responsible for calling .value
    def default_action(self):
        return self.default_action

    def evaluate(self, extended_obs):
        for rule in self.rules:
            result = rule.evaluate(extended_obs)
            if result != None:
                return rule.get_action(result)
        return self.default_action

    # WARNING: This will MODIFY self
    # This is ruby equivalent of .mutate!
    def mutate(self):
        ADD_CHANCE = 0.2
        REMOVE_CHANCE = 0.2
        MOVE_CHANCE = 0.1
        MUTATE_CHANCE = 0.1
        # 1) Add random rules:
        if random.random() < ADD_CHANCE:
            num_to_add = random.randint(1,3)
            for i in range(num_to_add):
                rule = EvaluationRule()
                self.rules.append(rule)
        # 2) Remove random rules:
        if random.random() < REMOVE_CHANCE:
            num_to_remove = random.randint(1,3)
            if len(self.rules) > num_to_remove + 1:
                for i in range(num_to_remove):
                    j = random.randrange(0,len(self.rules))
                    del self.rules[j]
        # 3) Move rules:
        for i in range(len(self.rules)):
            if random.random() < MOVE_CHANCE:
                j = random.randrange(0,len(self.rules))
                self.rules[j], self.rules[i] = self.rules[i], self.rules[j]
        # 4) Mutate rules:
        for i in range(len(self.rules)):
            if random.random() < MUTATE_CHANCE:
                self.rules[i].mutate()


    # TODO: Add to/from json
    def to_dict(self):
        return {
            "rules" : list(map(lambda x:x.to_dict(),self.rules)),
            "default_action" : self.default_action.value
        }