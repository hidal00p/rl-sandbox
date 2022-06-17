# PG methods
Policy gradient methods, as the name suggests, directly estimate gradient of the cost function with respect to policy parameters.
Such approach searches the theta parameter vector space for a set of values which would result in (sub)optimal agent bahaviour.

The simplest form of objective gradient may be found [here](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html#deriving-the-simplest-policy-gradient).
A standard argument against this particular representation is that it is extremely variant. Due to the fact that cost function gradient takes on a form of statstical expectation, it may be estimated/approximated somehow.
Such estimation is done by the means of Monte-Carlo sampling and averaging. Yet every grad log probability of an action taken at step t obtains a werid scaling factor of the full return over the whole trajectory.

A more logical way would be to scale each grad log probability of an action at t by the return which happened after this action. 
This creates a sort of cause-consequence relation between the probabilities of an action and its improvement factors.
