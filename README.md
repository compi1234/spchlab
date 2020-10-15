# spchlab
Global Repository for Speech Recognition Exercises in Python

## Getting Started with Google Colab

This exercise should be run in [Google Colab](https://colab.research.google.com/). Google Colab is a collabarative workspace in the cloud giving researchers easy access to GPUs.

* To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in. 
* In your browser, click on <exercise_name>.ipynb on the Github page. Once the notebook has opened, click on   <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>   at the top of the file.  [see also note2 !!]
* When you try to run one of the cells, you will get a warning about the fact that the notebook is not authored by Google. Make sure that you tick the box 'Reset all runtimes before running' and then click on 'Run anyway'. It will ask for confirmation, so click 'yes'.

**** IMPORTANT NOTES ****  
1. If you want to run this notebook outside the Google Colab environment, e.g. on your own PC,  make sure to download the spchlab/spchutils package and install it, see how it is done in Colab in the first cell'.
2. github has intermittent problems with opening python notebooks in a browser; sometimes it works, sometimes it doesn't ; the problem is old but has resurfaced recently.  If it doesn't open the first time, it probably will the second, third, ... time. Alternatively open Google Colab and open the github from there. 

## Notes on Notebooks, Python, sklearn, spchutils,  ...

A notebook contains a combination of text and Python code and is organized in cells. Text cells just contain an explanation of what is going on. Code cells can be executed one at a time by clicking on the arrow pointing to the cell. This step-by-step execution let's you follow at an easy pace what is going on in a long and complex program. Strictly speaking there is no requirement that you execute cells from top to bottom, but in practice notebooks are typically organized as such.  This is largely the case in these exercises as well, though at moments you may go a few cells back and run again with different settings.

Our notebook contains Python code. Most of the code (with the explanation) will be self-explanatory. If you're not familiar with Python, following information may be worthwhile reading:

* Python uses indexing starting at 0
* The import statement defines packages and parts thereof for you current program
* Python is object oriented. 
* sklearn is Python's basic Machine Learning package.  
* spchutils is a small local package this is used for this exercise. It contains the IO routines for the data we use. It also contains a class 'GaussianMixtureClf', which does Bayesian Classification with Gaussian Mixture modeling.  

