# 🎬 Movie Recommender: Pipeline de NLP e MLOps

### 📝 Descrição
Este projeto foca na etapa crítica de **Engenharia de Dados e NLP**, transformando descrições textuais brutas de filmes em dados estruturados. O diferencial é a aplicação de uma infraestrutura robusta de **MLOps**, garantindo que o ciclo de vida do modelo seja automatizado, rastreável e escalável.

---

### 🛠️ Stack Tecnológica

| Categoria | Tecnologias |
| :--- | :--- |
| **Linguagem & Dados** | Python, Pandas, NumPy |
| **NLP** | Regex, NLTK, Tokenização |
| **MLOps** | DVC (Dados), MLflow (Experimentos) |
| **Deploy & Infra** | FastAPI, Docker, Kaggle API |
| **Versão** | Git & GitHub |

---

### 🧠 O que eu desenvolvi?

#### **1. Pipeline de Limpeza Modular**
Criei uma função de limpeza que executa quatro tarefas essenciais:
* **Tratamento de Integridade:** Validação de tipos para evitar erros com `NaN`.
* **Limpeza por Regex:** Remoção de ruídos e caracteres especiais.
* **Normalização:** Conversão para minúsculas e tokenização.
* **Filtragem Semântica:** Remoção de *Stopwords* para focar no conteúdo relevante.

#### **2. Engenharia de MLOps**
* **DVC (Data Version Control):** Rastreio de dados sem sobrecarregar o Git.
* **MLflow:** Dashboard para auditoria de métricas e parâmetros.
* **FastAPI:** Modelo exposto via API REST, pronto para consumo.
* **Docker:** Containerização para garantir reprodutibilidade total.

---

### 🏗️ Estrutura do Projeto
```text
├── data/               # Dados rastreados pelo DVC
├── models/             # Artefatos (.pkl) dos modelos
├── src/
│   ├── ingestion.py    # Coleta via Kaggle API
│   ├── pipeline.py     # Pré-processamento e limpeza
│   └── train.py        # Treino e log no MLflow
├── app.py              # API FastAPI
├── Dockerfile          # Configuração do Container
└── requirements.txt    # Dependências

🚀 Como Executar

1. Instalação e Treino
Bash
# Instalar dependências
pip install -r requirements.txt

# Executar pipeline de dados e treino
python src/ingestion.py
python src/train.py

# Visualizar experimentos
mlflow ui
2. Execução via Docker
Bash
# Build da imagem
docker build -t movie-recommender .

# Rodar container
docker run -p 8000:8000 movie-recommender
Acesse http://localhost:8000/docs para testar as recomendações via Swagger UI.

## 🚀 Upgrade: Sistema de Recomendação Multi-Variável
Evolução do algoritmo para considerar não apenas a descrição, mas uma **Sopa de Metadados (Metadata Soup)**:
- **Elenco:** Extração dos 3 atores principais.
- **Keywords:** Termos técnicos da trama.
- **Gêneros:** Categorização cruzada.

**Técnica:** Utilizamos `CountVectorizer` e `Cosine Similarity` para medir a proximidade vetorial entre os filmes, permitindo recomendações muito mais precisas (ex: sugerir outros filmes de piratas com o mesmo estilo de atuação).


---
