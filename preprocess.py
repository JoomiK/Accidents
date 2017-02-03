"""Functions to clean up or preprocess string or group data"""

import numpy as np
import pandas as pd


def make_int(i):
    """
    Make strings into integers
    """
    if i == '':
        return None
    else:
        return int(i)
    
def group_data(data, key_name):
    """
    Building a dict of lists
    """
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data

def cleanup(dic):
    """
    Make string years into integers and sort (by year)
    """
    year, total = zip(*(sorted(dic.items())))
    return list(map(int,year)), total


