import os
from os import listdir
from tkinter import filedialog as fd
import datetime
import win32con
import win32api
import settings


def rename_sec(path, zv, date):
    files = listdir(path)
    num = 1
    for i in files:
        if '.sec' in i:
            full_path = f'{path}/{i}'
            file = f"{path}/{zv}_{date}_{num}"
            os.rename(full_path, f"{file}.mp4")
            win32api.SetFileAttributes(f"{file}.mp4", win32con.FILE_ATTRIBUTE_NORMAL)
            num += 1


def find_folder(serial_number):
    cd = settings.DISK










rename_sec(fd.askdirectory(), zv='zv', date="date")