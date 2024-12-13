from flask import Flask, request, jsonify
from flask_cors import CORS
from valores import cotizar

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir solicitudes desde cualquier origen

@app.route('/cotizar', methods=['POST'])
def cotizar_endpoint():
    data = request.json
    factura = cotizar(
        data['volumen'],
        data['peso'],
        data['tiempo'],
        data['tipo_filamento'],
        data['acabados'],
        data['envio']
    )
    return jsonify(factura)

if __name__ == "__main__":
    app.run(debug=True)
