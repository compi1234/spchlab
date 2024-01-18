# LAB02: SPECTROGRAMS


## Tutorials and Illustrattions

1. **mel_scale**   

This ["mel-scale" tutorial](https://compi1234.github.io/spchlab/lab02_spectrogram/mel_scale.html)
contains the design of the mel scale in a number of different variants.
   It also shows how to design a mel scaled filterbank that is used to convert a Fourier Spectrogram into a mel spectrogram

2. **Spectrogram_examples**

The notebook ["SpectrogramExamples.ipynb"] contains the code to make many of the plots in the course notes on Spectrograms.  The output can be seen [here](https://compi1234.github.io/spchlab/lab02_spectrogram/SpectrogramExamples.html)


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

**Mel_Spectrogram.ipynb** :
   + Mel.1: Mel Spectrogram

These exercises focus on properties of **human** speech and hearing.  
The mel spectrogram is especially adapted to the frequency scale of the human ear.  
Some things look similar, some a little different ...