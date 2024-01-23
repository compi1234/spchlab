# LAB04: Bayesian Classification using a Generative Model


## Background

- [Bayesian Classification](Bayes.md)  gives a brief refresh on Bayes formula and its application in classification problems.   It also introduces Gaussian Mixture models (GMMs) as universal probability density approximators. (skip if you know it)

## Exercises

Within these exercises we make use of the "Generative, Bayesian" Framework in which the data is modeled  by a simple Gaussian  Distribution or Mixture of Gaussians distribution.
By using psycho-acoustic features such as pitch and formants we can keep the number of features very small (1 to 3).

The different exercises all make use of the same paradigm and apply it to gradually more complex situations by increasing the dimensionality of the features and increasing the number of classes.

The work involves: data processing, data exploration, data modeling, building the classifier, testing the classifier.




- in lab03_source_filter  you looked at the distributions of pitch and formants in an exploratory way


##### Exercises

- [Hillenbrand-1.ipynb]   Gender Classification with Pitch as Feature

- [Hillenbrand-2.ipynb]   Vowel Classification with Formant Features

