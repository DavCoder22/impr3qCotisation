from flask import Flask, request, jsonify
from flask_cors import CORS
from valores import cotizar
import psycopg2

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir solicitudes desde cualquier origen

# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
    dbname="tu_base_de_datos",
    user="tu_usuario",
    password="tu_contraseña",
    host="tu_host",
    port="tu_puerto"
)

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
    except KeyError as e:
        return jsonify({"error": f"Campo faltante: {e}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pedidos")
            pedidos = cursor.fetchall()
        return jsonify(pedidos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pedidos/<int:pedido_id>', methods=['DELETE'])
def delete_pedido(pedido_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM pedidos WHERE id = %s", (pedido_id,))
            conn.commit()
        return jsonify({"message": "Pedido eliminado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pedidos/<int:pedido_id>', methods=['PUT'])
def update_pedido(pedido_id):
    data = request.json
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE pedidos SET volumen = %s, peso = %s, tiempo = %s, tipo_filamento = %s, acabados = %s, envio = %s, "
                "duracion_pintado = %s, tipo_acabado = %s, numero_colores = %s, dificultad_acceso = %s WHERE id = %s",
                (data['volumen'], data['peso'], data['tiempo'], data['tipo_filamento'], data['acabados'], data['envio'],
                 data['duracion_pintado'], data['tipo_acabado'], data['numero_colores'], data['dificultad_acceso'], pedido_id)
            )
            conn.commit()
        return jsonify({"message": "Pedido actualizado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
