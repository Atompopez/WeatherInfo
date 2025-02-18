from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import requests

app = Flask(__name__)
CORS(app)

API_KEY = 'fcee588c0ba260fb88028e46118d1161'

@app.route('/api/getData', methods=['GET'])
def get_data():
    locations = request.args.get('location')

    if locations:
        ciudades= locations.split(',')

        result = []

        for ciudad in ciudades: 

            url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad.strip()}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code == 200: 
                data = response.json()
                clima = {
                    "ciudad": data['name'],
                    "temperatura": data['main']['temp'],
                    "humedad": data['main']['humidity']
                }
                result.append(clima)
            else:
                result.append({"ciudad": ciudad, "message": "No se encontro la ciudad"})

        return jsonify(result), 200
    else:
        return jsonify({"message": "Falta el parametro location"}), 400

if __name__ == '__main__':
    app.run(debug=True)
