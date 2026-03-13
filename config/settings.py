# =========================
# Reproducibility
# =========================
RANDOM_STATE = 42

# =========================
# Data Split
# =========================
TEST_SIZE = 0.20

# =========================
# Preprocessing
# =========================
IMPUTATION_STRATEGY = "median"
WINSOR_LOWER = 0.01
WINSOR_UPPER = 0.99

# =========================
# Model Parameters
# =========================
RF_PARAMS = {
    "n_estimators": 300,
    "max_depth": None,
    "min_samples_split": 2,
    "min_samples_leaf": 1,
    "class_weight": "balanced",
    "random_state": RANDOM_STATE,
    "n_jobs": -1,
}

MLP_PARAMS = {
    "hidden_layer_sizes": (128, 64),
    "activation": "relu",
    "solver": "adam",
    "alpha": 1e-4,
    "batch_size": 256,
    "learning_rate": "adaptive",
    "max_iter": 300,
    "early_stopping": True,
    "validation_fraction": 0.1,
    "random_state": RANDOM_STATE,
}

# =========================
# Explanation Settings
# =========================
RF_SHAP_SAMPLE_SIZE = 200
MLP_SHAP_SAMPLE_SIZE = 100
MLP_LIME_SAMPLE_SIZE = 100
LIME_NUM_FEATURES = 10
PERMUTATION_N_REPEATS = 10

# =========================
# Stability / ESI
# =========================
DELTA_VALUES = [0.01, 0.03, 0.05, 0.10]
DEFAULT_DELTA = 0.05
TOP_K = 5
ESI_WEIGHTS = (1 / 3, 1 / 3, 1 / 3)

# =========================
# Covariate Shift
# =========================
COVARIATE_SHIFT_FEATURES = [
    "RevolvingUtilizationOfUnsecuredLines",
    "DebtRatio",
    "MonthlyIncome",
]

COVARIATE_SHIFT_PARAMS = {
    "RevolvingUtilizationOfUnsecuredLines": {"scale": 1.20, "noise_std": 0.02},
    "DebtRatio": {"scale": 1.15, "noise_std": 0.05},
    "MonthlyIncome": {"scale": 0.90, "noise_std": 1000.0},
}

# =========================
# Label Shift
# =========================
LABEL_SHIFT_TARGET_POS_RATIO = 0.15