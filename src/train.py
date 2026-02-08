import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pipeline import limpar_e_tokenizar # Importa sua função do outro arquivo

def executar_treinamento():
    # 1. Configura o MLflow
    mlflow.set_experiment("recomendacao_filmes")
    
    with mlflow.start_run():
        # 2. Carga dos dados
        # Supondo que você colocou os CSVs na pasta /data
        df_movies = pd.read_csv("data/tmdb_5000_movies.csv")
        df_credits = pd.read_csv("data/tmdb_5000_credits.csv")
        
        # Merge simples (baseado no seu notebook)
        df_credits.columns = ['id', 'title', 'cast', 'crew']
        df = df_movies.merge(df_credits, on='id')
        
        # 3. Processamento
        print("Limpando textos...")
        df['overview_clean'] = df['overview'].apply(limpar_e_tokenizar)
        
        # 4. Vetorização (Upgrade: TF-IDF para melhor relevância semântica)
        from sklearn.feature_extraction.text import TfidfVectorizer
        print("Vetorizando com TF-IDF...")
        tfidf = TfidfVectorizer(max_features=5000)
        vetores = tfidf.fit_transform(df['overview_clean']).toarray()
        
        # 5. Cálculo de Similaridade
        print("Calculando matriz de similaridade...")
        similaridade = cosine_similarity(vetores)
        
        # 6. Registro no MLflow (Vantagem do MLOps!)
        mlflow.log_param("max_features", max_features)
        mlflow.log_metric("num_filmes", len(df))
        
        # 7. Salvando os artefatos (Modelo e Dados Processados)
        # Precisamos do DF processado para saber os títulos depois
        joblib.dump(similaridade, "models/similaridade.pkl")
        df[['id', 'original_title']].to_csv("data/processed_movies.csv", index=False)
        
        print("Treino finalizado e salvo em /models!")

if __name__ == "__main__":
    executar_treinamento()