#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:45:06 2021

@author: nubiapiccirilli
"""

import requests
import pandas as pd 

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados?formato=json'



def get_data_from_api(URL):
    
    r = requests.get(URL)   # Obtendo os dados da API do Banco Cantral
    
    x = r.json()            # Transforman os dados em formato Json para dicionario
    
    df = pd.DataFrame(x)    # Recebe Dicionario e transforma em um pandas Dataframe
    
    return df

dados = get_data_from_api(URL)

dados.head()


dados.to_csv('Arquivo_resultado', index= False)
    