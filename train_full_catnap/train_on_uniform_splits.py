from deep_hiv_ab_pred.train_full_catnap.constants import SPLITS_UNIFORM, MODELS_FOLDER
from deep_hiv_ab_pred.training.training import train_network_n_times, eval_network
from deep_hiv_ab_pred.catnap.constants import CATNAP_FLAT
from deep_hiv_ab_pred.preprocessing.pytorch_dataset import AssayDataset, zero_padding
from deep_hiv_ab_pred.preprocessing.seq_and_cdr_to_tensor import parse_catnap_sequences_to_embeddings
from deep_hiv_ab_pred.util.tools import read_json_file
import torch as t
from deep_hiv_ab_pred.training.constants import ACCURACY, MATTHEWS_CORRELATION_COEFFICIENT, AUC
import mlflow
from deep_hiv_ab_pred.global_constants import DEFAULT_CONF, HYPERPARAM_FOLDER
from deep_hiv_ab_pred.train_full_catnap.train_hold_out_one_cluster import test
from deep_hiv_ab_pred.model.FC_GRU import get_FC_GRU_model
import logging
from deep_hiv_ab_pred.training.cv_pruner import CrossValidationPruner
from deep_hiv_ab_pred.util.logging import setup_logging
from deep_hiv_ab_pred.util.plotting import plot_epochs
from os.path import join
from deep_hiv_ab_pred.catnap.download_dataset import download_catnap
from deep_hiv_ab_pred.util.metrics import find_ideal_epoch

def log_metrics(metrics):
    logging.info(f'Acc {metrics[ACCURACY]}')
    logging.info(f'MCC {metrics[MATTHEWS_CORRELATION_COEFFICIENT]}')
    logging.info(f'AUC {metrics[AUC]}')
    mlflow.log_metrics({
        f'acc': metrics[ACCURACY],
        f'mcc': metrics[MATTHEWS_CORRELATION_COEFFICIENT],
        f'auc': metrics[AUC]
    })

def train_on_uniform_splits(splits, catnap, conf, pruner: CrossValidationPruner = None):
    virus_seq, virus_pngs_mask, antibody_light_seq, antibody_heavy_seq = parse_catnap_sequences_to_embeddings(
        conf['KMER_LEN_VIRUS'], conf['KMER_STRIDE_VIRUS']
    )
    train_ids, val_ids = splits['train'], splits['val']
    train_assays = [a for a in catnap if a[0] in train_ids]
    val_assays = [a for a in catnap if a[0] in val_ids]
    train_set = AssayDataset(train_assays, antibody_light_seq, antibody_heavy_seq, virus_seq, virus_pngs_mask)
    val_set = AssayDataset(val_assays, antibody_light_seq, antibody_heavy_seq, virus_seq, virus_pngs_mask)
    loader_train = t.utils.data.DataLoader(train_set, conf['BATCH_SIZE'], shuffle = True, collate_fn = zero_padding, num_workers = 0)
    loader_val = t.utils.data.DataLoader(val_set, conf['BATCH_SIZE'], shuffle = False, collate_fn = zero_padding, num_workers = 0)
    model = get_FC_GRU_model(conf)
    _, test_metrics, last = train_network_n_times(model, conf, loader_train, loader_val, None, conf['EPOCHS'], f'model', MODELS_FOLDER, pruner)
    epoch_index, best_metrics = find_ideal_epoch(test_metrics)
    logging.info(f'Best epoch is {epoch_index + 1}')
    log_metrics(best_metrics)
    return best_metrics

def inspect_performance_per_epocs(hyperparam_file, nb_epochs = 100):
    setup_logging()
    conf = read_json_file(join(HYPERPARAM_FOLDER, hyperparam_file))
    splits = read_json_file(SPLITS_UNIFORM)
    catnap = read_json_file(CATNAP_FLAT)
    virus_seq, virus_pngs_mask, antibody_cdrs = parse_catnap_sequences_to_embeddings(
        conf['KMER_LEN_VIRUS'], conf['KMER_STRIDE_VIRUS']
    )
    test_ids = splits['test']
    train_assays = [a for a in catnap if a[0] not in test_ids]
    test_assays = [a for a in catnap if a[0] in test_ids]
    train_set = AssayDataset(train_assays, antibody_cdrs, virus_seq, virus_pngs_mask)
    test_set = AssayDataset(test_assays, antibody_cdrs, virus_seq, virus_pngs_mask)
    loader_train = t.utils.data.DataLoader(train_set, conf['BATCH_SIZE'], shuffle = True, collate_fn = zero_padding, num_workers = 0)
    loader_test = t.utils.data.DataLoader(test_set, conf['BATCH_SIZE'], shuffle = False, collate_fn = zero_padding, num_workers = 0)
    model = get_FC_GRU_model(conf)
    model_name = 'model_test'
    train_metrics_list, test_metrics_list, last = train_network_n_times(
        model, conf, loader_train, loader_test, None, nb_epochs, model_name, MODELS_FOLDER)
    mccs = [m[MATTHEWS_CORRELATION_COEFFICIENT] for m in test_metrics_list]
    best_mcc = max(mccs)
    ideal_epoch = mccs.index(best_mcc) + 1
    logging.info(f'Best MCC {best_mcc} at epoch {ideal_epoch}')
    plot_epochs(train_metrics_list, test_metrics_list)

def main_train():
    setup_logging()
    # conf = read_yaml(CONF_ICERI_V2)
    conf = read_json_file(DEFAULT_CONF)
    splits = read_json_file(SPLITS_UNIFORM)
    catnap = read_json_file(CATNAP_FLAT)
    metrics = train_on_uniform_splits(splits, catnap, conf)

def main_test():
    setup_logging()
    # conf = read_yaml(CONF_ICERI_V2)
    conf = read_json_file(DEFAULT_CONF)
    splits = read_json_file(SPLITS_UNIFORM)
    catnap = read_json_file(CATNAP_FLAT)
    metrics = test(splits, catnap, conf)

if __name__ == '__main__':
    inspect_performance_per_epocs("hyperparam_fc_att_gru_uniform_one_hot_1_layer_trial_159.json", 100)
    # main_train()
    # main_test()