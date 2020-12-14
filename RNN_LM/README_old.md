# RNN language modeling

This is a Jupyter Notebook on RNN language modeling for the course [Speech Recognition](https://onderwijsaanbod.kuleuven.be/syllabi/e/H02A6AE.htm#activetab=doelstellingen_idp33776) (Master Artificial Intelligence) at KU Leuven.

## Goals of the exercise

This exercise gives a demonstration of the basics of language modeling with recurrent neural networks.
The different aspects of the work involved are illustrated: data processing, word embeddings, testing a network and hyperparameter tuning. By running it from a Notebook, little or no programming experience is expected from the user.

## Getting Started with Google Colab

This exercise should be run in [Google Colab](https://colab.research.google.com/). Google Colab is a collabarative workspace in the cloud giving researchers easy access to GPUs.

* To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in. 
* In your browser, click on rnn_lm.ipynb on the Github page. Once the notebook has opened, click on 'Open in Colab' at the top of the file.
* When you try to run one of the cells, you will get a warning about the fact that the notebook is not authored by Google. Make sure that you tick the box 'Reset all runtimes before running' and then click on 'Run anyway'. It will ask for confirmation, so click 'yes'.

## Notes on Notebooks, Python, TensorFlow

A notebook contains a combination of text and Python code and is organized in cells. Text cells are just meant to contain an explanation of what is going on. Code cells can be executed one at a time by clicking on the arrow pointing to the cell. This step-by-step execution let's you follow at an easy pace what is going on in a long and complex program. Strictly speaking there is no requirement that you execute cells from top to bottom, but in practice notebooks are typically organized as such.

Our notebook contains Python code. Most of the code (with the explanation) will be self-explanatory. If you're not familiar with Python, following information may be worthwhile reading:

* Python uses indexing starting at 0
* The import statement defines packages and parts thereof for you current program
* Python is object oriented. E.g. rnn_lm() creates an object of the class rnn_lm.
* TensorFlow is one of the most popular packages for DNN training. It is the computational workhorse for our exercise.

