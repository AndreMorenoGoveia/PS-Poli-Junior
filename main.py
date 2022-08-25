from array import array
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import limpeza
import cidades
import Lisboa
import estiloculinario
import media

def main():

    #le o arquivo do dataframe
    reviews = pd.read_csv('reviews_restaurantes.csv')

    #Questão 1
    a, reviews = limpeza.limpa(reviews)
    #a)
    #print("O numero de valores negativos encontrados eh de:", a, "\n")

    #b)
    #print(b,"\n")

    #Questão 2
    #a, b = cidades.reviews(reviews)
    #a)
    #print(a, "\n")
    #b)
    #print(b, "\n")

    #Questao 3
    #a = Lisboa.select(reviews)

    #print(a, "\n")

    #Questao 4

    #a , b = estiloculinario.seleciona(reviews)
    
    #a)
    #print("O estilo culinario mais frequente eh", a, "\n")

    #b)
    #print(b, "\n")

    #Questao 5

    #print("A media dos rankings eh de", media.media(reviews))
   
    print(np.nanmean(reviews.Ranking.unique()))





if __name__ == '__main__':
    main()



