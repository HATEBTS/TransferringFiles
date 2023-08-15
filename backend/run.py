from os import environ, path
import re

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime

from psql_to_xls import psql_to_excel_load
from main import main
from settings import BOOL_TRUE, BOOL_FALSE
from base_disk_xls import svod
from copy__RD_akt import perenos_aktov, perenos_rd


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
    time_obed = db.Column(db.String(15), nullable=True)


class GoogleCipher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cipher = db.Column(db.String, nullable=False)


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

    data = request.get_json()
    forms = SubmitForm(date=data["date"], number_camera=data["numberCamera"],
                       number_object=data["numberObject"], selected_path=data["selectedPath"],
                       time_obed=data['timeObed'])
    print(forms)
    if request.method == "POST":
        if not data["date"] or not is_valid_date(data["date"]):
            is_data_commit(forms, BOOL_FALSE)
            return jsonify({'date': 'Некорректная дата или дата в будущем'}), 400

        if len(data["selectedPath"]) == 0:
            is_data_commit(forms, BOOL_FALSE)
            return jsonify({'selectedPath': 'Пустой путь'}), 400
    fart = main(data)

    if fart == "NoFile":
        is_data_commit(forms, BOOL_FALSE)
        return jsonify({'Napas_lavandos': 'Нет mp4 или jpg'}), 400
    if fart == "NoDateFile":
        is_data_commit(forms, BOOL_FALSE)
        return jsonify({'NoDateFile': 'Нет файлов подходящих по дате'}), 400
    if fart == "PlsZap":
        is_data_commit(forms, BOOL_FALSE)
        return jsonify({'PlsZap': 'При разделении необходимо указывать 2 шифра'}), 400
    if fart == "Netotsh":
        is_data_commit(forms, BOOL_FALSE)
        return jsonify({'Netotsh': 'Шифр не совпадает со звеном'}), 400
    if fart == "Lename":
        is_data_commit(forms, BOOL_FALSE)
        return jsonify({'Lename': 'Некорректный шифр'}), 400
    is_data_commit(forms, BOOL_TRUE)
    return jsonify({'message': 'Upload completed'})


@app.route('/download_excel')
def download_excel():
    if request.method == "GET":
        psql_to_excel_load()
        return 'Good'


@app.route('/base_disk')
def base_disk():
    if request.method == "GET":
        svod()
        return "Oppa"


@app.route('/copy_rd')
def copy_rd():
    if request.method == "GET":
        perenos_rd()
        return jsonify({'Ok': 200})

@app.route('/move_act')
def copy_akt():
    if request.method == "GET":
        perenos_aktov()
        return jsonify({'Ok': 200})


if __name__ == "__main__":
    app.run(debug=True)
