import gym
import torch
from stable_baselines3.ppo import PPO
from stable_baselines3.common.policies import ActorCriticPolicy as a2cppoMlpPolicy


def initModel(env : gym.Env, netArch):
    return PPO(
        a2cppoMlpPolicy,
        env,
        policy_kwargs=dict(activation_fn=torch.nn.ReLU, net_arch=netArch),
        verbose=1
    )