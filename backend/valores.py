from flask import Flask, request, jsonify
from flask_cors import CORS
from config import (COSTOS_FILAMENTO, COSTO_POR_HORA, COSTO_ENERGIA_POR_HORA, COSTO_BOQUILLA,
                    COSTO_BOQUILLA_POR_HORA, COSTO_PINTADO_POR_HORA, COSTO_ACABADO_BRILLANTE, COSTO_ACABADO_TEXTURIZADO, COSTO_POR_COLOR,
                    FACTOR_COMPLEJIDAD_BAJO, FACTOR_COMPLEJIDAD_MEDIO, FACTOR_COMPLEJIDAD_ALTO, COSTO_RETOQUES, PORCENTAJE_GANANCIA, PORCENTAJE_IMPUESTO)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir solicitudes desde cualquier origen

def cotizar(volumen, peso, tiempo, tipo_filamento, acabados, envio, duracion_pintado, tipo_acabado, numero_colores, dificultad_acceso):
    # Convertir el peso a entero
    peso = int(peso)

    # Validar que el tipo de filamento sea válido
    if tipo_filamento not in COSTOS_FILAMENTO:
        raise ValueError(f"Tipo de filamento no válido: {tipo_filamento}")

    # Calcular costo de material
    costo_filamento_kg = COSTOS_FILAMENTO[tipo_filamento]
    costo_material = (peso / 1000) * costo_filamento_kg

    # Calcular IVA sobre el material
    iva_material = costo_material * (PORCENTAJE_IMPUESTO / 100)

    # Calcular costo de impresión
    costo_impresion = tiempo * COSTO_POR_HORA

    # Calcular costo de energía
    costo_energia = tiempo * COSTO_ENERGIA_POR_HORA

    # Calcular costo de boquillas
    costo_boquillas = tiempo * COSTO_BOQUILLA_POR_HORA

    # Calcular costo de pintado y acabados
    costo_pintado = 0
    if acabados == "true":
        costo_pintado = duracion_pintado * COSTO_PINTADO_POR_HORA
        if tipo_acabado == "brillante":
            costo_pintado += COSTO_ACABADO_BRILLANTE
        elif tipo_acabado == "texturizado":
            costo_pintado += COSTO_ACABADO_TEXTURIZADO
        costo_pintado += numero_colores * COSTO_POR_COLOR
        if dificultad_acceso == "bajo":
            costo_pintado *= FACTOR_COMPLEJIDAD_BAJO
        elif dificultad_acceso == "medio":
            costo_pintado *= FACTOR_COMPLEJIDAD_MEDIO
        elif dificultad_acceso == "alto":
            costo_pintado *= FACTOR_COMPLEJIDAD_ALTO
        costo_pintado += COSTO_RETOQUES

    # Subtotal
    subtotal = costo_material + costo_impresion + costo_energia + costo_boquillas + costo_pintado

    # Ganancia
    ganancia = subtotal * (PORCENTAJE_GANANCIA / 100)

    # Total final
    total = subtotal + ganancia + iva_material + envio

    return {
        "volumen_total": volumen,
        "peso_material": peso,
        "tiempo_impresion": tiempo,
        "costo_material": round(costo_material, 2),
        "iva_material": round(iva_material, 2),
        "costo_impresion": round(costo_impresion, 2),
        "costo_energia": round(costo_energia, 2),
        "costo_boquillas": round(costo_boquillas, 2),
        "costo_pintado": round(costo_pintado, 2),
        "subtotal": round(subtotal, 2),
        "ganancia": round(ganancia, 2),
        "costo_envio": round(envio, 2),
        "total_final": round(total, 2),
    }

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
            data.get('duracion_pintado', 0),
            data.get('tipo_acabado', 'mate'),
            data.get('numero_colores', 0),
            data.get('dificultad_acceso', 'bajo')
        )
        return jsonify(factura)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
