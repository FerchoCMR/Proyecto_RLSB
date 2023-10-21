# Reconocimiento LSB Lengua Señas Boliviana

Sistema de reconocimiento de Lengua Señas Boliviana (LSB) basado en el modelo de aprendizaje profundo de redes neuronales para la detección y la clasificación de gestos o señas de las comunidades con discapacidad auditiva.

Este sistema se compone de dos partes:

1. Backend: se encarga de la detección y clasificación de gestos o señas de las comunidades con discapacidad auditiva y de gestionar la interacción del usuario con los conceptos técnicos como los modelos, el entrenamiento del modelo, el registro de nuevas señas, el versionado, y la predicción de las señas. 
   
   Esta es orquestada con el framework de Python [FastAPI](https://fastapi.tiangolo.com/) para la creación de una API RESTful; y con la base de datos NoSQL ([TinyDB](https://tinydb.readthedocs.io/en/latest/)), y las carpetas de almacenamiento de los modelos y las señas.

2. Frontend: se encarga de la interacción del usuario no técnico con el sistema, ya sea para realizar la traducción de señas a texto y/o voz, o para registrar nuevas señas en el sistema. Esta es orquestada con el framework de [Angular](https://angular.io/) para la creación de una aplicación web.


