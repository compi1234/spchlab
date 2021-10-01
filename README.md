# spchlab
Global Repository for Speech Recognition Exercises in Python / Jupyter Notebooks

## Jupyter notebooks
A notebook contains a combination of text and Python code and is organized in cells. Text cells just contain an explanation of what is going on. Code cells can be executed one at a time by clicking on the arrow pointing to the cell. This step-by-step execution let's you follow at an easy pace what is going on in a long and complex program. Strictly speaking there is no requirement that you execute cells from top to bottom, but in practice notebooks are often organized as such.  This is largely the case in these exercises as well, though at moments you may go a few cells back, change some parameters and run an experiment again with different settings.



## Running a notebook in Google Colab

All of the exercises can be run in [Google Colab](https://colab.research.google.com/).
Google Colab is a collabarative workspace in the cloud.   All you need is a browser to get access.  For most people Google Colab will be the easiest way to run the exercises.  (For alternatives, see below)   
To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in.

Run a notebook in COLAB:
* METHOD1 (works best, but requires the "open in colab" browser extension):
  - go to the spchlab repository in Github
  - click on <exercise_name>.ipynb
  - click on the "open in colab" browser extension icon  (no need to way for github to open the notebook!)
  - the notebook will start in COLAB for you
* METHOD2
  - open a Google Colab session
  - enter the github address of the notebook you want to open
* METHOD3
   - work as method1, but click on "open in colab" widget at the top of the page
   - this should work, but often it doesn't
    + sometime github refuses to open the page
    + and sometimes the links in the widget are not correct :)

You may ignore warnings!

When you try to run one of the cells, you may get a warning about the fact that the notebook is not authored by Google. Make sure that you tick the box 'Reset all runtimes before running' and then click on 'Run anyway'. It will ask for confirmation, so click 'yes'.

## Running the notebooks on your own PC

If you want to run this notebook outside the Google Colab environment, e.g. on your own PC,  make sure to install the **pyspch** package (available in github/compi1234/pyspch).  

Dependencies:
+ pyspch expects Python >= 3.6
+ Have a look at the requirements to see that there are no conflicts with other installations.
+ The notebooks have been tested on Windows, MacOS and GoogleColab so we expect them to be rather robust
+ One of the most difficult issues to support in a machine independent way is audio, we did our best ... but it is frustrating to fight the poor level of audio standardization (also influenced by security concerns):
  - good example: the Audio HTML widget in IPython (Notebooks) behaves different in Google Colab than in any other modern installation
+ Some notebooks were tested on binder, but not in a systematic way

## What do you need to know about Python ?

Our notebooks contain Python code. Most of the code (with the explanation) will be self-explanatory. If you're not familiar with Python, following information may be worthwhile:

* Python uses indexing starting at 0
* Python is object oriented.
* The import statement defines packages and parts thereof for you current program, those cells are obviously essential
* Packages that we use:
  + **pyspch**: this is our own speech processing / recognition package.  the only goal of the package is to support teaching.  hence, this is by no means optimized or intended to develop full speech recognition systems.
  + **sklearn**: is Python's basic Machine Learning package.
  + **Pytorch, torchaudio**: one of the leading packages for DNNs used in the speech community
  + **tensorflow**: Googles own package for DNNs
