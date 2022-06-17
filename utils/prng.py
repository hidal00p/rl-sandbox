import gym

SEED = 42

def seedAndResetEnv(env: gym.Env, reseedObs: bool = False, reseedAct: bool = False):
    if reseedObs:
        env.seed(SEED)
    
    if reseedAct:
        env.action_space.seed(SEED)
    
    return env.reset()

def setEnvSeed(seed: int = 42):
    global SEED
    SEED = seed