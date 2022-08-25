import pandas as pd

class restaurantes():
    nome = []
    ranking = []

def select(reviews):

    obj = restaurantes()

    '''
     for loop que passa por todos os valores das cidades e precos do 
     dataframe, testando se condizem com os do enunciado e adicionando-os
     ao objeto para o novo dataframe
    '''
    for i in range(reviews.shape[0]):
        cidade = reviews.iloc[i][1]
        preco = reviews.iloc[i][5]
        if(cidade == 'Lisbon' and preco == '$'):
            obj.nome.append(reviews.iloc[i][0])
            obj.ranking.append(reviews.iloc[i][3])



    # cria o dataframe e o adequa à proposta
    objdf = {'Nome':obj.nome, 'Ranking':obj.ranking}
    df = pd.DataFrame(data=objdf)
    df.sort_values(by='Ranking', inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    df.drop(range(10, len(obj.nome)), axis=0, inplace=True)

    return df


