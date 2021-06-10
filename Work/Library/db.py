# -*- coding: utf-8 -*-
"""
Сохранение данных в файле
Бригада 4 БИВ205
"""
# Тестовая база
import pandas as pd

path_main_db = r"../Data/main_db.csv"  #Путь к базе с студентами
path_fs_db = r"../Data/fs_db.csv"    #Путь к базе с id дисциплин
path_sh_db = r"../Data/sh_db.csv"    #Путь к базе с id стипендий


def base_main():
    return pd.read_csv(path_main_db)


def base_fs():
    return pd.read_csv(path_fs_db)


def base_sh():
    return pd.read_csv(path_sh_db)
