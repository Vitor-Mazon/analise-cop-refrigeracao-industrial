# Fundamentos Físicos – Industrial Digital Twin

## Visão Geral

Este documento descreve os conceitos físicos e matemáticos utilizados no projeto para modelar o comportamento de um sistema de refrigeração industrial (chiller).

O foco está nas variáveis diretamente utilizadas no pipeline de dados e no cálculo do desempenho energético do sistema.

---

## Sistema Físico Modelado

O sistema simulado representa um chiller industrial, cujo objetivo é remover calor de um fluido (água ou mistura) por meio de um ciclo termodinâmico.

Os sensores simulados representam medições típicas de campo:

- Temperatura de entrada (°C)
- Temperatura de saída (°C)
- Vazão volumétrica (m³/h)
- Potência elétrica (kW)

A partir dessas variáveis, são calculadas grandezas físicas derivadas.

---

## 1. Diferença de Temperatura (ΔT)

A troca térmica depende da diferença de temperatura entre entrada e saída:

ΔT = T_entrada - T_saida

Interpretação:

- ΔT alto → maior remoção de calor
- ΔT baixo → menor eficiência térmica

---

## 2. Conversão de Vazão

A vazão fornecida pelo sensor é volumétrica:

vazao_m3_h → vazao_m3_s

vazao_m3_s = vazao_m3_h / 3600

---

## 3. Vazão Mássica (ṁ)

A transferência de calor depende da massa de fluido circulando:

ṁ = ρ × vazao_m3_s

Onde:

- ρ ≈ 1000 kg/m³ (água)

---

## 4. Transferência de Calor (Q̇)

Baseado na equação fundamental de calor sensível:

$$ \dot{Q} = \dot m \cdot c_p \cdot \Delta T $$

Onde:

- Q̇ → taxa de transferência de calor (kW)
- ṁ → vazão mássica (kg/s)
- c_p → calor específico da água (~4.18 kJ/kg·°C)
- ΔT → diferença de temperatura (°C)

Interpretação:

- Representa a energia térmica removida do sistema

---

## 5. Coefficient of Performance (COP)

O COP é o principal indicador de eficiência de sistemas de refrigeração:

$$COP = \frac{Q}{P}$$

Onde:

- Q → calor removido (kW)
- P → potência elétrica consumida (kW)

Interpretação:

- COP alto → sistema eficiente
- COP baixo → sistema ineficiente

Valores típicos:

- COP ≈ 3 a 5 → operação normal
- COP < 2 → possível anomalia

---

## 6. Validação Física dos Dados

Regras aplicadas no projeto:

### Temperatura
- T_saida deve ser menor que T_entrada

### Vazão
- Deve ser positiva e dentro de faixa operacional

### Potência
- Deve ser maior que zero

### COP
- Deve estar dentro de limites físicos plausíveis

Essas validações são implementadas na camada Silver através de flags de qualidade.

---

## 7. Relação com o Pipeline de Dados

As variáveis físicas são calculadas na camada Silver:

- dT → diferença de temperatura
- m_dot → vazão mássica
- qdot → transferência de calor
- COP → eficiência energética

Esses cálculos são utilizados posteriormente na camada Gold para:

- detecção de anomalias
- classificação de regime operacional
- geração de alertas

---

## Considerações Finais

O modelo físico utilizado é simplificado, porém consistente com princípios básicos de termodinâmica aplicada.

A abordagem permite:

- interpretar o comportamento do sistema
- detectar desvios operacionais
- conectar dados industriais a conceitos físicos reais

Esse alinhamento entre dados e física é essencial para projetos de Digital Twin.