import os
import openpyxl
import shutil
from dotenv import load_dotenv
from tkinter import filedialog as fd
import tkinter

load_dotenv()


def proverka_sh(file):
    d = 0
    if len(file) >= 5:
        for i in file[:5]:
            if i in "0123456789":
                d += 1
    return d >= 5

  
def perenos_aktov():
    akt_path = fd.askdirectory()

    akti = {}
    sps_papasha = {}
    #Создаем список имеющихся актов
    for root, paths, files in os.walk(os.path.abspath(akt_path)):
        for file in files:
            akti[file.lstrip()[:5]] = os.path.join(root, file)

    #Ищем папки с шифрами
    for root, paths, files in os.walk(os.path.abspath(os.environ.get("DISK"))):
        for subdirname in paths:
            if proverka_sh(subdirname):
                sps_papasha[subdirname] = os.path.join(root, subdirname)
    for i in akti:
        for j in sps_papasha.keys():
            if i in j:
                print(i, j)
                if os.path.isdir(f'{sps_papasha[j]}/Акты') is False:
                    os.makedirs(f'{sps_papasha[j]}/Акты')
                if os.path.isdir(f'{sps_papasha[j]}/Видео') is False:
                    os.makedirs(f'{sps_papasha[j]}/Видео')
                if os.path.isdir(f'{sps_papasha[j]}/Рд') is False:
                    os.makedirs(f'{sps_papasha[j]}/Рд')
                if akti[i][-1] not in os.listdir(f"{sps_papasha[j]}/Акты"):
                    if os.path.isfile(akti[i]):
                        if akti[i].split('\\')[-1] not in os.listdir(f"{sps_papasha[j]}/Акты"):
                            shutil.move(akti[i], f"{sps_papasha[j]}/Акты")
                            print(f'Файл {akti[i]} перенесен!')
                        else:
                            print(f'Файл {akti[i]} уже существует!')
                    else:
                        print(f'Файл {akti[i]} уже перенесен!')

                        
def perenos_rd():
    rd_path = fd.askdirectory()
    rd = {}
    # Ищем рабочую документацию
    for root, paths, files in os.walk(os.path.abspath(rd_path)):
        for file in files:
            rd[file] = os.path.join(root, file)

    for root, paths, files in os.walk(os.path.abspath(os.environ.get("DISK"))):

        for file in files:
            try:
                if '.xlsx' in file or '.xlsm' in file or '.XLSX' in file or '.XLSM' in file:
                    full_path = os.path.join(root, file)
                    book = openpyxl.load_workbook(full_path)
                    sheet = book.active
                    kks = str(sheet["C10"].value)
                    print(kks)

                    for i in rd.keys():
                        if kks.lower() in i.lower():
                            print(kks, i)
                            end_path = '/'.join(os.path.join(root, file).split('\\')[:-2])
                            if os.path.isdir(f'{end_path}/Акты') is False:
                                os.makedirs(f'{end_path}/Акты')
                            if os.path.isdir(f'{end_path}/Видео') is False:
                                os.makedirs(f'{end_path}/Видео')
                            if os.path.isdir(f'{end_path}/Рд') is False:
                                os.makedirs(f'{end_path}/Рд')
                            shutil.copy2(rd[i], f'{end_path}/Рд/{i}')
                            print('OK')
            except Exception as e:
                print(e)
perenos_rd()