from os import listdir
import datetime
import win32con
import win32api
import os
import shutil


def rename_sec(path, date, name):
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


def copy_to(path, zv, date, name, cd=os.environ.get('DISK')):
    file_list = listdir(path)

    gety = [i for i in file_list if '.mp4' in i.lower() or '.jpg' in i.lower()]
    gety1 = [i for i in file_list if get_video_creation_date(i) == date]
    if len(gety) == 0:
        return "NoFile"
    if len(gety1) == 0:
        return "NoDateFile"

    for file in file_list:

        all_path = f"{path}/{file}"
        path_to_end = f'{cd}/{zv}/{name}_{date}'
        print(date, get_video_creation_date(all_path))
        print(path_to_end)
        if date == get_video_creation_date(all_path):
            if os.path.isdir(path_to_end) is False:
                os.makedirs(path_to_end)

                if os.path.isdir(f'{path_to_end}/Акты') is False:
                    os.makedirs(f'{path_to_end}/Акты')
                if os.path.isdir(f'{path_to_end}/Видео') is False:
                    os.makedirs(f'{path_to_end}/Видео')

            if '.mp4' in file.lower() or '.jpg' in file.lower():
                shutil.copy2(all_path, f'{path_to_end}/Видео/{file}')


def main(dr):
    try:
        path = dr["selectedPath"]
        zv = dr["numberCamera"]
        date = dr["date"]
        name = dr["numberObject"]

        rename_sec(path, date, name)

        if copy_to(path, zv, date, name) == 'Parol1':
            return 'Parol1'

        return "OK"

    except Exception as e:
        print(e)

        return "NO OK"

