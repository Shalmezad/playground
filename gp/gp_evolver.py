import pommerman
from pommerman import agents
from pommerman import constants
from dummy_agent import DummyAgent
from genome import Genome
from gp_agent import GpAgent
import random
import copy
import json
import math
from multiprocessing import Pool
import pickle
import sys

def tournament(arr):
    if len(arr) == 0:
        raise Exception("Cannot have tournament with 0 members!")
    elif len(arr) == 1:
        # Win by default, I guess...
        return arr[0]
    elif len(arr) == 2:
        # Play a game:
        result = head_to_head(arr[0], arr[1])
        if result == 1:
            return arr[0]
        elif result == -1:
            return arr[1]
        else:
            # Tie....
            # Pick one:
            return random.choice(arr)
    else:
        # Longer than 2, 
        # Split in half:
        split_point = math.floor(len(arr)/2)
        side_a = arr[:split_point]
        side_b = arr[split_point:]
        side_a_winner = tournament(side_a)
        side_b_winner = tournament(side_b)
        return tournament([side_a_winner, side_b_winner])

# Returns 1 (genome_a_win), 0 (tie) or -1 (genome_b_win)
def head_to_head(genome_a, genome_b):
    agent_list = [
        GpAgent().set_genome(genome_a),
        GpAgent().set_genome(genome_b),
        GpAgent().set_genome(genome_a),
        GpAgent().set_genome(genome_b),
    ]
    env = pommerman.make('PommeTeamFast-v0', agent_list)        
    state = env.reset()
    done = False
    while not done:
        #env.render()
        actions = env.act(state)
        state, reward, done, info = env.step(actions)
    #print('  Result {}'.format(info))
    #Result {'result': <Result.Win: 0>, 'winners': [0, 2]}
    #Result {'result': <Result.Tie: 2>}
    env.close()
    # Figure out the result to return:
    if info['result'] == constants.Result.Tie:
        return 0
    elif info['result'] == constants.Result.Win:
        if 0 in info['winners']:
            return 1
        else:
            return -1
    else:
        raise Exception("Unknown result: {}", info)
        return 0

# Returns 1 (genome_a_win), 0 (tie) or -1 (genome_b_win)
def vs_simple_agent(genome_a):
    agent_list = [
        GpAgent().set_genome(genome_a),
        agents.SimpleAgent(),
        GpAgent().set_genome(genome_a),
        agents.SimpleAgent(),
    ]
    env = pommerman.make('PommeTeamFast-v0', agent_list)        
    state = env.reset()
    done = False
    while not done:
        #env.render()
        actions = env.act(state)
        state, reward, done, info = env.step(actions)
    #print('  Result {}'.format(info))
    #Result {'result': <Result.Win: 0>, 'winners': [0, 2]}
    #Result {'result': <Result.Tie: 2>}
    env.close()
    # Figure out the result to return:
    if info['result'] == constants.Result.Tie:
        return 0
    elif info['result'] == constants.Result.Win:
        if 0 in info['winners']:
            return 1
        else:
            return -1
    else:
        raise Exception("Unknown result: {}", info)
        return 0

def main():
    # Print all possible environments in the Pommerman registry
    #random.seed(1023)
    # POOL SIZE MUST BE DIVISIBLE BY 2!
    pool_size = 50
    tournament_size = 8
    mutate_chance = 0.1
    pool = []
    process_pool = Pool()
    for i in range(pool_size):
        pool.append(Genome())

    generation = 0
    while True:
        generation += 1
        print('GENERATION {}'.format(generation), flush=True)

        # So, we take the pool size, and run that many tournaments:
        print('  Building tournament schedule...')
        tournament_rounds = []
        for i in range(pool_size):
            tournament_round = []
            for j in range(tournament_size):
                tournament_round.append(random.choice(pool))
            tournament_rounds.append(tournament_round)

        # Play all the tournaments
        print('  Running tournaments...')
        parents = process_pool.map(tournament, tournament_rounds)

        print('  Building new pool...')
        new_pool = []
        for i in range(math.floor(pool_size/2)):
            parent_a = parents.pop()
            parent_b = parents.pop()
            children = Genome.crossover(parent_a, parent_b)
            child_a = children[0]
            child_b = children[1]
            if random.random() < mutate_chance:
                child_a.mutate()
            if random.random() < mutate_chance:
                child_b.mutate()
            new_pool.append(child_a)
            new_pool.append(child_b)

        pool = new_pool

        print('  Finding best in pool...')
        best = tournament(pool)
        pickle.dump(best, open("data/winners/best_{}.pkl".format(generation), "wb"))

        print('  Pitting against simple agent...')
        for i in range(3):
            result = vs_simple_agent(best)
            print('  Result: {}'.format(result))


if __name__ == '__main__':
    main()
