# TIMIT DATABASE

### GENERAL DESCRIPTION

The TIMIT corpus of read speech is designed to provide speech data for acoustic-phonetic studies and for the development and evaluation of automatic speech recognition systems. TIMIT contains broadband recordings of 630 speakers of eight major dialects of American English, each reading ten phonetically rich sentences. The TIMIT corpus includes time-aligned orthographic, phonetic and word transcriptions as well as a 16-bit, 16kHz speech waveform file for each utterance. Corpus design was a joint effort among the Massachusetts Institute of Technology (MIT), SRI International (SRI) and Texas Instruments, Inc. (TI). The speech was recorded at TI, transcribed at MIT and verified and prepared for CD-ROM production by the National Institute of Standards and Technology (NIST).

The TIMIT corpus transcriptions have been hand verified. Test and training subsets, balanced for phonetic and dialectal coverage, are specified. Tabular computer-searchable information is included as well as written documentation.


### USAGE IN THESE EXERCISES

##### WHY TIMIT

It is a well known standard database.  It is very small and too artificial according to today's standards.
However due to its compactness and huge number of references, it is still popular for **exploratory** research in acoustic-phonetic recognition.

It is often used for phone recognition as phone labels and timings are provided.  With this information we can provide a label to each feature vector.

TIMIT is used in 2 setups:

- phone classification:  we use the labels provided in the database and split the data in independent train and test set.  This can be used for both frame and segment classification where the label of the center frame is used as ground truth.

- phone recognition: in recognition mode we recognize phone sequences .  Typically this is done using a phone bigram model as extra knowledge source but without lexicons, language models, etc. and as such it can still be seen as a pure acoustic recognizer

##### PHONE SET

The original TIMIT transcriptions were made with detailed phonetic labels using a 61 symbol set.
This symbol set is rarely used today.  We typically collapse to 48 symbols and often even to 39.
The 39 symbol set is almost equivalent to the CMU alphabet which is the more commonly used in speech recognition today.


##### THE DATA SETS

TIMIT comes with standard train/test set divisions

- training: 462 speakers, 3696 sentences, 3.14 hrs
- core test set: 24 speakers, 192 sentences, 0.16 hrs
- full test set: 168 speakers, 1344 sentences, 0.81 hrs


##### TINYTIMIT

TINYTIMIT is a selection of 800 samples of 3 vowels each.



