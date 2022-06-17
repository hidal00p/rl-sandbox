# PG methods

## General
Policy gradient methods, as the name suggests, directly estimate gradient of the cost function with respect to policy parameters.
Such approach searches the theta parameter vector space for a set of values which would result in (sub)optimal agent bahaviour.

The simplest form of objective gradient may be found [here](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html#deriving-the-simplest-policy-gradient).
A standard argument against this particular representation is that it is extremely variant. Due to the fact that cost function gradient takes on a form of statstical expectation, it may be estimated/approximated somehow.
Such estimation is done by the means of Monte-Carlo sampling and averaging. Yet every grad log probability of an action taken at step t obtains a werid scaling factor of the full return over the whole trajectory.

A more logical way would be to scale each grad log probability of an action at t by the return which happened after this action. 
This creates a sort of cause-consequence relation between the probabilities of an action and its improvement factors.

As an attempt to decrease high variance behaviour, a baseline is introduced to the log probabilities corresponding to a certain reward-to-go.
A common choice for a baseline would a state-value function.
State-value function compares the reward-to-go obtained in a current episode with an estimate of how valuable this state is on average(how much reward it yields).

In fact some other profitability parameter may be used like state-action value or advantage function -> Fi function.
Such functions however are normally not known to us, as they depend on very rich and sparse trajectory roll-outs and reward signal.
Reward signal may not only be expressed as r(s), but as r(s, t), which adds to the complexity.

Due to the fact that these functions are not known they are approximated with various methods, and of course one of such methods is usage of NNs.
However approximations are not limited to NNs, any mathematical optimization approach may be used.
So optimization is used because a function space is searched to find A, Q or V representation which is close to true form.
Thus be it a polynimial, nn or trust region - anything would work to a degree of accuracy.

Thus as a small summary. It seems that most PG algos reduce to a couple steps:
1. Perform a policy roll-out. Run currently known policy, thus obtaining episodic samples.
2. Evaluate this policy, by analysing obtained samples.
 - Compute rewards to go
 - Compute critic values, and re-fit your critic Fi to new observations
3. Compute grad logs. Assemble everything into a full picture for objective grad. Backpropagate your gradient onto policy parameters. Repeat.

Or in simpler terms:
1. Run
2. Analyze
3. Learn & Repeat

## On policy

## Off policy