# LAB00: Using and Installing *spchlab* 

The notebooks have been developed and tested on *Google Colab*, *Windows 10/11* and *MacOS*.  Early 2024, Colab uses Python 3.10 and this would thus be the preferred installation platform.

Generally speaking we expect the code to run on platforms supporting Python 3.8, 3.9 and 3.10 (higher also, but not tested)

Additional information on getting started with Google Colab is found [here](COLAB.md).   


### First Time Usage

*spchlab* is divided in a number of topical lab sessions .
For each of the labs start with the README.
This will contain a short description of Tutorials and the Exercises that are available in the lab-folder.

As a first notebook, we suggest to run  **Segmentations.ipynb** in [lab00_introduction](https://github.com/compi1234/spchlab/tree/main/lab00_introduction/).  This notebook walks you through the typical structure of a spchlab notebook with plenty of comments:
- making sure that the prerequisite package *pyspch* is installed
- doing all the required/typical imports
- loading sampled data or other required data
- running the core of the notebook

In this introductory notebook we show how to access demo samples, listen to them and align them with provided transcripts


### Dependencies
*spchlab*  depends on the *pyspch* package.   
*pyspch* makes use of the mainstream machine learning stack (numpy, pandas, ... ) anf of *librosa* for speech processing   
A number of modules (using DNNs) require Pytorch, torchaudio and/or tensorflow

The most notable platform specific dependencies are thus:
- AUDIO: anything relating to AUDIO I/O tends to be hardware and platform dependent
- CUDA: Some notebooks rely on pytorch and torch audio and have been tested in a CUDA environmnet;  CUDA is not available on MAC and hence these notebooks need to be run in a CPU-only version. 

### Running on your own PC ?

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

