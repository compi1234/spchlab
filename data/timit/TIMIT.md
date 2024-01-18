# TIMIT DATABASE

### GENERAL DESCRIPTION

The TIMIT corpus of read speech is designed to provide speech data for acoustic-phonetic studies and for the development and evaluation of automatic speech recognition systems. TIMIT contains broadband recordings of 630 speakers of eight major dialects of American English, each reading ten phonetically rich sentences. The TIMIT corpus includes time-aligned orthographic, phonetic and word transcriptions as well as a 16-bit, 16kHz speech waveform file for each utterance. Corpus design was a joint effort among the Massachusetts Institute of Technology (MIT), SRI International (SRI) and Texas Instruments, Inc. (TI). The speech was recorded at TI, transcribed at MIT and verified and prepared for CD-ROM production by the National Institute of Standards and Technology (NIST).

The TIMIT corpus transcriptions have been hand verified. Test and training subsets, balanced for phonetic and dialectal coverage, are specified. Tabular computer-searchable information is included as well as written documentation.


### USAGE IN SPCHLAB

#### WHY TIMIT

It is a well known standard database.  It is very small and too artificial according to today's standards.
However due to its compactness and huge number of references, it is still popular for **exploratory** research in acoustic-phonetic recognition.

It is often used for phone recognition as phone labels and timings are provided.  With this information we can provide a label to each feature vector.

TIMIT is used in 2 setups:

- phone classification:  we use the labels provided in the database and split the data in independent train and test set.  This can be used for both frame and segment classification where the label of the center frame is used as ground truth.

- phone recognition: in recognition mode we recognize phone sequences .  Typically this is done using a phone bigram model as extra knowledge source but without lexicons, language models, etc. and as such it can still be seen as a pure acoustic recognizer

#### PHONE SETS

The original TIMIT transcriptions were made with detailed phonetic labels using a 61 symbol set.
This symbol set is rarely used today.  In TIMIT reference experiments on phone classification it is common to train on
a collapsed TIMIT48 symbol set and to recognize on an even more condensed 39 label set.   

In **spchlab** we typically use **TIMIT-41**, i.e. a collapsed set
corresponding to the CMU-39 phoneset + SIL(ence) + CL(closure) . 


#### THE DATA SETS

TIMIT comes with standard train/test set divisions

- training: 462 speakers, 3696 sentences, 3.14 hrs
- core test set: 24 speakers, 192 sentences, 0.16 hrs
- full test set: 168 speakers, 1344 sentences, 0.81 hrs


TIMIT contains for each speaker
- 2 sentences read by EVERY speaker (sa1,sa2)
- 8 sentences that are either speaker specific or only read by a small number of speakers

The 'sa' sentences are interesting for research on speaker variability.
However, they do more harm than good to train or evaluate speech recognition systems as they introduce tremendous bias.
So it is advised to eliminate the 'sa' sentences in speech recognition experiments.


#### Custom subsets

TIMIT is a small dataset by today's standard.
Still, for student exercises we sometimes prefer to use even smaller subsets.

**TIMIT_MINI** is a random sample of about 10% of the speakers in train
and 20% in test.

**TINYTIMIT**  is a selection of 800 samples of 3 vowels each.



