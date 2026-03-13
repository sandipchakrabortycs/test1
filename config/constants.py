# =========================
# Dataset Columns
# =========================
TARGET_COL = "SeriousDlqin2yrs"
DROP_COLUMNS = []

# =========================
# Model Names
# =========================
MODEL_RF = "RF"
MODEL_MLP = "MLP"

# =========================
# Explainer Names
# =========================
EXPLAINER_SHAP = "SHAP"
EXPLAINER_PERMUTATION = "PERMUTATION_IMPORTANCE"
EXPLAINER_LIME = "LIME"

# =========================
# Fixed Model–Explainer Pairs
# =========================
PAIR_RF_SHAP = "RF_SHAP"
PAIR_RF_PI = "RF_PI"
PAIR_MLP_SHAP = "MLP_SHAP"
PAIR_MLP_LIME = "MLP_LIME"

MODEL_EXPLAINER_PAIRS = [
    (MODEL_RF, EXPLAINER_SHAP, PAIR_RF_SHAP),
    (MODEL_RF, EXPLAINER_PERMUTATION, PAIR_RF_PI),
    (MODEL_MLP, EXPLAINER_SHAP, PAIR_MLP_SHAP),
    (MODEL_MLP, EXPLAINER_LIME, PAIR_MLP_LIME),
]

LOCAL_PAIRS = [
    PAIR_RF_SHAP,
    PAIR_MLP_SHAP,
    PAIR_MLP_LIME,
]

GLOBAL_PAIRS = [
    PAIR_RF_PI,
]

# =========================
# Shift Names
# =========================
SHIFT_COVARIATE = "covariate"
SHIFT_LABEL = "label"
SHIFT_TYPES = [SHIFT_COVARIATE, SHIFT_LABEL]

# =========================
# Class Labels
# =========================
NEGATIVE_CLASS = 0
POSITIVE_CLASS = 1

NEGATIVE_CLASS_NAME = "No Default"
POSITIVE_CLASS_NAME = "Default"

CLASS_NAMES = [NEGATIVE_CLASS_NAME, POSITIVE_CLASS_NAME]

# =========================
# Metric Column Names
# =========================
COL_INDEX = "index"
COL_Y_TRUE = "y_true"
COL_Y_PROB = "y_prob"
COL_Y_PRED = "y_pred"

COL_SHIFT_TYPE = "shift_type"
COL_PAIR = "pair"
COL_MODEL = "model"
COL_EXPLAINER = "explainer"
COL_MEAN_ESI = "mean_esi"
COL_STD_ESI = "std_esi"
COL_STABLE_RATIO = "stable_ratio"
COL_DRIFT_ESI_SPEARMAN = "drift_esi_spearman"