import math
import os
from routes.read_file_data import read_data
import statistics

THRESHOLD = 0.05
FACTOR = 10

def cost_data(file):
    cur_dir = os.getcwd()
    cur_dir += "/media/"
    file = os.path.join(cur_dir, file)
    data = read_data(file, [0,1,2])
    z_mean = statistics.mean([z[2] for z in data])
    z_median = statistics.median([z[2] for z in data])
    z_std = statistics.stdev([z[2] for z in data])
    xval = [z[2] for z in data if z[2]<z_mean-THRESHOLD]
    xval1 = [z[2] for z in data if z[2]>z_mean+THRESHOLD]
    xval.sort()
    xval1.sort()
    data_len = len(data)
    frequency = len(xval)/data_len

    amount = math.floor((frequency*data_len*z_std)/2)*FACTOR
    return amount