# -*- coding: utf-8 -*-
"""
Главная функция
"""


import pandas as pd
import os
import sys
import numpy as np
import tkinter as tki
import tkinter.ttk as ttk
import windows as sw

os.chdir(r'../Scripts/')
sys.path.append(r'../')
import Library as lib

common_x = "800"  # Ширина окна
common_y = "550"  # Высота окна


def main_func():
    root = tki.Tk()
    root.geometry((common_x + 'x' + common_y))
    root.title("Работа с базой студентов")
    sw.Start_window(root)
    root.mainloop()  # Запуск цикла обработки событий
    sys.exit()


if (__name__ == "__main__"):
    main_func()
