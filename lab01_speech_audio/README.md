# LAB01: SPEECH and AUDIO  
   
LAB01 touches on the *psychoacoustics* of speech and audio, already thinking ahead in terms of speech recognition.  Questions that we raise, are:   
- How do we hear ?  
- Which physical properties of the signal correlate to what element in our perception ?


## Notebooks 

- **Keyboard.ipynb** :
A very gentle introduction to the concept of pitch (tone on a musical scale)
- **HarmonicSignals.ipynb**:
A GUI for experimenting with perception of harmonic signals.   The goal is to show that frequency content has correlates along 3 very quite perceptual axis: pitch, timbre and rhythm 
- **AuditoryDemonstrations.ipynb**:
This is a wrapper notebook around some of the demos that were published on the "IPO Auditory Demonstration CD".  A small GUI and a spectrographic view are additions provided to the purely auditive demonstrations.


## Exercises
For the exercises and demos you need a properly working audio device.  Using good quality headphones is advised.

Exercises 1-3 show straightforward correspondance between physical properties (**amplitude, frequency**) and perception (**loudness, pitch/tone**).
Showing such relationshsip is easily done for "simple sounds" such as wideband noise signals or pure tones.

Exercises 4-6 deal with *"harmonic"* signals.  In first instance we focus on stationary sounds.
We show in various ways how perception of **pitch** and **timbre**
is largely independent and driven by different group properties of the spectrum.  
In many situations **pitch** depends on the fundamental frequecy while the **timbre** depends on the spectral envelope over the harmonics.

Exercise 7-8 focus on the **transient** nature of everyday speech and audio and how this influences perception with sometimes surprising results.

All exercise details and questions are available inside the notebooks.

### Exercise 1: Loudness

- Notebook: AuditoryDemonstrations.ipynb
- Demo: Demo4
- Reference: IPO Auditory Demonstrations CD (Demo4)


### Exercise 2: Pitch

- Notebook: Keyboard.ipynb

<img src="../figures/88_key_piano.jpg">


### Exercise 3: Frequency Sensitivity of Human Hearing

- Notebook: AuditoryDemonstrations.ipynb
- Demo: Demo6
- Reference: IPO Auditory Demonstrations CD (Demo6)

<img src="../figures/Fletcher_Munson.jpg" alt="Equal Loudness Curves" style="height: 400px">

### Exercise 4: Effect of Spectrum on Timbre

- Notebook: AuditoryDemonstrations.ipynb
- Demo: Demo28
- Reference: IPO Auditory Demonstrations CD (Demo28))

### Exercise 5: Pitch and Timbre of Harmonic Signals

- Notebook: HarmonicSignals.ipynb
- Exercises:
  + Fourier Synthesis of a Square Wave
  + Pitch and Timbre of Harmonic Signals

### Exercise 6: Harmonic Signals: digging deeper

- Notebook: HarmonicSignals.ipynb
- Exercises:
  + Periodicity and Rhythm
  + Influence of Tone Envelope on Timbre


### Exercise 7: Effect of Tone Envelope on Timbre

- Notebook: AuditoryDemonstrations.ipynb
- Demo: Demo29
- Reference: IPO Auditory Demonstrations CD(Demo29)

### Exercise 8: Effect of Echoes

- Notebook: AuditoryDemonstrations.ipynb
- Demo: Demo35
- Reference: IPO Auditory Demonstrations CD (Demo35)
