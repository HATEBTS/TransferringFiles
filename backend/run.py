from os import environ, makedirs, path
import io
import csv

import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_file, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime
from openpyxl import Workbook

from main import main
from settings import BOOL_TRUE, BOOL_FALSE


load_dotenv()
base_path = path.join(path.dirname(__file__), 'data_folder')


app = Flask(__name__)
CORS(app)  # Enable CORS for the entire application

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class SubmitForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    number_camera = db.Column(db.String(50), nullable=False)
    number_object = db.Column(db.String(15), nullable=False)
    selected_path = db.Column(db.String(100), nullable=False)
    status_request = db.Column(db.Boolean, default=False, nullable=False)


def is_valid_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return date <= datetime.today()
    except ValueError:
        return False


def is_data_commit(forms, bool):
    forms.status_request = bool
    db.session.add(forms)
    db.session.commit()


@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    # submit_table = db.session.execute(db.select(SubmitForm))

    data = request.get_json()
    forms = SubmitForm(date=data["date"], number_camera=data["numberCamera"],
                       number_object=data["numberObject"], selected_path=data["selectedPath"])
    if request.method == "POST":
        if not data["date"] or not is_valid_date(data["date"]):
            is_data_commit(forms, BOOL_FALSE)
            return jsonify({'date': 'Некорректная дата или дата в будущем'}), 400

        if len(data["selectedPath"]) == 0:
            print(355)
            is_data_commit(forms, BOOL_FALSE)
            return jsonify({'selectedPath': 'Пустой путь'}), 400

    fart = main(data)
    print(fart)

    if fart == "NoFile":
        is_data_commit(forms, BOOL_FALSE)
        return jsonify({'Napas_lavandos': 'Нет mp4 или jpg'}), 400
    if fart == "NoDateFile":
        is_data_commit(forms, BOOL_FALSE)

        return jsonify({'NoDateFile': 'Нет файлов подходящих по дате'}), 400
    is_data_commit(forms, BOOL_TRUE)
    return jsonify(data)


db_config = {
    'dbname': environ.get("DB_NAME"),
    'user': environ.get("DB_USER"),
    'password': environ.get("DB_PASS"),
    'host': environ.get("DB_HOST")
}


@app.route('/download_excel')
def download_excel():
    if request.method == "GET":

        # Установка соединения с базой данных
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Выполнение SQL-запроса для получения данных
        query = "SELECT * FROM submit_form"
        cursor.execute(query)
        data = cursor.fetchall()

        # Создание Excel-файла
        output = io.BytesIO()
        workbook = Workbook()
        sheet = workbook.active

        # Запись данных в Excel
        for row in data:
            sheet.append(row)

        # Сохранение в байтовом потоке
        workbook.save(output)
        output.seek(0)
        # excel_folder = r'C:\Users\1\Desktop\last'
        excel_filename = 'data.xlsx'
        excel_path = path.join(base_path, excel_filename)

        # Создание папки, если она не существует
        makedirs(base_path, exist_ok=True)

        with open(excel_path, 'wb') as f:
            f.write(output.read())
        # Отправка файла клиенту
        send_file(
            io.BytesIO(output.read()),
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name='data.xlsx'  # Задайте имя файла через заголовок Content-Disposition
        )
        return 'Good'


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
