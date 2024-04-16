import pandas as pd

pd.Series(data=5)

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

pd.Series(lista_nomes) # Cria uma Series com o valor a lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

dados = {
    'nome1' : 'Howard',
    'nome2' : 'Ian',
    'nome3' : 'Peter',
    'nome4' : 'Jonah',
    'nome5' : 'Kellie',
}

pd.Series(dados) # Cria uma Series com um dicionario

series_dados = pd.Series([10.2,-1,None,15,23.4])
print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o numero de linhas
print('Tipo de dados', series_dados.dtypes) # Retorna o tipo de dados,  se for misto sera object
print('Os Valores são únicos?', series_dados.is_unique) # Verifica se os valores são unicos (sem duplicações)
print('Existem valores nulos?',series_dados.hasnans) # Verifica se existem valores nulos
print('Quantos valores existem?',series_dados.count()) # Conta quantas valores existem (exclui os nulos)
