# Sandbox for RL algorithms

## Rational
Running RL algorithms in various environments is already made trivial. [Stable baseline 3](https://github.com/DLR-RM/stable-baselines3) litteraly provides one-line programs.
For some such level of abstraction is really desirable, however for others(like me) it causes a bit of confusion.
Instead of simply training on an off-the-shelf algo, I would like to add a level of tangibility to these algorithms.
This would involve examinig and measuring some of the core concepts like trajectories, rewards (in its various forms), intermediate value functions and action samling.

**Disclaimer**

*Currently the focus is going to be around PPO and SAC, as two state-of-the-art representatives for DRL on-ploicy and off-policy methods respectively.*

## Env setup
I use miniconda to control my envs, but other virtiual-env managers may be used as well following the same logic:

1. Create a project
2. Register an env in it
3. Activate the env and add neccessary packages
4. Run and debug

e.g. conda process

`$ conda create -n [your_name] python=3.8`

`$ conda activate [your_name]`

`$ pip3 install [packages]`

