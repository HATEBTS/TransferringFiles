from os import listdir
import datetime
import win32con
import win32api
import os
import shutil
import settings


def rename_sec(path, zv, date):
    files = listdir(path)
    num = 1
    for i in files:
        f = f"{path}/{zv}_{date}_{num}"
        if os.path.isfile(f'{f}.mp4'):
            while os.path.isfile(f'{f}.mp4'):
                num += 1
                f = f"{path}/{zv}_{date}_{num}"
                print(num, f)
        if '.sec' in i:
            full_path = f'{path}/{i}'

            file = f"{path}/{zv}_{date}_{num}"

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


def copy_to(path, zv, date, cd=settings.DISK):

    file_list = listdir(path)

    for file in file_list:

        all_path = f"{path}/{file}"
        print(date, get_video_creation_date(all_path))

        if date == get_video_creation_date(all_path):
            if os.path.isdir(f'{cd}/{zv}') is False:
                os.mkdir(f"{cd}/{zv}")

            shutil.copy2(all_path, f'{cd}/{zv}/{file}')


def main(dr):
    try:
        path = dr["selectedPath"]
        zv = dr["numberCamera"]
        date = dr["date"]

        rename_sec(path, zv, date)

        copy_to(path, zv, date)

        return "OK"

    except Exception as e:
        print(e)

        return "NO OK"

