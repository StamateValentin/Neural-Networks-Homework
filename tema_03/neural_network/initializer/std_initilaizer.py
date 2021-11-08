import random

import numpy as np


class StandardDeviationInitializer:
    @staticmethod
    def init(n, m):
        arr = np.zeros((n, m), dtype='float32')

        mag = 1 / (m ** 0.5)

        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                arr[i, j] = mag * (random.random() * 2) + (-mag)

        return arr
