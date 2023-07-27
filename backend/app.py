from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for the entire application


@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    print(data)
    print(data['numberCamera'])
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
