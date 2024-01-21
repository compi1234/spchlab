# LAB02: SPECTROGRAMS


## Tutorials

1. **Spectrogram**

The notebook ["Tut01_spectrogram.ipynb"] shows how a spectrogram is the result of the sliding window appoach and the computation of short-time Fourier Spectra.
It contains the code to make many of the plots in the course notes on Spectrograms.  The output can be seen [here](https://compi1234.github.io/spchlab/lab02_spectrogram/Tut01_spectrogram.html)

2. **mel_scale**   

This ["Tut02_mel-scale" tutorial](https://compi1234.github.io/spchlab/lab02_spectrogram/Tut02_mel_scale.html)
discusses the design of the mel scale in a number of different variants.
It also shows how to design a mel scaled filterbank that is used to convert a Fourier Spectrogram into a mel spectrogram

3. **mel Spectrogram**

 ["Tut03_mel_spectrogram.ipynb"] how we transform a traditional Fourier spectrogram into a mel spectrogram using mel scaled filterbanks.
 The output can be seen [here](https://compi1234.github.io/spchlab/lab02_spectrogram/Tut03_mel_spectrogram.html)


## Exercises

**Filtered_Signals.ipynb** :
   + Filt.1: Speech with Telephone Bandwidth
   + Filt.2: Redundancy in bandpass-filtered Speech
   + Filt.3: Filtering of Harmonic Signals

Filtering an audio signal, i.e. removing part of the frequency spectrum,  has an immediate impact on audio quality.   At the same time its impact on speech understanding can be small thanks to redundancy in the speech signal.   A classical example is speech passed over a telephone line.   These exercises go into more detail and elaborate on the links between spectrum and perception.

**Spectrogram.ipynb** :
   + Spec.1: Phonetic Segmentations
   + Spec.2: Fourier Spectrogram: parameters

A spectrogram is a time-frequency representation. It sounds generic, but different parameter settings give different tradeoffs and may give a very different 'view'.
Discover for yourself the Heisenberg uncertainty principle of spectral analysis and find those parameters that best aligns
the spectrographic view with perception in general.

Overlaying phonetic segmentations on a speech spectrogram illustrates well that there is a discrepancy between the continuity of
the speech signal and the discreteness of any symbolic (grapheme or phonetic) representation.  Phonetic boundaries
are more often than not fluid instead of abrupt.

**Tut03_mel_spectrogram.ipynb** :
    + MelSpec.1: Mel Spectrogram - Answer the questions at the end of the Tutorial notebook