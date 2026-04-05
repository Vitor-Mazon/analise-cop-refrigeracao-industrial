# Industrial Digital Twin – Análise de Eficiência Energética (COP)

## Visão Geral

Este projeto implementa um pipeline de dados completo para análise de eficiência energética em sistemas de refrigeração industrial, utilizando o indicador **Coefficient of Performance (COP)**.

A solução segue uma arquitetura moderna **Lakehouse (Databricks)**, transformando dados operacionais brutos em informações estruturadas e insights analíticos para apoio à tomada de decisão.

O projeto simula um **Digital Twin simplificado**, permitindo:

- monitorar o comportamento do sistema
- identificar padrões operacionais
- detectar eventos de degradação de desempenho

---

## Problema de Negócio

Sistemas de refrigeração industrial representam uma parcela significativa do consumo energético em plantas produtivas.

Pequenas variações operacionais podem gerar:

- aumento de consumo energético  
- perda de eficiência  
- desgaste prematuro de equipamentos  

O desafio é identificar esses desvios de forma **rápida, confiável e escalável**.

---

## Objetivos

- Monitorar a eficiência energética via COP  
- Identificar regimes operacionais  
- Detectar eventos de baixa performance  
- Relacionar eficiência com variáveis de processo  
- Estruturar um pipeline de dados escalável  

---

## Arquitetura de Dados

O projeto segue o modelo **Lakehouse**, dividido em três camadas:

- **Raw** → dados brutos simulados  
- **Silver** → dados tratados, validados e enriquecidos com lógica física  
- **Gold** → dados analíticos prontos para consumo  

Fluxo:

**Simulação → Raw → Silver → Gold → Análise**

Detalhes: [`docs/arquitetura.md`](docs/arquitetura.md)

---

## Pipeline Analítico

### Camada Silver (Engenharia de Dados)

- Cálculo de variáveis físicas:
  - ΔT (diferença de temperatura)
  - vazão mássica
  - carga térmica (q̇)
  - COP  
- Validação física dos dados (controle de qualidade)

Fundamentos físicos: [`docs/fisica.md`](docs/fisica.md)

---

### Camada Gold (Camada Analítica)

- Classificação de regimes operacionais  
- Identificação de alertas (baixa eficiência)  
- Detecção de eventos anômalos  
- Cálculo de métricas derivadas (ex: variabilidade do COP)

Dicionário de dados: [`docs/dicionario.md`](docs/dicionario.md)

---

## Análise Exploratória

A análise foi conduzida a partir da camada **Silver**, considerando apenas dados fisicamente válidos.

Principais abordagens:

- Distribuição do COP  
- Estatística descritiva  
- Análise temporal  
- Correlação com variáveis operacionais  
- Identificação de eventos de degradação  

---

## SQL – Consumo Analítico

A camada Gold é consumida via SQL para análise e monitoramento:

### Validação
- Distribuição por regime operacional  
- Percentual de alertas  
- Percentual de eventos anômalos  

### Análise
- Estatísticas por regime  
- Identificação de períodos críticos  

### Monitoramento
- Evolução temporal do COP  
- Volume de alertas operacionais  

---

## Tecnologias Utilizadas

- Python (Pandas, Matplotlib)  
- Databricks (Lakehouse)  
- SQL  
- Parquet  
- GitHub  

---

## Estrutura do Projeto

| Caminho                    | Descrição                         |
|--------------------------|----------------------------------|
| notebooks/               | Pipeline completo de dados        |
| ├── [01_dataset_generation](notebooks/01_dataset_generation) | Geração dos dados simulados       |
| ├── [02_feature_engineering](notebooks/02_feature_engineering) | Transformações (Silver)           |
| ├── [03_analysis_cop](notebooks/03_analysis_cop)      | Análise exploratória              |
| └── [04_gold_layer](notebooks/04_gold_layer)        | Criação da camada analítica       |
| [src/](src)                     | Scripts auxiliares                |
| [sql/](sql)                     | Queries analíticas                |
| [docs/](docs)                    | Documentação técnica              |
| [data/](data)                    | Referência das camadas            |
| README.md                | Visão geral do projeto            |

---

## Principais Resultados

- Operação predominantemente estável (COP ~3.2–3.4)  
- Quedas de eficiência associadas principalmente à redução de vazão  
- Variabilidade operacional impacta diretamente o desempenho  
- Possibilidade de detectar degradações antes de falhas críticas  

---

## Aplicação Prática

A abordagem pode ser aplicada em ambientes industriais reais para:

- Monitoramento contínuo de eficiência energética  
- Detecção precoce de falhas operacionais  
- Redução de consumo energético  
- Apoio à tomada de decisão  

---

## Diferenciais do Projeto

- Integração entre modelagem física e análise de dados  
- Pipeline estruturado (engenharia + analytics)  
- Arquitetura Lakehouse (Databricks)  
- Uso de SQL para consumo analítico  
- Estrutura compatível com cenários industriais reais  

---

## Autor

**Vitor Mazon Rocha**

Analista de Processos | Física Computacional | Transição para Dados  

🔗 LinkedIn: https://www.linkedin.com/in/vitor-mazon/