

import numpy as np


def prod_non_zero_diag(x):
    diag = x.diagonal()
    diag_without_zeros = diag[diag != 0]
    res = np.multiply.reduce(diag_without_zeros)
    return res


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    if np.array_equal(x, y) == True:
        return True
    else:
        return False


def max_after_zero(x):
    zeros = (x == 0)
    zeros_without_last = zeros[0:len(zeros) - 1]
    potential_elements = x[1:][zeros_without_last]
    return potential_elements.max()


def convert_image(img, coefs):
    return np.dot(img, coefs)


def run_length_encoding(x):
    x_diff = np.diff(x)
    y_non_zeros = (x_diff != 0)
    y_non_zeros = np.concatenate((y_non_zeros, np.array([True])))
    mass1 = x[y_non_zeros]  # это первый массив
    indexes_of_non_zeros = list(np.nonzero(x_diff)[0])
    indexes_of_non_zeros.append(len(x) - 1)
    indexes_of_non_zeros = [-1] + indexes_of_non_zeros
    lengths_of_nums = np.diff(indexes_of_non_zeros)
    return mass1, lengths_of_nums


def pairwise_distance(x, y):
    A = np.sqrt(np.sum((x[:, np.newaxis] - y) ** 2, axis=2))
    return A
