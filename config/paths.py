from pathlib import Path

# =========================
# Project Root
# =========================
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# =========================
# Top-Level Directories
# =========================
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
SRC_DIR = PROJECT_ROOT / "src"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# =========================
# Data Directories
# =========================
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
SHIFTED_DIR = DATA_DIR / "shifted"
SHIFTED_COV_DIR = SHIFTED_DIR / "covariate"
SHIFTED_LAB_DIR = SHIFTED_DIR / "label"
METADATA_DIR = DATA_DIR / "metadata"

# =========================
# Output Directories
# =========================
PREDICTIONS_DIR = OUTPUTS_DIR / "predictions"
PRED_BASE_DIR = PREDICTIONS_DIR / "baseline"
PRED_COV_DIR = PREDICTIONS_DIR / "covariate"
PRED_LAB_DIR = PREDICTIONS_DIR / "label"

EXPLANATIONS_DIR = OUTPUTS_DIR / "explanations"
EXP_BASE_DIR = EXPLANATIONS_DIR / "baseline"
EXP_COV_DIR = EXPLANATIONS_DIR / "covariate"
EXP_LAB_DIR = EXPLANATIONS_DIR / "label"

METRICS_DIR = OUTPUTS_DIR / "metrics"

FIGURES_DIR = OUTPUTS_DIR / "figures"
FIG_BASE_DIR = FIGURES_DIR / "baseline"
FIG_COV_DIR = FIGURES_DIR / "covariate"
FIG_LAB_DIR = FIGURES_DIR / "label"

# =========================
# Raw Data File
# =========================
RAW_DATA_FILE = RAW_DIR / "cs-training.csv"

# =========================
# Interim Data Files
# =========================
X_TRAIN_TREE_FILE = INTERIM_DIR / "X_train_tree.csv"
X_TEST_TREE_FILE = INTERIM_DIR / "X_test_tree.csv"
X_TRAIN_NN_FILE = INTERIM_DIR / "X_train_nn.csv"
X_TEST_NN_FILE = INTERIM_DIR / "X_test_nn.csv"
X_TRAIN_NN_SCALED_FILE = INTERIM_DIR / "X_train_nn_scaled.csv"
X_TEST_NN_SCALED_FILE = INTERIM_DIR / "X_test_nn_scaled.csv"
Y_TRAIN_FILE = INTERIM_DIR / "y_train.csv"
Y_TEST_FILE = INTERIM_DIR / "y_test.csv"

# =========================
# Shifted Data Files
# =========================
X_TEST_TREE_COV_FILE = SHIFTED_COV_DIR / "X_test_tree_cov.csv"
X_TEST_NN_COV_FILE = SHIFTED_COV_DIR / "X_test_nn_cov.csv"
X_TEST_NN_COV_SCALED_FILE = SHIFTED_COV_DIR / "X_test_nn_cov_scaled.csv"

X_TEST_TREE_LAB_FILE = SHIFTED_LAB_DIR / "X_test_tree_lab.csv"
X_TEST_NN_LAB_FILE = SHIFTED_LAB_DIR / "X_test_nn_lab.csv"
X_TEST_NN_LAB_SCALED_FILE = SHIFTED_LAB_DIR / "X_test_nn_lab_scaled.csv"
Y_TEST_LAB_FILE = SHIFTED_LAB_DIR / "y_test_lab.csv"

# =========================
# Metadata Files
# =========================
RF_SHAP_SAMPLE_IDX_FILE = METADATA_DIR / "shap_sample_indices_rf.json"
MLP_SHAP_SAMPLE_IDX_FILE = METADATA_DIR / "shap_sample_indices_mlp.json"
MLP_LIME_SAMPLE_IDX_FILE = METADATA_DIR / "lime_sample_indices_mlp.json"

RF_STABLE_COV_IDX_FILE = METADATA_DIR / "stable_indices_rf_cov.json"
MLP_STABLE_COV_IDX_FILE = METADATA_DIR / "stable_indices_mlp_cov.json"
RF_STABLE_LAB_IDX_FILE = METADATA_DIR / "stable_indices_rf_lab.json"
MLP_STABLE_LAB_IDX_FILE = METADATA_DIR / "stable_indices_mlp_lab.json"

