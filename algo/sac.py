import gym, torch
from stable_baselines3.sac import SAC, MlpPolicy

def initPolicy():
    return MlpPolicy()

def initModel(env : gym.Env):
    return SAC(
        MlpPolicy,
        env,
        policy_kwargs=dict(activation_fn=torch.nn.ReLU, net_arch=[512, 512, 256, 128]),
        verbose=1
    )