# LAB02: SPECTROGRAMS


## Tutorials

1. **Spectrogram**
\( [HTML](https://compi1234.github.io/spchlab/HTML/Spectrogram.html) \) 

shows how a spectrogram is the result of the sliding window appoach and the computation of short-time Fourier Spectra.

2. **MelScale**   \(  [HTML](https://compi1234.github.io/spchlab/HTML/MelScale.html) \)  

discusses the design of the mel scale in a number of different variants.
It also shows how to design a mel scaled filterbank that is used to convert a Fourier Spectrogram into a mel spectrogram

3. **MelSpectrogram** \(  [HTML](https://compi1234.github.io/spchlab/HTML/MelSpectrogram.html) \)
   
shows how we transform a traditional Fourier spectrogram into a mel spectrogram using mel scaled filterbanks.

## Exercises

**[FilteredSignals.ipynb](FilteredSignals.ipynb)** :
+ Filt-Ex.1: Speech with Telephone Bandwidth
+ Filt-Ex.2: Redundancy in bandpass-filtered Speech
+ Filt-Ex.3: Filtering of Harmonic Signals

Filtering an audio signal, i.e. removing part of the frequency spectrum,  has an immediate impact on audio quality.   At the same time its impact on speech understanding can be small thanks to redundancy in the speech signal.   A classical example is speech passed over a telephone line.   These exercises go into more detail and elaborate on the links between spectrum and perception.

**[SpectrogramGUI.ipynb](SpectrogramGUI.ipynb)** :
+ Spec-Ex.1: Phonetic Segmentations
+ Spec-Ex.2: Fourier Spectrogram: parameters

A spectrogram is a time-frequency representation. It sounds generic, but different parameter settings give different tradeoffs and may give a very different 'view'.
Discover for yourself the Heisenberg uncertainty principle of spectral analysis and find those parameters that best aligns
the spectrographic view with perception in general.

Overlaying phonetic segmentations on a speech spectrogram illustrates well that there is a discrepancy between the continuity of
the speech signal and the discreteness of any symbolic (grapheme or phonetic) representation.  Phonetic boundaries
are more often than not fluid instead of abrupt.

**[MelSpectrogram.ipynb](MelSpectrogram.ipynb)** :   
 + MelSpec-Ex.1: Mel Spectrogram - Answer the questions at the end of the Tutorial notebook