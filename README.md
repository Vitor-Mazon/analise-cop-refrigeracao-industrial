# Industrial Digital Twin – Análise de Eficiência Energética (COP)

## Visão Geral

Este projeto implementa um pipeline de dados completo para análise de eficiência energética em sistemas de refrigeração industrial, utilizando o indicador **Coefficient of Performance (COP)**.

A solução segue uma arquitetura moderna **Lakehouse (Databricks)**, transformando dados operacionais brutos em insights analíticos para apoio à tomada de decisão.

Além disso, o projeto simula um **Digital Twin simplificado**, permitindo:

* monitorar o comportamento do sistema
* identificar padrões operacionais
* detectar eventos de degradação de desempenho

---

## Problema de Negócio

Sistemas de refrigeração industrial representam uma parcela relevante do consumo energético em plantas produtivas.

Pequenas variações operacionais podem gerar:

* aumento significativo de consumo
* perda de eficiência energética
* desgaste prematuro de equipamentos

O desafio é detectar esses desvios de forma **rápida, confiável e escalável**.

---

## Objetivos

* Monitorar a eficiência energética via COP
* Identificar regimes operacionais
* Detectar eventos de baixa performance
* Relacionar eficiência com variáveis de processo
* Construir um pipeline de dados estruturado e escalável

---

## Arquitetura de Dados

O projeto segue o modelo **Lakehouse**, dividido em três camadas:

* **Raw** → dados brutos simulados
* **Silver** → dados tratados e enriquecidos com lógica física
* **Gold** → dados analíticos prontos para consumo

Fluxo:

**Simulação → Raw → Silver → Gold → Análise**

📄 Detalhes: `docs/arquitetura.md`

---

## Pipeline Analítico

### Camada Silver (Engenharia de Dados)

* Cálculo de variáveis físicas:

  * ΔT (diferença de temperatura)
  * vazão mássica
  * carga térmica (q̇)
  * COP
* Validação física dos dados (remoção de inconsistências)

### Camada Gold (Camada Analítica)

* Classificação de regimes operacionais
* Identificação de alertas (baixa eficiência)
* Detecção de eventos anômalos
* Cálculo de métricas derivadas (ex: variabilidade do COP)

---

## Análise Exploratória

A análise foi conduzida a partir da camada **Silver**, considerando apenas dados fisicamente válidos.

Principais abordagens:

* Distribuição do COP
* Estatística descritiva
* Análise temporal
* Correlação com variáveis operacionais
* Identificação de eventos de degradação

---

## SQL – Consumo Analítico

O projeto inclui queries SQL para análise e monitoramento da camada Gold:

### Validação

* Distribuição por regime operacional
* Percentual de alertas
* Percentual de eventos anômalos

### Análise

* Estatísticas por regime
* Identificação de períodos críticos

### Monitoramento

* Evolução temporal do COP
* Volume de alertas operacionais

---

## Tecnologias Utilizadas

* Python (Pandas, Matplotlib)
* Databricks (Lakehouse)
* SQL
* Parquet
* GitHub

---

## Estrutura do Projeto

| Caminho                    | Descrição                   |
| -------------------------- | --------------------------- |
| notebooks/                 | Pipeline completo de dados  |
| ├── 01_dataset_generation  | Geração dos dados simulados |
| ├── 02_feature_engineering | Transformações (Silver)     |
| ├── 03_analysis_cop        | Análise exploratória        |
| └── 04_gold_layer          | Criação da camada analítica |
| src/                       | Scripts auxiliares          |
| sql/                       | Queries analíticas          |
| docs/                      | Documentação técnica        |
| data/                      | Referência das camadas      |
| README.md                  | Visão geral                 |

---

## Principais Resultados

* Operação predominantemente estável (COP ~3.2–3.4)
* Baixa eficiência associada à redução de vazão
* Variabilidade operacional impacta diretamente o desempenho
* Detecção antecipada de degradações antes de falhas críticas

---

## Reprodutibilidade

O projeto foi desenvolvido em ambiente **Databricks**, utilizando armazenamento em volumes.

Para execução local:

* adapte os paths para diretórios locais
* utilize os notebooks como referência do pipeline

Uma versão simplificada dos dados pode ser incluída para testes locais.

---

## Aplicação Prática

Este modelo pode ser aplicado em cenários reais para:

* Monitoramento contínuo de eficiência energética
* Detecção precoce de falhas
* Redução de consumo energético
* Apoio à decisão operacional

---

## Diferenciais

* Integração entre modelagem física e análise de dados
* Pipeline estruturado (engenharia + analytics)
* Arquitetura Lakehouse (Databricks)
* Simulação próxima de cenário industrial real
* Uso de SQL para consumo analítico

---

## Autor

**Vitor Mazon Rocha**

Analista de Processos | Física Computacional | Transição para Dados

LinkedIn: https://www.linkedin.com/in/vitor-mazon/
