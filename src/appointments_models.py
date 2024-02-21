from typing import Optional, Dict, Any
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


DEFAULT_POLY_DEGREE = 2
DEFAULT_PCA_COMPONENTS = 2


LINEAR_REGRESSION_GRID_SEARCH = {
    "linear_regression__fit_intercept": [True, False],
    "linear_regression__normalize": [True, False],
}
POLYNOMIAL_GRID_SEARCH = {
    "polynomial__degree": [2, 3, 4],
    "polynomial__interaction_only": [True, False],
    "polynomial__include_bias": [True, False],
}

PCA_GRID_SEARCH = {
    "preprocess_demo__pca__n_components": [2, 3, 4],
    "preprocess_demo__pca__svd_solver": ["auto", "full", "arpack", "randomized"],
    "preprocess_demo__pca__whiten": [True, False],
    "preprocess_demo__pca__copy": [True, False],
    "preprocess_demo__pca__iterated_power": [None, "auto", "arpack", "randomized"],
    "preprocess_demo__pca__tol": [None, 0.0, 0.1, 0.01],
}

RIDGE_REGRESSION_GRID_SEARCH = {
    "ridge__alpha": stats.uniform(loc=0, scale=1),
    "ridge__fit_intercept": [True, False],
    "ridge__normalize": [True, False],
}


BASIC_ONEHOT_GRID_SEARCH = {**LINEAR_REGRESSION_GRID_SEARCH}

ONEHOT_POLYNOMIAL_LINEAR_GRID_SEARCH = {
    **POLYNOMIAL_GRID_SEARCH,
    **LINEAR_REGRESSION_GRID_SEARCH,
}

ONEHOT_POLYNOMIAL_RIDGE_GRID_SEARCH = {
    **POLYNOMIAL_GRID_SEARCH,
    **RIDGE_REGRESSION_GRID_SEARCH,
}

ONEHOT_PCA_LINEAR_GRID_SEARCH = {**PCA_GRID_SEARCH, **LINEAR_REGRESSION_GRID_SEARCH}

ONEHOT_PCA_RIDGE_GRID_SEARCH = {**PCA_GRID_SEARCH, **RIDGE_REGRESSION_GRID_SEARCH}

REGRESSION_METRICS = [
    "explained_variance",
    "max_error",
    "neg_mean_absolute_error",
    "neg_mean_squared_error",
    "neg_root_mean_squared_error",
    "neg_mean_squared_log_error",
    "neg_root_mean_squared_log_error",
    "neg_median_absolute_error",
    "r2",
]



class ModelConfig(BaseModel):
    name: str
    estimator: Pipeline
    grid_search_params: Dict[str, Any]
    metrics: Dict[str, float | int] = Field(default_factory=dict)
    best_params_by_metric: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True


def basic_onehot_pipeline(pipeline_kwargs: Optional[dict] = None) -> Pipeline:
    """
    Creates a basic pipeline for one-hot encoding categorical features and performing linear regression.

    Args:
        pipeline_kwargs (Optional[dict]): Optional keyword arguments to set pipeline parameters.

    Returns:
        Pipeline: The constructed pipeline object.
    """
    # Define the pipeline
    onehot_pipeline = Pipeline(
        [
            ("preprocess", ColumnTransformer([("onehot", OneHotEncoder(), ["month"])])),
            ("linear_regression", LinearRegression()),
        ]
    )
    if pipeline_kwargs:
        onehot_pipeline.set_params(**pipeline_kwargs)
    return onehot_pipeline


def onehot_polynomial_linear_pipeline(
    pipeline_kwargs: Optional[dict] = None,
) -> Pipeline:
    """
    Creates a pipeline for one-hot encoding, polynomial feature transformation, and linear regression.

    Args:
        pipeline_kwargs (Optional[dict]): Optional keyword arguments to set pipeline parameters.

    Returns:
        Pipeline: The constructed pipeline.

    """
    # Define the pipeline
    poly_pipeline = Pipeline(
        [
            ("preprocess", ColumnTransformer([("onehot", OneHotEncoder(), ["month"])])),
            ("polynomial", PolynomialFeatures(degree=DEFAULT_POLY_DEGREE)),
            ("linear_regression", LinearRegression()),
        ]
    )
    if pipeline_kwargs:
        poly_pipeline.set_params(**pipeline_kwargs)
    return poly_pipeline


