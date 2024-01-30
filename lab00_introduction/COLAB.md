# Working in GOOGLE COLAB with *spchlab* and *pyspch*

### Running a notebook in Google Colab

To be able to use Google Colab, you need to have a Google account. If you have one, make sure you are logged in.

To run a notebook in COLAB:
  - go to the spchlab repository on Github [https://github.com/compi1234/spchlab]
  - open the desired \<notebook>.ipynb
  - to run in COLAB, do one of the following:
	1. click the <a href="" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab" title="Open in Google Colab" style="vertical-align: middle" ></a> badge at the top of the notebook
    2. click on the <img src="../figures/co_icon_20px.png" style="vertical-align: middle" > "open in colab" browser extension icon  (if you have it installed)
	3. Paste the GitHub exercise URL in a running colab session
  - start running the notebook in colab
  - neglect the Colab Warnings (see below)

You may ignore following specific Colab WARNINGS
1. After you install the pyspch package (which is the first thing you need to do, unless you have it permanently installed), you may get a warning that you need to *restart the runtime*, IGNORE THIS, just CLICK and continue.
2. When you start running a notebook, you may get a warning that the notebook is not authored by Google.  IGNORE THIS (for our notebooks) and CLICK  *Run anyway*.

### Setting up pyspch
**spchlab** uses the **pyspch** package for almost all demos / exercises.
**pyspch** is not pre-installed on Google Colab, so you need to install it yourself.
In the first cell of most spchlab notebooks you find the required code to download and install

> !pip install git+https://github.com/compi1234/pyspch.git   

### Setting up your Google Drive
If you want to save some work for future usage, you can best do this by mounting your Google Drive into Colab
This is done with the following commands.
> import os, sys   
> from google.colab import drive   
> drive.mount('/content/drive')   

Google will ask permission to give the current runtime session read/write access to your drive.  You need to accept this.    
Once agreed you can access and write data in the local folder **/content/drive**.


### Additional Remarks 
These are not relevant for most users, but included for sake of completeness:   
- If you need to install a specific version of pyspch, e.g. v.0.8.2, just modify the last part to *\/pyspch.git@0.8.2*
- There is way to avoid reinstalling pyspch with every runtime; i.e. by installing it in your Google Drive.
However, this process is not trivial and has failed in several use cases; so we don't recommend it at this moment.


.
