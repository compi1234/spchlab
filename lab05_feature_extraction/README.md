#  LAB05:  Feature Extraction for Speech Recognition


## Background

Frame based speech analysis extracts features on a frame by frame basis.  Best known example is the spectrogram, which is just a stacking of short time spectra computed over successive frames.   Fourier style spectral analysis is often just a first step and is followed by mel-spectral or cepstral processing.

Apart from spectral analysis, there are also a number of features that may be computed from the signal directly, most notably: energy, pitch and zero-crossing rate.


## Exercises

1. **Time Domain Feature Extraction**

- Notebook: TimeDomainFeatures.ipynb
- Notebook: TrimAudio.ipynb

This exercise focuses on energy and pitch and the influence of window length and shift.  The results are straightforward to interpret when thinking about the role of pitch in the source-filter model. By and large we reach the same conclusions as for spectral analysis. 

In the second task we apply the results to construct an endpointing and trimming tool.  We use frame based energy as feature and combine it with simple heuristics to create a trimming tool that cuts silence at the edges of a recording.


2. **CepstralLiftering**

- Notebook: CepstralLiftering.ipynb


