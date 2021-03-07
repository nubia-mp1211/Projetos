#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:43:37 2021

@author: nubiapiccirilli
"""

import pandas as pd
from whatsapp_api import WhatsApp
agenda = pd.read_csv('agenda.csv')
wp = WhatsApp()

#input("Pressione Enter QR Code")

for contato in agenda["Nome"].unique():
    mensagem = agenda.loc[agenda["Nome"] == contato, "Mensagem"].values
    print(contato, mensagem)
    wp.search_contact(contato)
    wp.write_message(mensagem)
    