import math
import os
from routes.read_file_data import read_data
import statistics

THRESHOLD = 0.1
FACTOR = 10
COST = 10

def cost_data(file, distance):
    cur_dir = os.getcwd()
    cur_dir += "/media/"
    file = os.path.join(cur_dir, file)
    data = read_data(file, [0,1,2])
    z_mean = statistics.mean([z[2] for z in data])
    xval_min = [z[2] for z in data if z[2]<z_mean-THRESHOLD]
    xval_max = [z[2] for z in data if z[2]>z_mean+THRESHOLD]
    x_len = len(xval_max)+len(xval_min)
    data_len = len(data)
    try:
        x1_threshold = statistics.mean(xval_max) - (z_mean+THRESHOLD)
        x2_threshold = statistics.mean(xval_min) - (z_mean-THRESHOLD)
    except Exception:
        return 0
    x_avg = (abs(x1_threshold)+abs(x2_threshold))/2
    x_avg = x_avg*(x_len/3)
    l_distance = distance.split(' ')
    distance1 = (float(l_distance[0])*x_len)/data_len
    cost = math.floor(COST*x_avg*distance1)
    if cost > 200:
        cost = 200
    print(cost)
    return cost
