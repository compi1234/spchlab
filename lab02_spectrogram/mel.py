import librosa
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# convert frequency in Hz to MEL
def hz2mel(f,scale='slaney',melfac=None):
    scale=scale.upper()
    if scale == 'OS':
        return(  11.27*np.log(1+f/700) )
    elif scale == 'FANT':
        return(2595 * np.log10(f/700.))
    elif scale == 'HTK':
        if melfac is None: melfac = 100.0
        return( librosa.hz_to_mel(f,htk=True)/melfac )
    elif scale == 'SLANEY':
        if melfac is None: melfac = 1.5
        return( librosa.hz_to_mel(f,htk=False)/melfac )
    elif scale == 'DM':
        m = np.array(f)
        for i in range(len(f)):
             m[i] = f[i]/100. if (f[i] <= 1000.) else  10. + 5.*np.log2(f[i]/1000.)
        return(m)
    
# convert MEL to frequency in Hz
def mel2hz(mel,scale='slaney',melfac=None):
    scale=scale.upper()                                                               
    if scale == 'OS':
        return( 700. * (np.exp(mel/11.27) - 1.))
    elif scale == 'FANT':
        return( 700.*np.exp(mel/2595) )
    elif scale == 'HTK':
        if melfac is None: melfac = 100
        return( librosa.mel_to_hz(melfac*mel ,htk=True) ) 
    elif scale == 'SLANEY':
        if melfac is None: melfac = 1.5
        return( librosa.mel_to_hz(melfac*mel ,htk=False) )  
    elif scale == 'DM':
        f = np.array(mel)
        for i in range(len(mel)):
             f[i] = mel[i]*100. if (mel[i] <= 10.) else  1000.*np.power(2.,(mel[i]-10.)/5.)
        return(f)

# find channel of a freq 'f' in fb specification freqs
# where freqs contains [ low_cutoff, ... all center frequencies ... , high_cutoff ]
# channels run from 1 to len(freqs)-1
def f2ch(f,freqs):
    ch = (np.abs(freqs - f)).argmin()
    return(ch+1)
# the linear approximations f->(pseudo)channel and (pseudo)channel->f
def f2xch(f,ch0=1,f0=100,dfdc=100):
    ch = ch0 + (f-f0)/dfdc
    return(ch)
def xch2f(ch,f0=100,ch0=1,dfdc=100):
    f = f0 + (dfdc)*(ch-ch0)
    return(f)

                                    
def mel_defaults(sr=8000):
    '''
    Returns full set of spectrogram + mel filterbank parameters in function of sampling frequency:
    (n_fft,fmin,fmax)
    
    - n_fft is 256 pts up to 10kHz sampling ratte, 256 point above that
    - fmin = 50Hz
    - fmax = 6500Hz or 0.5*sr for lower sampling rates

    Any of the defaults can be overwritten separately by passing it to this function
    '''
    n_fft = 256 if (sr <= 10000) else 512
    fmin = 50.
    fmax = 6500.0 if sr > 13000 else 0.5*sr
    return(n_fft,fmin,fmax)
         

def mel_frequencies(n_mels=24,sr=8000,n_fft=None,fmin=None,fmax=None,htk=False):
    '''
    wrapper around librosa.mel_frequencies, with added functionality the pyspch defaults
    '''
    # set default parameters if not specified
    (n_fft_0,fmin_0,fmax_0) = mel_defaults(sr=sr)
    n_fft = n_fft if n_fft else n_fft_0
    fmin = fmin if fmin else fmin_0
    fmax = fmax if fmax else fmax_0
    
    # compute edge and center frequencies of the mel filterbank with 50% overlap
    # freqs contains [ low_cutoff, ... all center frequencies ... , high_cutoff ]
    freqs = librosa.mel_frequencies(n_mels=n_mels+2,fmin=fmin,fmax=fmax,htk=htk)
    return(freqs)
    
def mel_filterbank(n_mels=24,sr=8000,n_fft=None,fmin=None,fmax=None,htk=False,norm=None):
    # compute edge and center frequencies of the mel filterbank with 50% overlap
    # freqs contains [ low_cutoff, ... all center frequencies ... , high_cutoff ]
    (n_fft_0,fmin_0,fmax_0) = mel_defaults(sr=sr)
    n_fft = n_fft if n_fft else n_fft_0
    freqs = mel_frequencies(n_mels=n_mels,fmin=fmin,fmax=fmax,htk=htk)
    # compute filterbank interpolation matrix
    fbank=librosa.filters.mel(sr=sr,n_fft=n_fft,fmin=fmin,fmax=fmax,n_mels=n_mels,htk=htk,norm=norm)
    return(freqs,fbank)

# convert mel channel index to Hz for center frequency
# this overrides librosa.mel_frequencies with our own defaults
def melch2hz(ch,n_mels=24,sr=8000,n_fft=None,fmin=None,fmax=None,htk=False,norm=None):
    freqs = mel_frequencies(n_mels=n_mels+2,fmin=fmin,fmax=fmax,htk=htk)
    return(freqs[ch])

