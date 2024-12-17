# config.py

# Costos de filamento por gramo
COSTOS_FILAMENTO = {
    "pla": 0.02,    # 2 centavos por gramo
    "ptge": 0.025,
    "abs": 0.03,
    "tpu": 0.035
}

# Costos por hora
COSTO_POR_HORA = 1.5  # Costo por hora de impresión
COSTO_ENERGIA_POR_HORA = 0.4  # Costo de energía por hora
COSTO_BOQUILLA_POR_HORA = 0.08  # Costo de boquilla por hora
COSTO_PINTADO_POR_HORA = 0.8  # Costo de pintado por hora

# Costos adicionales de acabados
COSTO_ACABADO_BRILLANTE = 4
COSTO_ACABADO_TEXTURIZADO = 8
COSTO_POR_COLOR = 1.5

# Factores de complejidad
FACTOR_COMPLEJIDAD_BAJO = 1
FACTOR_COMPLEJIDAD_MEDIO = 1.1
FACTOR_COMPLEJIDAD_ALTO = 1.2

# Costos de retoques
COSTO_RETOQUES = 4

# Porcentajes de ganancia e impuesto
PORCENTAJE_GANANCIA = 10
PORCENTAJE_IMPUESTO = 16
