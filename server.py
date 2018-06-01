# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api
from webscraping.asignatura import lista_titulaciones, lista_asignaturas
import json

app = Flask(__name__)
api = Api(app)

class Titulaciones(Resource):
    def get(self):
        return lista_titulaciones()

class Asignaturas(Resource):
    def get(self, titulacion):
        return lista_asignaturas(titulacion)

api.add_resource(Titulaciones, '/titulaciones')
api.add_resource(Asignaturas, '/asignaturas/<titulacion>')

if __name__ == '__main__':
    app.run(port='5002')