# config.py

# Costo de filamentos por kilogramo (incluidos impuestos locales)
COSTOS_FILAMENTO = {
    "pla": 25.0,     # Precio por kg de PLA
    "ptge": 27.0,    # Precio por kg de PTGE
    "tpu": 30.0,     # Precio por kg de TPU
    "abs": 32.0      # Precio por kg de ABS
}

# Configuración de impresión
COSTO_POR_HORA = 0.24  # Costo por hora de impresión
VELOCIDAD_IMPRESION_ESTANDAR = 50  # Velocidad estándar para cálculos iniciales en mm/s

# Configuración de acabados
COSTO_ACABADOS = 10.0  # Costo fijo por acabados

# Configuración de ganancias e impuestos
PORCENTAJE_GANANCIA = 35.0  # Porcentaje de ganancia sobre el subtotal
PORCENTAJE_IMPUESTO = 18.0  # Porcentaje de impuesto sobre el subtotal

# Configuración de envío
COSTO_ENVIO_UNIVERSIDAD = 0.0  # Sin costo para entregas en la universidad
