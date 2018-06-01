# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api
from webscraping.asignatura import lista_titulaciones, lista_asignaturas, lista_reservas_asignatura
import json

app = Flask(__name__)
api = Api(app)

class Titulaciones(Resource):
    def get(self):
        return lista_titulaciones()

class Asignaturas(Resource):
    def get(self):
        args = request.args
        if 'titulacion' not in args:
            return "Error"
        return lista_asignaturas(args['titulacion'])

class ReservasAsignatura(Resource):
    def get(self):
        args = request.args
        if('titulacion' not in args and 'asignatura' not in args):
            return "Error"
        else:
            if 'grupo' in args: grupo = args['grupo']
            else: grupo = "T"
            if 'fechaini' in args: fechaini = args['fechaini']
            else: fechaini = "01-06-2018" #TODO hoy
            if 'fechafin' in args: fechafin = args['fechafin']
            else: fechafin = "01-06-2018" #TODO hoy
        return lista_reservas_asignatura(args['titulacion'], args['asignatura'], grupo, fechaini, fechafin)

api.add_resource(Titulaciones, '/titulaciones')
api.add_resource(Asignaturas, '/asignaturas')
api.add_resource(ReservasAsignatura, '/reservasasignatura')

if __name__ == '__main__':
    app.run(port='5002')