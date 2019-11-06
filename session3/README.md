# Bayesian Classification and GMMs in Speech Recognition

This is a collection Jupyter Notebooks on Classification for the course [Speech Recognition](https://onderwijsaanbod.kuleuven.be/syllabi/e/H02A6AE.htm#activetab=doelstellingen_idp33776) (Master Artificial Intelligence) at KU Leuven.

## Goals of the exercise

Within this exercise we make use of the "Generative, Bayesian" Framework in which the data is modeled  by a Gaussian  Mixture. (For course notes on this topic, see  http://homes.esat.kuleuven.be/~compi/H02A6/course_notes/html/ch3_classification )
The different exercises all make use of the same paradigm and apply it to gradually more complex situations by increasing the dimensionality of the featuresand increasing the number of classes.

The work involves: data processing, data exploration, data modeling, building the classifier, testing the classifier.

In this folder you find 4 notebooks:
- [BayesGMM]       A very brief refresh on Bayes formula and GMMs (skip if you know it)
- [Hillenbrand-1]  Gender Classification with Pitch as Feature
- [Hillenbrand-2]  Vowel Classification with Formant Features
- [TIMIT-1]        Vowel Classification from a single frame of MELSPEC or MELFBANK features


## Getting Started with Google Colab

This exercise should be run in [Google Colab](https://colab.research.google.com/). Google Colab is a collabarative workspace in the cloud giving researchers easy access to GPUs.

* To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in. 
* In your browser, click on <exercise_name>.ipynb on the Github page. Once the notebook has opened, click on   <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>   at the top of the file.
* When you try to run one of the cells, you will get a warning about the fact that the notebook is not authored by Google. Make sure that you tick the box 'Reset all runtimes before running' and then click on 'Run anyway'. It will ask for confirmation, so click 'yes'.

**** IMPORTANT NOTE ****  
If you want to run this notebook outside the Google Colab environment, e.g. on your own PC,  make sure to download the spchlab/spchutils package and install it, see how it is done in Colab in the first cell'.


## Notes on Notebooks, Python, sklearn, spchutils,  ...

A notebook contains a combination of text and Python code and is organized in cells. Text cells just contain an explanation of what is going on. Code cells can be executed one at a time by clicking on the arrow pointing to the cell. This step-by-step execution let's you follow at an easy pace what is going on in a long and complex program. Strictly speaking there is no requirement that you execute cells from top to bottom, but in practice notebooks are typically organized as such.  This is largely the case in these exercises as well, though at moments you may go a few cells back and run again with different settings.

Our notebook contains Python code. Most of the code (with the explanation) will be self-explanatory. If you're not familiar with Python, following information may be worthwhile reading:

* Python uses indexing starting at 0
* The import statement defines packages and parts thereof for you current program
* Python is object oriented. 
* sklearn is Python's basic Machine Learning package.  
* spchutils is a small local package this is used for this exercise. It contains the IO routines for the data we use. It also contains a class 'GaussianMixtureClf', which does Bayesian Classification with Gaussian Mixture modeling.  


