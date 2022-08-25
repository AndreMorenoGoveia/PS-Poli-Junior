import re
import pandas as pd
import math

def limpa(reviews):

    err = []
    cont = 0

    # for loop que seleciona e armazena todos os valores nan do dataframe
    for i in range(reviews.shape[0]):
        if(math.isnan(reviews.iloc[i][4])):
            err.append(i)
            cont = cont + 1

    # refaz o o dataframe removendo as linhas com valores negativos em sua nota
    reviews.drop(err, axis=0, inplace=True)
    reviews.reset_index(inplace=True)
    reviews.drop('index', axis=1, inplace=True)

    return cont, reviews

    
