from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

class data():
    
    @staticmethod
    def vetorizacao(dados):
        matriz_vetores = CountVectorizer().fit_transform(dados).toarray()
        return matriz_vetores


    @staticmethod
    def indice_jaccard(vetor1,vetor2):
        intersecao = np.logical_and(vetor1,vetor2)
        uniao = np.logical_or(vetor1,vetor2)
        similaridade = intersecao.sum() / float(uniao.sum())
        return similaridade
    
    @staticmethod
    def cosine(vetor1,vetor2):
        # Ensure length of x and y are the same
        if len(vetor1) != len(vetor2) :
            return None
    
        # Compute the dot product between x and y
        produto_escalar = np.dot(vetor1, vetor2)
    
        # Compute the L2 norms (magnitudes) of x and y
        modulo_vetor1 = np.sqrt(np.sum(vetor1**2)) 
        modulo_vetor2 = np.sqrt(np.sum(vetor2**2))
    
        # Compute the cosine similarity
        similaridade = produto_escalar / (modulo_vetor1 * modulo_vetor2)
    
        return similaridade

    @staticmethod
    def comparacao_vetores_cossine(array):
        lista_cossine = []
        for i in range(len(array)):
            for j in range(i+1, len(array)):  # Começa do próximo índice após o i
                cossine = data.cosine(array[i], array[j])
                lista_cossine.append(cossine)
        return lista_cossine
    
    @staticmethod
    def comparacao_vetores_jaccard(array):
        lista_jaccard = []
        for i in range(len(array)):
            for j in range(i+1, len(array)):  # Começa do próximo índice após o i
                indice_jaccard = data.indice_jaccard(array[i], array[j])
                lista_jaccard.append(indice_jaccard)
        return lista_jaccard
    
    @staticmethod
    def media_em_porcentagem(lista):
        media_porcentagem = ((np.sum(lista))/len(lista))*100
        return media_porcentagem