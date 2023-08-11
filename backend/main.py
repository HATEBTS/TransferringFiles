from dotenv import load_dotenv
import os
import datetime
import win32con
import win32api
import shutil
from flask import request
import requests

load_dotenv()

def zv_check():
    pass
def compare_times(time1, time2):
    time_format = "%H:%M"  # Формат времени, например, "чч:мм:сс"
    parsed_time1 = datetime.datetime.strptime(time1, time_format)
    parsed_time2 = datetime.datetime.strptime(time2, time_format)

    return parsed_time1 > parsed_time2

def rename_sec(path, date, name, time):
    files = os.listdir(path)
    num = 1
    listic = []
    for i in files:
        f = f"{path}/{name}_{date}_{num}"
        if os.path.isfile(f'{f}.mp4'):
            while os.path.isfile(f'{f}.mp4'):
                num += 1
                f = f"{path}/{name}_{date}_{num}"
                print(num, f)
        if '.sec' in i:
            full_path = f'{path}/{i}'

            file = f"{path}/{name}_{date}_{num}"
            if get_video_creation_date(full_path) == date:
                os.rename(full_path, f"{file}.mp4")
                listic.append(f"{name}_{date}_{num}.mp4")
                win32api.SetFileAttributes(f"{file}.mp4", win32con.FILE_ATTRIBUTE_NORMAL)
                num += 1
    return listic


def get_video_creation_date(video_path):
    try:
        # Получаем статистику о файле
        stat_info = os.stat(video_path)

        # Извлекаем время создания из статистики и преобразуем в строку
        creation_time = stat_info.st_mtime
        creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')

        return creation_date

    except Exception as e:
        print(f"Ошибка при получении даты создания: {e}")

        return None

def get_video_creation_time(video_path):
    try:
        # Получаем статистику о файле
        stat_info = os.stat(video_path)

        # Извлекаем время создания из статистики и преобразуем в строку
        creation_time = stat_info.st_mtime
        creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%H:%M')

        return creation_date

    except Exception as e:
        print(f"Ошибка при получении времени создания: {e}")

        return None
def copy_to(path, zv, date, name, list_failov, time, cd=os.environ.get("DISK")):

    file_list = os.listdir(path)

    gety = [i for i in file_list if '.mp4' in i.lower() or '.jpg' in i.lower()]
    gety1 = [i for i in file_list if get_video_creation_date(f"{path}/{i}") == date]
    if len(gety) == 0:
        return "NoFile"
    if len(gety1) == 0:
        return "NoDateFile"

    for file in file_list:

        all_path = f"{path}/{file}"
        path_to_end = f'{cd}/{zv}/{name}_{date}'
        if date == get_video_creation_date(all_path):

            if '.jpg' in file.lower() or file in list_failov:
                if time is None:
                    if os.path.isdir(path_to_end) is False:
                        os.makedirs(path_to_end)
                        if os.path.isdir(f'{path_to_end}/Акты') is False:
                            os.makedirs(f'{path_to_end}/Акты')
                        if os.path.isdir(f'{path_to_end}/Видео') is False:
                            os.makedirs(f'{path_to_end}/Видео')
                        if os.path.isdir(f'{path_to_end}/Рд') is False:
                            os.makedirs(f'{path_to_end}/Рд')
                    shutil.copy2(all_path, f'{path_to_end}/Видео/{file}')

                else:
                    if compare_times(get_video_creation_time(all_path), time):
                        print(time, get_video_creation_time(all_path))
                        path_vtor = f'{cd}/{zv}/{str(name).split("_")[0].split(",")[1].lstrip()}_{date}'
                        print(path_vtor, 'Vtor')
                        if os.path.isdir(path_vtor) is False:
                            os.makedirs(path_vtor)
                            if os.path.isdir(f'{path_vtor}/Акты') is False:
                                os.makedirs(f'{path_vtor}/Акты')
                            if os.path.isdir(f'{path_vtor}/Видео') is False:
                                os.makedirs(f'{path_vtor}/Видео')
                            if os.path.isdir(f'{path_vtor}/Рд') is False:
                                os.makedirs(f'{path_vtor}/Рд')
                        shutil.copy2(all_path, f'{path_vtor}/Видео/{file}')
                    else:
                        path_per = f'{cd}/{zv}/{str(name).split("_")[0].split(",")[0].lstrip()}_{date}'
                        print(path_per, 'Per')
                        if os.path.isdir(path_per) is False:
                            os.makedirs(path_per)
                            if os.path.isdir(f'{path_per}/Акты') is False:
                                os.makedirs(f'{path_per}/Акты')
                            if os.path.isdir(f'{path_per}/Видео') is False:
                                os.makedirs(f'{path_per}/Видео')
                            if os.path.isdir(f'{path_per}/Рд') is False:
                                os.makedirs(f'{path_per}/Рд')
                        shutil.copy2(all_path, f'{path_per}/Видео/{file}')


def main(dr):
    try:
        path = dr["selectedPath"]
        zv = dr["numberCamera"]
        date = dr["date"]
        name = dr["numberObject"]
        time = dr['timeObed']

        izbraneo = rename_sec(path, date, name, time)
        prov = copy_to(path, zv, date, name, izbraneo, time)
        if prov == 'NoFile':
            return 'NoFile'
        if prov == 'NoDateFile':
            return 'NoDateFile'

        return "OK"

    except Exception as e:
        print(e)

        return "NO OK"