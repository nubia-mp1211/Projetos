#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:43:37 2021

@author: nubiapiccirilli
"""
# Importando 
import pandas as pd
from whatsapp_api import WhatsApp

#Faz leitura do arquivo agenda.csv que foi criada com dados: Nome,Mensage 
agenda = pd.read_csv('agenda.csv')

#Utiliza as APIs desenvolvida do WhasApp
wp = WhatsApp()

# Faz a litura do QR code pelo celular
input("Pressione Enter QR Code")

#Procura o nome de contato e envia mensagem:
for contato in agenda["Nome"].unique():
    mensagem = agenda.loc[agenda["Nome"] == contato, "Mensagem"].values
    print(contato, mensagem)
    wp.search_contact(contato)
    wp.send_message(mensagem)
    
