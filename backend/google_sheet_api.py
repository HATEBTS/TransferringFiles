import os
from base_disk_xls import unload_disk_base
from dotenv import load_dotenv
import gspread


load_dotenv()

# Указываем путь к JSON
gc = gspread.service_account(filename=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))


def google_vg():
    # Открываем тестовую таблицу
    sh = gc.open("Выходная таблица")
    worksheet = sh.worksheet("Лист3")
    # Выводим значение ячейки H1
    print(worksheet.get('H2:H'))
    list_shifr = worksheet.get('H2:H')
    disk_dict = unload_disk_base()

    status_list = []

    list_zv_disk = disk_dict['Звено']
    list_pn_disk = disk_dict['Номер акта']

    list_akt_disk = disk_dict['Статус акта']
    list_vid_disk = disk_dict['Статус видео']
    list_rd_disk = disk_dict['Статус РД']

    list_shifr_disk = [''.join(x) for x in zip(list_zv_disk, list_pn_disk)]

    for i in range(0, len(list_shifr)):
        if len(list_shifr[i]) > 0:
            dast = list_shifr[i][0]
            if '`' in dast:
                dast = dast.replace('`', '')
            if "'" in dast:
                dast = dast.replace("'", '')
            if "_" in dast:
                dast = dast.replace("_", '-')
            if " " in dast:
                dast = dast.split(' ')[0]
            if len(dast) != 0 and dast in list_shifr_disk:
                ind = list_shifr_disk.index(dast)
                status_list.append([list_akt_disk[ind], list_vid_disk[ind], list_rd_disk[ind]])
            elif len(dast) != 0 and f'0{dast}' in list_shifr_disk:
                ind = list_shifr_disk.index(f'0{dast}')
                status_list.append([list_akt_disk[ind], list_vid_disk[ind], list_rd_disk[ind]])
            elif len(dast) != 0:
                print(dast, 'Не подходит')
                status_list.append([False, False, False])
        else:
            status_list.append(['', '', ''])
    worksheet.update(f"L2:N{len(list_shifr) + 1}", status_list)
