import os
import openpyxl
import shutil
from dotenv import load_dotenv

load_dotenv()
def perenos_aktov():
    akt_path = r"C:\Users\Dmitry\Desktop\Акты\Акты"

    rd_path = r"C:\Users\Dmitry\Desktop\Акты\Рд"

    dir_count = len(os.environ.get("DISK").split('\\')) + 1

    akti = {}
    rd = {}
    #Создаем список имеющихся актов
    for root, paths, files in os.walk(os.path.abspath(akt_path)):
        for file in files:
            akti[file.lstrip()[:5]] = os.path.join(root, file)

    # #Ищем рабочую документацию
    # for root, paths, files in os.walk(os.path.abspath(rd_path)):
    #     for file in files:
    #         rd[file] = os.path.join(root, file)

    #Ищем папки с шифрами
    for root, paths, files in os.walk(os.path.abspath(os.environ.get("DISK"))):
        for subdirname in paths:
            a = os.path.join(root, subdirname)
            name = os.path.join(root, subdirname).split('\\')
            print(name)
            if len(os.path.join(root, subdirname).split('\\'))  < dir_count + 1:
                continue
            for i in akti:
                if i in name[dir_count]:
                    print(name[dir_count], i)
                    if os.path.isdir(f'{a}/Акты') is False:
                        os.makedirs(f'{a}/Акты')
                    if os.path.isdir(f'{a}/Видео') is False:
                        os.makedirs(f'{a}/Видео')
                    shutil.move(akti[i], f"{a}/Акты")
                    print(akti[i])
                    del akti[i]
