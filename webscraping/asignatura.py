# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from config import ConsultaReservasAsignaturaFormUrl, ConsultaReservasAsignaturaPostUrl

def lista_titulaciones():
    page = requests.get(ConsultaReservasAsignaturaFormUrl)
    soup = BeautifulSoup(page.content, 'html.parser')
    titulaciones = list(soup.find('select', {'class':'listaG', 'name':'tpp1'}).find_all('option'))[1:]
    titulaciones = [(item['value'], item.get_text().split(' ', 2)[2]) for item in titulaciones]
    return titulaciones

def lista_asignaturas(titulacion):
    page = requests.get(ConsultaReservasAsignaturaFormUrl, params={'tTit':titulacion, 'tAsig':'---'})
    soup = BeautifulSoup(page.content, 'html.parser')
    asignaturas = list(soup.find('select', {'class':'listaG', 'name':'ttp2'}).find_all('option'))[1:]
    asignaturas = [(item['value'].split(' ', 1)[0], item.get_text().split(' ', 3)[3]) for item in asignaturas]
    return asignaturas

def lista_reservas_asignatura(titulacion, asignatura, grupo, fechaini, fechafin):
    page = requests.post(ConsultaReservasAsignaturaPostUrl, data={'tTit':titulacion, 'tAsig':asignatura, 'cGrupo':grupo, 'calendarDate1':fechaini, 'calendarDate2':fechafin})
    soup = BeautifulSoup(page.content, 'html.parser')
    reservas_table = list(soup.find('table', {'class':'tablaDatos'}).find_all('tr'))[1:]
    reservas = []
    for item in reservas_table:
        item = list(item.find_all('td'))
        fecha = item[0].next.get_text()
        [timeIni, timeFin] = item[4].get_text().split('-')
        aula = item[5].next.get_text().split(' ', 1)
        aulaCode = aula[0]
        detallesAula = aula[1]
        profesor = item[6].get_text()
        grupo = item[8].get_text()
        reservas.append({'fecha':fecha, 'horaIni':timeIni, 'horaFin':timeFin, 'codigo-aula':aulaCode, 'aula':detallesAula, 'profesor':profesor, 'grupo':grupo})
    return reservas