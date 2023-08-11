import gspread
from base_disk_xls import svod
# Указываем путь к JSON
gc = gspread.service_account(filename=r'C:\Users\Dmitry\PycharmProjects\Transferring\backend\credentials.json')
#Открываем тестовую таблицу
sh = gc.open("Выходная таблица")
worksheet = sh.worksheet("Лист2")
#Выводим значение ячейки A1
print(worksheet.get('H:H'))
list_shifr = worksheet.get('H:H')
disk_dict = svod()
for i in range(1, len(list_shifr) + 1):
    worksheet.update(f"L2:N2", [[1,2,3]])
