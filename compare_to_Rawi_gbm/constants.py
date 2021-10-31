from os.path import join

COMPARE_RAWI_FOLDER = join('deep_hiv_ab_pred', 'compare_to_Rawi_gbm')
RAWI_DATA = join(COMPARE_RAWI_FOLDER, 'Rawi_data.json')
COMPARE_SPLITS_FOR_RAWI = join(COMPARE_RAWI_FOLDER, 'splits_Rawi_comparison.json')
CATNAP_DATA = join(COMPARE_RAWI_FOLDER, 'catnap_classification.json')
MODELS_FOLDER = join(COMPARE_RAWI_FOLDER, 'models')

HYPERPARAM_FOLDER = join('deep_hiv_ab_pred', 'hyperparameters')
HYPERPARAM_PRETRAIN = join(HYPERPARAM_FOLDER, 'hyperparameters_iceri_2021_v2_30_10_2021.json')
HYPERPARAM_FOLDER_ANTIBODIES = join(HYPERPARAM_FOLDER, 'specific_antibodies', 'ICERI_v2')

# Need to clone https://github.com/RedaRawi/bNAb-ReP.git
SEQ_FOLDER = r'C:\DOC\Workspace\bNAb-ReP\alignments'

KMER_LEN = 'KMER_LEN'
KMER_STRIDE = 'KMER_STRIDE'

CV_FOLDS_TRIM = 10
N_TRIALS = 1000
PRUNE_TREHOLD = .1

# This is 31 because 2 antibodies were removed, they didn't have sequences
ANTIBODIES_LIST = ['10-1074', '2F5', '2G12', '35O22', '3BNC117', '4E10', '8ANC195', 'b12', 'CH01', 'DH270.1', 'DH270.5', 'DH270.6', 'HJ16', 'NIH45-46', 'PG16', 'PG9', 'PGDM1400', 'PGT121', 'PGT128', 'PGT135', 'PGT145', 'PGT151', 'VRC-CH31', 'VRC-PG04', 'VRC01', 'VRC03', 'VRC07', 'VRC26.08', 'VRC26.25', 'VRC34.01', 'VRC38.01']