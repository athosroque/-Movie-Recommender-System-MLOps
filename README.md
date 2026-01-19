🎬 Movie Recommender System: De Notebook para MLOps
Este projeto implementa um sistema de recomendação de filmes baseado em conteúdo, transformando um modelo experimental em uma aplicação produtiva e escalável.

📝 Contexto e Metodologia
A recomendação é baseada na técnica de Content-Based Filtering. Diferente da filtragem colaborativa (que olha para o comportamento de outros usuários), este modelo analisa os atributos dos itens (gêneros, palavras-chave, sinopse) para encontrar similaridades.

Conforme detalhado por Francesco Franco, o processo consiste em:

Vetorização de Texto: Transformar metadados dos filmes em vetores numéricos.

Cosseno de Similaridade: Calcular o ângulo entre vetores para determinar quão próximos dois filmes estão no espaço multidimensional.

🛠️ Engenharia de MLOps
O diferencial deste repositório é a aplicação de princípios de MLOps para garantir a reprodutibilidade:

Ingestão Automática: Script dedicado para coleta de dados via Kaggle API.

Versionamento de Dados (DVC): Os dados e modelos não são salvos no Git, mas sim rastreados pelo DVC para evitar repositórios pesados.

Experimentos (MLflow): Cada treino gera um log de parâmetros e métricas, permitindo auditar o desempenho do modelo.

Serviço (FastAPI): O modelo é exposto via API REST, pronto para consumo.

Containerização (Docker): Todo o ambiente é isolado, garantindo que o projeto rode em qualquer máquina.

🏗️ Estrutura do Projeto
Plaintext
├── data/              # Dados brutos e processados (rastreados pelo DVC)
├── models/            # Modelos treinados (.pkl)
├── src/
│   ├── ingestion.py   # Script de coleta de dados
│   ├── pipeline.py    # Lógica de pré-processamento e limpeza
│   └── train.py       # Script de treinamento e log no MLflow
├── app.py             # API FastAPI para servir recomendações
├── Dockerfile         # Configuração de containerização
└── requirements.txt   # Dependências do projeto
🚀 Como Executar
1. Requisitos
Python 3.9+

Docker (opcional)

Kaggle API Token (kaggle.json)

2. Instalação e Treino
Bash
# Instalar dependências
pip install -r requirements.txt

# Baixar dados e treinar o modelo
python src/ingestion.py
python src/train.py

# Iniciar o painel de experimentos
mlflow ui
3. Execução via Docker
Bash
docker build -t movie-recommender .
docker run -p 8000:8000 movie-recommender
Acesse http://localhost:8000/docs para testar as recomendações.
