import pandas as pd
import math

class cities():
    city = []
    totalrev = []
    totalcont = []


def reviews(dt):

    obj = cities()
    
    # for loop que passa pelo dataframe lendo suas informacoes
    # e armazenando-as nas variaveis e consertando seu formato
    for i in range(dt.shape[0]):
        rep = True
        name = dt.iloc[i][1]
        rev  = str((dt.iloc[i][6])).replace(',', '.')
        if(math.isnan(float(rev))):
            rev = 0
        rev = float(rev)

        cont = 1

        
        # for loop que testa para que o nome da cidade não se repita
        for j in range(len(obj.city)):
            if(obj.city[j] == name):
                rep = False
                k = j

        # armaze na os dados da funcao, criando um novo elemento caso haja
        # a cidade na lista ou somando os dados nos elementos ja existentes
        if(rep):
            obj.city.append(name)
            obj.totalcont.append(cont)
            obj.totalrev.append(rev)
        else:    
            obj.totalrev[k] += rev
            obj.totalcont[k] += 1

    #Cria os dataframes limitando seu formato ao indicado pela proposta
    
    obja = {'Cidade': obj.city, 'Restaurantes avaliados':obj.totalcont}

    dfa = pd.DataFrame(data=obja)
    dfa.sort_values(by='Restaurantes avaliados', ascending=False, inplace=True)
    dfa.reset_index(inplace=True)
    dfa.drop('index', axis=1, inplace=True)
    dfa.drop(range(5, len(obj.city)), axis=0, inplace=True)

    objb = {'Cidade': obj.city, 'Total de avaliacoes':obj.totalrev}

    dfb = pd.DataFrame(data=objb)
    dfb.sort_values(by='Total de avaliacoes', ascending=False, inplace=True)
    dfb.reset_index(inplace=True)
    dfb.drop('index', axis=1, inplace=True)
    dfb.drop(range(0, len(obj.city) - 5), axis=0, inplace=True)

    return dfa, dfb



        






