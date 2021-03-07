#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:07:43 2021

@author: nubiapiccirilli
"""

import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
from time import sleep

requests.get('https://imoveis.mercadolivre.com.br/casas/aluguel/sao-paulo/sao-paulo-zona-sul/_Desde_145').content
ZONAS = ['norte', 'sul', 'leste', 'oeste']
PAGINAS = ['', '_Desde_49', '_Desde_97', '_Desde_145', '_Desde_193', '_Desde_241']
URL_ML = 'https://lista.mercadolivre.com.br/sao-paulo-alugueis-zona-sul#D[A:sao%20paulo%20alugueis%20zona%20sul,L:undefined]{}/{}'

# Podemos definir dois padrões regex, um para o numero de quartos e outro para a area
re_quarto = '\| (.*) quarto'
re_area = '> (.*) m²'
re_quarto_area_ausente = "> (.*) quarto"
def coletar_dados_ml(url, zona):
  c = requests.get(url).content
  soup = BeautifulSoup(c)
  atributos = soup.find_all('div', {"class": "item__attrs"})
  precos = soup.find_all('span', {"class": "price__fraction"})

  lista_precos = []
  for s in precos:
    p = re.findall('<span class="price__fraction">(.*)</span>', str(s))
    lista_precos.append(int(p[0].replace('.','')))

  # Inicializar duas listas vazias, uma para a area e outra para o numero de quartos
  lista_areas = []
  lista_quartos = []
  lista_zonas = []
  for a in atributos:
    # Extrair area e número de quartos
    n_quartos = re.findall(re_quarto, str(a))
    area = re.findall(re_area, str(a))
    
    # Atribuir np.nan quando o número de quartos estiver ausente 
    if n_quartos==[]:
      n_quartos = re.findall(re_quarto_area_ausente, str(a))

      if n_quartos==[]:
        n_quartos=np.nan
      else:
        n_quartos=n_quartos[0]
  
    else:
        n_quartos=n_quartos[0]

    if area==[]:
      area=np.nan
    else:
      area=area[0]
    #print(n_quartos)

    # Anexar às listas acima
    lista_quartos.append(n_quartos)
    lista_areas.append(area)
    lista_zonas.append(zona)

  dados = {
      'zona': lista_zonas,
      'quartos': lista_quartos,
      'area': lista_areas,
      'preco': lista_precos
      }

  df = pd.DataFrame(dados)
  return df


lista_dfs = []
for zona in ZONAS:
  for pg in PAGINAS:
    url = URL_ML.format(zona, pg)
    print('Carregando a URL', url)

    df = coletar_dados_ml(url, zona)
    lista_dfs.append(df)
    sleep(1)
    
    dados = pd.concat(lista_dfs)

dados  

dados['quartos'] = dados['quartos'].astype(float)
dados['area'] = dados['area'].astype(float)


dados.to_csv('dados_calculadora_imoveis_aula.csv', index=False)



  