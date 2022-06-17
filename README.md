# Sandbox for RL algorithms

## Rational
Running RL algorithms in various environments is already made trivial. [Stable baseline 3](https://github.com/DLR-RM/stable-baselines3) litteraly provides one-liner programs.
For some such level of abstraction is really desirable, however for others(like me) it causes a bit of pain. 
Instead of simply training on an off-the-shelf algo, I would like to reproduce this algo myself and understand it better.

RL is saturated with concepts of roll-outs(trajectories), rewards, state and action spaces.
For newcomers(like me) these objects may feel intangible through the lense of formulas, however in actuality they are very computable.
Thus in this repo I will attempt to capture concepts like trajectories, log probabilities, advantage functions, etc for different state-of-the-art algos.

## Env setup
I use miniconda to control my envs, but other virtiual env managers may be used as well following the same logic:

1. Create a project
2. Register an env in it
3. Activate env and add neccessary packages
4. Run

e.g. conda process

`$ conda create -n [your_name] python=3.8`

`$ conda activate [your_name]`

`$ pip3 install packages // Actually add packages here`

