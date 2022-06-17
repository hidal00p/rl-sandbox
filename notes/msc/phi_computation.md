# Phi function conputation

## General
Phi function encapsulates a generalized term that defines a contribution magnitude to the whole grad of J_theta for grad log probability of each action (a_t) selection from state s_t.
In more intuitive terms, each time a gradient of cost function is computed, it is constructed of small pieces.
Each piece attempts to indicate how beneficial it turned out to take a particular action a_t from state s_t.
Based on this indication a gradient is constructed in such a way that pieces with large index become more probable, and pieces with low(or negative) index become less probable.