# =========================
# Model Files
# =========================
RF_MODEL_FILE = MODELS_DIR / "rf_model.joblib"
MLP_MODEL_FILE = MODELS_DIR / "mlp_model.joblib"

# =========================
# Prediction Output Files
# =========================
RF_BASE_PRED_FILE = PRED_BASE_DIR / "rf_predictions.csv"
MLP_BASE_PRED_FILE = PRED_BASE_DIR / "mlp_predictions.csv"

RF_COV_PRED_FILE = PRED_COV_DIR / "rf_predictions_cov.csv"
MLP_COV_PRED_FILE = PRED_COV_DIR / "mlp_predictions_cov.csv"

RF_LAB_PRED_FILE = PRED_LAB_DIR / "rf_predictions_lab.csv"
MLP_LAB_PRED_FILE = PRED_LAB_DIR / "mlp_predictions_lab.csv"

# =========================
# Explanation Output Files
# =========================
RF_SHAP_BASE_FILE = EXP_BASE_DIR / "rf_shap_values.npy"
RF_PERM_BASE_FILE = EXP_BASE_DIR / "rf_perm_importance.csv"
MLP_SHAP_BASE_FILE = EXP_BASE_DIR / "mlp_shap_values.npy"
MLP_LIME_BASE_FILE = EXP_BASE_DIR / "mlp_lime_explanations.json"

RF_SHAP_COV_FILE = EXP_COV_DIR / "rf_shap_values_cov.npy"
RF_PERM_COV_FILE = EXP_COV_DIR / "rf_perm_importance_cov.csv"
MLP_SHAP_COV_FILE = EXP_COV_DIR / "mlp_shap_values_cov.npy"
MLP_LIME_COV_FILE = EXP_COV_DIR / "mlp_lime_explanations_cov.json"

RF_SHAP_LAB_FILE = EXP_LAB_DIR / "rf_shap_values_lab.npy"
RF_PERM_LAB_FILE = EXP_LAB_DIR / "rf_perm_importance_lab.csv"
MLP_SHAP_LAB_FILE = EXP_LAB_DIR / "mlp_shap_values_lab.npy"
MLP_LIME_LAB_FILE = EXP_LAB_DIR / "mlp_lime_explanations_lab.json"

# =========================
# Metrics Output Files
# =========================
BASELINE_METRICS_FILE = METRICS_DIR / "baseline_metrics.csv"
STABILITY_RATIOS_FILE = METRICS_DIR / "stability_ratios.csv"
ESI_COVARIATE_FILE = METRICS_DIR / "esi_covariate.csv"
ESI_LABEL_FILE = METRICS_DIR / "esi_label.csv"
ESI_SUMMARY_FILE = METRICS_DIR / "esi_summary.csv"
CORRELATION_SUMMARY_FILE = METRICS_DIR / "correlation_summary.csv"

# =========================
# Base Figure Output Files
# =========================
CLASS_DISTRIBUTION_FIG = FIG_BASE_DIR / "class_distribution.png"
ROC_CURVES_FIG = FIG_BASE_DIR / "roc_curves.png"
RF_PERM_IMPORTANCE_FIG = FIG_BASE_DIR / "rf_permutation_importance.png"
MLP_SHAP_DISTRIBUTION_FIG = FIG_BASE_DIR / "mlp_shap_distribution.png"

# =========================
# Shift Sanity Check Files
# =========================
COVARIATE_SANITY_FILE = METRICS_DIR / "covariate_shift_sanity.csv"
LABEL_RATIO_SANITY_FILE = METRICS_DIR / "label_shift_ratio_sanity.csv"

# =========================
# Preprocessing Artifact Files
# =========================
NN_SCALER_FILE = MODELS_DIR / "nn_scaler.joblib"
PREPROCESS_ARTIFACTS_FILE = MODELS_DIR / "preprocess_artifacts.joblib"

# =========================
# Covariate Drift Output Files
# =========================
RF_COV_DRIFT_FILE = PRED_COV_DIR / "rf_prediction_drift_cov.csv"
MLP_COV_DRIFT_FILE = PRED_COV_DIR / "mlp_prediction_drift_cov.csv"

