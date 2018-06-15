# UCOSRA-API

*En Desarrollo*

Implementación simple de una API para el sistema de reserva de aulas de la Universidad de Córdoba utilizalndo Flask y BeautifulSoup.

``` bash
# crear y activar entorno virtual
virtualenv UCOSRA-API-ENV
source UCOSRA-API-ENV/bin/activate

# instalar dependencias
pip install flask
pip install beautifulsoup4
pip install requests

# ejecutar servidor
python server.py
```

### Ejemplos de uso

* Lista de titulaciones:
```
http://localhost:5002/titulaciones
```
``` json
[
    ......
	[
		"0108",
		"GRADO DE INGENIERÍA FORESTAL"
	],
	[
		"0114",
		"GRADO DE INGENIERÍA INFORMÁTICA"
	],
	[
		"0111",
		"GRADO DE INGENIERÍA MECÁNICA"
	],
	......
]
```

* Lista de asignaturas:
```
localhost:5002/asignaturas?titulacion=0114
```
``` json
[
    ......
    [
		"101384",
		"ÁLGEBRA LINEAL"
	],
	[
		"101422",
		"ALGORÍTMICA"
	],
	[
		"101397",
		"ARQUITECTURA DE COMPUTADORES"
	],
	......
]
```

* Reservas asignatura:
```
RESERVAS HOY:
localhost:5002/reservasasignatura?titulacion=0114&asignatura=101384

RESERVAS ESPECIFICANDO FECHAS:
localhost:5002/reservasasignatura?titulacion=0114&asignatura=101384&fechaini=01-03-2018&fechafin=31-03-2018
```

``` json
[
    ......
    {
		"fecha": "01-03-2018",
		"horaFin": "14:00",
		"horaIni": "12:00",
		"aula": "01051MA",
		"profesor": "",
		"grupo": "2"
	},
	{
		"fecha": "02-03-2018",
		"horaFin": "11:30",
		"horaIni": "10:00",
		"aula": "0111B06",
		"profesor": "",
		"grupo": "1"
	},
	......
]
```

### Pendiente de Implementar
* Detalles de reserva
* Detalles de aula
* Lista de centros
* Lista de edificios
* Lista de aulas
* Reservas de aula