from pommerman.agents import BaseAgent
from pommerman import constants


class TestAgent(BaseAgent):
    """Sometimes the best move is to not move"""

    def act(self, obs, action_space):
        return constants.Action.Bomb.value
