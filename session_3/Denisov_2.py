

import numpy as np


def prod_non_zero_diag(x):
    res = 1
    for i in range(len(x[1])):
        if x[i][i] != 0:
            res = res * x[i][i]
    return res


def are_multisets_equal(x, y):
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    for i in range(len(y)):
        for j in range(i, len(y)):
            if y[i] > y[j]:
                y[i], y[j] = y[j], y[i]
    flag = 1
    for i in range(len(x)):
        if x[i] != y[i]:
            flag = 0
            break
    return True if flag == 1 else False


def max_after_zero(x):
    max_x = None
    for i in range(len(x) - 1):
        if ((x[i] == 0) & (max_x is None)):
            max_x = x[i + 1]
        elif ((x[i] == 0) & (x[i + 1] > max_x)):
            max_x = x[i + 1]
    return max_x


def convert_image(img, coefs):
    answ = np.zeros((len(img), len(img[0])))
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(len(img[0][0])):
                answ[i][j] = answ[i][j] + img[i][j][k] * coefs[k]
    return answ


def run_length_encoding(x):
    prev = x[0]
    count = 0
    counts = []
    elements = []
    for i in range(len(x)):
        if x[i] == prev:
            count += 1
        else:
            counts.append(count)
            elements.append(x[i - 1])
            count = 1
            prev = x[i]
    elements.append(x[i])
    counts.append(count)
    return elements, counts


def pairwise_distance(x, y):
    A = []
    for i in range(len(x)):
        a = []
        for j in range(len(y)):
            b = [(x[i][k]-y[j][k]) ** 2 for k in range(len(x[0]))]
            c = sum(b)
            a.append(c ** 0.5)
        A.append(a)
    return A
