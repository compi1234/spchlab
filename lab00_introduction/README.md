# LAB00: Introduction to *spchlab* 

### What is spchlab ?
*spchlab* is a collection of notebooks for teaching and experimenting with speech understanding, speech processing and speech recognition.
*spchlab* uses primarily python as a programming language is and is available on github **https://github.com/compi1234/spchlab**

*spchlab* is divided in a number of ***labs*** that group a number of notebooks on one specific topic such as **lab02_Spectrogram**, **lab06_Classification**, **lab07_Hidden Markov Models**, ...
Within each ***lab*** you will find both ***Tutorial*** and ***Exercise*** Notebooks.
The README file contains a short description of all material in the lab-folder.

Most students will use *spchlab* in the **Google Colab** environment. If you are not familiar with Google Colab you should read the following first:  **[Introduction to Colab](COLAB.md)**.

###  Use of *spchlab* in  H02A6A
*spchlab* is extensively used in the KULeuven course H02A6A on speech recognition and was originally developed for that course.
However, students should be aware that the current version of *spchlab* goes broader and contains quite a bit of extra material, in the form of extra Tutorials or exercises on topics that are not covered in the current version of the course.

### Running your first notebook in *spchlab*

As a first notebook, we suggest to run  **Segmentations.ipynb** in this folder.  This notebook walks you through the typical structure of a spchlab notebook with plenty of how-to comments:
- making sure that the prerequisite package *pyspch* is installed
- doing all the required/typical imports
- loading sampled data or other required data
- running the core of the notebook

In this introductory notebook we show how to access demo audio samples, listen to them and align them with provided transcripts

### Some Platform Notes

The notebooks have been developed and tested on *Google Colab*, *Windows 10/11* and *MacOS*.  
The preferred python version at this moment is Python 3.10, but it is expect to  run on platforms supporting Python 3.8, 3.9 and 3.10 (higher also for most notebooks, but not extensively tested)



#### Dependencies
*spchlab*  depends on the *pyspch* package.   
*pyspch* makes use of the mainstream machine learning stack (numpy, pandas, ... ) and of *librosa* for speech processing   
A number of modules (using DNNs) require Pytorch, torchaudio and/or tensorflow

The most notable platform specific dependencies are thus:
- AUDIO: anything relating to AUDIO I/O tends to be hardware and platform dependent
- CUDA: Some notebooks rely on pytorch and torch audio and have been tested in a CUDA environmnet;  CUDA is not available on MAC and hence these notebooks need to be run in a CPU-only version, making them potentially slower.

#### Running on your own PC ?

If you want to run these notebooks outside the Google Colab environment, e.g. on your own PC,  make sure to install the **pyspch** package (available in github/compi1234/pyspch).  

Dependencies:
+ preferably Python >=3.8, <=3.10
+ Most secure is to build a dedicated environment based e.g. on the available in py39.yml 
+ You may just add pyspch to your current environment, but be aware that this may lead to conflicts
+ Some notebooks require pytorch
    - look at https://pytorch.org/get-started/locally/  for installation instructions for pytorch and its dependencies

### Required skill level of Python and Jupyter

*spchlab* notebooks are about running demos and exercises and mainly about answering conceptual questions.

The idea is that the coding has been done for you.   At the most you need to provide a bit of glue.
What is expected is that you adjust parameter settings, that you understand what is happening ,
that you can answer conceptual questions. 


#### Structure of our Jupyter notebooks
Jupyter notebooks contain a combination of text and Python code.  Notebooks are organized in cells. Text cells just contain an explanation of what is going on. Code cells can be executed one at a time by clicking on the arrow pointing to the cell. This step-by-step execution let's you follow at your own pace what is going on in a long and complex program. Strictly speaking there is no requirement that you execute cells from top to bottom, but in practice notebooks are often organized as such.  Especially the first couple of cells with imports and new function definitions should be run in their natural order.

#### How about Python ?
Our notebooks contain Python code. 

If you're not familiar with Python, following information may be worthwhile:
+ Python uses indexing starting at 0
+ Python is object oriented
+ The import statement defines packages and parts thereof that you want to access in your current  project.

