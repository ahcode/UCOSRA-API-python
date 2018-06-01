# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from config import ConsultaReservasAsignaturaUrl

def lista_titulaciones():
    page = requests.get(ConsultaReservasAsignaturaUrl)
    soup = BeautifulSoup(page.content, 'html.parser')
    titulaciones = list(soup.find('select', {'class':'listaG', 'name':'tpp1'}).find_all('option'))
    t = [(item['value'], item.get_text().split(' ', 2)[2]) for item in titulaciones[1:]]
    return t

def lista_asignaturas(titulacion):
    page = requests.get(ConsultaReservasAsignaturaUrl + "&tTit=" + titulacion + "&tAsig=---")
    soup = BeautifulSoup(page.content, 'html.parser')
    titulaciones = list(soup.find('select', {'class':'listaG', 'name':'ttp2'}).find_all('option'))
    t = [(item['value'], item.get_text().split(' ', 2)[2]) for item in titulaciones[1:]]
    return t
