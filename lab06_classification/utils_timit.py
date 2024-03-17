# TIMIT Utilities: getting processed data from server, down sampling the database, statistics
import numpy as np
import pandas as pd
import pyspch
#
def load_timit_data(corpus="train",ftrs="mfcc13",alphabet="timit41",
                 root='https://homes.esat.kuleuven.be/~spchlab/data/timit/'):
    '''
    get processed TIMIT data (part of it) from the server
    
    corpus         should be "train" or "test"
                    or supplemented with  "", "_mini", "_dr1" ,"_si1"  for full, mini(10%), single subdirectory dr1, only 1 SI sentence (=10%)
    ftrs:          type of preprocessed features (mfcc13, mel24 or mel80)
    alphabet:      choice of alphabet to use  (TIMIT61 should be convertable to it)
    '''
    
    corpus_file = root + "conf/timit_" + corpus + ".corpus"
    corpus_data = pyspch.read_txt(corpus_file)
    
    # pickled files of features are available for 'master' corpus only
    # subcorpus selection happens later
    master_corpus = corpus.split("_",1)[0]   # 
    pickle_file = root + "features/" + ftrs + "/" + master_corpus + ".pkl"
    ftrs_df = pd.read_pickle(pickle_file)
    data = pyspch.core.DataFrame_to_SpchData(ftrs_df, delete_df=True) 
    data = data.subset(corpus_data) 
    
    # map originial TIMIT 61 transcriptions to the chosen alphabet
    lab2classes = pyspch.timit.get_timit_mapping('timit61'+'_'+alphabet) 
    data.modify_labels(lab2classes) # timit61 -> timit41    
    return(data)

def create_selection_indx(y,labels=None,downsample=1,mincount=1):
    '''
    creates a truth array for making a selection items labeled in y
       by (1) only selecting items with label in labels
       and (2) downsampling though while respecting a given mincount per class
    '''
    
    if labels is None:
        labels = np.unique(y)
    indx = np.full(len(y),False,dtype='bool')
    
    for lbl in labels:
        selection = (y==lbl)
        n = sum(selection)
        #print(n,selection)
        ds = min(downsample, max(1,n//mincount) ) # ds is downsample for lbl
        A = np.where(selection)[0]
        indx[A[::ds]]=True    
    return(indx)

def select_subset(X,y,labels=None,downsample=1,mincount=64):
    '''
    downsample an existing dataset (X,y)
    '''
    indx = create_selection_indx(y,labels=labels,downsample=downsample,mincount=mincount)
    return( X[indx] , y[indx] )

def print_dataset_statistics(y,Details=False,txt="dataset"):
    '''
    print global dataset statistics
    if Details=True, you also get statistics per label
    '''
    labels = np.unique(y)
    print("Statistics for %s:" % txt)
    print("Number of classes",len(labels))
    print("Number of samples",len(y)) 
    samples_per_class = [ sum(y==lbl) for lbl in labels ]
    print("Minimun/Maximum number of samples per class: ",np.min(samples_per_class), ' / ',np.max(samples_per_class))
    if(Details):
        print([ (labels[i],samples_per_class[i]) for i in range(len(labels)) ] )





def _downsample_data_sets_1(X_in,y_in,downsample=1,mincount=64):
    '''
    downsample an existing dataset (X,y)
    '''
    #print(X_in.shape,y_in.shape)
    dim = X_in.shape[1]
    X = np.empty((0,dim),'float64')
    y = np.empty((0,),dtype='<U3')
    labels = np.unique(y_in)
    #print(labels)
    for lbl in labels:
        selection = (y_in==lbl)
        n = sum(selection)
        ds = min(downsample, max(1,n//mincount) )
        #print(lbl,n,ds)
        X = np.vstack((X,X_in[selection][::ds]))
        y = np.concatenate((y,y_in[selection][::ds]))
    return(X,y)

