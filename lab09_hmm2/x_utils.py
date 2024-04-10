# Auxiliary functions for testing recognizers and showing results
import pyspch
import seaborn as sns
import pandas as pd
import numpy as np

def plot_probs( probs, labels,  fig, iax=2, x0=0.,dx = .01, title="", yrange=[0.,1.],cmap="Greys", style="line",**kwargs):
    '''
    Utility to add selected phone predictors/posteriors ...  to an axis in line or img view 
    '''
    ax = fig.axes[iax]
    
    ## 
    if style =="img":
        sns.heatmap(probs.T, ax=ax, yticklabels=labels, cmap=cmap,linewidths=1,linecolor='k',cbar_kws={'pad':0.01},**kwargs)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
        ax.set_xticks([])
    elif style == "line":
        fig.add_line_plot(probs.T, iax=iax, x0=x0, dx=dx, yrange = yrange ,**kwargs)
        fig.axes[iax].legend(labels, loc='center right')  
    ax.set_title(title)


# Helper routines for loading test samples
def get_test_file(file_id, feature_args=None,
                          root='https://homes.esat.kuleuven.be/~spchlab/data/',type=None):
    '''
    extracts waveform and metadata for a named file
    
    PARAMETERS:
    -----------
    file_id         either number (0..5) or a filename in the TIMIT directory
    feature_args    signal processing specifications
    root            root directory (default is ./data/  on spchlab public html)
    type            "TIMIT" or None
    
    RETURNS:
    --------
    wavdata  wav data
    sr     sample_rate
    spg    spectrogram
    ftrs   feature extraction according to feature_args
    txt    utterance transcription
    wrd    wrd segmentation
    phn    phn segmentation
    '''
    timit_test_files =  ['dr1/faks0/si2203',  'dr8/fcmh1/si1493', 'dr4/fadg0/si1279', 
                         'dr1/mdab0/sx409', 'dr4/mbns0/si1220',
                         'dr1/fcjf0/sx307', 'dr1/fdaw0/sx236', 'dr1/faks0/sx313'] 
    if file_id in [0,1,2,3,4,5,6,7]:
        name = "test/"+timit_test_files[file_id]
    else:
        name = file_id
        
    if type == "TIMIT":
        dt = 1/16000
        xlat = 'timit61_timit41'
        audio_root = root+'timit/audio/'
        seg_root = root+'timit/segmentation/'
    else:
        dt = 1
        xlat = None
        audio_root = root
        seg_root = root
        
    # get audio
    if 'sample_rate' in feature_args.keys():
        sr = feature_args['sample_rate']
    else:
        sr = None
    wavdata, sr = pyspch.audio.load(audio_root + name + ".wav",sample_rate=sr)
    # get segmentations
    wrd = pyspch.timit.read_seg_file(seg_root + name + ".wrd",dt=dt)   
    phn = pyspch.timit.read_seg_file(seg_root + name + ".phn",dt=dt,xlat=xlat)
    if phn is None: # try grapheme if no phn is available
            phn = pyspch.timit.read_seg_file(seg_root + name + ".gra",dt=dt)
        
    spg = pyspch.sp.feature_extraction(wavdata, sample_rate=sr)
    ftrs = pyspch.sp.feature_extraction(wavdata, **feature_args)
    txt = ' '.join(wrd['seg'])
    
    return(wavdata,sr,spg,ftrs,txt,wrd,phn)