# plot the design center frequencies and bandwidth of mel filterbank
def plot_filterbank_cf_bw(freqs,sr,colormap='hsv',Labels=True):
    mels = hz2mel(freqs)
    nb = len(freqs)-2
    cf = range(1,nb+1)
    low = range(0,nb)
    high = range(2,nb+2)

    fig,ax = plt.subplots()
    colors = (mpl.colormaps[colormap]( np.linspace(0, 1, nb)))
    ax.scatter(freqs[cf],np.arange(0,nb),marker='^',s=30,color=colors)
    for i in range(nb):
        plt.plot([freqs[low][i],freqs[high][i]],[i,i],color=colors[i],linewidth=1)
    ax.grid('on')
    ax.set_xlim([0.,sr/2])
    ylim = [-1,nb+1]
    ax.set_ylim(ylim)
    if Labels:
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel("CHANNEL [0:%d]" %(nb-1) )
        ax.set_title("MEL FILTERBANK (center frequencies and bandwidths)\n %d channels, fmin=%.1fHz, fmax=%.1fHz" % (nb,freqs[0],freqs[-1]) )
    ax2 = ax.twinx()
    # define y2_ticks explicitly as y_ticks on original axis may have out of domain (negative) values
    y2_ticks = np.arange(0,nb,5*(1+nb//40))
    y2_ticklabels = ['{:.0f}'.format(freqs[cf][i]).rjust(8) for i in y2_ticks] 
    
    # (matplotlib programming note) 
    # you need to do the following lines in STRICT order to avoid warnings and/or plotting mistakes
    # 1. set the y_ticks, 2. set the y_ticklables, 3. set the y_lim identical to axis1
    ax2.set_yticks(y2_ticks)
    ax2.set_yticklabels(y2_ticklabels)
    ax2.set_ylim(ylim)
    if Labels:
        ax2.set_ylabel( 'Hz' );

def plot_filterbank(freqs,sr,colormap='hsv',ax=None,Labels=True):
    nb = len(freqs)-2
    low = freqs[0:nb]
    cf = freqs[1:nb+1]
    high = freqs[2:nb+2]

    if ax is None:    fig,ax = plt.subplots()
    colors = (mpl.colormaps[colormap]( np.linspace(0, 1, nb)))
    for i in range(nb):
        ax.plot([low[i],cf[i]],[0,1], color=colors[i])
        ax.plot([high[i],cf[i]],[0,1], color=colors[i])
    ax.grid('on')
    ax.set_xlim([0.,sr/2])
    ax.set_ylim([0,1.1])
    if Labels:
        ax.set_xlabel('Frequency (Hz)')
        ax.set_title("MEL TRIANGULAR FILTERBANK\n %d channels, fmin=%.1fHz, fmax=%.1fHz" % (nb,freqs[0],freqs[-1]) )

def plot_filterbank_weights(fbank,sr,n_fft=None,colormap='hsv',Labels=True,ax=None):
    if n_fft is None: n_fft = 256 if (sr < 10000) else 512
    nb,_ = fbank.shape

    colors = (mpl.colormaps[colormap]( np.linspace(0, 1, nb)))
    xrange = np.linspace(0.,sr/2,int(n_fft/2 + 1))
    #print(xrange)
    if ax is None:    fig,ax = plt.subplots()
    for i in range(nb):
        ax.plot(xrange,fbank[i],color=colors[i],marker='+',linestyle='dashed')
    ax.grid()
    ax.set_xlim(0.,sr/2)
    ax.set_ylim(0,1.1)
    if Labels:
        ax.set_xlabel('Frequency (Hz)')
        ax.set_title("MEL FILTERBANK INTERPOLTATION WEIGHTS (%d channels)" % (nb)   )

# this type of plot highlight the preservation of low frequencies and warping (compression) at high frequencies
def plot_filterbank_mapping(freqs,sr):
    # define a linear approximation of freq to channel 
    # which is an extrapolation of the approximate "linear range" of the mel mapping
    # we take as linear range [center_frequency[1], 1kHz]
    n_mels = len(freqs)-2
    ch1 = f2ch(1000.,freqs)
    ch0 = 1
    f1 = freqs[ch1]
    f0 = freqs[ch0]
    dfdc = (f1-f0)/(ch1-ch0)

    fig,ax = plt.subplots(2,1,figsize=(10,5),constrained_layout = True)
    plot_filterbank(freqs,sr=sr,ax=ax[0],Labels=False)
    for i in range( n_mels):
        ch = i+1
        ax[1].plot([f2xch(freqs[ch],f0=f0,ch0=ch0,dfdc=dfdc),ch],[1,0],linestyle='dashed',color='b') 
    
    xticks = np.arange(0,n_mels, 5*(1+n_mels//40))
    xticks[0] = 1
    xticks[-1] = n_mels
    freq_xticks = [freqs[x] for x in xticks]
    labels = ['{:.0f}'.format(freqs[x]).rjust(6) for x in xticks]
    
    ax[0].set_xlabel("center frequency of mel band")
    ax[0].tick_params(axis='x',labeltop=True)
    ax[0].tick_params(axis='x',labelbottom=False)
    ax[0].xaxis.set_label_position('top') 
    ax[0].set_xticks(freq_xticks,labels=labels)
    ax[1].set_xlim([f2xch(0,f0=f0,ch0=ch0,dfdc=dfdc),f2xch(sr/2,f0=f0,ch0=ch0,dfdc=dfdc)])
    ax[1].set_xticks(xticks)
    ax[1].set_xlabel("mel band")
    ax[0].set_title("MEL FILTERBANK MAPPING TO MEL INDEX")