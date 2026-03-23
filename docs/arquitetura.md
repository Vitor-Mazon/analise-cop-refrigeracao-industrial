# Arquitetura de Dados – Industrial Digital Twin

## Visão Geral

Este projeto implementa um pipeline de dados inspirado em arquiteturas modernas de Lakehouse para simular, processar e analisar o desempenho de um sistema de refrigeração industrial.

O objetivo é transformar dados operacionais brutos em informações estruturadas e confiáveis, capazes de apoiar a tomada de decisão em ambiente industrial.

A arquitetura foi organizada em camadas (Raw, Silver e Gold), separando claramente as responsabilidades de ingestão, tratamento e consumo dos dados.

---

## Fluxo de Dados

O pipeline segue o fluxo:

Simulação → Raw → Silver → Gold → Análise

Cada etapa adiciona valor ao dado, evoluindo de registros brutos para indicadores operacionais.

A execução do pipeline é realizada via notebooks no Databricks, permitindo reprocessamento e rastreabilidade completa.

---

## Camadas de Dados

### 🟫 Raw – Dados Brutos

- Origem: dados sintéticos gerados pelo script `simularDados.py`
- Armazenamento: `/Volumes/analytics/digital_twin/data/raw`
- Formato: CSV

Características:

- Dados sem tratamento
- Representam leituras de sensores industriais
- Podem conter inconsistências físicas e operacionais

Objetivo:

- Garantir rastreabilidade total dos dados originais

---

### 🟪 Silver – Dados Tratados e Validados

- Origem: transformação dos dados da camada Raw
- Armazenamento: `/Volumes/analytics/digital_twin/data/silver`
- Formato: CSV

Processos aplicados:

#### 🔹 Padronização
- Conversão de tipos (timestamp)
- Ordenação temporal

#### 🔹 Validação física (regras de negócio)
- Temperaturas invertidas
- Vazão inválida
- Potência inconsistente
- COP fora de faixa operacional

#### 🔹 Engenharia de variáveis
- Delta T (dT)
- Vazão mássica (m_dot)
- Transferência térmica (qdot)
- Coefficient of Performance (COP)

#### 🔹 Controle de qualidade
- `flag_temp_invertida`
- `flag_vazao_invalida`
- `flag_potencia_invalida`
- `flag_cop_invalido`
- `flag_invalido`

Objetivo:

- Garantir consistência física e confiabilidade dos dados

---

### 🟨 Gold – Dados para Consumo Analítico

- Origem: dados válidos da camada Silver
- Armazenamento: `/Volumes/analytics/digital_twin/data/gold`
- Formato: Parquet

Transformações aplicadas:

- Filtragem de dados inválidos (`flag_invalido = False`)
- Criação de indicadores operacionais

#### 🔹 Indicadores:
- `regime_operacao` (baixo, médio, alto)
- `status_alerta` (COP abaixo do limite)
- `evento_anomalo`

#### 🔹 Lógica de anomalia:
- baixa eficiência (COP reduzido)
- aumento de variabilidade
- redução de vazão

Estrutura final:

- Dataset enxuto
- Foco em interpretação operacional
- Pronto para consumo via SQL, dashboards ou monitoramento

Objetivo:

- Disponibilizar dados prontos para tomada de decisão

---

## Governança e Qualidade de Dados

A qualidade dos dados é tratada principalmente na camada Silver.

A utilização de flags permite:

- Rastreabilidade de inconsistências
- Separação entre dados válidos e inválidos
- Auditoria e reprocessamento

Na camada Gold, apenas dados confiáveis são utilizados, garantindo consistência analítica.

---

## Ambiente e Tecnologias

- Databricks
- Python (Pandas, Matplotlib)
- SQL
- Parquet
- Lakehouse Architecture
- Volumes (`CREATE VOLUME`)

Benefícios:

- Escalabilidade
- Reprodutibilidade
- Organização de dados em camadas

---

## Considerações Finais

A arquitetura proposta segue práticas utilizadas em ambientes industriais modernos, permitindo controle sobre qualidade, rastreabilidade e consumo dos dados.

Embora os dados sejam simulados, a estrutura foi projetada para fácil adaptação a cenários reais, como integração com sistemas SCADA ou historiadores industriais.

O resultado é um pipeline simples, porém robusto, capaz de transformar dados operacionais em insights acionáveis.