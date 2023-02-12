# spchlab

*spchlab* is a Repository of Jupyter Noteboobs for Speech Recognition Demos and Exercises.

*spchlab* heavily relies on the *pyspch* package.   
Both *spchlab* and *pyspch* reside on GitHub and are freely available.   

*spchlab* is divided in a number of different topics
that stand rather independent from each other.

## Platforms and Requirements

The notebooks have been developed and tested on Google Colab, Windows and MacOS.
The code is 99% platform independent, but some dependencies are heavily platform dependent, especially w.r.t. audio I/O.

Generally speaking we expect the code to run on platforms supporting Python 3.7 or higher.
pyspch has a list of dependencies that guarantee (within the bounds of our testing) full functionality.
In the coding we avoided features that are considered too novel to be robust.  
So we expect great robustness against upcoming novel releases, though we are aware that Python's extremely fast and often non forgiving update practices may break the code here and there if you are running the most recent version of all packages that we rely on.

A special note on 'pytorch'.  Some notebooks rely on pytorch and torch audio; these have not been verified on macOS.



## Jupyter notebooks
A notebook contains a combination of text and Python code and is organized in cells. Text cells just contain an explanation of what is going on. Code cells can be executed one at a time by clicking on the arrow pointing to the cell. This step-by-step execution let's you follow at your own pace what is going on in a long and complex program. Strictly speaking there is no requirement that you execute cells from top to bottom, but in practice notebooks are often organized as such.  This is largely the case in these exercises as well, though at moments you may go a few cells back, change some parameters and run an experiment again with different settings.



## Running a notebook in Google Colab

All of the exercises can be run in [Google Colab](https://colab.research.google.com/).
Google Colab is a collabarative workspace in the cloud.   All you need is a browser to get access.  For most people Google Colab will be the easiest way to run the exercises.  
To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in.

Run a notebook in COLAB:
  - go to the spchlab repository in Github [https://github.com/compi1234/spchlab]
  - click to open <exercise_name>.ipynb
  - now, do one of the following:
	1. click on the "open in colab" browser extension icon  (if you have it installed)
	2. Paste the GitHub exercise URL in a running colab session
  - start running the notebook in colab

When you start running the notebook, you may get a warning that the notebook is not authored by Google.   Just ignore and click  'Run anyway'. 


## Running the notebooks on your own PC

If you want to run these notebooks outside the Google Colab environment, e.g. on your own PC,  make sure to install the **pyspch** package (available in github/compi1234/pyspch).  

Dependencies:
+ expects Python >= 3.6 (preferably >=3.7, <=3.9)
+ Most secure is to build a dedicated environment based e.g. on the available in py37.yml 
+ You may just add pyspch to your current environment, but be aware that this may lead to conflicts
+ Some notebooks require pytorch
    - look at https://pytorch.org/get-started/locally/  for installation instructions for pytorch and its dependencies
+ The notebooks have been tested on Windows, MacOS and GoogleColab so we expect them to be rather robust
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
