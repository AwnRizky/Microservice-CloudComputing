from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SERVICES = {
    "temperature": "http://localhost:5001",
    "length": "http://localhost:5002"
}

@app.route('/converter/convert-temperature', methods=['POST'])
def convert_temperature():
    data = request.json
    try:
        if 'value' not in data or 'from_unit' not in data or 'to_unit' not in data:
            return jsonify({"error": "Invalid request data"}), 400

        response = requests.post(f"{SERVICES['temperature']}/convert", json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/converter/convert-length', methods=['POST'])
def convert_length():
    data = request.json
    try:
        if 'value' not in data or 'from_unit' not in data or 'to_unit' not in data:
            return jsonify({"error": "Invalid request data"}), 400

        response = requests.post(f"{SERVICES['length']}/convert", json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
