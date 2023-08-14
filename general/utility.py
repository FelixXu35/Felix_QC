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


def all_quantum_states(n_qubits) -> list:
    states = []
    for i in range(2**n_qubits):
        a = f"{bin(i)[2:]:0>{n_qubits}}"
        n_ones = 0
        for j in a:
            if j == "1":
                n_ones += 1
        states.append(a)
    return states
