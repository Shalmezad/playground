import pommerman
from pommerman import agents
from test_agent import TestAgent
from dummy_agent import DummyAgent


def main():
    # Print all possible environments in the Pommerman registry
    print(pommerman.registry)
    # Create a set of agents (exactly four)
    agent_list = [
        DummyAgent(),
        DummyAgent(),
        DummyAgent(),
        DummyAgent(),
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