def onehot_polynomial_ridge_pipeline(
    pipeline_kwargs: Optional[dict] = None,
) -> Pipeline:
    """
    Creates a pipeline for one-hot encoding, polynomial feature transformation, and ridge regression.

    Args:
        pipeline_kwargs (Optional[dict]): Optional keyword arguments to set pipeline parameters.

    Returns:
        Pipeline: The constructed pipeline.
    """
    # Define the pipeline
    poly_pipeline = Pipeline(
        [
            ("preprocess", ColumnTransformer([("onehot", OneHotEncoder(), ["month"])])),
            ("polynomial", PolynomialFeatures(degree=DEFAULT_POLY_DEGREE)),
            ("ridge", Ridge()),
        ]
    )
    if pipeline_kwargs:
        poly_pipeline.set_params(**pipeline_kwargs)
    return poly_pipeline


def onehot_pca_linear_pipeline(pipeline_kwargs: Optional[dict] = None) -> Pipeline:
    """
    Creates a pipeline for one-hot encoding, PCA dimensionality reduction, and linear regression.

    Args:
        pipeline_kwargs (Optional[dict]): Optional keyword arguments to set pipeline parameters.

    Returns:
        Pipeline: The constructed pipeline.

    """
    # Define the pipeline
    pca_pipeline = Pipeline(
        [
            (
                "preprocess_month",
                ColumnTransformer([("onehot", OneHotEncoder(), ["month"])]),
            ),
            (
                "preprocess_demo",
                ColumnTransformer(
                    [
                        ("scale", StandardScaler(), const.GP_LIST_LABELS),
                        ("pca", PCA(n_components=2), const.GP_LIST_LABELS),
                    ]
                ),
            ),
            ("linear_regression", LinearRegression()),
        ]
    )
    if pipeline_kwargs:
        pca_pipeline.set_params(**pipeline_kwargs)
    return pca_pipeline


def onehot_pca_ridge_pipeline(pipeline_kwargs: Optional[dict] = None) -> Pipeline:
    """
    Creates a pipeline for one-hot encoding, PCA dimensionality reduction, and linear regression.

    Args:
        pipeline_kwargs (Optional[dict]): Optional keyword arguments to set pipeline parameters.

    Returns:
        Pipeline: The constructed pipeline.

    """
    # Define the pipeline
    pca_pipeline = Pipeline(
        [
            (
                "preprocess_month",
                ColumnTransformer([("onehot", OneHotEncoder(), ["month"])]),
            ),
            (
                "preprocess_demo",
                ColumnTransformer(
                    [
                        ("scale", StandardScaler(), const.GP_LIST_LABELS),
                        ("pca", PCA(n_components=2), const.GP_LIST_LABELS),
                    ]
                ),
            ),
            ("ridge", Ridge()),
        ]
    )
    if pipeline_kwargs:
        pca_pipeline.set_params(**pipeline_kwargs)
    return pca_pipeline


# create all the model configs
MODEL_CONFIGS = [
    ModelConfig(name="basic", estimator=basic_onehot_pipeline(), grid_search_params=BASIC_ONEHOT_GRID_SEARCH),
    ModelConfig(name="poly_linear", estimator=onehot_polynomial_linear_pipeline(), grid_search_params=POLYNOMIAL_GRID_SEARCH),
    ModelConfig(name="poly_ridge", estimator=onehot_polynomial_ridge_pipeline(), grid_search_params=ONEHOT_POLYNOMIAL_RIDGE_GRID_SEARCH),
    ModelConfig(name="pca_linear", estimator=onehot_pca_linear_pipeline(), grid_search_params=ONEHOT_PCA_LINEAR_GRID_SEARCH),
    ModelConfig(name="pca_ridge", estimator=onehot_pca_ridge_pipeline(), grid_search_params=ONEHOT_PCA_RIDGE_GRID_SEARCH),
]

def baseline_scorer(y_true, y_pred):
    #run all the metrics in the regression_metrics list
    metrics_dict = {}
    for metric in REGRESSION_METRICS:
        if metric.startswith("neg"):
            score = -1 * getattr(metrics, metric)(y_true, y_pred)
        else:
            score = getattr(metrics, metric)(y_true, y_pred)
        metrics_dict[metric] = score
    return metrics_dict
    
