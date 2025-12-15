from datetime import date
from datetime import datetime
from datas import (
    AGENCIAS,
    VEICULOS_INVENTARIO,
    CARROS_INDIVIDUAIS,
    RESERVAS_ATIVAS
)

# =========================
# UTILIDADES
# =========================

def datas_conflitam(inicio1, fim1, inicio2, fim2):
    return inicio1 <= fim2 and inicio2 <= fim1


def calcular_diarias(data_retirada, data_devolucao):
    # +1 para contar o dia da retirada
    dias = (data_devolucao - data_retirada).days + 1
    return max(1, dias)


def validar_datas(retirada, devolucao):
    if not isinstance(retirada, date) or not isinstance(devolucao, date):
        return "Datas inválidas"

    hoje = date.today()

    if retirada < hoje:
        return "A data de retirada não pode ser anterior a hoje."

    if devolucao <= retirada:
        return "A data de devolução deve ser posterior à retirada."

    return True


# =========================
# DISPONIBILIDADE
# =========================

def verificar_disponibilidade(grupo, agencia, data_inicio, data_fim):
    resultado = []

    for carro in CARROS_INDIVIDUAIS:
        if carro["categoria_id"] != grupo or carro["agencia_id"] != agencia:
            continue

        disponivel = True

        for reserva in RESERVAS_ATIVAS:
            if reserva["carro_id"] == carro["carro_id"]:
                if datas_conflitam(
                    data_inicio,
                    data_fim,
                    reserva["inicio"],
                    reserva["fim"]
                ):
                    disponivel = False
                    break

        resultado.append({
            "carro_id": carro["carro_id"],
            "modelo": carro["modelo"],
            "disponivel": disponivel
        })

    return resultado


# =========================
# DEMANDA
# =========================

def calcular_fator_demanda(agencia_id):
    capacidade_total = next(
        (a["capacidade_total"] for a in AGENCIAS if a["agencia_id"] == agencia_id),
        1
    )

    reservas_na_agencia = 0

    for reserva in RESERVAS_ATIVAS:
        carro = next(
            (c for c in CARROS_INDIVIDUAIS if c["carro_id"] == reserva["carro_id"]),
            None
        )

        if carro and carro["agencia_id"] == agencia_id:
            reservas_na_agencia += 1

    taxa = reservas_na_agencia / capacidade_total

    if taxa > 0.8:
        return 1.20, "Alta Demanda (+20%)"
    elif taxa > 0.6:
        return 1.10, "Média Demanda (+10%)"
    else:
        return 1.00, "Demanda Normal"


# =========================
# SIMULAÇÃO FINAL
# =========================

def simular_preco_final(parametros):
    categoria_id = parametros.get("categoria_id")
    agencia_id = parametros.get("agencia_id")

    data_retirada_str = parametros.get("data_retirada")
    data_devolucao_str = parametros.get("data_devolucao")

    if not categoria_id or not agencia_id or not data_retirada_str or not data_devolucao_str:
        return {"erro": "Parâmetros incompletos."}

    try:
        data_retirada = datetime.strptime(data_retirada_str, "%Y-%m-%d").date()
        data_devolucao = datetime.strptime(data_devolucao_str, "%Y-%m-%d").date()
    except Exception:
        return {"erro": "Formato de data inválido. Use AAAA-MM-DD."}

    validacao = validar_datas(data_retirada, data_devolucao)
    if validacao is not True:
        return {"erro": validacao}

    validacao = validar_datas(data_retirada, data_devolucao)
    if validacao is not True:
        return {"erro": validacao}

    categoria = next(
        (v for v in VEICULOS_INVENTARIO if v["categoria_id"] == categoria_id),
        None
    )

    if not categoria:
        return {"erro": "Categoria não encontrada."}

    tarifa_diaria = categoria["tarifa_diaria"]
    diarias = calcular_diarias(data_retirada, data_devolucao)

    preco_bruto = tarifa_diaria * diarias
    preco_final = preco_bruto
    fatores = []

    fator_demanda, desc_demanda = calcular_fator_demanda(agencia_id)
    preco_final *= fator_demanda
    if fator_demanda > 1:
        fatores.append(desc_demanda)

    if diarias >= 7:
        preco_final *= 0.85
        fatores.append("Desconto Longa Duração (-15%)")

    dias_antecedencia = (data_retirada - date.today()).days
    if dias_antecedencia >= 30:
        preco_final *= 0.95
        fatores.append("Desconto Reserva Antecipada (-5%)")

    carros = verificar_disponibilidade(
        categoria_id,
        agencia_id,
        data_retirada,
        data_devolucao
    )

    return {
        "categoria": categoria["nome"],
        "tarifa_diaria": tarifa_diaria,
        "diarias": diarias,
        "preco_bruto": round(preco_bruto, 2),
        "preco_final": round(preco_final, 2),
        "fatores_aplicados": fatores,
        "carros": carros
    }
