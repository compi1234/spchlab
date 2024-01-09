#  SOURCE FILTER MODEL of SPEECH, PITCH and FORMANTS


## Background

The source filter model is a compact and insightfull model of speech production.
It provides a direct link between speech production, articulation and acoustic-phonetics.  
The basis of all this is the uncoupling of the "source" and the "filter" in the model:
- The source is created by release of energy from the lungs.   The air flow may either pass directly or be modulated by the vocal cords.
The vocal cords are thus the source of (short-term) periodicity in the produced speech.
- This source signal is "filtered" in the vocal (and nasal) tract.   The spectrum of the source filter is flat (up to a global tilt), hence the spectrum of the resulting speech is a one-to-one copy of the filter characteristic of the vocal tract which is in its terms the result of the positioning of our articulators (mainly the opening of vocal tract and the position of the tongue). The resonances of the vocal tract filter lead to peaks in the spectral envelope.  These are deemd to be a robust and compact representation of the spectral envelope as they are robust against background noise and many types of filtering and signal distortions.
Hence not surprisingly, formants correlate very well with vowel identity.



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
    + Remark that prototypical formant values are almost positioned on a triangle with corners "iy"-"aa"-"uw"
    + Explain gender dependent effect
    + Multi-dimensional scatter analysis with more features: eg. f0,F1,F2,F3 


