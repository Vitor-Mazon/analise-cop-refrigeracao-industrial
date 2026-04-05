import numpy as np
import pandas as pd
from pathlib import Path


def gerar_dados_fake(
    filename="dados_refrigeracao.csv",
    dias=7,
    freq_min=5,
    seed=42,
    output_dir="/Volumes/analytics/digital_twin/data/raw"
):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    filepath = Path(output_dir) / filename

    rng = np.random.default_rng(seed)

    # Número de amostras
    n = int(dias * 24 * 60 / freq_min)
    tempo = pd.date_range("2026-01-01", periods=n, freq=f"{freq_min}min")

    # ============================================================
    # 1) VARIÁVEIS INTERNAS (não exportadas)
    # ============================================================

    # Temperatura ambiente (latente): afeta eficiência do chiller
    temp_ambiente_c = 30 + 3.0 * np.sin(np.linspace(0, 2 * np.pi, n) - 0.8)
    temp_ambiente_c += rng.normal(0, 0.4, n)

    # Carga térmica do processo (latente): representa a demanda de refrigeração
    carga_processo = 1.00 + 0.10 * np.sin(np.linspace(0, 8 * np.pi, n))
    carga_processo += rng.normal(0, 0.02, n)
    carga_processo = np.clip(carga_processo, 0.75, 1.20)

    # Fatores internos de degradação
    fator_hidraulico = np.ones(n)
    fator_troca_termica = np.ones(n)
    fator_eficiencia_global = np.ones(n)

    # ============================================================
    # 2) EVENTOS ANÔMALOS
    # ============================================================

    # Evento 1: filtro entupindo / bomba perdendo eficiência
    idx1 = slice(int(n * 0.25), int(n * 0.30))
    fator_hidraulico[idx1] *= 0.65
    fator_eficiencia_global[idx1] *= 0.90

    # Evento 2: problema de troca térmica / fouling / setpoint ruim
    idx2 = slice(int(n * 0.60), int(n * 0.63))
    fator_troca_termica[idx2] *= 0.72
    fator_eficiencia_global[idx2] *= 0.85

    # Evento 3: nível baixo do tanque / instabilidade hidráulica
    idx3 = slice(int(n * 0.80), int(n * 0.83))
    fator_hidraulico[idx3] *= 0.85

    # ============================================================
    # 3) VAZÃO (sensor observável)
    # ============================================================

    vazao_base_m3_h = 90 + 6 * np.sin(np.linspace(0, 6 * np.pi, n) - 0.5)
    vazao_base_m3_h += rng.normal(0, 1.8, n)

    vazao_m3_h = vazao_base_m3_h * fator_hidraulico
    vazao_m3_h = np.clip(vazao_m3_h, 40, 130)

    # ============================================================
    # 4) TEMPERATURA DE ENTRADA (sensor observável)
    #    Com inércia térmica para parecer processo real
    # ============================================================

    T_in_target = 29 + 1.1 * np.sin(np.linspace(0, 8 * np.pi, n))
    T_in_target += 1.8 * (carga_processo - 1.0)

    T_in = np.zeros(n)
    T_in[0] = T_in_target[0]

    for i in range(1, n):
        T_in[i] = (
            0.94 * T_in[i - 1]
            + 0.06 * T_in_target[i]
            + rng.normal(0, 0.05)
        )

    # ============================================================
    # 5) DELTA T INTERNO -> gera temperatura de saída observável
    # ============================================================

    dT_nominal = 4.5 + 0.5 * (carga_processo - 1.0) / 0.10
    dT_nominal += 0.25 * np.sin(np.linspace(0, 4 * np.pi, n) + 0.3)
    dT_nominal += rng.normal(0, 0.10, n)

    # DeltaT real depende da troca térmica e um pouco da condição hidráulica
    dT_real = dT_nominal * fator_troca_termica * (0.96 + 0.04 * fator_hidraulico)
    dT_real = np.clip(dT_real, 1.5, 7.0)

    T_out = T_in - dT_real

    # ============================================================
    # 6) POTÊNCIA (sensor observável)
    #    Calculada internamente com base em física simplificada
    # ============================================================

    # Conversão para cálculo interno da capacidade térmica
    rho = 1000.0      # kg/m³
    cp = 4.186        # kJ/kg.K

    vazao_m3_s = vazao_m3_h / 3600.0
    vazao_kg_s = rho * vazao_m3_s

    capacidade_kw_interna = vazao_kg_s * cp * dT_real

    # COP interno depende de ambiente, carga e degradação
    cop_interno = 3.9 - 0.045 * (temp_ambiente_c - 30)
    cop_interno += 0.08 * (carga_processo - 1.0) / 0.10
    cop_interno *= fator_eficiencia_global
    cop_interno += rng.normal(0, 0.05, n)
    cop_interno = np.clip(cop_interno, 2.2, 4.8)

    P_kW = capacidade_kw_interna / cop_interno
    P_kW += rng.normal(0, 1.5, n)
    P_kW = np.clip(P_kW, 80, 220)

    # ============================================================
    # 7) PRESSÃO DE ÓLEO (sensor observável)
    # ============================================================

    pressao_oleo_bar = 2.85 - 0.003 * (P_kW - 140)
    pressao_oleo_bar += 0.08 * np.sin(np.linspace(0, 10 * np.pi, n))
    pressao_oleo_bar += rng.normal(0, 0.04, n)

    # Evento 1 força uma pequena queda extra
    pressao_oleo_bar[idx1] -= 0.18

    pressao_oleo_bar = np.clip(pressao_oleo_bar, 1.6, 3.6)

    # ============================================================
    # 8) NÍVEL DO TANQUE (sensor observável)
    # ============================================================

    nivel_tanque_pct = 60 + 7 * np.sin(np.linspace(0, 2 * np.pi, n) + 1.2)
    nivel_tanque_pct += rng.normal(0, 1.2, n)

    # Evento 3: nível baixo
    nivel_tanque_pct[idx3] -= 25

    nivel_tanque_pct = np.clip(nivel_tanque_pct, 20, 95)

    # ============================================================
    # 9) SAÍDA FINAL - SOMENTE DADOS DE SENSOR
    # ============================================================

    df = pd.DataFrame({
        "timestamp": tempo,
        "temp_entrada_c": np.round(T_in, 2),
        "temp_saida_c": np.round(T_out, 2),
        "vazao_m3_h": np.round(vazao_m3_h, 2),
        "potencia_kw": np.round(P_kW, 2),
        "pressao_oleo_bar": np.round(pressao_oleo_bar, 2),
        "nivel_tanque_pct": np.round(nivel_tanque_pct, 1),
    })

    df.to_csv(filepath, index=False)
    return filepath