#  LAB04:  Feature Extraction for Speech Recognition


## Background

Frame based speech analysis extracts features on a frame by frame basis.  Best known example is the spectrogram, which is just a stacking of short time spectra computed over successive frames.   Fourier style spectral analysis is often just a first step and is followed by mel-spectral or cepstral processing.

Apart from spectral analysis, there are also a number of features that may be computed from the signal directly, most notably: energy, pitch and zero-crossing rate.


## Exercises

**Ex.1 Time Domain Feature Extraction** (TimeDomainFeatures.ipynb)


This exercise focuses on energy and pitch and the influence of window length and shift.  The results are straightforward to interpret when thinking about the role of pitch in the source-filter model. By and large we reach the same conclusions as for spectral analysis. 

In the second task we apply the results to construct an endpointing and trimming tool.  We use frame based energy as feature and combine it with simple heuristics to create a trimming tool that cuts silence at the edges of a recording.


**Ex.2 CepstralLiftering** (CepstralLiftering.ipynb)

This exercise demonstrates the magic of cepstral liftering to separate spectral envelope from pitch information in an automatic way.



**Ex.3 MelSpectrogram**

Hereunder we list a number of exercises related to the mel spectrum, that may have been executed before or the can be done as one group at this point.
- lab02/Filt-Ex.2 : Revisit your answers to this exercise (on bandpass and bandstop filtering of speech) from the previous session and remotivate (or adjust) your answers based on the mel frequency concept.
- lab02/Melspec-Ex.1:
    + motivating the mel spectrogram
    + difference between high resolution and critical band mel spectra
- lab03/SpgR-Ex.2: implications of the mel scale for pitch and formant analysis


