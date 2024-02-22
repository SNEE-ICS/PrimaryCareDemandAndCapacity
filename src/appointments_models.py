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

set_config(transform_output='pandas')


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
    metrics.max_error,
    metrics.mean_absolute_error,
    metrics.mean_squared_error,
    metrics.median_absolute_error,
    metrics.r2_score
]



class ModelConfig(BaseModel):
    name: str
    estimator: Pipeline
    grid_search_params: Dict[str, Any]
    metrics: Dict[str, float | int] = Field(default_factory=dict)
    best_params_by_metric: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True




def basic_onehot_pipeline() -> Pipeline:
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
            ("preprocess", ColumnTransformer([("onehot", OneHotEncoder(sparse_output=False), ["month"])], remainder="passthrough")),
            ("linear_regression", LinearRegression()),
        ]
    )
    onehot_pipeline.set_output(transform='pandas')
    return onehot_pipeline


def onehot_polynomial_linear_pipeline() -> Pipeline:
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
            ("preprocess", ColumnTransformer([("onehot", OneHotEncoder(sparse_output=False), ["month"])], remainder="passthrough")),
            ("polynomial", PolynomialFeatures(degree=DEFAULT_POLY_DEGREE)),
            ("linear_regression", LinearRegression()),
        ]
    )
    return poly_pipeline


def onehot_polynomial_ridge_pipeline() -> Pipeline:
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
            ("preprocess", ColumnTransformer([("onehot", OneHotEncoder(sparse_output=False), ["month"])], remainder="passthrough")),
            ("polynomial", PolynomialFeatures(degree=DEFAULT_POLY_DEGREE)),
            ("ridge", Ridge()),
        ]
    )
    return poly_pipeline


def onehot_pca_linear_pipeline() -> Pipeline:
    """
    Creates a pipeline for one-hot encoding, PCA dimensionality reduction, and linear regression.

    Args:
        pipeline_kwargs (Optional[dict]): Optional keyword arguments to set pipeline parameters.

    Returns:
        Pipeline: The constructed pipeline.

    """
    # Define the pipeline
    pca_pipeline = Pipeline(
        steps=[
            (
                "preprocess",
                ColumnTransformer(
                    transformers=[
                        ("onehot", OneHotEncoder(sparse_output=False), ["month"]),
                        ("scale_pca", Pipeline([
                            ("scale", StandardScaler()),
                            ("pca", PCA(n_components=2))
                        ]), const.GP_LIST_AGE_LABELS),
                    ],
                    remainder="passthrough"
                ),
            ),
            ("linear_regression", LinearRegression()),
        ]
    )
    return pca_pipeline


def onehot_pca_ridge_pipeline() -> Pipeline:
    """
    Creates a pipeline for one-hot encoding, PCA dimensionality reduction, and linear regression.

    Args:
        pipeline_kwargs (Optional[dict]): Optional keyword arguments to set pipeline parameters.

    Returns:
        Pipeline: The constructed pipeline.

    """
    # Define the pipeline
    pca_pipeline = Pipeline(
        steps=[
            (
                "preprocess",
                ColumnTransformer(
                    transformers=[
                        ("onehot", OneHotEncoder(sparse_output=False), ["month"]),
                        ("scale_pca", Pipeline([
                            ("scale", StandardScaler()),
                            ("pca", PCA(n_components=2))
                        ]), const.GP_LIST_AGE_LABELS),
                    ],
                    remainder="passthrough"
                ),
            ),
            ("ridge", Ridge()),
        ]
    )
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
            score = metric(y_true, y_pred)
            metrics_dict[metric.__name__] = score
    return metrics_dict
    
