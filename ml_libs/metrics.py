import numpy as np

def mse(y, y_pred):
    return np.sum(( y - y_pred ) ** 2) / y.shape[0]

def rmse(y, y_pred):
    return mse(y, y_pred) ** 0.5

def accuracy(y_pred, y_test):
    return sum(y_pred == y_test) / y_test.shape[0]