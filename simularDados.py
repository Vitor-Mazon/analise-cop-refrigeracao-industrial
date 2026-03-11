import numpy as np
import pandas as pd

def gerar_dados_fake(
    filename="dados_refrigeracao.csv",
    dias=7,
    freq_min=5,
    seed=42
):
    rng_toggle = np.random.default_rng(seed)

    n = int(dias * 24 * 60 / freq_min)
    tempo = pd.date_range("2026-01-01", periods=n, freq=f"{freq_min}min")

    # ---- Base "normal" do processo ----
    # Temperatura de entrada (°C): varia com carga térmica do processo
    T_in = 28 + 1.2*np.sin(np.linspace(0, 8*np.pi, n)) + R_toggle_normal(RNG=(RNG:=np.random.default_rng(seed)), n=n, scale=0.25)

    # DeltaT típico (entrada - saída): 3 a 6°C, com ruído
    dT = 4.5 + 0.8*np.sin(np.linspace(0, 4*np.pi, n) + 0.5) + RNG.normal(0, 0.25, n)
    dT = np.clip(dT, 1.5, 7.0)

    T_out = T_in - dT

    # Vazão volumétrica (m³/h): 60 a 120 dependendo do sistema; aqui simulando em torno de 90
    vazao_m3_h = 90 + 8*np.sin(np.linspace(0, 6*np.pi, n) - 0.7) + RNG.normal(0, 2.5, n)
    vazao_m3_h = np.clip(vazao_m3_h, 40, 130)

    # Potência elétrica total do CAG (kW): correlaciona com carga e com vazão/ΔT
    # (bem simplificado, só pra gerar dado coerente)
    P_kW = 140 + 15*(dT - 4.5) + 0.2*(vazao_m3_h - 90) + RNG.normal(0, 3.0, n)
    P_kW = np.clip(P_kW, 80, 220)

    # pressao_oleo_bar (bar): pressão de óleo; normal 2.0–3.5 (depende)
    pressao_oleo_bar = 2.8 + 0.15*np.sin(np.linspace(0, 10*np.pi, n)) + RNG.normal(0, 0.06, n)
    pressao_oleo_bar = np.clip(pressao_oleo_bar, 1.6, 3.6)

    # Nível do tanque (%): normal 40–80
    L = 60 + 8*np.sin(np.linspace(0, 2*np.pi, n) + 1.2) + RNG.normal(0, 1.5, n)
    L = np.clip(L, 20, 95)

    df = pd.DataFrame({
        "timestamp": tempo,
        "temp_entrada_c": np.round(T_in, 2),
        "temp_saida_c": np.round(T_out, 2),
        "vazao_m3_h": np.round(vazao_m3_h, 2),  # aqui em m³/h
        "potencia_kw": np.round(P_kW, 2),
        "pressao_oleo_bar": np.round(pressao_oleo_bar, 2),
        "nivel_tanque_pct": np.round(L, 1),
    })

    # ---- Injetar eventos (pioras) pra ter história pra contar ----
    # Evento 1: filtro entupindo / bomba perdendo eficiência -> vazão cai e COP piora
    idx1 = slice(int(n*0.25), int(n*0.30))
    df.loc[df.index[idx1], "vazao_m3_h"] *= 0.65
    df.loc[df.index[idx1], "potencia_kw"] *= 1.10  # esforço
    df.loc[df.index[idx1], "pressao_oleo_bar"] -= 0.25

    # Evento 2: problema de troca térmica / setpoint -> ΔT cai (resfriando menos)
    idx2 = slice(int(n*0.60), int(n*0.63))
    df.loc[df.index[idx2], "temp_saida_c"] += 1.5  # saída fica mais quente -> ΔT cai

    # Evento 3: nível do tanque baixo (cavitação/instabilidade)
    idx3 = slice(int(n*0.80), int(n*0.83))
    df.loc[df.index[idx3], "nivel_tanque_pct"] -= 25
    df.loc[df.index[idx3], "vazao_m3_h"] *= 0.85

    # Salvar
    df.to_csv(filename, index=False)
    return filename

def R_toggle_normal(RNG, n, scale=1.0):
    return RNG.normal(0, scale, n)

# Gere o arquivo
arquivo = gerar_dados_fake()
print("Gerado:", arquivo)
