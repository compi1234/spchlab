# Setup
timit_path = '/users/spraak/spchdata/timit/CDdata/timit/' # to extract corpus, features, labels
write_path = '/users/spraak/spchlab/public_html/data/timit/' # to write corpus, features, labels
read_path = '/users/spraak/spchlab/public_html/data/timit/' # to read corpus, features, labels

data_path = read_path

# corpus
train_corpus_file = data_path + 'conf/timit_train.corpus'
val_corpus_file = None
test_corpus_file = data_path + 'conf/timit_test.corpus'
meta_file = data_path + 'conf/timit.meta'

# pickled data
load_from_pickle = True
train_pickle_file = data_path + 'features/mel80/train.pkl'
test_pickle_file = data_path + 'features/mel80/test.pkl'

# features 
load_from_feature = False
feature_path = data_path + 'features/mel80/'
feature_args = {
    'spg': None,
    'Deltas': None,
    'Norm': 'meanvar',
    'sample_rate': 16000,
    'f_shift': 0.01,
    'f_length': 0.03,
    'preemp': 0.97,
    'window': 'hamm',
    'mode': 'dB',
    'n_mels': 80,
    'n_cep': None
    }

# labels
label_path = data_path + 'segmentation/'
label_args = {
    'extension': '.phn', 
    'pad': 'h#',
    }
labset_in = "timit61"
labset_out = "timit41"

# meta labels
meta_label_args = None

# SpchDataset
sampler_args = {
    'N': 0,
    'stride': 1,
    'mode': 'flatten',
    }

# model 
model_args = {
    'model': 'ffdnn',
    'model_args': {
        'in_dim': 80,
        'out_dim': 41,
        'hidden_layer_dims': [1024, 768, 512],
        'nonlinearity': 'sig',
        'dropout': 0.1
        }
    }
use_cuda_if_available = True

# training
current_epoch = 0
print_every = 1
training_args = {
    'n_epoch': 250,
    'patience': 20,
    'criterion': 'crossentropy',
    'criterion_args': {},
    'optimizer': 'adamw',
    'optimizer_args': {
        'lr': 0.001,
        },
    'scheduler': 'plateau',
    'scheduler_args': {
        'factor': 0.1,
        'patience': 10,
        'threshold': 0.0001
        },
    'clip_args': {},
    'batch_size': 64,
    'shuffle': True,
    'num_workers': 0,
    'val_frac': 0.1,
    'val_seed': 1234,
    }

# evaluate
evaluate_args = {
    'batch_size': 256,
    'shuffle': False,
    'num_workers': 0,
    }

# output
output_path = write_path + "models/default/mel80mv/N0s1/"
output_file = output_path + "out.txt"
train_file = output_path + "train.npz"
evaluate_file = output_path + "evaluate.npz"
train_jsonfile = output_path + "train.json"
evaluate_jsonfile = output_path + "evaluate.json"
setup_jsonfile = output_path + "setup.json"
model_file = output_path + "model.pt"
log_file = output_path + "log.txt"