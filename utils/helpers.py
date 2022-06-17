# TODO:
# implement average reward function or class, implement reward to go calculation

class RLPayload():
    def __init__(
        self, 
        episode, 
        itteration,
        prevObs,
        action,
        currentObs,
        reward,
        fTerminal
    ):
        self.episode = episode
        self.itteration = itteration
        self.prevObs = prevObs
        self.action = action
        self.currentObs = currentObs
        self.reward = reward
        self.fTerminal = fTerminal
    
    def __strRaw__(self):
        raise NotImplementedError()

    def __str__(self):
        return f"[{self.episode}][{self.itteration}][{self.fTerminal}]:\n\tTransition: {self.prevObs} -> {self.currentObs}\n\tAction: {self.action}\n\tReward: {self.reward}"
