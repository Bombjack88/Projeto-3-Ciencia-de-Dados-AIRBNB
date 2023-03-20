#!/usr/bin/env python
# coding: utf-8

# In[55]:


#não apresentar os warnings

import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')


# In[56]:


import streamlit as st
import joblib


# In[57]:


# Fazer dicionários com as diferntes variáveis: numéricos, V e F, e listas
import pandas as pd
import streamlit as st
import joblib


x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 
               'extra_people': 0, 'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period','Outros']
            }

# Campos de listas dicionario com a combinação do campo item com o valor 

dicionario={}
for item in x_listas:
    # item é a chave do dicionário -> estou a percorrer as chaves
    # x_listas['property_type'] -> a lista do property_type
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}']=0

        
for item in x_numericos:
    if item in ('latitude','longitude'):
        valor=st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f") #quero 5 casas decimais
        
    elif item=='extra_people':
        valor=st.number_input(f'{item}', step=0.01, value=0.0) # o padrão já é 2 casas decimais 
    
    else:
        valor=st.number_input(f'{item}', step=1, value=0) # número inteiro
        
    x_numericos[item]=valor
        
        
for item in x_tf:
    valor=st.selectbox(f'{item}',('Sim','Não')) #posso colocar uma tupla ou uma lista
    if valor=='Sim':
        x_tf[item]=1
    else:
        x_tf[item]=0
    
for item in x_listas:
    valor=st.selectbox(f'{item}',x_listas[item]) #posso colocar uma tupla ou uma lista
    dicionario[f'{item}_{valor}']=1
    
    
botao=st.button('Prever o valor do imóvel')

if botao:
    #juntar os 3 dicionários -> a ordem interessa 
    dicionario.update(x_numericos)
    dicionario.update(x_tf)
    #transformar num dataframe -> o input para o meu modelo é um dataframe
    valores_x=pd.DataFrame(dicionario, index=[0])
    
    dados=pd.read_csv('dados.csv') #importo o DataFrame para ver a lista de colunas
    colunas=list(dados.columns)[1:-1] # excluir a primeira e a última coluna que não são usadas na previsão
    
    # novo dataframe= antigo com as colunas ordenadad
    novo_df=valores_x[colunas]
    
    #importar o modelo
    modelo=joblib.load('modelo.joblib')
    preco=modelo.predict(novo_df) # o output é um dataframe de 1 linha e 1 coluna
    st.write(preco[0]) 
    


# In[58]:


# Código para correr o programa no anaconda prompt: 
# 1)ir para o local aonde está o programa .py -> cd Desktop\Impressionador\Projeto 3 - Ciência de Dados e Recomendações
# 2) correr -> python -m streamlit run DeployProjetoAirbnb.py

