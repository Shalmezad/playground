import pommerman
from pommerman import agents
from test_agent import TestAgent
import pickle
from gp_agent import GpAgent


def main():
    # Print all possible environments in the Pommerman registry
    print(pommerman.registry)
    genome = pickle.load( open( "data/good/best_1251.pkl", "rb" ) )
    #genome = pickle.load( open( "data/good/best_3096.pkl", "rb" ) )
    # Create a set of agents (exactly four)
    agent_list = [
        GpAgent().set_genome(genome),
        agents.SimpleAgent(),
        GpAgent().set_genome(genome),
        agents.SimpleAgent(),
    ]
    # Make the "Free-For-All" environment using the agent list
    env = pommerman.make('PommeTeamFast-v0', agent_list)

    # Run the episodes just like OpenAI Gym
    for i_episode in range(1):
        state = env.reset()
        done = False
        while not done:
            #env.render()
            actions = env.act(state)
            state, reward, done, info = env.step(actions)
        print('Episode {} finished'.format(i_episode))
        print('  Result {}'.format(info))
        #Result {'result': <Result.Win: 0>, 'winners': [0, 2]}
        #Result {'result': <Result.Tie: 2>}
    env.close()


if __name__ == '__main__':
    main()
