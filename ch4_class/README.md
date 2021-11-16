# CH4: Classification in Speech Recognition

## Lecture Notes
- [lecture notes in .html](https://homes.esat.kuleuven.be/~spchlab/H02A6/lectures/ch4_html/index.html)
- [lecture notes in .pdf](https://homes.esat.kuleuven.be/~spchlab/H02A6/lectures/ch4.pdf)



## Exercises

Within this chapter classification of speech (single frame or segment) is tackled with a Bayesian approach.

In these exercises we work with real speech data and feature vectors derived from prototypical feature extraction modules. 

In the first part (TIMIT-1) we gradually more complex situations by increasing the dimensionality of the features and increasing the number of classes.

We explore both a generative approach with GMMs and a discriminative approach with Neural Nets



#### TIMIT-1:  Vowel Classification from a single frame with FBANK, FBANK-PCA or MFCC features using GMMs

In TIMIT-1 we analyze the importance of feature extraction and resulting properties of features for a classifier built with Gaussian Mixture Models

- FBANK features are the most natural ones, but are correlated, a property that doesn't go well with GMMs

- FBANK-PCA are the FBANK features subject to a PCA (Principal Component Transform).  The PCA transform is a linear transform learned from the data as a whole and generates features that are overall maximally decorrelated.  Realize, however, that this does not imply decorrelatedness on a class per class basis.
In practice - at least for the small example we work with - this seems to performa very well.
One other potential drawback is that the transform is data dependent, thus potentially language, database, noise, ... dependent.  We do not test this in this exercise, but should be aware of it.

- MFCC features are derived by a DCT transform on the FBANK features.   The MFCC features seem to posess all desirable properties of good feature vectors.  The transform is simlpe, data independent and results in highly decorrelated features.  Hence MFCCs are easily modeled by GMMs.

Remark that PCA and DCT are both linear transform.  This implies they don't modify the data in any sense, they only present the data in a different view to the backend recognizer and do it in such a way that this backend performs significantly better.   They both also show that most information (for our task) can be captured by a rather low dimensional (13D or even less) feature vector .

In the last section we perform a number of experiments with a Multilayer Perceptron (MLP) classifier, using the sklearn package.   We may observe that classification rates are not better or worse than with GMMs, but the MLP works equally well for all feature representations


#### TIMIT-2   from a single frame with FBANK, FBANK-PCA or MFCC features using MLPs

This notebook replicates and extends the MLP classifier using a different python package: PyTorch.
PyTorch is one of the most popular packages used for speech recognition.

#### TIMIT-3


