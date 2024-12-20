from flask import Flask, request, jsonify

app = Flask(__name__)

def meter_to_kilometer(meters):
    return meters / 1000

def kilometer_to_meter(kilometers):
    return kilometers * 1000

def meter_to_inches(meters):
    return meters * 39.3701

@app.route('/convert', methods=['POST'])
def convert_length():
    data = request.json
    value = data['value']
    from_unit = data['from_unit'].lower()
    to_unit = data['to_unit'].lower()

    try:
        if from_unit == "meter" and to_unit == "kilometer":
            result = meter_to_kilometer(value)
        elif from_unit == "kilometer" and to_unit == "meter":
            result = kilometer_to_meter(value)
        elif from_unit == "meter" and to_unit == "inch":
            result = meter_to_inches(value)
        else:
            return jsonify({"error": "Conversion not supported"}), 400

        return jsonify({"converted_value": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5002)
