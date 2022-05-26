# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import argparse

def generate_data(rows, cols, intersect_rate, party):
    np.random.seed(100)
    
    val = np.random.uniform(-1, 1, (rows, cols))
    
    if party == "g":
        idx = np.arange(rows).reshape(-1, 1)
        label = np.random.randint(0, 2, (rows, 1))
        data = pd.DataFrame(np.hstack((idx, val, label)))
        data.to_csv("psi_guest.csv", index=None)
    elif party == 'h':
        start_idx = rows * (1 - intersect_rate)
        end_idx = rows + start_idx
        idx = np.arange(start_idx, end_idx, 1).reshape(-1, 1)
        data = pd.DataFrame(np.hstack((idx, val)))
        data.to_csv("psi_host.csv", index=None)
        
parser = argparse.ArgumentParser()
parser.add_argument('-r', dest="rows", type=int, help='Rows of the datasets')
parser.add_argument('-c', dest="cols", type=int, help='Cols of the datasets')
parser.add_argument('-i', dest="intersect_rate", type=float, help='Intersect_rate of the datasets')
parser.add_argument('-p', dest="party", type=str, help='Party of the datasets')
args = parser.parse_args()

generate_data(args.rows, args.cols, args.intersect_rate, args.party)
