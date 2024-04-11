from typing import Optional, Dict, Any, Callable
from pydantic import Field, BaseModel

from sklearn.pipeline import Pipeline, FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge, LinearRegression
from sklearn import metrics
import scipy.stats as stats

import src.constants as const

from sklearn import set_config

set_config(transform_output="pandas")


DEFAULT_POLY_DEGREE = 2
DEFAULT_PCA_COMPONENTS = 2


LINEAR_REGRESSION_GRID_SEARCH = {
    "linear_regression__fit_intercept": [True, False],
    "linear_regression__positive": [True, False],
}
POLYNOMIAL_GRID_SEARCH = {
    "polynomial__degree": [2, 3, 4],
    "polynomial__interaction_only": [True, False],
    "polynomial__include_bias": [True, False],
}

PCA_GRID_SEARCH = {
    "preprocess_scale_pca__pca__n_components": [2, 3, 4],
    "preprocess_scale_pca__pca__svd_solver": ["auto", "full", "arpack", "randomized"],
    "preprocess_scale_pca__pca__whiten": [True, False],
    "preprocess_scale_pca__pca__copy": [True, False],
    "preprocess_scale_pca__pca__iterated_power": [None, "auto", "arpack", "randomized"],
    "preprocess_scale_pca__pca__tol": [None, 0.0, 0.1, 0.01],
}

RIDGE_REGRESSION_GRID_SEARCH = {
    "ridge__alpha": stats.uniform(loc=0, scale=1),
    "ridge__fit_intercept": [True, False],
    "ridge__positive": [True, False],
    "ridge__positive": [True, False],
    "ridge__solver": ["auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga"],
}


REGRESSION_METRICS = [
    metrics.max_error,
    metrics.mean_absolute_error,
    metrics.mean_squared_error,
    metrics.median_absolute_error,
    metrics.r2_score,
]


class ModelConfig(BaseModel):
    name: str
    estimator: Pipeline
    grid_search_params: Dict[str, Any]
    train_metrics: Dict[str, float | int] = Field(default_factory=dict)
    test_metrics: Dict[str, float | int] = Field(default_factory=dict)
    best_params_by_metric: Dict[str, dict] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True


# create all the model configs
MODEL_CONFIGS = [
    ModelConfig(
        name="basic",
        estimator=Pipeline(
            [
                (
                    "preprocess",
                    ColumnTransformer(
                        [("onehot", OneHotEncoder(sparse_output=False), ["month"])],
                        remainder="passthrough",
                    ),
                ),
                ("linear_regression", LinearRegression()),
            ]
        ),
        grid_search_params={**LINEAR_REGRESSION_GRID_SEARCH},
    ),
    ModelConfig(
        name="poly_linear",
        estimator=Pipeline(
            [
                (
                    "preprocess",
                    ColumnTransformer(
                        [("onehot", OneHotEncoder(sparse_output=False), ["month"])],
                        remainder="passthrough",
                    ),
                ),
                ("polynomial", PolynomialFeatures(degree=DEFAULT_POLY_DEGREE)),
                ("linear_regression", LinearRegression()),
            ]
        ),
        grid_search_params={
    **POLYNOMIAL_GRID_SEARCH,
    **LINEAR_REGRESSION_GRID_SEARCH,
},
    ),
    ModelConfig(
        name="poly_ridge",
        estimator=Pipeline(
            [
                (
                    "preprocess",
                    ColumnTransformer(
                        [("onehot", OneHotEncoder(sparse_output=False), ["month"])],
                        remainder="passthrough",
                    ),
                ),
                ("polynomial", PolynomialFeatures(degree=DEFAULT_POLY_DEGREE)),
                ("ridge", Ridge()),
            ]
        ),
        grid_search_params={
    **POLYNOMIAL_GRID_SEARCH,
    **RIDGE_REGRESSION_GRID_SEARCH,
},
    ),
    ModelConfig(
        name="pca_linear",
        estimator=Pipeline(
            steps=[
                (
                    "preprocess",
                    ColumnTransformer(
                        transformers=[
                            ("onehot", OneHotEncoder(sparse_output=False), ["month"]),
                            (
                                "scale_pca",
                                Pipeline(
                                    [
                                        ("scale", StandardScaler()),
                                        ("pca", PCA(n_components=2)),
                                    ]
                                ),
                                const.GP_LIST_AGE_LABELS,
                            ),
                        ],
                        remainder="passthrough",
                    ),
                ),
                ("linear_regression", LinearRegression()),
            ]
        ),
        grid_search_params={**PCA_GRID_SEARCH, **LINEAR_REGRESSION_GRID_SEARCH},
    ),
    ModelConfig(
        name="pca_ridge",
        estimator=Pipeline(
            steps=[
                (
                    "preprocess",
                    ColumnTransformer(
                        transformers=[
                            ("onehot", OneHotEncoder(sparse_output=False), ["month"]),
                            (
                                "scale_pca",
                                Pipeline(
                                    [
                                        ("scale", StandardScaler()),
                                        ("pca", PCA(n_components=2)),
                                    ]
                                ),
                                const.GP_LIST_AGE_LABELS,
                            ),
                        ],
                        remainder="passthrough",
                    ),
                ),
                ("ridge", Ridge()),
            ]
        ),
        grid_search_params={**PCA_GRID_SEARCH, **RIDGE_REGRESSION_GRID_SEARCH},
    ),
]


def baseline_scorer(y_true, y_pred):
    """
    Calculate the scores for a baseline model.

    Parameters:
    - y_true: The true values of the target variable.
    - y_pred: The predicted values of the target variable.

    Returns:
    - metrics_dict: A dictionary containing the scores for each metric in the REGRESSION_METRICS list.
    """
    metrics_dict = {}
    for metric in REGRESSION_METRICS:
        score = metric(y_true, y_pred)
        metrics_dict[metric.__name__] = score
    return metrics_dict
