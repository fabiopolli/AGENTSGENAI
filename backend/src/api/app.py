from flask import Flask, jsonify
from flask_cors import CORS
from src.api.routes import bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Permitir acesso via frontend

app.register_blueprint(bp)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
