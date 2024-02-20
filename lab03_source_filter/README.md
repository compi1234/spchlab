#  SOURCE FILTER MODEL of SPEECH - PITCH and FORMANTS


### Background

The source filter model is a compact and insightfull model of speech production.
It provides a direct link between speech production, articulation and acoustic-phonetics.  
The basis of all this is the uncoupling of the "source" and the "filter" in the model:
- The source is created by release of energy from the lungs.   The air flow may either pass unobstructed or be modulated by the vocal cords.  When unobstructed the source signal is like white noise.  When the vocal cords are vibrating, the resulting signal is a periodic sequence of pulses.
The vocal cords are thus the source of (short-term) periodicity in the produced speech.
- This source signal is "filtered" in the vocal (and nasal) tract.   The spectrum of the source filter is flat (up to a global tilt), hence the spectrum of the resulting speech is a one-to-one mapping of the filter characteristic of the vocal tract which is the result of the positioning of our articulators (mainly the opening of vocal tract and the position of the tongue). The resonances of the vocal tract filter lead to peaks in the spectral envelope.  These are deemed to be a robust and compact representation of the spectral envelope as they are robust against background noise and many types of filtering and signal distortions.
Hence not surprisingly, formants correlate very well with vowel identity.

In this lab we analyze the promises made by the source filter model for speech recognition:   
- is pitch a reliable feature for gender recognition ?
- are formants reliable features for vowel recognition ?

We don't perform the feature extraction as such, but start from available databases.


### Tutorials

1. **[Peterson Barney](https://compi1234.github.io/spchlab/Tutorials/PetersonBarney.html)** 

Here we try to replicate the main results (tables and figures) of the seminal Peterson and Barney 1952 paper.

2. **[Pitch Distribution (Hillenbrand Database)](https://compi1234.github.io/spchlab/Tutorials/PitchDistribution.html)**

provides histograms of average pitch for different classes: male, female, boy, girl and a simple Gaussian fit

3. **[Formant Distribution (Hillenbrand Database)](https://compi1234.github.io/spchlab/Tutorials/FormantDistribution.html)**

provides different views on the distribution of formant values (mainly F1 and F2) as measured in the Hillenbrand database.
This analysis shows well how F1-F2 clusters are well separate for a small number of vowels, but also how much overlap there is when including all vowels.
The overlap between classes is significantly larger than was suggested by the 1952 Peterson Barney data.


### Exercises


1. **[SpectrogramAnalysis.ipynb](SpectrogramAnalysis.ipynb)**

Waveforms, spectrograms and spectral slices are just different views of the same signal.   In this exercise explore the different views and try to read as much information from them.
We see how the different views can lead to consistent estimates of pitch and formants.
See if you can determine gender and/or vowel identity from your extracted values.

+ SgpAna-Ex.1: Extracting pitch and formants in time and or frequency domain
+ SpgAna-Ex.2: Extracting pitch and formants from the mel spectrum


2. **Bayesian Recognition using Pitch and Formants as Features**
3. [FormantDistribution.ipynb](FormantDistribution.ipynb)**

This notebook contains a collection of plots.  Focus on the last couple of plots showing gender dependent distributions of F1-F2 and showing higher dimensional data
in a grid plot including f0 as well

+ FmtDist-Ex.1: Could you have predicted the gender dependent formant distributions from looking at the f0-F1-F2 grid plot ?


