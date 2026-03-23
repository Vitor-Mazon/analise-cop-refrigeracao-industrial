# Industrial Digital Twin – Análise de Eficiência Energética (COP)

## Visão Geral

Este projeto implementa um pipeline de dados completo para análise de eficiência energética em sistemas de refrigeração industrial, utilizando o indicador **Coefficient of Performance (COP)**.

A solução segue uma arquitetura moderna de dados (Lakehouse), transformando dados operacionais brutos em indicadores analíticos capazes de apoiar a tomada de decisão em ambientes industriais.

O projeto simula um **Digital Twin simplificado**, permitindo analisar o comportamento do sistema, identificar padrões operacionais e detectar eventos de degradação de desempenho.

---

## Problema de Negócio

Sistemas de refrigeração industrial representam uma parcela significativa do consumo energético em plantas produtivas.

Pequenas variações operacionais podem gerar:
- aumento de consumo energético
- perda de eficiência
- desgaste prematuro de equipamentos

O desafio é identificar esses desvios de forma rápida e confiável.

---

## Objetivos

- Monitorar a eficiência energética do sistema (COP)
- Identificar padrões e regimes operacionais
- Detectar eventos de baixa performance
- Relacionar eficiência com variáveis de processo
- Estruturar um pipeline de dados escalável

---

## Arquitetura de Dados

O projeto segue o modelo **Lakehouse**, dividido em três camadas:

- **Raw** → dados brutos simulados  
- **Silver** → dados tratados e enriquecidos com lógica física  
- **Gold** → dados analíticos prontos para consumo  

Fluxo:

**Simulação → Raw → Silver → Gold → Análise**


📄 Detalhes: `docs/arquitetura.md`

---

## Pipeline Analítico

### Camada Silver
- Cálculo de variáveis físicas:
  - ΔT (diferença de temperatura)
  - vazão mássica
  - carga térmica (q̇)
  - COP
- Validação física dos dados

### Camada Gold
- Classificação de regimes operacionais
- Identificação de alertas (baixa eficiência)
- Detecção de eventos anômalos
- Cálculo de métricas derivadas (ex: variabilidade do COP)

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

## SQL – Camada Gold

O projeto inclui queries SQL para consumo analítico:

### Validação
- Distribuição por regime operacional
- Percentual de alertas
- Percentual de eventos anômalos

### Análise
- Estatísticas por regime
- Identificação dos períodos mais críticos

### Monitoramento
- Evolução diária do COP
- Volume de alertas operacionais

---

## Tecnologias Utilizadas

- Python (Pandas, Matplotlib)
- Databricks
- SQL
- Parquet
- Lakehouse Architecture
- GitHub

---

## Estrutura do Projeto

| Caminho | Tipo | Descrição |
|--------|------|----------|
| industrial-digital-twin/ | Diretório raiz | Estrutura principal do projeto |
| ├── notebooks/ | Pasta | Notebooks do pipeline de dados |
| │   ├── 01_dataset_generation | Notebook | Geração dos dados simulados |
| │   ├── 02_feature_engineering | Notebook | Tratamento e criação de variáveis (Silver) |
| │   ├── 03_analysis_cop | Notebook | Análise exploratória e eficiência energética |
| │   └── 04_gold_layer | Notebook | Criação da camada Gold |
| ├── src/ | Pasta | Código fonte auxiliar |
| │   └── simularDados.py | Script Python | Geração dos dados sintéticos |
| ├── sql/ | Pasta | Scripts SQL para consumo e validação |
| │   ├── create_gold_table.sql | SQL | Criação de tabela analítica |
| │   ├── gold_validation.sql | SQL | Validação dos dados Gold |
| │   └── gold_analysis.sql | SQL | Consultas analíticas |
| ├── docs/ | Pasta | Documentação do projeto |
| │   ├── arquitetura.md | Documento | Arquitetura de dados |
| │   └── dicionario.md | Documento | Dicionário de dados |
| ├── data/ | Pasta | Referência lógica das camadas de dados |
| └── README.md | Documento | Visão geral do projeto |

---

## Principais Resultados

- Sistema apresenta operação predominantemente estável (COP ~3.2–3.4)
- Eventos de baixa eficiência estão associados principalmente à redução de vazão
- A variabilidade operacional influencia diretamente o desempenho energético
- É possível detectar degradações antes de falhas críticas

---

## Aplicação Prática

Este modelo pode ser aplicado em ambientes industriais reais para:

- Monitoramento contínuo de eficiência energética
- Detecção precoce de falhas
- Redução de consumo energético
- Apoio à tomada de decisão operacional

---

## Diferenciais do Projeto

- Integração entre modelagem física e análise de dados
- Pipeline estruturado em camadas (engenharia de dados)
- Uso de arquitetura Lakehouse (Databricks)
- Abordagem próxima de cenários industriais reais
- SQL aplicado para consumo analítico

---

## Autor

**Vitor Mazon Rocha**

Analista de Processos com formação em Física Computacional, atuando na interseção entre dados, engenharia e operações industriais.

🔗 LinkedIn: https://www.linkedin.com/in/vitor-mazon/
