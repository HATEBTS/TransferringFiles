from psycopg2 import connect
from openpyxl import Workbook
from settings import DB_CONFIG
from os import makedirs, path
from io import BytesIO
from flask import send_file


base_path = path.join(path.dirname(__file__), 'data_folder')


def psql_to_excel_load():
    # Установка соединения с базой данных
    conn = connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Выполнение SQL-запроса для получения данных
    query = "SELECT * FROM submit_form"
    cursor.execute(query)
    data = cursor.fetchall()

    # Создание Excel-файла
    output = BytesIO()
    workbook = Workbook()
    sheet = workbook.active

    # Запись данных в Excel
    for row in data:
        sheet.append(row)

    # Сохранение в байтовом потоке
    workbook.save(output)
    output.seek(0)
    excel_filename = 'data.xlsx'
    excel_path = path.join(base_path, excel_filename)

    # Создание папки, если она не существует
    makedirs(base_path, exist_ok=True)

    with open(excel_path, 'wb') as f:
        f.write(output.read())
    # Отправка файла клиенту
    send_file(
        BytesIO(output.read()),
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='data.xlsx'  # Задайте имя файла через заголовок Content-Disposition
    )
    return "Ok", 200
