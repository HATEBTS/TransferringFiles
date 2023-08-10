import os

import openpyxl
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

dir_count = len(os.environ.get("DISK").split('\\')) + 1


def unload_disk_base(dirs):
    check_list = []
    dict_base_path = {
        "Звено": [],
        "Номер акта": [],
        "Статус акта": [],
        "Статус видео": [],
        "Кол-во видео": [],
        "Статус РД": [],
        "Ссылка на папку": []
    }
    for root, dirs, files in os.walk(os.path.abspath(dirs)):
        for file in files:
            print(('_'.join(check_list)), (os.path.join(root, file).split('\\')[dir_count].split('_')[0]))
            if len(os.path.join(root, file).split('\\')) > dir_count and \
                    '_' in os.path.join(root, file).split('\\')[dir_count] and \
                    os.path.join(root, file).split('\\')[dir_count].split('_')[0] not in '_'.join(check_list):
                path_file = os.path.join(root, file).split('\\')
                zv = path_file[dir_count].split('_')[0][:2]
                num_act = path_file[dir_count].split('_')[0][2:5]
                dict_base_path["Звено"].append(zv)
                dict_base_path["Номер акта"].append(num_act)
                list_files = []
                d = [list_files.extend(files1) for root1, dirs1, files1 in
                     os.walk(os.path.abspath("/".join(path_file[:dir_count + 1]))) if files1]
                f = list_files
                list_files = '_'.join(list_files)
                if (".xlsx" in list_files or ".xlsm" in list_files or ".XLSX" in list_files or ".XLSM" in
                        list_files or ".xlsb" in list_files or ".XLSB" in list_files):
                    dict_base_path["Статус акта"].append(True)
                    last_akt = True
                else:
                    dict_base_path["Статус акта"].append(False)
                    last_akt = False
                if '.mp4' in list_files or '.sec' in list_files:
                    dict_base_path["Статус видео"].append(True)
                    last_colvid = len([i for i in f if '.mp4' in i or ".sec" in i])
                    dict_base_path["Кол-во видео"].append(last_colvid)
                    last_vid = True
                else:
                    dict_base_path["Статус видео"].append(False)
                    last_colvid = 0
                    dict_base_path["Кол-во видео"].append(0)
                    last_vid = False
                if ".pdf" in list_files or ".PDF" in list_files or '.zip' in list_files \
                        or '.rar' in list_files or '.ZIP' in list_files or '.RAR' in list_files:
                    dict_base_path["Статус РД"].append(True)
                    last_rd = True
                else:
                    dict_base_path["Статус РД"].append(False)
                    last_rd = False
                dict_base_path["Ссылка на папку"].append("/".join(str(root).split("\\")[0:-1]))
                if "," in os.path.join(root, file).split('\\')[dir_count]:
                    check_list.append(path_file[dir_count].split('_')[0])
                    prost = os.path.join(root, file).split('\\')[dir_count].split('_')[0].split(',')
                    for _ in range(1, len(prost)):
                        dict_base_path["Звено"].append(prost[_].lstrip()[:2])
                        dict_base_path["Номер акта"].append(prost[_].lstrip()[2:5])
                        dict_base_path["Статус акта"].append(last_akt)
                        dict_base_path["Статус видео"].append(last_vid)
                        dict_base_path["Кол-во видео"].append(last_colvid)
                        dict_base_path["Статус РД"].append(last_rd)
                        dict_base_path["Ссылка на папку"].append("/".join(str(root).split("\\")[0:-1]))
                        check_list.append(prost[_])
                else:
                    check_list.append(path_file[dir_count].split('_')[0])
    return dict_base_path


def svod(paths=os.environ.get("DISK")):
    try:
        d = unload_disk_base(paths)
        for i in d.values():
            print(len(i))
        writer = openpyxl.Workbook()
        writer.save("Sozdal.xlsx")
        writer.close()

        writer = pd.ExcelWriter('Sozdal.xlsx')
        df_marks = pd.DataFrame(d)
        df_marks.to_excel(writer)
        writer._save()
        return "K KOK"
    except Exception as e:
        print(e)
        return "WHAT"
