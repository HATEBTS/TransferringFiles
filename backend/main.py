from os import listdir
import datetime
import win32con
import win32api
import os
import shutil
import settings


def rename_sec(path, zv, date, name):
    files = listdir(path)
    num = 1
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

            os.rename(full_path, f"{file}.mp4")

            win32api.SetFileAttributes(f"{file}.mp4", win32con.FILE_ATTRIBUTE_NORMAL)
            num += 1


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


def copy_to(path, zv, date, name, cd=settings.DISK):
    file_list = listdir(path)

    gety = [i for i in file_list if '.mp4' in i.lower() or '.jpg' in i.lower()]
    if len(gety) == 0:
        print('Sabaka')
        return "Parol1"

    for file in file_list:

        all_path = f"{path}/{file}"
        path_to_end = f'{cd}/{zv}/{name}_{date}'
        print(date, get_video_creation_date(all_path))

        if date == get_video_creation_date(all_path):
            if os.path.isdir(path_to_end) is False:
                os.mkdir(path_to_end)

            if '.mp4' in file.lower() or '.jpg' in file.lower():
                shutil.copy2(all_path, f'{path_to_end}/{file}')


def main(dr):
    try:
        path = dr["selectedPath"]
        zv = dr["numberCamera"]
        date = dr["date"]
        name = dr["numberObject"]

        rename_sec(path, zv, date, name)

        ch_to = copy_to(path, zv, date, name)
        if ch_to == 'Parol1':
            return 'Parol1'

        return "OK"

    except Exception as e:
        print(e)

        return "NO OK"

