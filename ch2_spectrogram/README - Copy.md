# CH2: HEARING

## Lecture Notes
- [lecture notes in .html](https://homes.esat.kuleuven.be/~spchlab/H02A6/lectures/ch2_html/index.html)
- [lecture notes in .pdf](https://homes.esat.kuleuven.be/~spchlab/H02A6/lectures/ch2.pdf)

## Jupyter Notebooks

- [Filtered_signals.ipynb] : experiment with low-pass and band-pass filters on speech and artificial signals
- [formants.ipynb] : from spectrogram to formant scatter-plot 


## Exercises

1. **Spectrograms.ipynb** : spectrogram, cepstrogram, .. with flexible parameters and segmental zoom or split screen with spectrogram in LHS and spectral slice in RHS selected by slider.

    + Exercise 1: Phonetic Segmentations
    + Exercise 2: Fourier Spectrogram: parameters
    + Exercise 3: Spectrogram: pitch and formants


2. **Filtered_signals.ipynb** :

    + Speech with Telephone Bandwidth
    + Redundancy in filtered Speech
    + Filtering of Harmonic Signals
    



### Exercise 1: Phonetic Segmentations

- Notebook: Spectrogram.ipynb

1. setting up:
    + load misc/friendly.wav and load also the phonetic segmentation in misc/friendly.phn
    + load set your audio at a comfortable loudness when you play the sentence
2. focus on the first word 'friendly', segment, listen and comment
    + 'f-r-ih-n-d-l-iy'
    + 'ih-n-d-l-iy' 
    + 'f' and 'f-r'
    + what was your most striking observation
    + to what extent do you agree with the given segmentation, based on perception, based on time waveform and based on spectrogram ?

### Exercise 2: Fourier Spectrogram: parameters

- Notebook: Spectrogram.ipynb

1. setting up:
    + load again misc/friendly.was with its phonetic transcript (or some other speech wavfile)
2. adjust different spectrogram settings, always start from defaults (shift=10msec, length=30msec, preemphasis=.97)
    + describe what you observed when deviating from the defaults
    + for what parameters and in what way does the spectrogram deviate from speech perception ?
    + choose as frame_length 10, 30, 50, 100 msec. Which values would you describe as good, acceptable, not acceptible and why ?
    + choose as frame_shift 5,10, 20 msec. Which values would you describe as good, acceptable, not acceptable and why ?


### Exercise 3: Spectrogram: pitch and formants

- Notebook: Spectrogram2.ipynb

1. setting up:
    + load any speech waveform  (suggestions: misc/expansionist.wav, misc/friendly.wav)
    + use default spectrogram parameters
    
2. Find pitch and formants in time and/or frequecy domain
    + put the range cursor in the middle of a vowel
    + find pitch in three ways: time waveform, spectral slice, spectrogram: are your values consistent ?
    + could you determine gender from the obtained pitch values
    + find vowel identity by finding first and second formant and then looking up in formant tables; which is your preferred view ?
    
3. Pitch and formants in the mel spectrum
    + add the mel spectrogram (and mel spectrum slide) to your view
    + find the formants in the mel spectrum both for low resolution (nb=20-30) and high resolution (>80) mel filterbanks
    + in which representation is found formants easiest ?
    + try to map formant frequencies to mel filterbank 


### Exercise 4: Filtered Speech

- Notebook: Filtered_signals.ipynb
- WARNING: be aware that when using Google COLAB, all signals are rescaled to max amplitude = 1.0 ; so total energy / loudness is not representative of the filtering that is going on.

1. Telephone Bandwidth
    + load a speech signal and filter to telephone bandwidth; listen
    
2. Formant filtering
    + design a 'filter' that encompasses the second formant range
    + what frequency range did you use; do you need a priori knowledge about the gender ?
    + listen to the result both in bandpass and bandstop mode ; what does it say about the relevance of F2 ?

3. Mel spectrum
    + check the mel spectrogram view on
    + design a bandpass filter, such that you loose roughly the 10% highest mel band and the 10% lowest mel bands
    + what are your filter design parameters in Hz ?  what does it tell you about the mel scale ?
    

### Exercise 5: Filtering Harmonic Signals

- Notebook: Filtered_signals.ipynb

1. Spectrum view
- use some of the artificial signals 

