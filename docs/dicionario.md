# Dicionário de Dados – Industrial Digital Twin

## Visão Geral

Este documento descreve as variáveis utilizadas no projeto, incluindo significado físico, unidade de medida e observações operacionais.

---

## Variáveis Originais (Raw)

| Variável | Descrição | Unidade |
|--------|----------|--------|
| timestamp | Data e hora da medição | datetime |
| temp_entrada_c | Temperatura da água na entrada | °C |
| temp_saida_c | Temperatura da água na saída | °C |
| vazao_m3_h | Vazão volumétrica de água | m³/h |
| potencia_kw | Potência elétrica consumida | kW |
| pressao_oleo_bar | Pressão do óleo do sistema | bar |
| nivel_tanque_pct | Nível do tanque | % |

---

## Variáveis Derivadas (Silver)

| Variável | Descrição | Unidade |
|--------|----------|--------|
| dT_c | Diferença de temperatura (entrada - saída) | °C |
| vazao_m3_s | Vazão convertida para m³/s | m³/s |
| m_dot_kg_s | Vazão mássica | kg/s |
| qdot_kw | Transferência térmica | kW |
| cop | Coefficient of Performance (eficiência) | adimensional |

---

## Flags de Qualidade

| Variável | Descrição |
|--------|----------|
| flag_temp_invertida | Indica temperatura de saída menor que entrada |
| flag_vazao_invalida | Vazão fora do intervalo esperado |
| flag_potencia_invalida | Potência inconsistente |
| flag_cop_invalido | COP fora do intervalo físico |
| flag_invalido | Indica registro inválido geral |

---

## Variáveis Analíticas (Gold)

| Variável | Descrição |
|--------|----------|
| regime_operacao | Classificação do regime (baixo, médio, alto) |
| status_alerta | Indica operação com baixa eficiência |
| evento_anomalo | Identificação de comportamento fora do padrão |

---

## Observações

- Apenas dados com `flag_invalido = False` são utilizados na camada Gold
- O COP é o principal indicador de desempenho energético
- Variáveis derivadas são baseadas em princípios de balanço de energia

---

## Uso Recomendado

- **Silver** → análises técnicas e engenharia
- **Gold** → dashboards, relatórios e tomada de decisão