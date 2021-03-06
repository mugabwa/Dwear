import os
import numpy as np
import pandas as pd


def read_data(file, columns):
    if not os.path.isfile(file):
        raise AssertionError(file, 'not found')
    with open(file, 'r') as fl:
        lines = fl.readlines()
        l_str = [x.rstrip('\n').split(',') for x in lines]
        row_no = len(l_str)
        print('Contains {} rows'.format(row_no))
        col_no = len(columns)
        data = np.zeros([row_no,col_no])
        for index, line in enumerate(l_str):    #can change slice
            for i, j in enumerate(columns):
                try:
                    data[index, i] = line[j]
                except ValueError:
                    data[index, i] = 0
    return data
