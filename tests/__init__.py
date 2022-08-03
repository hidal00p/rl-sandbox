"""
Functional tests to check method correctness or validate ideas.
It is a simple script that fetches a particular function, finds its annontated value, and runs it if it is asked for.
Test cases a priori do not accept arguments. They are run as is, all the neccessary information should be defined within the test case.
"""

import time

TestCases = {}

def testCase(testName = None):
    assert testName != None, "Please give your test a unique name"
    def _testable(func):
        if testName not in TestCases.keys():
            TestCases[testName] = func
        else:
            raise RuntimeError(
                f"Function _{func.__name__}_ cannot be registered under case name _{testName}_ as it is already in use.\n"
                f"A function _{TestCases[testName].__name__}_ was previously encountered among test case list.\n"
                "Please provide a unique name and re-run the program!"
                )
        
        return func

    return _testable

@testCase("sac")
def testRunSAC():
    import gym
    from envs import ENVS
    import algo.sac as sac

    env = gym.make(ENVS["lunar"])
    model = sac.initModel(env)
    model.train()

@testCase("ppo-run")
def testRunPPO():
    import gym
    from envs import ENVS
    import algo.ppo as ppo

    totalSteps = 300_000
    netArch = [64, 128, 128, 32]

    saveFolderName = str(totalSteps)
    for dim in netArch:
        saveFolderName += f"-{dim}"

    env = gym.make(ENVS["lunar"])
    model = ppo.initModel(env, netArch)
    model.learn(total_timesteps=totalSteps)
    model.save(f"ppo/{saveFolderName}/model.zip")

@testCase("ppo-eval")
def testTrainedPPO():
    import gym
    from envs import ENVS
    import algo.ppo as ppo

    env = gym.make(ENVS["lunar"])
    model = ppo.PPO.load(f"ppo/model.zip")
    
    obs = env.reset()
    done = False
    
    while not done:
        env.render()
        time.sleep(.02)

        action, _ = model.predict(obs, deterministic=True)
        obs, _, done, _ = env.step(action)

@testCase("ppo-continous-run")
def testContinousPPORun():
    # TODO: a multi threaded loop that tests various NN configurations, and saves their trained values with some frequency
    pass

@testCase("hello-world")
def testHelloWorld():
    print("Hello World")