from flask import Flask, request, jsonify

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

@app.route('/convert', methods=['POST'])
def convert_temperature():
    data = request.json
    value = data['value']
    from_unit = data['from_unit'].lower()
    to_unit = data['to_unit'].lower()

    try:
        if from_unit == "celsius" and to_unit == "fahrenheit":
            result = celsius_to_fahrenheit(value)
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            result = fahrenheit_to_celsius(value)
        elif from_unit == "celsius" and to_unit == "kelvin":
            result = celsius_to_kelvin(value)
        else:
            return jsonify({"error": "Conversion not supported"}), 400

        return jsonify({"converted_value": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)
