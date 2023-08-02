from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime
from main import main
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire application

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12qwasZX@localhost:5432/staticakt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class SubmitForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    number_camera = db.Column(db.String(50), nullable=False)
    number_object = db.Column(db.String(15), nullable=False)
    selected_path = db.Column(db.String(100), nullable=False)


def is_valid_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return date <= datetime.today()
    except ValueError:
        return False


@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    # submit_table = db.session.execute(db.select(SubmitForm))

    data = request.get_json()
    if request.method == "POST":
        if not data["date"] or not is_valid_date(data["date"]):
            return jsonify({'date': 'Некорректная дата или дата в будущем'}), 400
        if len(data["selectedPath"]) == 0:
            print(355)
            return jsonify({'selectedPath': 'Пустой путь'}), 400

    forms = SubmitForm(date=data["date"], number_camera=data["numberCamera"],
                       number_object=data["numberObject"], selected_path=data["selectedPath"])
    db.session.add(forms)
    db.session.commit()


    print(main(data))
    return jsonify(data)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
