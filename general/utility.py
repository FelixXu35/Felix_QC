import numpy as np


def symmetric_matrix_generator(dim: int) -> np.array:
    """
    Generate a random symmetric matrix with a give dimension.
    args:
        dim: the number of dimension
    return:
        mat: a symmetric matrix
    """
    mat = np.random.rand(dim**2).reshape(dim, dim)
    mat = np.triu(mat)
    mat += mat.T - np.diag(mat.diagonal())
    
    return mat