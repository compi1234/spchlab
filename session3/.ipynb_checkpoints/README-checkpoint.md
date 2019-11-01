# Classification in Speech Recognition

This is a Jupyter Notebook on Classification for the course [Speech Recognition](https://onderwijsaanbod.kuleuven.be/syllabi/e/H02A6AE.htm#activetab=doelstellingen_idp33776) (Master Artificial Intelligence) at KU Leuven.

## Goals of the exercise

These exercises develops a set of different classifiers.
Within this exercise we make use of the "Generative, Bayesian" Framework in which the data is modeled  by a Gaussian  Mixture.
The different aspects of the work involved are: data processing, data exploration, data modeling, building the classifier, testing the classifier.

There are three parts to the exercise:
- [Hillenbrand1]  Gender Classification with Pitch as Feature
- [Hillenbrand2]  Vowel Classification with Formant Features
- [TIMIT1]        Vowel Classification from a single frame of MELSPEC or MELFBANK features


## Getting Started with Google Colab

This exercise should be run in [Google Colab](https://colab.research.google.com/). Google Colab is a collabarative workspace in the cloud giving researchers easy access to GPUs.

* To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in. 
* In your browser, click on <exercise_name>.ipynb on the Github page. Once the notebook has opened, click on 'Open in Colab' at the top of the file.
* When you try to run one of the cells, you will get a warning about the fact that the notebook is not authored by Google. Make sure that you tick the box 'Reset all runtimes before running' and then click on 'Run anyway'. It will ask for confirmation, so click 'yes'.

**** IMPORTANT NOTE ****  Make sure that in the second cell,  the environment variable is set to COLAB, such that the correct packages get installed and can be loaded !!


## Notes on Notebooks, Python, sklearn, spchutils,  ...

A notebook contains a combination of text and Python code and is organized in cells. Text cells just contain an explanation of what is going on. Code cells can be executed one at a time by clicking on the arrow pointing to the cell. This step-by-step execution let's you follow at an easy pace what is going on in a long and complex program. Strictly speaking there is no requirement that you execute cells from top to bottom, but in practice notebooks are typically organized as such.  This is largely the case in these exercises as well, though at moments you may go a few cells back and run again with different settings.

Our notebook contains Python code. Most of the code (with the explanation) will be self-explanatory. If you're not familiar with Python, following information may be worthwhile reading:

* Python uses indexing starting at 0
* The import statement defines packages and parts thereof for you current program
* Python is object oriented. 
* sklearn is Python's basic Machine Learning package.  For this exercise we have expanded sklearn with a class 'GaussianMixtureClass', which does Bayesian Classification involving Gaussian Mixtures and we will load this from the 'spchutils' package.  This is automatically done for you at the beginning of the notebook.


