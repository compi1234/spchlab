# Colab_intro - Working with *spchlab* and *pyspch* on Google Colab

## Running a notebook in Google Colab

To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in.

To run a notebook in COLAB:
  - go to the spchlab repository on Github [https://github.com/compi1234/spchlab]
  - click to open \<notebook>.ipynb
  - now, do one of the following:
	1. click on the "open in colab" browser extension icon  (if you have it installed)
	2. Paste the GitHub exercise URL in a running colab session
  - start running the notebook in colab
  - neglect the Colab Warnings (see below)

You may ignore following specific Colab WARNINGS
1. After you install the pyspch package (which is the first thing you need to do, unless you have it permanently installed), you probably get a warning that you need to *restart the runtime*, Just CLICK and CONTINUE.
2. When you start running the notebook, you may get a warning that the notebook is not authored by Google.  Just ignore and click  *Run anyway*.

## Setting up pyspch
**spchlab** uses the **pyspch** package for almost all demos / exercises.
**pyspch** is not pre-installed on Google Colab, so you need to install it yourself.
In the first cell of most spchlab notebooks you find the required code to download and install

> !pip install git+https://github.com/compi1234/pyspch.git


**NOTE**  
- If you need to install a specific version of pyspch, e.g. v.0.8.2, just modify the last part to *\/pyspch.git@0.8.2*
- There is way to avoid reinstalling pyspch with every runtime; i.e. by installing it in your Google Drive.
However, this process is not trivial and has failed in several use cases; so we don't recommend it at this moment.

## Setting up your Google Drive
If you want to save some work for future usage, you can best do this by mounting your Google Drive into Colab
This is done with the following commands.
> import os, sys   
> from google.colab import drive   
> drive.mount('/content/drive')   

Google will ask permission to give the current runtime session read/write access to your drive.  You need to accept this.    
Once agreed you can access and write data in the local folder **/content/drive**.
.
