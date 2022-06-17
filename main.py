import gym
import time
from algo.others import heuristic
from utils import RLPayload, Logger, prng

def run(
	envName: str, 
	itters: int = 100,
	fRender: bool = False
):
	assert itters >= 100, "More than a 100 itterations are required to invoke unfold function"
	
	logger = Logger()
	env = gym.make(envName)
	
	obs = prng.seedAndResetEnv(env, True, True)
	step = 0
	episode = 1
	for _ in range(1, itters + 1):
		action = heuristic(env, obs)
		# action = env.action_space.sample()
		
		prevObs = obs
		obs, reward, done, _ = env.step(action)
		step += 1

		if fRender:
			env.render()
			time.sleep(.02)
		
		logger.store(
			RLPayload(episode, step, prevObs, action, obs, reward, done)
		)
		if done:
			prng.seedAndResetEnv(
				env,
				True,
				False
			)
			episode += 1
			step = 0
			logger.logAll()
	
	env.close()

if __name__ == "__main__":
	# TODO: add cli args
	# 1) Seed
	# 2) Env choice
	# 3) fRender param

	# TODO: make envs work
	# 1) Lunar lander works
	# 2) Cheetah does not work
	envs = {
		"lunar":"LunarLander-v2",
		"cheetah":"HalfCheetah-v2"
	}

	run(envs["lunar"], 2000, True)