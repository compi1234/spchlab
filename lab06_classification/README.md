# LAB 06: Classification of frames with Spectral and Cepstral Feature Vectors

## Exercises

In these exercises we work with prototypical speech feature vectors.
(mel frequency filterbanks, mel frequency cepstral coefficients and related representations).

Mostly we base the classification on single frames, but sometimes also on segments in which consecutive frames are spliced together.

ALl exercises in this lab, make use of (parts of) the [TIMIT database](../data/TIMIT.md)




#### TIMIT-1:  Vowel Classification from a single frame with MELFB, MELFB-PCA or MFCC features using GMMs
**Notebook: timit-1.ipynb**

In TIMIT-1 the focus is on the feature extraction and the impact of feature properties on classification results, both for GMM and DNN classifiers.
We work with a very small subset of the TIMIT database (tinyTIMIT) and use just 3 phone classes.
Despite this limited investigation, a number of general properties of the features and their interplay with the classifier will be more than obvious and general enough.

- MELFB features are the baseline.   
The MELFB come natural but are correlated, a property that doesn't go well with a Euclidean distance measure and with GMMs.

- MELFB-PCA are the MELFB features subject to a PCA (Principal Component Transform).  
The PCA transform is a linear transform learned from the data as a whole and generates features that are overall maximally decorrelated.  
Realize, however, that this does not imply decorrelatedness on a class per class basis.
In practice - at least for the small example we work with - this seems to perform very well.
Another potential drawback is that the transform is data dependent, thus potentially language, database, noise, ... dependent.  We do not test this in this exercise, but we should be aware of it.
A generally more performing - data driven - transform is  LDA (Linear Discriminant Analysis) as it takes class-ids into account.

- MFCC features are derived from MELFB by a DCT transform.   
The MFCC features seem to posess all desirable properties of good feature vectors.  The transform is simple, data independent and results in highly decorrelated features.  Moreover the information seems concentrated in the lower order coefficients. Hence MFCCs are a natural fit to any distance metric / machine learning operation that follows.

Remark that PCA, LDA and DCT are all linear transform.  This implies they don't modify the data in any sense, they only present the data in a different view to the backend recognizer and do it in such a way that this backend performs significantly better.   They all show that most information (for our task) can be captured by a rather low dimensional (13D or even less) feature vector .

In the last section we perform a number of experiments with a Multilayer Perceptron (MLP) classifier, using the sklearn package.   We may observe that classification rates are not better or worse than with GMMs for this small task.
The striking difference is however that the MLP works equally well for all feature representations including the raw MELFB.


#### TIMIT-2   from a single frame with MELFB, MELFB-PCA or MFCC features using MLPs

This notebook replicates and extends the MLP classifier using a different python package: PyTorch.
PyTorch is one of the most popular packages used for speech recognition.
It is meant for students who want to familiarize themselves with a few concepts from DNN learning such as learning rate, bach size, ...


#### TIMIT-3   GMM Training

In TIMIT-3 we work with the whole TIMIT database and train and evaluate a number of different models


#### TIMIT-4   GMM vs DNN

In this notebook we compare GMM and DNN frame based output for speech utterances.



#### GMM-M-F (DEMO):  Utterance Classification with GMMs

**Notebook: demo_gmm_mg.ipynb**

The goals is to classify an utterance (or a longer recording) according to a stable attribute such as gender of the speaker , dialect, language, age .  Obvious this always has the implicit assumption of having a single speaker in the recording.   The same setup can work to classify recording attributes instead of speaker attributes, e.g.  noisy background, quiet, narrowband telephone speech, in-car recording,  ...

The approach is simple.  A frame based classifier is trained with each frame labeled with the attribute.   Utterance classification is done by accumulating frame based evidence. Simply multiplying likelihoods or adding up the loglikelihoods is mathematically correct under the assumptions that all frames are independent (iid).   This is bending reality more than a bit as successive frames are not at all independent of each other.   The obtained utterance level posteriors are gross exagerations, but just working with loglikelihood ratios will still be a quite correct indication of which class is the more likely one.    Normalizing the total loglikelihood by the number of observation gives an average per frame evidence score, which often yields a quite interpretable result.

