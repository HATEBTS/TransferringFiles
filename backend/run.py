from os import environ
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime
from main import main
from settings import BOOL_TRUE, BOOL_FALSE


load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire application

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
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


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
