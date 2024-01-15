# LAB02: SPECTROGRAMS


## Tutorials

1. **mel_scale**
   [This notebook](melscale.html) contains the design of the mel scale in a number of different variants.
   It also shows how to design a mel scaled filterbank that is used to convert a Fourier Spectrogram into a mel spectrogram
   
## Exercises

**1. Filtered_signals.ipynb** :
   + Exercise 1: Speech with Telephone Bandwidth
   + Exercise 2: Redundancy in bandpass-filtered Speech
   + Exercise 3: Filtering of Harmonic Signals

Frequency filtering, partially or completely, has a clear impact on audio quality.   At the same time its impact on speech understanding is often small thanks to redundancy in the speech signal.   A classical example is speech passed over a telephone line.  The other examples elaborate on other situations.

2. **Spectrogram.ipynb** :
   + Exercise 1: Phonetic Segmentations
   + Exercise 2: Fourier Spectrogram: parameters

A spectrogram is a time-frequency representation. It sounds generic, but different parameter settings give different tradeoffs and may give a very different 'view'.
Discover for yourself the Heisenberg uncertainty principle of spectral analysis and find those parameters that best aligns
the spectrographic view with perception in general.

Overlaying phonetic segmentations on a speech spectrogram illustrates well that there is a discrepancy between the continuity of
the speech signal and the discreteness of any symbolic (grapheme or phonetic) representation.  Phonetic boundaries
are more often than not fluid instead of abrupt.



3. **Mel_Spectrogram.ipynb** :
   + Exercise 1: Mel Spectrogram

These exercises focus on properties of **human** speech and hearing.  
The mel spectrogram is especially adapted to the frequency scale of the human ear.  
Some things look similar, some a little different ...