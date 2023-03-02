#  JUPYTER NOTEBOOKS on SOURCE FILTER MODEL of SPEECH, PITCH and FORMANTS


## Background

The source filter model of speech gives us great conceptual insight in the link between speech production and important psychoacoustic
properties of speech.
- The vocal cords are the source of periodicity in speech production.  This is reflected in the periodicity in speech and ultimately the pitch percept.
- The resonances of the vocal tract filter lead to peaks in the spectral envelope.  These are the most robust features of the spectral envelope as they are robust against background noise and many types of filtering and signal distortions.   Formants correlate very well with vowel identity.



## Exercises

In these exercises we explore formants and pitch in a number of different ways: 
(i) how to derive them from the signal or the spectrogram
(ii) distribution of pitch relating to gender
(iii) distribution of formants relating to vowel ID

For parts (ii) and (iii) we make use of the Hillenbrand database, i.e. a database with human annotations of pitch and formants,
i.e. people who had analysis tools as in (i) to their disposition.

1. **PitchFormant_Analysis.ipynb**

    + Exercise 1: find pitch and formants from a prerecorded sample

2. **Pitch_Statistics.ipynb**

    + Make histogram of pitch values and compare distributions wrt gender


3. **Formant_Statistics.ipynb**

    + Make scatterplots of F1-F2 formant values
    + Do this for increasing number of vowels and see confusion growing
    + Remark that prototypical formant values are almost positioned on a triangle with corners "i"-"a"-"u"
    + Explain gender dependent effect
    + Multi-dimensional scatter analysis with more features: eg. f0,F1,F2,F3 


