import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def train(self, X: NDArray[np.float64], y: NDArray[np.float64], epochs: int, lr: float) -> Tuple[NDArray[np.float64], float]:
        # X: (n_samples, n_features)
        # y: (n_samples,) targets
        # epochs: number of training iterations
        # lr: learning rate
        #
        # Model: y_hat = X @ w + b
        # Loss: MSE = (1/n) * sum((y_hat - y)^2)
        # Initialize w = zeros, b = 0
        # return (np.round(w, 5), round(b, 5))
        
        w = np.zeros(X.shape[1])
        b = 0
        n = X.shape[0]
        for i in range(epochs):
            y_hat = np.zeros(n)
            for j in range(n):
                y_hat[j] = np.matmul(X[j], w) + b
                loss = np.mean((y_hat - y) ** 2)

            dL_dw = (2/n) * np.matmul(X.T, (y_hat - y))    
            dL_db = (2/n) * np.sum(y_hat - y)
            w = w - lr * dL_dw
            b = b - lr * dL_db
    
        return np.round(w, 5), np.round(b, 5)

