import os
import openpyxl
import shutil
from dotenv import load_dotenv

load_dotenv()
def perenos_aktov():
    akt_path = r"E:\!Проверено"

    rd_path = r"C:\Users\Dmitry\Desktop\Акты\Рд"

    dir_count = len(os.environ.get("DISK").split('\\')) + 1

    akti = {}
    rd = {}
    #Создаем список имеющихся актов
    for root, paths, files in os.walk(os.path.abspath(akt_path)):
        for file in files:
            akti[file.lstrip()[:5]] = os.path.join(root, file)

    #Ищем папки с шифрами
    for root, paths, files in os.walk(os.path.abspath(os.environ.get("DISK"))):
        for subdirname in paths:
            a = os.path.join(root, subdirname)
            name = os.path.join(root, subdirname).split('\\')
            print(name)
            if len(os.path.join(root, subdirname).split('\\')) < dir_count + 1:
                continue
            for i in akti:
                if i in name[dir_count]:
                    print(name[dir_count], i)

                    if os.path.isdir(f'{a}/Акты') is False:
                        os.makedirs(f'{a}/Акты')
                    if os.path.isdir(f'{a}/Видео') is False:
                        os.makedirs(f'{a}/Видео')
                    if os.path.isdir(f'{a}/Рд') is False:
                        os.makedirs(f'{a}/Рд')
                    if name[-1] not in '_'.join(os.listdir(f"{a}/Акты")):
                        print(name, os.listdir(f"{a}/Акты"))
                        shutil.move(akti[i], f"{a}/Акты")
                    print(akti[i])
                    del akti[i]
def perenos_rd():
    rd_path = r"C:\Users\Dmitry\Desktop\Акты\Рд"

    dir_count = len(os.environ.get("DISK").split('\\')) + 1
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

                    for i in rd.keys():
                        if kks.lower() in i.lower():
                            print(kks, i)
                            end_path = '/'.join(os.path.join(root, file).split('\\')[:-2])
                            print(end_path)
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


perenos_aktov()
