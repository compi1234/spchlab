# Hidden Markov Models - Real Speech Examples


## Exercise1 - Effect of Transition Probabilities

In this exercise we make more and more effective use of the topology in an HMM.
In the code we always implement this via the transition probability matrix.

1. when there is no underlying HMM we basically do a frame by frame classification
2. The simplest HMM is an ergodic HMM allowing for transitions between any states
	- if the transition probs are all equal we basically revert to situation '1'
	- we use the state model because we expect to stay several frames in a state, this is encouraged by setting a selfloop probability which is significantly higher than the transition probabilities.  
	- note: The exact values depend on the 'observation model' as transition probabilities are multiplied with observation probabilities.
3. A "forced alignment" is obtained by only allowing a state sequence that corresponds with a given transcription.  Plenty of applications use such forced alignment.   It is also part of HMM Viterbi training.
	- sometimes it is advised to do an alignment that is not 100% strict.  This can be the case if we allow for small deviations from the reference transcription, e.g. due to pronunciation variants or to right-out mispronunciations, ommissions of words, insertions, ...
