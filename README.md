# Análise de Eficiência Energética (COP) em Sistema de Refrigeração Industrial

## Contexto

Sistemas de refrigeração industrial possuem impacto direto no consumo energético e nos custos operacionais de plantas produtivas. A eficiência desses sistemas pode ser avaliada por meio do Coefficient of Performance (COP), indicador que relaciona a capacidade de remoção de calor com a potência elétrica consumida.

Este projeto realiza uma análise exploratória do desempenho de um sistema de refrigeração ao longo de uma semana de operação, com foco na identificação de padrões, regimes operacionais e eventos de degradação de eficiência.

## Objetivos

- Avaliar a estabilidade operacional do sistema.
- Identificar períodos de queda no COP.
- Relacionar o COP com variáveis operacionais críticas.
- Gerar insights que possam apoiar decisões rápidas em ambiente industrial.

## Dados Utilizados

A estrutura dos dados inclui as seguintes variáveis:

- Temperatura da água na entrada do sistema (°C)
- Temperatura da água na saída (°C)
- Vazão total de água (m³)
- Potência elétrica consumida (kW)
- Pressão do óleo
- Nível do tanque

*Observação*:
Os dados utilizados neste repositório são sintéticos, gerados com o objetivo de simular o comportamento de um sistema real. Eles não representam dados operacionais de nenhuma empresa.

## Metodologia

A análise foi conduzida utilizando Python, com foco em interpretação rápida e aplicável ao contexto industrial.

As etapas principais incluíram:

- Cálculo do COP ao longo do tempo
- Análise de séries temporais
- Estatística descritiva
- Histogramas para avaliação da distribuição do desempenho
- Análise de correlação entre COP e variáveis operacionais
- Identificação visual de regimes operacionais distintos

Optou-se por uma abordagem exploratória robusta, porém pragmática, adequada a cenários industriais onde decisões precisam ser tomadas mesmo com dados incompletos.

## Ferramentas Utilizadas

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

Em ambientes industriais produtivos, análises similares poderiam ser realizadas com ferramentas estatísticas como Minitab ou plataformas de análise de séries temporais integradas ao historiador de dados da planta.

## Estrutura do projeto

analise-cop-refrigeracao-industrial/

- notebooks/        → Notebook principal da análise

- data/             → Dados sintéticos utilizados

- reports/          → Versão em PDF do estudo

- src/              → Código auxiliar (geração de dados)

- README.md

## Principais Resultados

- Identificação de períodos pontuais de degradação de eficiência
- Associação entre quedas de vazão e redução do COP
- Indícios de regimes operacionais distintos ao longo da semana analisada
- Comportamento predominantemente estável, com eventos anômalos localizados

## Autor

Vitor Mazon Rocha

Profissional com formação em Física Computacional, atuando no desenvolvimento de análises aplicadas a processos industriais.

🔗 LinkedIn: https://www.linkedin.com/in/vitor-mazon/