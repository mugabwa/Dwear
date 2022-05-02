import os
import numpy as np
import pandas as pd


def read_data(file, columns):
    if not os.path.isfile(file):
        raise AssertionError(file, 'not found')
    extension = file.split('.')[-1]
    if extension.lower() == 'txt':
        file1 = convert_txt_to_csv(file)
    with open(file1, 'r') as fl:
        lines = fl.readlines()
        l_str = [x.rstrip('\n').split(',') for x in lines]
        row_no = len(l_str)
        print('Contains {} rows'.format(row_no))
        col_no = len(columns)
        data = np.zeros([row_no,col_no])
        for index, line in enumerate(l_str):    #can change slice
            for i, j in enumerate(columns):
                data[index, i] = line[j]
    return data


def convert_txt_to_csv(file_path):
    i_path = file_path.split('\\')
    i_path[-1] = '.'.join([i_path[-1].split('.')[0],'csv'])
    path_n = '\\'.join(i_path)
    if not os.path.isfile(path_n):
        data = pd.read_csv(file_path, header=None, encoding = "unicode_escape")
        data.to_csv(path_n, index=False, header=False)
    return path_n