# -*- coding: utf-8 -*-
"""
Главная функция

"""
os.chdir(r'../Scripts/')
sys.path.append(r'../')
import pandas as pd
import os
import sys
import library as lib



def main_func():
    df = pd.read_csv('../Data/sh_db.csv')
    print(df)



if (__name__ == "__main__"):
    main_func()
