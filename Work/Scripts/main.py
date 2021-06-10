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



def main_func():
    mass_elements = []
    root = tki.Tk()
    root.geometry('800x450')
    root.title("Работа с базой студентов")
    sw.Start_window(root)

    root.mainloop() # Запуск цикла обработки событий


if (__name__ == "__main__"):
    main_func()
