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

x = "800" #Ширина окна
y = "550" #Высота окна


def main_func():
    root = tki.Tk()
    root.geometry((x+'x'+y))
    root.title("Работа с базой студентов")
    sw.Start_window(root)
    root.mainloop() # Запуск цикла обработки событий


if (__name__ == "__main__"):
    main_func()
