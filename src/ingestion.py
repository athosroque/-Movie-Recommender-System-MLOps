import os
import kagglehub
import shutil

def download_dados():
    # AJUSTE AQUI: coloque o caminho da pasta onde você baixou o seu kaggle.json
    os.environ['KAGGLE_CONFIG_DIR'] = r'C:\Users\athos\.kaggle\kaggle.json' 
    
    print("Iniciando download do Kaggle...")
    
    try:
        path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
        
        if not os.path.exists('data'):
            os.makedirs('data')
            
        for item in os.listdir(path):
            origem = os.path.join(path, item)
            destino = os.path.join('data', item)
            shutil.copy(origem, destino)
            
        print("✅ Dados baixados e movidos para 'data/' com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao baixar dados: {e}")

if __name__ == "__main__":
    download_dados()