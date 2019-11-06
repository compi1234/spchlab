# Classification with Bayes Rule and a Generative Model (Gaussian Mixture Models)

## Generative and Discriminative Models

The standard approach to classify data from some feature observation $x$, is to compute a set of *discriminant functions* $f(C|x)$ for each class $C$ .  The class with maximum value will be recognised.
Using the *posterior probabilities* $P(C|x)$ as discriminant functions furthermore guarantees minimization of the error rate.   
However, this is easier said than done as in most cases there exists no mathematically tractable solution to estimate those posterior probabilities.

This has lead to two distinct classes of pattern classifiers.

#### Discriminative Models

In a discriminative system we learn the discriminant functions directly by minimizing the classification error on a given train set.

#### Generative Models

In generative models we compute the feature distributions of each class and by application of Bayes rule we then compute the posteriors:

$ P(C|x) = \frac{P(x|C) . P(C)}{ P(x) } $

The generative model has a number of advantages and disadvantages:
- the feature distributions can be estimated for each class independently, making a generative model in most cases computationally less demanding than a discriminative model
- the feature distributions will be estimated well in high density regions; on the other hand in low density regions the estimates may be poor if not very poor.  Now, it is the contrast $P(x|C_1)$ vs. $P(x|C_2)$ that contributes most in the discrimination and what is high density for $C_1$ will be low density for $C_2$ and vice versa.  Thus, in all situations these poor low density estimates have a significant impact on the computation of the discriminant functions.

## Building a Classifier with GMMs

In a generative model we must estimate the feature distributions per class with a priori unknown distribution.  A powerful approach exists in modeling the unknown distribution as a mixture of Gaussians. This type of model fits well with the assumption/observation that the features tend to cluster around one or a couple of centroids.  

STEPS:
1. Training the Feature Distributions $P(x|C)$

- Group the (labeled) data per class
- For each class: Fit a Gaussian Mixture to the train data

2. Construct the classifier


+ For each class : compute the likelihoods $P(x|C)$ and weighted likelihoods $P(x|C) . P(C)$
+ Compute the total likelihood of the feature vector: $P(x) = \Sum_c P(x|C) . P(C)$
+ For each class: compute the posteriors: $ P(C|x) = \frac{P(x|C) . P(C)}{ P(x) } $
+ Find the class with maximum posterior probability

Note: for plain classification we may omit the computation of $P(x)$ as it is identical over all classes and does not influence the maximisation operation.  On the other hand the exact posteriors are more intuitive and this simple normalization is not a computational burden to worry about.
