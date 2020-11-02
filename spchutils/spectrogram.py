import os,sys,io
import scipy.signal
from urllib.request import urlopen
import numpy as np
import pandas as pd
import librosa as librosa
import soundfile as sf

# routine for reading audio from different inputs
def read_audio_from_url(url):
  fp = io.BytesIO(urlopen(url).read())
  data, sr = sf.read(fp,dtype='float32')
  return(data,sr)

# time to index converstions;  inputs can be scalars, lists or numpy arrays  outputs are always numpy arrays
def t2indx(t,sr):
  return (np.array(t).astype(float)*float(sr)+0.5).astype(int)
def indx2t(i,sr):
  return np.array(i).astype(float)/float(sr)

def spectrogram(y,sr=16000,fshift=0.01,flength=0.03,preemp=0.95,n_mels=80,n_fft=512,window='hamm',output='dB'):
    '''
    spectrogram is a wrapper making use of the librosa() library
        for computing spectrograms (regular or fbank) with a single call

    required arguments:
      y       waveform data (numpy array)

    optional arguments:
      sr      sample rate, default=16000
      fshift  frame shift in secs, default=0.010 secs
      flength frame length in secs, default=0.030 secs
      preemp  preemphasis coefficient, default=0.95
      window  window type, default='hamm'
      n_mels  number of mel channels, default=80
      n_fft   number of fft coefficients, default=512
      output  output scale, default='dB', options['dB','power']

    output:
      mel spectrogram
      !! if n_mel==None, the magnitude spectrogram will be returned

    Notes on frame positioning:
      By default we select:
      - center=True          frames are centered at y[t*hop_length]. The number of frames will be ceil(n_samples/hop_length)
      - pad_mode=reflect     data is reflected around the edges
      - initial condition preemphasis: -y[0]
      These settings create a frame sequence that can be logically aligned with a time axis / segmentations at sample level
        and the number of frames is solely dependent on the hop size
      note1: this is similar to Kaldi / Torchaudio with option snip_edges=False
      note2: in SPRAAK centering is at y[(t+0.5) * hop_length ] creating floor(n_samples/hop_length) number of frames

    '''

    b = np.asarray([1.0, -preemp], dtype=y.dtype)
    a = np.asarray([1.0], dtype=y.dtype)
    zi = np.asarray(-y[0:1], dtype=y.dtype)
    y_pre,zf = scipy.signal.lfilter(b, a, y, zi=zi)

    nshift = int(float(sr)*fshift/2.0)*2
    nlength = int(float(sr)*flength)

    spg_stft = librosa.stft(y_pre,n_fft=n_fft,hop_length=nshift,win_length=nlength,window=window,center='True',pad_mode='reflect')
    spg_power = np.abs(spg_stft)**2
    if n_mels == None:
      spg = spg_power
    else:
      spg = librosa.feature.melspectrogram(S=spg_power,n_mels=n_mels,sr=sr)

    if output== 'dB':
        return(librosa.power_to_db(spg))
    else:
        return(spg)