# 🎬 Movie Recommender: Pipeline de NLP e MLOps

## Visão Geral do Projeto

Este projeto foca na construção de um **Sistema de Recomendação de Filmes** robusto, com ênfase nas etapas de **Engenharia de Dados**, **Processamento de Linguagem Natural (NLP)** e **MLOps (Machine Learning Operations)**. O objetivo é transformar descrições textuais brutas de filmes em dados estruturados e utilizá-los para gerar recomendações precisas, garantindo que o ciclo de vida do modelo seja automatizado, rastreável e escalável.

O diferencial deste projeto é a aplicação de uma infraestrutura MLOps completa, que abrange desde o versionamento de dados até o deploy do modelo como uma API, assegurando reprodutibilidade e facilidade de manutenção.

## ✨ Funcionalidades e Inovações

### 1. Pipeline de Limpeza Modular e Otimizada

Foi desenvolvida uma função de limpeza de dados modular e eficiente, que executa as seguintes tarefas essenciais para o pré-processamento de texto:

*   **Tratamento de Integridade**: Validação e tratamento de tipos de dados para evitar erros com valores nulos (`NaN`), garantindo a robustez do pipeline.
*   **Limpeza por Regex**: Utilização de Expressões Regulares para remover ruídos, caracteres especiais e padrões indesejados das descrições textuais.
*   **Normalização**: Conversão de todo o texto para minúsculas e aplicação de tokenização para padronizar o vocabulário.
*   **Filtragem Semântica**: Remoção de *Stopwords* (palavras comuns sem significado relevante, como 
