import os
from os import listdir
from tkinter import filedialog as fd
import datetime
import win32con
import win32api
import os
import shutil
import settings

pat1 = fd.askopenfilename()


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


def get_video_creation_date(video_path):
    try:
        # Получаем статистику о файле
        stat_info = os.stat(video_path)

        # Извлекаем время создания из статистики и преобразуем в строку
        creation_time = stat_info.st_ctime
        creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%d.%m.%Y')

        return creation_date

    except Exception as e:
        print(f"Ошибка при получении даты создания: {e}")
        return None


def copy_to(serial_number, path, date, cd=settings.DISK):
    file_list = listdir(path)
    for file in file_list:
        all_path = f"{path}/{file}"
        if date == get_video_creation_date(all_path):
            shutil.copyfile(all_path, f'{cd}/{serial_number}')


def main():
    pass


if __name__ == "__main__":
    main()


print(get_video_creation_date(pat1))
# rename_sec(fd.askdirectory(), zv='zv', date="date")

