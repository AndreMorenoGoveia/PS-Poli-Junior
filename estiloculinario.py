from asyncore import readwrite
import pandas as pd
import ast
import numpy as np

class count():
    estilo = []
    cont = []

class restaurantes():
    nome = []
    cidade = []
    ranking = []



def maisPresente(reviews):

    obj = count()


    for i in range(reviews.shape[0]):
        str1 = reviews.iloc[i][2]
        estilos = ast.literal_eval(str1)
        for j in range(len(estilos)):
            b = True
            for k in range(len(obj.estilo)):
                if(estilos[j] == obj.estilo[k]):
                    b = False

            if(b):
                obj.estilo.append(estilos[j])
                obj.cont.append(1)

            ++obj.cont[j]


    return obj.estilo[np.argmax(obj.cont)]



def seleciona(reviews):

    obj = restaurantes()
    estilo = maisPresente(reviews)
    
    for i in range(reviews.shape[0]):
        str1 = reviews.iloc[i][2]
        styles = ast.literal_eval(str1)

        b1 = False
        for j in range(len(styles)):
            if(estilo == styles[j]):
                b1 = True

        if(b1):
            b2 = False
            b3 = False
            cidade = reviews.iloc[i][1]
            ranking = reviews.iloc[i][3]
            nome = reviews.iloc[i][0]
            for j in range(len(obj.cidade)):
                if(cidade == obj.cidade[j]):
                    b2 = True
                    if(ranking < obj.ranking[j]):
                        b3 = True
                        m = j
                        
            if(b3):
                obj.ranking[m] = ranking
                obj.nome[m] = nome

            if(not b2):
                obj.cidade.append(cidade)
                obj.nome.append(nome)
                obj.ranking.append(ranking)

    objaux = {'Cidade':obj.cidade, 'Ranking':obj.ranking, 'Nome':obj.nome}

    dt = pd.DataFrame(data= objaux)
    
    dt = dt.groupby("Cidade")

      
    return estilo, dt.min()