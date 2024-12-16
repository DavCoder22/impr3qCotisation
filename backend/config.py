# config.py

# Costo de filamentos por kilogramo (incluidos impuestos locales)
COSTOS_FILAMENTO = {
    "pla": 25.0,     # Precio por kg de PLA
    "ptge": 27.0,    # Precio por kg de PTGE
    "tpu": 30.0,     # Precio por kg de TPU
    "abs": 32.0      # Precio por kg de ABS
}

# Configuración de impresión
COSTO_POR_HORA = 0.50  # Costo por hora de impresión
COSTO_ENERGIA_POR_HORA = 0.5  # Costo de energía por hora
COSTO_BOQUILLA = 2  # Costo por boquilla
COSTO_BOQUILLA_POR_HORA = 0.05  # Costo por hora de desgaste de boquilla

# Configuración de acabados
COSTO_PINTADO_POR_HORA = 3.50  # Costo por hora de pintado
COSTO_ACABADO_BRILLANTE = 3  # Costo adicional por acabado brillante
COSTO_ACABADO_TEXTURIZADO = 5  # Costo adicional por acabado texturizado
COSTO_POR_COLOR = 1  # Costo adicional por color
FACTOR_COMPLEJIDAD_BAJO = 1.0  # Factor de complejidad para dificultad baja
FACTOR_COMPLEJIDAD_MEDIO = 1.2  # Factor de complejidad para dificultad media
FACTOR_COMPLEJIDAD_ALTO = 1.5  # Factor de complejidad para dificultad alta
COSTO_RETOQUES = 5  # Costo adicional por retoques manuales

# Configuración de ganancias e impuestos
PORCENTAJE_GANANCIA = 20.0  # Porcentaje de ganancia sobre el subtotal
PORCENTAJE_IMPUESTO = 15.0  # Porcentaje de impuesto sobre el material
