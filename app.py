from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib
import os

app = FastAPI(title="Sistema de Recomendação de Filmes")

# Carregando os dados que o seu train.py gerou
try:
    df = pd.read_csv("data/processed_movies.csv")
    similarity = joblib.load("models/similaridade.pkl")
except Exception as e:
    print(f"Erro ao carregar arquivos: {e}. Certifique-se de que o treino rodou!")

@app.get("/recomendar/{nome_filme}")
def recomendar(nome_filme: str):
    # Procura o filme no DataFrame (ignorando maiúsculas/minúsculas)
    filme_lower = nome_filme.lower()
    df_temp = df.copy()
    df_temp['original_title_lower'] = df_temp['original_title'].str.lower()
    
    if filme_lower not in df_temp['original_title_lower'].values:
        raise HTTPException(status_code=404, detail="Filme não encontrado na base.")

    idx = df_temp[df_temp['original_title_lower'] == filme_lower].index[0]
    
    # Lógica de similaridade
    distancias = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
    # Pega os 5 filmes mais parecidos
    recomendacoes = []
    for i in distancias[1:6]:
        recomendacoes.append(df.iloc[i[0]].original_title)
        
    return {"filme_buscado": nome_filme, "recomendacoes": recomendacoes}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)