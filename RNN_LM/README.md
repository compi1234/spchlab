# RNN language modeling

This is a Jupyter Notebook on RNN language modeling for the course [Speech Recognition](https://onderwijsaanbod.kuleuven.be/syllabi/e/H02A6AE.htm#activetab=doelstellingen_idp33776) (Master Artificial Intelligence) at KU Leuven.

## Goals of the exercise

This exercise gives a demonstration of the basics of language modeling with recurrent neural networks.
The different aspects of the work involved are illustrated: data processing, word embeddings, testing a network and hyperparameter tuning. By running it from a Notebook, little or no programming experience is expected from the user.

## Getting Started with Google Colab

This exercise should be run in [Google Colab](https://colab.research.google.com/), which is a collabarative workspace in the cloud giving you easy access to GPUs.

* To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in.
* In your browser, click on rnn_lm.ipynb on the Github page. Once the notebook has opened, click on 'Open in Colab' at the top of the file.
* When you try to run one of the cells, you will get a warning about the fact that the notebook is not authored by Google. Make sure that you tick the box 'Reset all runtimes before running' and then click on 'Run anyway'. It will ask for confirmation, so click 'yes'.

## Dependencies for Python, TensorFlow

This notebook contains Python code. Most of the code (with the explanation) will be self-explanatory. It also makes extensive use of the TensorFlow package for DNN training.  It is the computational workhorse for our exercise.

Dependencies (as of 12/12/2020):

- rnn_lm.ipynb (current version)
  + Python 3.6 or above  (current standard in Colab)
  + Tensorflow V1.0  still supported by Colab, but will be deprecated at some point


- rnn_lm_py27.ipynb (legacy code)
  + Python 2.7    this will NOT run in COLAB anymore, but could be handy if your local machine still runs Python 2
  + Tensorflow V1.0
