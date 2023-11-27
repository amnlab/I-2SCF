import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def add_padding(input_data, split_point1, split_point2, index):
    if split_point1 == 0:
        if index == 1:
            padded_data_zero = np.pad(input_data, ((0, 0), (1, 1), (1, 1), (0, 0)), mode='constant')
            padded_data = padded_data_zero[:, 0:split_point2 + 2, :, :]
            return padded_data

        elif index == 2:
            padded_data_zero = np.pad(input_data, ((0, 0), (1, 1), (1, 1), (0, 0)), mode='constant')
            padded_data = padded_data_zero[:, split_point2:, :, :]
            return padded_data

    else:
        if index == 0:
            padded_data_zero = np.pad(input_data, ((0, 0), (1, 1), (1, 1), (0, 0)), mode='constant')
            padded_data = padded_data_zero[:, 0:split_point1 + 2, :, :]
            return padded_data

        elif index == 1:
            padded_data_zero = np.pad(input_data, ((0, 0), (1, 1), (1, 1), (0, 0)), mode='constant')
            padded_data = padded_data_zero[:, split_point1:split_point2 + 2, :, :]
            return padded_data

        elif index == 2:
            padded_data_zero = np.pad(input_data, ((0, 0), (1, 1), (1, 1), (0, 0)), mode='constant')
            padded_data = padded_data_zero[:, split_point2:, :, :]
            return padded_data
