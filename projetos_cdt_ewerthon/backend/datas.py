from datetime import date

# ================================
# INVENTÁRIO DE CARROS (POR GRUPO)
# ================================

CARROS_INDIVIDUAIS = [
    # ===== GRUPO CE - Econômico Especial =====
    {"carro_id": 1, "modelo": "Fiat Argo 1.0", "categoria_id": "CE", "agencia_id": "SP_A"},
    {"carro_id": 2, "modelo": "VW Polo 1.0", "categoria_id": "CE", "agencia_id": "RJ_C"},

    # ===== GRUPO FX - Intermediário Automático =====
    {"carro_id": 3, "modelo": "Fiat Cronos 1.3 AT", "categoria_id": "FX", "agencia_id": "SP_A"},
    {"carro_id": 4, "modelo": "Onix Plus 1.0 Turbo AT", "categoria_id": "FX", "agencia_id": "RJ_C"},

    # ===== GRUPO B - Compacto =====
    {"carro_id": 5, "modelo": "Renault Kwid 1.0", "categoria_id": "B", "agencia_id": "RJ_C"},

    # ===== GRUPO CS - Econômico Sedan =====
    {"carro_id": 6, "modelo": "Onix Sedan 1.0", "categoria_id": "CS", "agencia_id": "RJ_C"},

    # ===== GRUPO NX - Pick-up =====
    {"carro_id": 7, "modelo": "Fiat Toro 1.3 Turbo", "categoria_id": "NX", "agencia_id": "SP_A"},

    # ===== GRUPO GX - SUV Automático =====
    {"carro_id": 8, "modelo": "Jeep Renegade 1.3", "categoria_id": "GX", "agencia_id": "RJ_C"},

    # ===== GRUPO GC - SUV Compacto =====
    {"carro_id": 9, "modelo": "VW Tera 1.0 AT", "categoria_id": "GC", "agencia_id": "SP_A"},

    # ===== GRUPO LE - SUV Especial =====
    {"carro_id": 10, "modelo": "Jeep Compass 1.3 Turbo", "categoria_id": "LE", "agencia_id": "SP_A"},

    # ===== GRUPO RX - Minivan =====
    {"carro_id": 11, "modelo": "GM Spin 1.8 (7 lugares)", "categoria_id": "RX", "agencia_id": "SP_A"},

    # ===== GRUPO U - Furgão =====
    {"carro_id": 12, "modelo": "Fiat Fiorino 1.4", "categoria_id": "U", "agencia_id": "SP_A"},
]



# Estrutura de Dados 1: Inventário de Veículos
VEICULOS_INVENTARIO = [
    {"categoria_id": "CE", "nome": "Econômico Especial", "tarifa_diaria": 85},
    {"categoria_id": "B",  "nome": "Compacto",            "tarifa_diaria": 75},
    {"categoria_id": "CS", "nome": "Econômico Sedan",     "tarifa_diaria": 95},
    {"categoria_id": "F",  "nome": "Intermediário",       "tarifa_diaria": 110},
    {"categoria_id": "FX", "nome": "Intermediário Auto",  "tarifa_diaria": 140},
    {"categoria_id": "GX", "nome": "SUV Automático",      "tarifa_diaria": 160},
    {"categoria_id": "GC", "nome": "SUV Compacto Auto",   "tarifa_diaria": 150},
    {"categoria_id": "LE", "nome": "SUV Especial",        "tarifa_diaria": 220},
    {"categoria_id": "NX", "nome": "Pick-up",             "tarifa_diaria": 210},
    {"categoria_id": "RX", "nome": "Minivan 7L",          "tarifa_diaria": 180},
    {"categoria_id": "U",  "nome": "Furgão",              "tarifa_diaria": 200},
]



# Estrutura de Dados 2: Agências da Localiza
AGENCIAS = [
    {
        "agencia_id": "SP_A",
        "nome": "São Paulo - Congonhas",
        "capacidade_total": 50
    },
    {
        "agencia_id": "RJ_C",
        "nome": "Rio de Janeiro - Copacabana",
        "capacidade_total": 30
    },
]

# Estrutura de Dados 3: Reservas Ativas (Simulação de Ocupação)
RESERVAS_ATIVAS = [
    {
        "carro_id": 1,
        "inicio": date(2025, 12, 15),
        "fim": date(2025, 12, 18)
    },
    {
        "carro_id": 4,
        "inicio": date(2025, 12, 12),
        "fim": date(2025, 12, 20)
    }
    # Adicione mais reservas aqui para simular diferentes taxas de ocupação
]