from typing import Callable, Tuple

import numpy as np
from numpy import ndarray


def get_covariance_matrix(cov_fun, x1, x2=None):
    if x2 is None:
        x2 = x1

    return cov_fun(x1[:, None], x2[None, :])


def get_posterior_mean_cov(
        prior_mean: float, prior_cov_fun: Callable, obs_var: float,
        x1: ndarray, y1: ndarray, x2: ndarray
) -> Tuple[ndarray, ndarray]:
    """ Return mean and covariance matrix of the posterior Gaussian process evaluated at `x2`.

    Args:
        prior_mean:
        prior_cov_fun:
        obs_var:
        x1:
        y1:
        x2:

    We denote by `f2` the unknown values of our function

    Returns:
        vector `f2_mean` and positive definite matrix `f2_cov`
    """

    # k11, k21, k22 are the blocks of the covariance matrix of the prior on
    # the concatenated vector [f1, f2] where f1, f2 are the (unknown) values of our function at x1 and x2
    k11 = get_covariance_matrix(prior_cov_fun, x1)
    k21 = get_covariance_matrix(prior_cov_fun, x2, x1)
    k22 = get_covariance_matrix(prior_cov_fun, x2)

    m = np.linalg.inv(k11 + obs_var * np.eye(len(x1)))
    f2_mean = prior_mean + k21 @ (m @ (y1 - prior_mean))
    f2_cov = k22 - k21 @ m @ k21.T

    return f2_mean, f2_cov


def get_log_evidence(mean: float, cov_fun: Callable, obs_var: float,
                     x: ndarray, y: ndarray) -> float:
    n = len(x)
    cov = get_covariance_matrix(cov_fun, x) + obs_var * np.eye(n)
    cov_inv = np.linalg.inv(cov)
    cov_det = np.linalg.det(cov)
    y1 = y - mean
    return - n/2 * np.log(2 * np.pi) - 1/2 * np.log(cov_det) - 1/2 * y1 @ cov_inv @ y1