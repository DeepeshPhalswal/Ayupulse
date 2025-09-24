# server.py
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access variables
Port = os.getenv("PORT")

app = Flask(__name__)

@app.route('/process_health', methods=['POST'])
def process_health():
    try:
        data = request.json
        temp = data.get('temp')
        spo2 = data.get('spo2')
        ir = data.get('ir')

        # --- Simple example logic ---
        if spo2 < 50:
            condition = "Low Oxygen!"
        elif temp > 38:
            condition = "High Temp!"
        elif ir < 2000:
            condition = "Weak Pulse!"
        else:
            condition = "Normal"

        return jsonify({"condition": condition})
    except Exception as e:
        return jsonify({"condition": "Error", "details": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Port)
