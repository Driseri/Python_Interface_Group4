# -*- coding: utf-8 -*-
"""
Главная функция

"""
import pandas as pd
import os
import sys

os.chdir(r'../Scripts/')
sys.path.append(r'../')

def main_func():
    df = pd.read_csv('../Data/sh_db.csv')
    print(df)



if (__name__ == "__main__"):
    main_func()
