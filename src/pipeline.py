# 1. Tratamento de Erros (isinstance)
# 2. Limpeza com Regex (re.sub)
# 3. Padronização e Tokenização (lower().split())
# 4. Remoção de Stopwords (List Comprehension):

import re
import nltk
from nltk.corpus import stopwords

# Garante que as stopwords existam
nltk.download('stopwords')
stop_words = set(stopwords.words('english')) # Linguagem das palavras do dataset

def limpar_e_tokenizar(texto):
    if not isinstance(texto, str):
        return ""
    
    # Remove pontuação
    texto_limpo = re.sub(r'[^\w\s]', '', texto)
    
    # Minúsculas e Split
    palavras = texto_limpo.lower().split()
    
    # Remove Stopwords e junta de volta em string para o Vectorizer
    palavras_limpas = [w for w in palavras if w not in stop_words]
    return " ".join(palavras_limpas)

