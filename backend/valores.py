from config import COSTOS_FILAMENTO, COSTO_POR_HORA, COSTO_ACABADOS, PORCENTAJE_GANANCIA, PORCENTAJE_IMPUESTO

def cotizar(volumen, peso, tiempo, tipo_filamento, acabados, envio):
    # Convertir el peso a entero
    peso = int(peso)

    # Validar que el tipo de filamento sea válido
    if tipo_filamento not in COSTOS_FILAMENTO:
        raise ValueError(f"Tipo de filamento no válido: {tipo_filamento}")

    # Calcular costo de material
    costo_filamento_kg = COSTOS_FILAMENTO[tipo_filamento]
    precio_filamento_gramo = costo_filamento_kg / 1000  # Precio por gramo
    costo_material = (peso / 1000) * costo_filamento_kg

    # Calcular costo de impresión
    costo_impresion = tiempo * COSTO_POR_HORA

    # Calcular costo de acabados
    costo_terminados = COSTO_ACABADOS if acabados else 0

    # Subtotal
    subtotal = costo_material + costo_impresion + costo_terminados

    # Ganancia
    ganancia = subtotal * (PORCENTAJE_GANANCIA / 100)

    # Impuesto
    impuesto = (subtotal + ganancia) * (PORCENTAJE_IMPUESTO / 100)

    # Total final
    total = subtotal + ganancia + impuesto + envio

    return {
        "volumen_total": volumen,
        "peso_material": peso,
        "tiempo_impresion": tiempo,
        "costo_material": round(costo_material, 2),
        "costo_impresion": round(costo_impresion, 2),
        "costo_terminados": round(costo_terminados, 2),
        "subtotal": round(subtotal, 2),
        "ganancia": round(ganancia, 2),
        "impuesto": round(impuesto, 2),
        "costo_envio": round(envio, 2),
        "total_final": round(total, 2),
        "precio_filamento_gramo": round(precio_filamento_gramo, 2)  # Añadir este campo
    }
