# Hidden Markov Models - Elementary Examples



## Background

For some background reading and course note examples, cfr:   
- hmm_examples_discrete.ipynb
- hmm_examples_gauss1.ipynb
- hmm_examples_gauss2.ipynb


## Exercise1 - Computing with HMMs: basics

The purpose of this exercise is do basic computations, such as Viterbi alignment, with a given HMM.

The HMMs used are very simple, but as you will experience, they get involved quite quickly.
Doing these BY HAND will help you in understanding how the problem gets manageable by splitting the observation probabilities out of trellis computations.  


## Exercise2 - Computing with HMMs: feature transformations

Exercise 2 draws your attention to the stationarity assumption in HMMs.
When you look at an observation sequence we tend to (visualy) infer sequence information.
In a way you could say that we are halucinating the order as to an HMM the order in which
observations follow in an individual state doesn't matter at all.
This exercise shows on one hand how strong and misleading this can be, but on the other
hand we show that there is often an easy fix in the use of delta features.

This exercise CAN be done by hand but involves quite a few computations.
You can also track it in the notebook and do a few computations.  
However, try to answer each of the questions as you progress and without looking ahead !!


## Exercise3 - Recognition with HMMs: