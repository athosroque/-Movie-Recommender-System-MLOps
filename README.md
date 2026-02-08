# 🎬 Movie Recommender: Pipeline de NLP & MLOps

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Serving-green.svg)](https://fastapi.tiangolo.com/)
[![MLOps](https://img.shields.io/badge/MLOps-DVC%20%7C%20MLflow-orange.svg)](https://mlflow.org/)

Este projeto implementa um **Sistema de Recomendação Baseado em Conteúdo** (*Content-Based Filtering*) seguindo os princípios de **NLP** e **MLOps**. O objetivo é resolver a "fadiga de decisão" dos usuários, convertendo sinopses brutas em vetores semânticos para recomendações ultra-precisas.

---

## 🧠 Base Teórica: Content-Based Filtering

Diferente da Filtragem Colaborativa (que olha para outros usuários), este sistema foca nas **características intrínsecas** do item. Como referenciado em estudos da *AI Mind Labs*, o sistema analisa atributos como diretor, elenco, gênero e principalmente o **enredo (overview)**.

### 📐 Similaridade de Cosseno
Utilizamos a **Similaridade de Cosseno** para calcular a proximidade entre o filme buscado e o restante da base. 
- **Por que não Distância Euclidiana?** Em espaços vetoriais de texto (NLP), a magnitude do vetor (tamanho da descrição) importa menos que a **direção/ângulo** das palavras. A Similaridade de Cosseno ignora o tamanho da descrição e foca puramente no contexto.
- **Vetorização**: O pipeline suporta `TF-IDF (Term Frequency-Inverse Document Frequency)`, que penaliza palavras muito comuns e valoriza termos únicos que definem o gênero/nicho do filme.

---
## 🧪 Engenharia de MLOps: O Pilares

### 1. Reprodutibilidade de Dados (DVC)
Arquivos CSV grandes não devem estar no Git. Utilizamos o **DVC (Data Version Control)** para rastrear as versões dos datasets. Isso garante que o modelo treinado hoje use exatamente os mesmos dados se for re-treinado amanhã.
- Comando: `dvc pull` (para baixar os dados rastreados).

### 2. Rastreamento de Experimentos (MLflow)
Cada execução do script `train.py` é logada no **MLflow**. 
- **Parâmetros:** `max_features` da vetorização.
- **Métricas:** Número de filmes processados.
- **Artefatos:** A matriz de similaridade gerada.
Isso permite auditar e comparar diferentes versões do recomendador de forma visual.

### 3. Ambiente Isolado (Docker)
Para eliminar o clássico "na minha máquina funciona", o projeto é totalmente containerizado. O **Dockerfile** encapsula todas as dependências do sistema e bibliotecas Python.

---

## 🎯 Por que estas escolhas técnicas?

| Componente | Escolha | Motivo (The "Why") |
| :--- | :--- | :--- |
| **NLP** | `CountVectorizer` | Para a "Sopa de Metadados", a frequência absoluta de nomes (atores/diretores) é mais relevante que a frequência inversa (TF-IDF). |
| **Similadidade** | `Cosine Similarity` | Eficiente para comparar vetores de alta dimensão gerados pelo texto. |
| **Framework** | `FastAPI` | Processamento assíncrono e documentação automática (Swagger) pronta para integração com frontends. |

---
## 🏗️ Arquitetura MLOps
O diferencial deste projeto é o ciclo de vida automatizado:

```mermaid
graph LR
    subgraph Ingestão
    A[Kaggle API] --> B[(Raw CSVs)]
    end
    subgraph Processamento
    B --> C[NLP Pipeline]
    C --> D[TF-IDF Vetores]
    end
    subgraph Treinamento
    D --> E[Cossine Matrix]
    E -->|Tracking| F[MLflow]
    end
    subgraph Serving
    E --> G[FastAPI]
    G --> H[Docker Container]
    end
    DVC[(DVC: Versionamento de Dados)] -.-> C
    DVC -.-> E
```

---

## 🚀 Tecnologias

*   **Lógica**: `Scikit-Learn`, `NLP (NLTK)`.
*   **Versionamento**: `DVC` (Data Version Control) para datasets versionados no S3/Google Drive.
*   **Gestão**: `MLflow` para rastrear experimentos e versões do modelo.
*   **API**: `FastAPI` (Assíncrona e Alta Performance).

---

## 🛠️ Como Executar

### 1. Ingestão e Preparação
```bash
pip install -r requirements.txt
python src/ingestion.py
```

### 2. Ciclo de MLOps (Treino e Registro)
```bash
# Executa o treino e registra métricas no MLflow
python src/train.py
```

### 3. Servindo Recomendações
```bash
uvicorn app:app --reload
```
Acesse `http://127.0.0.1:8000/recomendar/Inception` para ver o sistema em ação.

---

## 📊 Impacto e Resultados
- **Redução de Latência**: Busca por similaridade otimizada com matrizes Joblib.
- **Reprodutibilidade**: 100% de rastreabilidade via DVC e MLflow.
- **Escalabilidade**: Pronto para deploy via Docker.
