"""
Module with various utility functions
"""

import numpy as np

def euclidean_dist_matrix(data_1, data_2):
    """
    Returns matrix of pairwise, squared Euclidean distances
    """
    norms_1 = (data_1 ** 2).sum(axis=1)
    norms_2 = (data_2 ** 2).sum(axis=1)
    return np.abs(norms_1.reshape(-1, 1) + norms_2 - 2 * np.dot(data_1, data_2.T))

def vec(data):
    """
    Reshapes matrix to a vector.
    """
    return np.reshape(data, (data.shape[0] * data.shape[1], 1));

def vec_t(data):
    """
    Returns vec(data)^T.
    """
    v = vec(data)
    return np.reshape(v, (1, v.shape[0]))