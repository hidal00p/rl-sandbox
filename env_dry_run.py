import gym
from algo.vpg import heuristic

# Add cli arg for a seed
SEED = 42 # Currently SEED serves for space-action reproducebility

class AvailableStates:
	# Add enums instead of this arr
	_states = ["SILENT", "REGISTER", "LOG"]

	def check_state(state: str) -> bool :
		if state in AvailableStates._states:
			return True
		raise Exception("State has to be one of the following: SILENT, REGISTER, LOG")
	

class UnfoldingCallback:

	def __init__(self, state:str, num_episodes: int) -> None:
		AvailableStates.check_state(state)
		self.performance_compute_freq = int(0.1 * num_episodes)
		self.state = state
		self.init_state_vars()

	def run(self, itter, obs, action, reward, step, episode):
		if self.state == "LOG":
			self.performance_buffer.append(reward)
			if itter % self.performance_compute_freq == 0:
				UnfoldingCallback.log(
					itter,
					f"av_reward: {UnfoldingCallback.compute_average_performance(self.performance_buffer)}, steps: {step}"
				)
				self.performance_buffer.clear()
		if self.state == "REGISTER":
			self.register_trajectory(episode, obs, action, reward)

	def finalize(self):
		if self.state == "REGISTER":
			self.log_trajectories()

	def init_state_vars(self) -> None:
		if self.state == "LOG":
			self.performance_buffer = []
		if self.state == "REGISTER":
			self.trajectory_buffer = {}

	def compute_average_performance(performance_buffer: list) -> float :
		average= 0
		
		for performance in performance_buffer:
			average += performance
		
		return average / len(performance_buffer)

	def log(itter, value):
		print(f"\n[INFO itter #{itter}]: {value}")

	def register_trajectory(self, episode, obs, action, reward):
		key = str(episode)
		if key not in self.trajectory_buffer.keys():
			self.trajectory_buffer[key] = []
		self.trajectory_buffer[key].append((action, obs, reward))
	
	def log_trajectories(self):
		for episode in self.trajectory_buffer.keys():
			trajectory = self.trajectory_buffer[episode]
			trajectory_len = len(trajectory)
			logging_freq = int(0.1 * trajectory_len)
			count = 1
			UnfoldingCallback.log(
				episode,
				f"The trajectory follows with {trajectory_len} steps"
			)
			for a, s, r in trajectory:
				if count % logging_freq == 0:
					print(f"\tTau_{count}: \n\t\ta -> {a}\n\t\ts -> {s.tolist()}\n\t\tr -> {r}")
				count += 1


def to_string(env: gym.Env):
	print(f"env metadata: \n{env.metadata}\n")
	print(f"action space: {env.action_space}")
	print(f"random action space sample: {env.action_space.sample()}")
	print(f"observation space: {env.observation_space}")


def unfold(env: gym.Env, unfolding_state: str, itters: int = 100):
	assert itters >= 100, "More than a 100 itterations are required to invoke unfold function"
	
	cback = UnfoldingCallback(unfolding_state, itters)
	obs = seed_and_reset(env, True, True)
	
	step = 0
	episode = 1
	for itter in range(1, itters + 1):
		# action = heuristic(env, obs)
		action = env.action_space.sample()
		obs, reward, done, _ = env.step(action)
		# Add headless mode if no rendering is desired
		# env.render()
		step += 1
		cback.run(itter, obs, action, reward, step, episode)

		if done:
			seed_and_reset(env)
			episode += 1
			step = 0
	
	# Add lvl of verbosity for this
	cback.finalize()
	env.close()


def seed_and_reset(env: gym.Env, init_space: bool = False, init_actions: bool = False):
	if init_space:
		env.seed(SEED)

	if init_actions:
		env.action_space.seed(SEED)
	return env.reset()


def main(env_name: str, unfolding_state: str):
	env = gym.make(env_name)
	unfold(env, unfolding_state, 2000)
	

if __name__ == "__main__":
	# Add parser for seeding
	# Add cli args

	envs = {
		"lunar":"LunarLander-v2",
		"cheetah":"HalfCheetah-v2"
	}

	main(envs["lunar"], "SILENT")