# =========================
# Covariate ESI Output Files
# =========================
ESI_RF_SHAP_COV_FILE = METRICS_DIR / "esi_rf_shap_cov.csv"
ESI_RF_PI_COV_FILE = METRICS_DIR / "esi_rf_pi_cov.csv"
ESI_MLP_SHAP_COV_FILE = METRICS_DIR / "esi_mlp_shap_cov.csv"
ESI_MLP_LIME_COV_FILE = METRICS_DIR / "esi_mlp_lime_cov.csv"

ESI_COV_SUMMARY_FILE = METRICS_DIR / "esi_covariate_summary.csv"
CORRELATION_COV_FILE = METRICS_DIR / "correlation_covariate.csv"

# =========================
# Label ESI Output Files
# =========================
ESI_RF_SHAP_LAB_FILE = METRICS_DIR / "esi_rf_shap_lab.csv"
ESI_RF_PI_LAB_FILE = METRICS_DIR / "esi_rf_pi_lab.csv"
ESI_MLP_SHAP_LAB_FILE = METRICS_DIR / "esi_mlp_shap_lab.csv"
ESI_MLP_LIME_LAB_FILE = METRICS_DIR / "esi_mlp_lime_lab.csv"

ESI_LAB_SUMMARY_FILE = METRICS_DIR / "esi_label_summary.csv"
CORRELATION_LAB_FILE = METRICS_DIR / "correlation_label.csv"

def delta_tag(delta: float) -> str:
    """
    Convert a delta value like 0.05 into a filesystem-safe tag like d005.
    """
    return f"d{int(round(delta * 100)):03d}"


# =========================
# Dynamic Path Builders for Multi-Delta Experiments
# =========================
def rf_stable_cov_idx_file(delta: float):
    return METADATA_DIR / f"stable_indices_rf_cov_{delta_tag(delta)}.json"


def mlp_stable_cov_idx_file(delta: float):
    return METADATA_DIR / f"stable_indices_mlp_cov_{delta_tag(delta)}.json"


def rf_stable_lab_idx_file(delta: float):
    return METADATA_DIR / f"stable_indices_rf_lab_{delta_tag(delta)}.json"


def mlp_stable_lab_idx_file(delta: float):
    return METADATA_DIR / f"stable_indices_mlp_lab_{delta_tag(delta)}.json"


def rf_cov_drift_file(delta: float):
    return PRED_COV_DIR / f"rf_prediction_drift_cov_{delta_tag(delta)}.csv"


def mlp_cov_drift_file(delta: float):
    return PRED_COV_DIR / f"mlp_prediction_drift_cov_{delta_tag(delta)}.csv"


def rf_lab_drift_file(delta: float):
    return PRED_LAB_DIR / f"rf_prediction_drift_lab_{delta_tag(delta)}.csv"


def mlp_lab_drift_file(delta: float):
    return PRED_LAB_DIR / f"mlp_prediction_drift_lab_{delta_tag(delta)}.csv"


def esi_rf_shap_cov_file(delta: float):
    return METRICS_DIR / f"esi_rf_shap_cov_{delta_tag(delta)}.csv"


def esi_rf_pi_cov_file(delta: float):
    return METRICS_DIR / f"esi_rf_pi_cov_{delta_tag(delta)}.csv"


def esi_mlp_shap_cov_file(delta: float):
    return METRICS_DIR / f"esi_mlp_shap_cov_{delta_tag(delta)}.csv"


def esi_mlp_lime_cov_file(delta: float):
    return METRICS_DIR / f"esi_mlp_lime_cov_{delta_tag(delta)}.csv"


def esi_rf_shap_lab_file(delta: float):
    return METRICS_DIR / f"esi_rf_shap_lab_{delta_tag(delta)}.csv"


def esi_rf_pi_lab_file(delta: float):
    return METRICS_DIR / f"esi_rf_pi_lab_{delta_tag(delta)}.csv"


def esi_mlp_shap_lab_file(delta: float):
    return METRICS_DIR / f"esi_mlp_shap_lab_{delta_tag(delta)}.csv"


def esi_mlp_lime_lab_file(delta: float):
    return METRICS_DIR / f"esi_mlp_lime_lab_{delta_tag(delta)}.csv"