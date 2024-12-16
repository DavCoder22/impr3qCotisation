from flask import Flask, request, jsonify
from flask_cors import CORS
from valores import cotizar

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir solicitudes desde cualquier origen

@app.route('/cotizar', methods=['POST', 'OPTIONS'])
def cotizar_endpoint():
    if request.method == 'OPTIONS':
        return jsonify({"message": "CORS preflight"}), 200

    data = request.json
    try:
        factura = cotizar(
            data['volumen'],
            data['peso'],
            data['tiempo'],
            data['tipo_filamento'],
            data['acabados'],
            data['envio'],
            data['duracion_pintado'],
            data['tipo_acabado'],
            data['numero_colores'],
            data['dificultad_acceso']
        )
        return jsonify(factura)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
